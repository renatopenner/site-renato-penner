#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Proteção permanente dos produtos do site Penner Tech
=====================================================

Nenhum produto pode desaparecer do site. Para cada produto listado em
``dados/produtos_protegidos.json`` este script garante que existam:

  1. a página ``p/<slug>.html`` com o link de afiliado correto;
  2. a entrada em ``dados/produtos.json`` com o mesmo link;
  3. os cards ``<article class="card">`` nas páginas onde ele já aparecia
     (index, categoria e/ou promocoes), dentro do ``<div class="grid">``;
  4. a URL no ``sitemap.xml``;
  5. a imagem em ``img/`` (nos produtos "fixados" também confere o hash
     do arquivo, para detectar troca/sobrescrita da foto).

Se algo faltar ou estiver corrompido, restaura a partir de
``dados/produtos_backup/`` (cópia do último estado saudável).

Comandos
--------
  python scripts/protege_produtos.py --verificar   # só relata (código 1 se houver problema)
  python scripts/protege_produtos.py --restaurar   # conserta o que faltar (padrão)
  python scripts/protege_produtos.py --gerar       # registra páginas novas de p/*.html (nunca remove)
  python scripts/protege_produtos.py --backup      # grava backup do estado saudável atual
  python scripts/protege_produtos.py --rotina      # restaurar + gerar + backup + verificar
  python scripts/protege_produtos.py --atualizar SLUG   # aceita o estado atual como novo padrão
  python scripts/protege_produtos.py --refixar SLUG     # refaz a trava/hash da imagem

