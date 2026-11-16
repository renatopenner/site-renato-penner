"""Adiciona o Kit 2 Walkie-Talkies Baofeng BF-777S ao site loja.pennertech.com.br."""
import json
import os
import re
from PIL import Image

BASE = r"C:\Users\renat\SitesGithub\site-renato-penner"
FOTO_ORIG = r"C:\Users\renat\.gemini\antigravity\brain\a7825e10-5c25-4b7b-be18-1c00467a9e4f\.user_uploaded\media_1794867033108_c95f5ec5.jpg"
SLUG = "walkie-talkie-baofeng-bf-777s"
DATA = "16/11/2026"
DATA_ISO = "2026-11-16"
MARCA_W, MARCA_H = 1120, 840

PRODUTO = {
    "slug": SLUG,
    "titulo_card": "Walkie-Talkie Baofeng BF-777S (Kit 2 Rádios) 16 Canais UHF",
    "h1": "Kit 2 Rádios Comunicadores Baofeng BF-777S UHF 400–470 MHz 5W com 16 Canais e Homologação Anatel",
    "meta_desc": "Kit com 2 walkie-talkies Baofeng BF-777S, 1º mais vendido na categoria no Mercado Livre (nota 4.8 em 6.669 opiniões). 16 canais UHF 400–470 MHz, 5W de potência, bateria 1,5 Ah (8h), função VOX, lanterna e homologação Anatel nº 103612114108.",
    "cat_badge": "Mercado Livre · 1º Mais Vendido · Nota 4.8 ★★★★★ (6.669)",
    "cat_css": "perifericos",
    "categoria_nome": "Periféricos e acessórios",
    "sub": "Kit 2 Rádios · 16 Canais UHF (400–470 MHz) · 5W · Bateria 1,5 Ah (8h) · Anatel 103612114108",
    "resumo": "O rádio comunicador mais vendido do Mercado Livre (nota 4.8 em mais de 6.600 avaliações). Kit com 2 unidades Baofeng BF-777S na faixa UHF 400–470 MHz, 16 canais, potência de 5W, função mãos livres VOX, lanterna integrada e bateria recarregável para até 8 horas de uso.",
    "link": "https://meli.la/1rSgMyf",
    "preco_de": "",
    "preco_por": "R$ 99,90",
    "preco_cartao": "18x R$ 6,72 cartão Mercado Pago · R$ 3 de cashback Meli Dólar",
    "desconto": "",
    "porque": "Em suporte de campo, passagem de cabos entre andares, eventos, portaria ou comboios em viagem onde o sinal de celular falha ou é lento para coordenação imediata, um par de rádios UHF dedicados resolve a comunicação com um aperto de botão (PTT). O Baofeng BF-777S é o clássico absoluto de custo-benefício: robusto, simples de operar via seletor rotativo de 16 canais, homologado pela Anatel (nº 103612114108) e com mais de 6.600 avaliações mantendo média 4.8 por menos de R$ 100 o par.",
    "destaques": [
        ("1º mais vendido e nota 4.8", "Líder de vendas em Walkie-talkies no Mercado Livre com 6.669 opiniões reais de compradores"),
        ("Faixa UHF 400–470 MHz com 5W", "16 canais pré-programáveis com boa penetração em ambientes fechados, galpões, prédios e áreas urbanas"),
        ("Alcance de até 6 km (campo aberto)", "Cobertura nominal de até 6 km sem barreiras; ideal para equipes de campo, obras, segurança e trilhas"),
        ("Bateria recarregável de 1,5 Ah", "Autonomia de até 8 horas de operação contínua com base carregadora inclusa (escolha 127/220V, 127V ou 220V no anúncio)"),
        ("Função VOX (mãos livres) e lanterna", "Permite transmissão ativada por voz sem apertar o PTT e conta com lanterna LED embutida no topo"),
        ("Homologado pela Anatel", "Certificação Anatel nº 103612114108, garantindo conformidade técnica para uso regular no Brasil"),
    ],
    "ficha": [
        "Marca / Fabricante: Baofeng (Fujian Baofeng Electronic Co., Ltd.)",
        "Modelo: BF-777S (Cor: Preto)",
        "Quantidade no kit: 2 rádios comunicadores com baterias recarregáveis e bases carregadoras",
        "Faixa de frequência: UHF 400 MHz – 470 MHz (tecnologia analógica)",
        "Potência de saída: 5 W",
        "Quantidade de canais: 16 canais",
        "Alcance máximo nominal: até 6 km (em campo aberto, sem obstáculos)",
        "Bateria: Íons de lítio recarregável de 1,5 Ah (1500 mAh) · autonomia estimada de 8 horas",
        "Recursos: Função mãos livres (VOX), lanterna LED integrada e resistência à água",
        "Homologação Anatel Nº: 103612114108",
        "Voltagem do carregador: selecionar 127/220V, 127V ou 220V no ato da compra",
    ],
    "pros": [
        "1º lugar em Walkie-talkies no Mercado Livre com nota 4.8 de 5 em 6.669 avaliações",
        "Excelente custo-benefício: kit completo com 2 rádios por R$ 99,90 (e opção de R$ 96,32 no ML Negócios a partir de 2 kits)",
        "Homologação Anatel nº 103612114108",
        "Operação direta e intuitiva com seletor físico de 16 canais, sem menus complexos",
        "Bateria recarregável de 1,5 Ah com até 8 horas de uso e função VOX mãos livres",
    ],
    "contras": [
        "O alcance máximo de 6 km refere-se a campo aberto sem barreiras; dentro de prédios ou áreas urbanas densas o alcance real cai proporcionalmente aos obstáculos",
        "Atenção na hora da compra para selecionar a voltagem correta do carregador (127/220V, 127V ou 220V) nas variações do anúncio",
        "Tecnologia analógica sem visor digital, Bluetooth ou Wi-Fi (focado em simplicidade e robustez)",
    ],
    "para_quem": "Técnicos de TI e cabeamento estruturado trabalhando em equipes separadas por andares/salas, equipes de segurança, portaria, logística, depósitos, eventos, obras e passeios/trilhas em grupo.",
}


def prepara_imagem():
    im = Image.open(FOTO_ORIG).convert("RGB")
    canvas = Image.new("RGB", (MARCA_W, MARCA_H), (255, 255, 255))
    pad = 24
    max_w = MARCA_W - 2 * pad
    max_h = MARCA_H - 2 * pad
    scale = min(max_w / im.width, max_h / im.height)
    nw = int(round(im.width * scale))
    nh = int(round(im.height * scale))
    im_res = im.resize((nw, nh), Image.Resampling.LANCZOS)
    canvas.paste(im_res, ((MARCA_W - nw) // 2, (MARCA_H - nh) // 2))

    jpg_path = os.path.join(BASE, "img", f"{SLUG}.jpg")
    webp_path = os.path.join(BASE, "img", f"{SLUG}.webp")
    canvas.save(jpg_path, "JPEG", quality=88, optimize=True)
    canvas.save(webp_path, "WEBP", quality=85, method=6)
    print("Imagens geradas:", jpg_path, os.path.getsize(jpg_path), "|", webp_path, os.path.getsize(webp_path))


def bloco_preco(p):
    html = '<div class="preco">'
    html += f'<span class="de">{"de " + p["preco_de"] if p["preco_de"] else ""}</span>'
    html += f'<span class="por">por {p["preco_por"]}</span>'
    if p["preco_cartao"]:
        html += f'<span class="cartao">{p["preco_cartao"]}</span>'
    nota = f'preço conferido em {DATA}'
    if p["desconto"]:
        nota += f' · {p["desconto"]}'
    html += f"<small>{nota}</small></div>"
    return html


def gera_card(p):
    busca = re.sub(r"[^a-z0-9 ]", " ", (p["titulo_card"] + " " + p["sub"] + " " + p["slug"] + " baofeng radio comunicador").lower())
    busca = re.sub(r"\s+", " ", busca).strip()
    return f'''<article class="card" data-cat="{p['cat_css']}" data-busca="{busca}">
      <div class="thumbwrap"><a class="thumb" href="{p['link']}" target="_blank" rel="sponsored nofollow noopener"><span class="badge">Mercado Livre · 1º Mais Vendido</span><picture><source srcset="img/{p['slug']}.webp" type="image/webp"><img width="1120" height="840" src="img/{p['slug']}.jpg" alt="{p['titulo_card']}" loading="lazy"></picture></a></div>
      <div class="body">
        <span class="cat">{p['categoria_nome']}</span>
        <h3><a href="p/{p['slug']}.html" style="color:inherit">{p['titulo_card']}</a></h3>
        <span class="sub">{p['sub']}</span>
        <p class="resumo">{p['resumo']}</p>
        {bloco_preco(p)}
        <div class="btns">
          <a class="btn" href="{p['link']}" target="_blank" rel="sponsored nofollow noopener">Ver oferta →</a><a class="btn ghost" href="p/{p['slug']}.html">Detalhes</a>
        </div>
      </div>
    </article>'''


def gera_pagina(p, template):
    ini = template.index('<main class="wrap">')
    fim = template.index('</main>') + len('</main>')
    cabeca = template[:ini]
    cauda = template[fim:]

    cabeca = re.sub(r"<title>.*?</title>", f"<title>{p['titulo_card']} — Penner Tech</title>", cabeca, flags=re.S)
    cabeca = re.sub(r'<meta name="description" content="[^"]*"', f'<meta name="description" content="{p["meta_desc"]}"', cabeca)
    cabeca = re.sub(r'<link rel="canonical" href="[^"]*"', f'<link rel="canonical" href="https://loja.pennertech.com.br/p/{p["slug"]}.html"', cabeca)
    cabeca = re.sub(r'<meta property="og:title"[^>]*>', f'<meta property="og:title" content="{p["titulo_card"]} — Penner Tech">', cabeca)
    cabeca = re.sub(r'<meta property="og:description" content="[^"]*"', f'<meta property="og:description" content="{p["meta_desc"]}"', cabeca)
    cabeca = re.sub(r'<meta property="og:url" content="[^"]*"', f'<meta property="og:url" content="https://loja.pennertech.com.br/p/{p["slug"]}.html"', cabeca)
    cabeca = re.sub(r'<meta name="twitter:title" content="[^"]*"', f'<meta name="twitter:title" content="{p["titulo_card"]} — Penner Tech">', cabeca)
    cabeca = re.sub(r'<meta name="twitter:description" content="[^"]*"', f'<meta name="twitter:description" content="{p["meta_desc"]}"', cabeca)
    cabeca = re.sub(r'<meta name="build" content="[^"]*">', f'<meta name="build" content="{DATA_ISO} 19:20">', cabeca)

    cabeca = cabeca.replace('class="link on"', 'class="link "')
    cabeca = cabeca.replace(f'class="link " href="../{p["cat_css"]}.html"', f'class="link on" href="../{p["cat_css"]}.html"')

    destaques = "".join(f'<li class="dt"><strong>{t}:</strong> {d}</li>' for t, d in p["destaques"])
    ficha = "".join(f'<li class="dt">{x}</li>' for x in p["ficha"])
    pros = "".join(f'<li class="ok">{x}</li>' for x in p["pros"])
    contras = "".join(f'<li class="no">{x}</li>' for x in p["contras"])

    bc = json.dumps({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Início", "item": "https://loja.pennertech.com.br/"},
            {"@type": "ListItem", "position": 2, "name": p["categoria_nome"], "item": f"https://loja.pennertech.com.br/{p['cat_css']}.html"},
            {"@type": "ListItem", "position": 3, "name": p["h1"], "item": f"https://loja.pennertech.com.br/p/{p['slug']}.html"},
        ],
    }, ensure_ascii=False)

    corpo = f'''<main class="wrap">
  <div class="migalha"><a href="../index.html">Início</a> /
    <a href="../{p['cat_css']}.html">{p['categoria_nome']}</a> / {p['titulo_card']}</div>
  <section class="prod">
    <div class="foto"><a href="{p['link']}" target="_blank" rel="sponsored nofollow noopener" title="Ver oferta no Mercado Livre"><picture><source srcset="../img/{p['slug']}.webp" type="image/webp"><img width="1120" height="840" fetchpriority="high" src="../img/{p['slug']}.jpg" alt="{p['titulo_card']}"></picture></a></div>
    <div>
      <span class="cat" style="color:var(--acento);font-size:11px;font-weight:800;letter-spacing:.1em">{p['cat_badge']}</span>
      <h1>{p['h1']}</h1>
      <div class="pmeta">{p['sub']}</div>
      {bloco_preco(p)}
      <div class="btns" style="margin-top:18px">
        <a class="btn" href="{p['link']}" target="_blank" rel="sponsored nofollow noopener">Ver oferta no Mercado Livre →</a>
      </div>
      <div class="box"><h2>Por que eu recomendo</h2><p style="color:var(--texto-corpo);font-size:14.5px">{p['porque']}</p></div>
      <div class="box"><h2>Destaques e Funções</h2><ul>{destaques}</ul></div>
      <div class="box"><h2>Ficha Técnica e Conteúdo</h2><ul>{ficha}</ul></div>
      <div class="box"><h2>Prós</h2><ul>{pros}</ul><h2 style="margin-top:14px">Contras</h2><ul>{contras}</ul></div>
      <div class="box"><h2>Para quem serve</h2><p style="color:var(--texto-corpo);font-size:14.5px">{p['para_quem']}</p></div>
    </div>
  </section>

<script type="application/ld+json">{bc}</script>
</main>'''

    preco_num = re.sub(r"[^\d,]", "", p["preco_por"]).replace(".", "").replace(",", ".")
    ld = (
        '<script type="application/ld+json">'
        + json.dumps({
            "@context": "https://schema.org",
            "@type": "Product",
            "name": p["titulo_card"],
            "description": p["meta_desc"],
            "brand": {"@type": "Brand", "name": "Baofeng"},
            "offers": {
                "@type": "Offer",
                "url": p["link"],
                "price": preco_num,
                "priceCurrency": "BRL",
                "availability": "https://schema.org/InStock",
                "itemCondition": "https://schema.org/NewCondition",
            },
            "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.8", "reviewCount": "6669"},
            "url": f"https://loja.pennertech.com.br/p/{p['slug']}.html",
            "image": f"https://loja.pennertech.com.br/img/{p['slug']}.jpg",
        }, ensure_ascii=False)
        + "</script>"
    )
    cauda = re.sub(r'<script type="application/ld\+json">.*?</script>', ld, cauda, count=1, flags=re.S)
    return cabeca + corpo + cauda