Variável de ambiente ``PROTECAO_PERMITIR_EXCLUSAO=1`` libera a exclusão
consciente de um produto (usada apenas em manutenção manual).
"""

import hashlib
import json
import os
import re
import sys
from datetime import datetime

REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
DADOS_DIR = os.path.join(REPO_DIR, "dados")
LOGS_DIR = os.path.join(REPO_DIR, "logs")
CATALOGO = os.path.join(DADOS_DIR, "produtos.json")
MANIFESTO = os.path.join(DADOS_DIR, "produtos_protegidos.json")
BACKUP_DIR = os.path.join(DADOS_DIR, "produtos_backup")
BACKUP_PAGINAS = os.path.join(BACKUP_DIR, "paginas")
BACKUP_CARTOES = os.path.join(BACKUP_DIR, "cartoes")
BACKUP_CATALOGO = os.path.join(BACKUP_DIR, "catalogo.json")
BACKUP_IMG = os.path.join(BACKUP_DIR, "img")

PAGINAS_RAIZ = ("index.html", "promocoes.html", "notebooks.html", "ssd.html",
                "carregadores.html", "saude.html", "casa.html", "auto.html",
                "perifericos.html", "moda.html")

RE_GRID = re.compile(r'<div class="grid"[^>]*>')
RE_CARD = re.compile(r'<article class="card"[^>]*>.*?</article>', re.DOTALL)
RE_SLUG_CARD = re.compile(r'p/([a-z0-9\-]+)\.html')
RE_TITULO = re.compile(r'<title>(.*?)</title>', re.DOTALL)
RE_HREF = re.compile(r'href="([^"]+)"')
RE_FOTO = re.compile(r'<div class="foto[^"]*">.*?<img[^>]*src="([^"]+)"', re.DOTALL)

_hoje = datetime.now().strftime("%d/%m/%Y")
_hoje_iso = datetime.now().strftime("%Y-%m-%d")


# --------------------------------------------------------------------------- #
# utilidades
# --------------------------------------------------------------------------- #
def log(msg):
    linha = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}"
    try:
        if sys.stdout is not None:  # pythonw (tarefa agendada) roda sem console
            print(linha)
    except (OSError, ValueError):
        pass
    try:
        os.makedirs(LOGS_DIR, exist_ok=True)
        with open(os.path.join(LOGS_DIR, f"protecao_{_hoje_iso}.log"), "a", encoding="utf-8") as f:
            f.write(linha + "\n")
    except OSError:
        pass


def ler(caminho):
    # newline="" preserva exatamente o fim de linha do arquivo (index.html usa CRLF)
    with open(caminho, "r", encoding="utf-8", errors="ignore", newline="") as f:
        return f.read()


def escrever(caminho, texto):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, "w", encoding="utf-8", newline="") as f:
        f.write(texto)


def normalizar_link(link):
    return (link or "").replace("&amp;", "&").strip()


def sha256(caminho):
    h = hashlib.sha256()
    with open(caminho, "rb") as f:
        for bloco in iter(lambda: f.read(1 << 20), b""):
            h.update(bloco)
    return h.hexdigest()


def carregar_json(caminho, padrao):
    if not os.path.exists(caminho):
        return padrao
    try:
        return json.loads(ler(caminho))
    except (ValueError, OSError) as e:
        log(f"AVISO: falha ao ler {os.path.basename(caminho)}: {e}")
        return padrao


def salvar_json(caminho, dados):
    escrever(caminho, json.dumps(dados, ensure_ascii=False, indent=2) + "\n")


def grids_da_pagina(html):
    """Lista (inicio_tag, fim_tag, chave) das grades da página."""
    grades = []
    for i, m in enumerate(RE_GRID.finditer(html)):
        chave = f"idx:{i}"
        mid = re.search(r'id="([^"]+)"', m.group(0))
        if mid:
            chave = f"id:{mid.group(1)}"
        grades.append((m.start(), m.end(), chave))
    return grades


def regiao_da_grade(html, grades, indice):
    inicio = grades[indice][1]
    fim = grades[indice + 1][0] if indice + 1 < len(grades) else len(html)
    return inicio, fim


def cards_da_pagina(html, slug):
    """Retorna lista de chaves de grade em que há card do slug."""
    grades = grids_da_pagina(html)
    encontrados = []
    for m in RE_CARD.finditer(html):
        ref = RE_SLUG_CARD.search(m.group(0))
        if not ref or ref.group(1) != slug:
            continue
        alvo = None
        for i, (ini, _fim, chave) in enumerate(grades):
            if ini <= m.start():
                alvo = chave
        if alvo:
            encontrados.append(alvo)
    return encontrados


def extrair_card(html, slug, grade_chave):
    """Devolve o HTML do card do slug que está dentro da grade indicada."""
    grades = grids_da_pagina(html)
    for i, (ini, fim, chave) in enumerate(grades):
        if chave != grade_chave:
            continue
        r_ini, r_fim = regiao_da_grade(html, grades, i)
        for m in RE_CARD.finditer(html, r_ini, r_fim):
            ref = RE_SLUG_CARD.search(m.group(0))
            if ref and ref.group(1) == slug:
                return m.group(0).strip()
    return None


def imagem_da_pagina(html):
    m = RE_FOTO.search(html)
    if not m:
        return ""
    src = m.group(1).split("?")[0].strip()
    src = re.sub(r"^\.\./", "", src)
    return src


def pagina_catalogo(catalogo, slug):
    for i, p in enumerate(catalogo):
        if p.get("slug") == slug:
            return i, p
    return -1, None


# --------------------------------------------------------------------------- #
# manifesto
# --------------------------------------------------------------------------- #
def carregar_manifesto():
    return carregar_json(MANIFESTO, {"descricao": "Produtos que NUNCA podem sumir do site.",
                                    "versao": 1, "atualizado_em": _hoje_iso,
                                    "produtos": []})


def salvar_manifesto(manifesto):
    manifesto["atualizado_em"] = _hoje_iso
    manifesto["produtos"] = sorted(manifesto["produtos"], key=lambda p: p.get("slug", ""))
    salvar_json(MANIFESTO, manifesto)


def entrada_do_estado_atual(slug, catalogo, existente=None):
    """Monta a entrada do manifesto a partir dos arquivos atuais (estado saudável)."""
    pagina = os.path.join(REPO_DIR, "p", f"{slug}.html")
    if not os.path.exists(pagina):
        return None
    html = ler(pagina)

    idx, cat = pagina_catalogo(catalogo, slug)
    link = ""
    m_btn = re.search(r'<a\s+class="btn"[^>]*href="([^"]+)"', html)
    if m_btn:
        link = normalizar_link(m_btn.group(1))
    if not link and cat:
        link = normalizar_link(cat.get("link", ""))

    cartoes = []
    for pg in PAGINAS_RAIZ:
        caminho = os.path.join(REPO_DIR, pg)
        if not os.path.exists(caminho):
            continue
        for chave in cards_da_pagina(ler(caminho), slug):
            cartoes.append({"pagina": pg, "grid": chave})

    sitemap_loc = ""
    sm = os.path.join(REPO_DIR, "sitemap.xml")
    if os.path.exists(sm):
        for loc in re.findall(r'<loc>([^<]+)</loc>', ler(sm)):
            if loc.rstrip("/").endswith(f"/p/{slug}.html"):
                sitemap_loc = loc.strip()
                break

    imagem = imagem_da_pagina(html) or (f"img/{slug}.png")
    titulo = ""
    if cat:
        titulo = cat.get("title", "")
    if not titulo:
        m = RE_TITULO.search(html)
        if m:
            titulo = re.sub(r"\s+—\s+Renato Penner.*$", "", m.group(1)).strip()

    entrada = {
        "slug": slug,
        "titulo": titulo,
        "link": link,
        "pagina": f"p/{slug}.html",
        "imagem": imagem,
        "sitemap": sitemap_loc,
        "cartoes": cartoes,
    }
    if existente:
        entrada["fixado"] = bool(existente.get("fixado"))
        if existente.get("imagem_sha256"):
            entrada["imagem_sha256"] = existente["imagem_sha256"]
    else:
        entrada["fixado"] = False
    return entrada


def gerar_manifesto():
    """Registra no manifesto todo p/*.html que ainda não está protegido. NUNCA remove."""
    manifesto = carregar_manifesto()
    catalogo = carregar_json(CATALOGO, [])
    por_slug = {p["slug"]: p for p in manifesto["produtos"]}
    novos = 0
    paginas = sorted(f for f in os.listdir(os.path.join(REPO_DIR, "p")) if f.endswith(".html"))
    for arquivo in paginas:
        slug = arquivo[:-5]
        existente = por_slug.get(slug)
        entrada = entrada_do_estado_atual(slug, catalogo, existente)
        if not entrada:
            continue
        if existente is None:
            manifesto["produtos"].append(entrada)
            por_slug[slug] = entrada
            novos += 1
            log(f"  [proteção] novo produto registrado: {slug}")
        else:
            # Atualiza só campos estruturais que podem evoluir (cards, sitemap, imagem).
            # Nunca sobrescreve link/fixado/hash de um produto já protegido.
            if entrada.get("cartoes") and entrada["cartoes"] != existente.get("cartoes"):
                existente["cartoes"] = entrada["cartoes"]
            if entrada.get("sitemap") and not existente.get("sitemap"):
                existente["sitemap"] = entrada["sitemap"]
            if entrada.get("imagem") and not existente.get("imagem"):
                existente["imagem"] = entrada["imagem"]
            if entrada.get("titulo"):
                existente["titulo"] = entrada["titulo"]
            por_slug[slug] = existente
    salvar_manifesto(manifesto)
    log(f"[proteção] manifesto com {len(manifesto['produtos'])} produtos ({novos} novos).")
    return manifesto


# --------------------------------------------------------------------------- #
# verificação
# --------------------------------------------------------------------------- #
def verificar(manifesto=None):
    """Devolve lista de problemas encontrados."""
    manifesto = manifesto or carregar_manifesto()
    catalogo = carregar_json(CATALOGO, [])
    problemas = []

    if not manifesto.get("produtos"):
        problemas.append({"slug": "-", "tipo": "manifesto_vazio",
                          "detalhe": "manifesto sem produtos; rode --gerar"})
        return problemas

    htmls = {}
    for pg in PAGINAS_RAIZ:
        caminho = os.path.join(REPO_DIR, pg)
        if os.path.exists(caminho):
            htmls[pg] = ler(caminho)
    sitemap = ler(os.path.join(REPO_DIR, "sitemap.xml")) if os.path.exists(os.path.join(REPO_DIR, "sitemap.xml")) else ""

    for prod in manifesto["produtos"]:
        slug = prod["slug"]
        pagina = os.path.join(REPO_DIR, prod["pagina"])
        if not os.path.exists(pagina):
            problemas.append({"slug": slug, "tipo": "pagina_ausente", "detalhe": prod["pagina"]})
        else:
            html = ler(pagina)
            link = normalizar_link(prod.get("link", ""))
            if link and link not in html.replace("&amp;", "&"):
                problemas.append({"slug": slug, "tipo": "pagina_link_divergente",
                                  "detalhe": f"esperado {link}"})

        _i, cat = pagina_catalogo(catalogo, slug)
        if cat is None:
            problemas.append({"slug": slug, "tipo": "catalogo_ausente", "detalhe": "dados/produtos.json"})
        elif normalizar_link(cat.get("link")) != normalizar_link(prod.get("link")):
            problemas.append({"slug": slug, "tipo": "catalogo_link_divergente",
                              "detalhe": f"catálogo: {cat.get('link')} | esperado: {prod.get('link')}"})

        for cartao in prod.get("cartoes", []):
            pg = cartao["pagina"]
            chave = cartao["grid"]
            html = htmls.get(pg, "")
            if not html:
                problemas.append({"slug": slug, "tipo": "pagina_ausente", "detalhe": pg})
                continue
            if chave not in cards_da_pagina(html, slug):
                problemas.append({"slug": slug, "tipo": "card_ausente",
                                  "detalhe": f"{pg} ({chave})"})

        if prod.get("sitemap") and prod["sitemap"] not in sitemap:
            problemas.append({"slug": slug, "tipo": "sitemap_ausente", "detalhe": prod["sitemap"]})

        imagem = prod.get("imagem") or ""
        caminho_img = os.path.join(REPO_DIR, imagem) if imagem else ""
        if imagem and not os.path.exists(caminho_img):
            problemas.append({"slug": slug, "tipo": "imagem_ausente", "detalhe": imagem})
        elif imagem and prod.get("fixado") and prod.get("imagem_sha256"):
            if sha256(caminho_img) != prod["imagem_sha256"]:
                problemas.append({"slug": slug, "tipo": "imagem_trocada",
                                  "detalhe": f"{imagem} (hash diferente do fixado)"})

    return problemas


# --------------------------------------------------------------------------- #
# restauração
# --------------------------------------------------------------------------- #
def restaurar(manifesto=None):
    manifesto = manifesto or carregar_manifesto()
    catalogo = carregar_json(CATALOGO, [])
    problemas = verificar(manifesto)
    if not problemas:
        log("[proteção] tudo certo: nenhum produto removido.")
        return True, []

    log(f"[proteção] {len(problemas)} problema(s) encontrado(s). Restaurando...")
    nao_recuperavel = []

    for prod in manifesto["produtos"]:
        slug = prod["slug"]
        meus = [p for p in problemas if p["slug"] == slug]
        if not meus:
            continue
        tipos = {p["tipo"] for p in meus}

        # 1. catálogo
        if tipos & {"catalogo_ausente", "catalogo_link_divergente"}:
            idx, atual = pagina_catalogo(catalogo, slug)
            backup_cat = carregar_json(BACKUP_CATALOGO, [])
            _bi, de_backup = pagina_catalogo(backup_cat, slug)
            if idx >= 0:
                atual["link"] = prod.get("link", atual.get("link", ""))
            elif de_backup is not None:
                catalogo.append(de_backup)
            else:
                if idx < 0:
                    catalogo.append({
                        "slug": slug, "title": prod.get("titulo", slug),
                        "file": f"{slug}.html", "cat": "Mercado Livre",
                        "link": prod.get("link", ""), "preco_de": "", "preco_por": "",
                        "preco_cartao": "", "cupom": "", "ultima_conferencia": _hoje,
                    })
            log(f"  [proteção] catálogo restaurado: {slug}")

        # 2. página
        if tipos & {"pagina_ausente", "pagina_link_divergente"}:
            origem = os.path.join(BACKUP_PAGINAS, f"{slug}.html")
            destino = os.path.join(REPO_DIR, prod["pagina"])
            if os.path.exists(origem):
                escrever(destino, ler(origem))
                log(f"  [proteção] página restaurada: {prod['pagina']}")
            else:
                nao_recuperavel.append(f"{slug}: página sem backup")

        # 3. cards
        htmls = {pg: ler(os.path.join(REPO_DIR, pg)) for pg in PAGINAS_RAIZ
                 if os.path.exists(os.path.join(REPO_DIR, pg))}
        for cartao in prod.get("cartoes", []):
            pg = cartao["pagina"]
            chave = cartao["grid"]
            if pg not in htmls:
                nao_recuperavel.append(f"{slug}: página {pg} não existe")
                continue
            if chave in cards_da_pagina(htmls[pg], slug):
                continue
            backup_card = os.path.join(BACKUP_CARTOES, pg, f"{slug}@{chave.replace(':', '-')}.html")
            if not os.path.exists(backup_card):
                nao_recuperavel.append(f"{slug}: card de {pg} ({chave}) sem backup")
                continue
            card_html = ler(backup_card).strip()
            html = htmls[pg]
            sep = "\r\n" if "\r\n" in html else "\n"
            grades = grids_da_pagina(html)
            inseriu = False
            for i, (_ini, fim, c) in enumerate(grades):
                if c == chave:
                    html = html[:fim] + sep + card_html + sep + html[fim:]
                    inseriu = True
                    break
            if not inseriu:
                nao_recuperavel.append(f"{slug}: grade {chave} não existe em {pg}")
                continue
            escrever(os.path.join(REPO_DIR, pg), html)
            htmls[pg] = html
            log(f"  [proteção] card restaurado: {slug} em {pg}")

        # 4. sitemap
        if tipos & {"sitemap_ausente"}:
            caminho_sm = os.path.join(REPO_DIR, "sitemap.xml")
            sm = ler(caminho_sm)
            if prod.get("sitemap") and prod["sitemap"] not in sm:
                if "</urlset>" in sm:
                    sm = sm.replace("</urlset>",
                                    f'  <url><loc>{prod["sitemap"]}</loc><lastmod>{_hoje_iso}</lastmod></url>\n</urlset>')
                    escrever(caminho_sm, sm)
                    log(f"  [proteção] sitemap restaurado: {prod['sitemap']}")

        # 5. imagem
        if tipos & {"imagem_ausente", "imagem_trocada"}:
            origem = os.path.join(BACKUP_IMG, os.path.basename(prod.get("imagem", "")))
            destino = os.path.join(REPO_DIR, prod.get("imagem", ""))
            if origem and os.path.exists(origem):
                os.makedirs(os.path.dirname(destino), exist_ok=True)
                with open(origem, "rb") as fr, open(destino, "wb") as fw:
                    fw.write(fr.read())
                log(f"  [proteção] imagem restaurada: {prod['imagem']}")
            else:
                nao_recuperavel.append(f"{slug}: imagem sem backup")

    salvar_json(CATALOGO, catalogo)
    restantes = verificar(manifesto)
    for p in restantes:
        log(f"  [proteção] PENDENTE: {p['slug']} / {p['tipo']} / {p['detalhe']}")
    if nao_recuperavel:
        for item in nao_recuperavel:
            log(f"  [proteção] NÃO RECUPERÁVEL: {item}")
    ok = not restantes
    log("[proteção] restauração concluída." if ok else "[proteção] restauração INCOMPLETA.")
    return ok, nao_recuperavel


# --------------------------------------------------------------------------- #
# backup
# --------------------------------------------------------------------------- #
def atualizar_backup(manifesto=None):
    manifesto = manifesto or carregar_manifesto()
    catalogo = carregar_json(CATALOGO, [])
    problemas = verificar(manifesto)
    com_problema = {p["slug"] for p in problemas}
    os.makedirs(BACKUP_PAGINAS, exist_ok=True)
    os.makedirs(BACKUP_CARTOES, exist_ok=True)
    os.makedirs(BACKUP_IMG, exist_ok=True)

    copiados = 0
    for prod in manifesto["produtos"]:
        slug = prod["slug"]
        if slug in com_problema:
            log(f"  [proteção] backup ignorado para {slug} (estado com problema)")
            continue
        pagina = os.path.join(REPO_DIR, prod["pagina"])
        if not os.path.exists(pagina):
            continue
        escrever(os.path.join(BACKUP_PAGINAS, f"{slug}.html"), ler(pagina))
        html = ler(pagina)
        for cartao in prod.get("cartoes", []):
            pg, chave = cartao["pagina"], cartao["grid"]
            caminho = os.path.join(REPO_DIR, pg)
            if not os.path.exists(caminho):
                continue
            card_html = extrair_card(ler(caminho), slug, chave)
            if card_html:
                escrever(os.path.join(BACKUP_CARTOES, pg,
                                      f"{slug}@{chave.replace(':', '-')}.html"), card_html)
        # imagem: só guarda cópia nos produtos "fixados" (evita ~18 MB de backup no repo)
        imagem = prod.get("imagem") or ""
        if imagem and prod.get("fixado"):
            destino_img = os.path.join(BACKUP_IMG, os.path.basename(imagem))
            if os.path.exists(os.path.join(REPO_DIR, imagem)):
                with open(os.path.join(REPO_DIR, imagem), "rb") as fr, open(destino_img, "wb") as fw:
                    fw.write(fr.read())
        copiados += 1

    salvar_json(BACKUP_CATALOGO, catalogo)
    log(f"[proteção] backup atualizado para {copiados} produto(s).")
    return copiados


# --------------------------------------------------------------------------- #
# comandos de manutenção
# --------------------------------------------------------------------------- #
def atualizar_produto(slug, refixar=False):
    manifesto = carregar_manifesto()
    catalogo = carregar_json(CATALOGO, [])
    por_slug = {p["slug"]: p for p in manifesto["produtos"]}
    existente = por_slug.get(slug)
    entrada = entrada_do_estado_atual(slug, catalogo, existente)
    if not entrada:
        log(f"[proteção] {slug}: página p/{slug}.html não existe.")
        return False
    if refixar:
        imagem = os.path.join(REPO_DIR, entrada.get("imagem", ""))
        if os.path.exists(imagem):
            entrada["imagem_sha256"] = sha256(imagem)
            os.makedirs(BACKUP_IMG, exist_ok=True)
            with open(imagem, "rb") as fr, open(os.path.join(BACKUP_IMG, os.path.basename(imagem)), "wb") as fw:
                fw.write(fr.read())
            entrada["fixado"] = True
            log(f"[proteção] {slug}: imagem refixada ({entrada['imagem']}).")
    if existente is None:
        manifesto["produtos"].append(entrada)
    else:
        por_slug[slug].update(entrada)
    salvar_manifesto(manifesto)
    log(f"[proteção] {slug}: manifesto atualizado.")
    # atualiza também o backup do produto
    atualizar_backup(manifesto)
    return True


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #
def main(argv):
    acao = "--restaurar"
    alvo = None
    args = [a for a in argv[1:]]
    if args:
        acao = args[0]
        if len(args) > 1:
            alvo = args[1]

    if acao in ("-h", "--help"):
        print(__doc__)
        return 0

    if acao in ("--verificar", "--check"):
        problemas = verificar()
        if not problemas:
            log("[proteção] OK: todos os produtos protegidos estão no site.")
            return 0
        for p in problemas:
            log(f"[proteção] PROBLEMA: {p['slug']} / {p['tipo']} / {p['detalhe']}")
        log(f"[proteção] {len(problemas)} problema(s). Rode --restaurar.")
        return 1

    if acao == "--gerar":
        gerar_manifesto()
        return 0

    if acao == "--backup":
        atualizar_backup()
        return 0

    if acao == "--atualizar":
        if not alvo:
            log("[proteção] informe o slug: --atualizar <slug>")
            return 2
        return 0 if atualizar_produto(alvo) else 2

    if acao == "--refixar":
        if not alvo:
            log("[proteção] informe o slug: --refixar <slug>")
            return 2
        return 0 if atualizar_produto(alvo, refixar=True) else 2

    if acao == "--rotina":
        manifesto = gerar_manifesto()
        ok, _pend = restaurar(manifesto)
        if ok:
            atualizar_backup(manifesto)
        return 0 if ok else 2

    # padrão: restaurar
    ok, _pend = restaurar()
    return 0 if ok else 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