def main():
    p = PRODUTO
    prepara_imagem()

    template_path = os.path.join(BASE, "p", "luva-isolante-eletricista-400v.html")
    with open(template_path, encoding="utf-8") as f:
        template = f.read()

    page_html = gera_pagina(p, template)
    page_path = os.path.join(BASE, "p", f"{SLUG}.html")
    with open(page_path, "w", encoding="utf-8") as f:
        f.write(page_html)
    print("Página criada:", page_path)

    caminho_json = os.path.join(BASE, "dados", "produtos.json")
    with open(caminho_json, encoding="utf-8") as f:
        dados = json.load(f)
    if not any(x.get("slug") == SLUG for x in dados):
        dados.append({
            "slug": SLUG,
            "title": p["titulo_card"],
            "file": f"{SLUG}.html",
            "cat": p["cat_badge"],
            "link": p["link"],
            "preco_de": p["preco_de"],
            "preco_por": p["preco_por"],
            "preco_cartao": p["preco_cartao"],
            "cupom": "",
            "ultima_conferencia": DATA,
        })
        with open(caminho_json, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
        print("produtos.json atualizado com", SLUG)

    card_html = gera_card(p)
    for nome in ["index.html", "perifericos.html"]:
        caminho = os.path.join(BASE, nome)
        with open(caminho, encoding="utf-8") as f:
            content = f.read()
        if f"p/{SLUG}.html" in content:
            print(f"Card já existe em {nome}")
            continue
        pos = content.find('<article class="card"')
        if pos < 0:
            raise RuntimeError(f"Não achou card em {nome}")
        pos = content.rfind("\n", 0, pos) + 1
        content = content[:pos] + "    " + card_html + "\n" + content[pos:]
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Card inserido em {nome}")

    sm_path = os.path.join(BASE, "sitemap.xml")
    with open(sm_path, encoding="utf-8") as f:
        sm_content = f.read()
    if f"{SLUG}.html" not in sm_content:
        item = f"  <url><loc>https://loja.pennertech.com.br/p/{SLUG}.html</loc><lastmod>{DATA_ISO}</lastmod></url>\n"
        sm_content = sm_content.replace("</urlset>", item + "</urlset>")
        with open(sm_path, "w", encoding="utf-8") as f:
            f.write(sm_content)
        print("sitemap.xml atualizado")


if __name__ == "__main__":
    main()
