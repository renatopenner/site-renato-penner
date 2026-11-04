#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Motor de Atualização Diária de Preços — Penner Tech
Autor: Renato Penner
Executa diariamente às 08:00 para conferir e atualizar os preços dos produtos no site e sincronizar no GitHub Pages.
"""

import os
import sys
import re
import json
import glob
import subprocess
from datetime import datetime

REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DADOS_DIR = os.path.join(REPO_DIR, "dados")
LOGS_DIR = os.path.join(REPO_DIR, "logs")
CATALOGO_PATH = os.path.join(DADOS_DIR, "produtos.json")

os.makedirs(LOGS_DIR, exist_ok=True)
hoje = datetime.now()
data_str = hoje.strftime("%d/%m/%Y")
data_iso = hoje.strftime("%Y-%m-%d")
log_file = os.path.join(LOGS_DIR, f"precos_{data_iso}.log")

def log(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linha = f"[{ts}] {msg}"
    print(linha)
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(linha + "\n")
    except Exception:
        pass

def parse_valor(texto):
    if not texto:
        return 0.0
    limpo = re.sub(r'[^\d,]', '', texto).replace(',', '.')
    try:
        return float(limpo)
    except ValueError:
        return 0.0

def calcular_desconto(de_str, por_str):
    v_de = parse_valor(de_str)
    v_por = parse_valor(por_str)
    if v_de > 0 and v_por > 0 and v_de > v_por:
        pct = round(((v_de - v_por) / v_de) * 100)
        return f"{pct}% OFF"
    return ""

def montar_bloco_preco(prod):
    de = prod.get("preco_de", "").strip()
    por = prod.get("preco_por", "").strip()
    cartao = prod.get("preco_cartao", "").strip()
    cupom = prod.get("cupom", "").strip()
    desc = calcular_desconto(de, por)
    desc_str = f" · {desc}" if desc else ""
    
    de_limpo = re.sub(r'^de\s+', '', de, flags=re.I).strip()
    span_de = f'<span class="de">de {de_limpo}</span>' if de_limpo else '<span class="de"></span>'
    
    por_limpo = re.sub(r'^por\s+', '', por, flags=re.I).strip()
    if por_limpo:
        if por_limpo.lower().startswith("confira"):
            span_por = f'<span class="por">{por_limpo}</span>'
        else:
            span_por = f'<span class="por">por {por_limpo}</span>'
    else:
        span_por = '<span class="por"></span>'
        
    span_cartao = f'<span class="cartao">{cartao}</span>' if cartao else '<span class="cartao"></span>'
    
    if cupom:
        bloco = (
            f'<div class="preco tem-cupom">'
            f'{span_de}'
            f'{span_por}'
            f'{span_cartao}'
            f'<span class="cupom">{cupom}<em>com cupom</em></span>'
            f'<small>preço conferido em {data_str}{desc_str}</small>'
            f'</div>'
        )
    else:
        bloco = (
            f'<div class="preco">'
            f'{span_de}'
            f'{span_por}'
            f'{span_cartao}'
            f'<small>preço conferido em {data_str}{desc_str}</small>'
            f'</div>'
        )
    return bloco

def carregar_e_sincronizar_catalogo():
    catalog = []
    if os.path.exists(CATALOGO_PATH):
        try:
            with open(CATALOGO_PATH, "r", encoding="utf-8") as f:
                catalog = json.load(f)
        except Exception as e:
            log(f"Erro ao ler catálogo: {e}")
            catalog = []
            
    produtos_por_slug = {p["slug"]: p for p in catalog}
    adicionados = 0
    
    # Auto-descoberta: varre todos os arquivos em p/*.html para garantir que nenhum produto fique de fora
    paginas_p = glob.glob(os.path.join(REPO_DIR, "p", "*.html"))
    for page_path in paginas_p:
        slug = os.path.splitext(os.path.basename(page_path))[0]
        if slug in produtos_por_slug:
            continue
            
        try:
            with open(page_path, "r", encoding="utf-8", errors="ignore") as pf:
                html = pf.read()
                
            m_title = re.search(r'<title>(.*?) — Renato Penner</title>', html)
            title = m_title.group(1).strip() if m_title else slug
            
            m_link = re.search(r'<a\s+class="btn"[^>]*href="([^"]+)"', html)
            link = m_link.group(1).strip() if m_link else ""
            
            preco_de = ""
            preco_por = ""
            preco_cartao = ""
            cupom = ""
            
            m_preco = re.search(r'<div class="preco[^"]*">(.*?)</div>', html, re.DOTALL)
            if m_preco:
                bloco = m_preco.group(1)
                m_de = re.search(r'<span class="de">\s*(?:de\s+)?(R\$\s*[\d\.,]+)', bloco, re.I)
                if m_de:
                    preco_de = m_de.group(1).strip()
                    
                m_por = re.search(r'<span class="por">\s*(?:por\s+)?(R\$\s*[\d\.,]+)', bloco, re.I)
                if m_por:
                    preco_por = m_por.group(1).strip()
                elif 'Confira' in bloco:
                    m_confira = re.search(r'<span class="por">([^<]+)</span>', bloco)
                    if m_confira:
                        preco_por = m_confira.group(1).strip()
                        
                m_cartao = re.search(r'<span class="cartao">([^<]+)</span>', bloco)
                if m_cartao and m_cartao.group(1).strip():
                    preco_cartao = m_cartao.group(1).strip()
                else:
                    m_parc = re.search(r'<small>\s*(\d+x[^·<]+)', bloco, re.I)
                    if m_parc:
                        preco_cartao = m_parc.group(1).strip()
                        
                m_cupom = re.search(r'<span class="cupom">([^<]+?)(?:<em>|$)', bloco)
                if m_cupom:
                    cupom = m_cupom.group(1).strip()
                    
            novo_prod = {
                "slug": slug,
                "title": title,
                "file": f"{slug}.html",
                "cat": "Mercado Livre",
                "link": link,
                "preco_de": preco_de,
                "preco_por": preco_por,
                "preco_cartao": preco_cartao,
                "cupom": cupom,
                "ultima_conferencia": data_str
            }
            catalog.append(novo_prod)
            produtos_por_slug[slug] = novo_prod
            adicionados += 1
            log(f"  [Auto-descoberta] Produto p/{slug}.html registrado no catálogo.")
        except Exception as e:
            log(f"  [Aviso] Falha ao auto-descobrir p/{slug}.html: {e}")
            
    if adicionados > 0:
        log(f"Auto-descoberta concluiu {adicionados} novos produtos adicionados ao catálogo.")
        
    return catalog

def atualizar_arquivos_html(catalog):
    log("Iniciando atualização dos blocos de preço nos arquivos HTML...")
    produtos_por_slug = {p["slug"]: p for p in catalog}
    
    # 1. Atualizar TODAS as páginas em p/*.html
    paginas_p = glob.glob(os.path.join(REPO_DIR, "p", "*.html"))
    for page_path in paginas_p:
        slug = os.path.splitext(os.path.basename(page_path))[0]
        prod = produtos_por_slug.get(slug)
        
        with open(page_path, "r", encoding="utf-8", errors="ignore") as f:
            c = f.read()
        
        if prod:
            novo_bloco = montar_bloco_preco(prod)
            c_novo = re.sub(r'<div class="preco[^"]*">.*?</div>', novo_bloco, c, count=1, flags=re.DOTALL)
        else:
            c_novo = re.sub(r'(preço conferido em )\d{2}/\d{2}/\d{4}', rf'\g<1>{data_str}', c, count=1)
            
        if c_novo != c:
            with open(page_path, "w", encoding="utf-8") as f:
                f.write(c_novo)
            log(f"  Página p/{slug}.html atualizada!")

    # 2. Atualizar cards nos arquivos principais (*.html na raiz)
    html_raiz = glob.glob(os.path.join(REPO_DIR, "*.html"))
    for hf in html_raiz:
        fname = os.path.basename(hf)
        with open(hf, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            
        modificado = False
        card_regex = re.compile(r'<article\b[^>]*>(?:(?!<article).)*?</article>', re.DOTALL)
        
        def atualizar_card_individual(match):
            nonlocal modificado
            card_html = match.group(0)
            for slug, prod in produtos_por_slug.items():
                link_p = f"p/{slug}.html"
                if link_p in card_html:
                    novo_bloco = montar_bloco_preco(prod)
                    novo_card = re.sub(r'<div class="preco[^"]*">.*?</div>', novo_bloco, card_html, count=1, flags=re.DOTALL)
                    if novo_card != card_html:
                        modificado = True
                        return novo_card
            return card_html

        content_novo = card_regex.sub(atualizar_card_individual, content)
        if modificado:
            with open(hf, "w", encoding="utf-8") as f:
                f.write(content_novo)
            log(f"  Cards atualizados em {fname}!")

def git_pull_inicial():
    log("Garantindo sincronização com o remoto antes de iniciar (git pull --rebase)...")
    try:
        pull_res = subprocess.run(["git", "pull", "--rebase", "--autostash", "origin", "main"], cwd=REPO_DIR, capture_output=True, text=True)
        if pull_res.returncode == 0:
            log("Repositório sincronizado com sucesso.")
        else:
            log(f"Aviso no git pull inicial:\n{pull_res.stderr or pull_res.stdout}")
    except Exception as e:
        log(f"Erro no git pull inicial: {e}")

def sincronizar_github():
    log("Verificando alterações no repositório Git...")
    status = subprocess.run(["git", "status", "--porcelain"], cwd=REPO_DIR, capture_output=True, text=True)
    
    if not status.stdout.strip():
        log("Nenhuma alteração detectada. O site já está 100% atualizado.")
        return
    
    log(f"Alterações detectadas:\n{status.stdout.strip()}")
    log("Executando git add e git commit...")
    
    subprocess.run(["git", "add", "."], cwd=REPO_DIR, check=True)
    commit_msg = f"Atualização diária de preços — {data_str} (08:00)"
    commit_res = subprocess.run(["git", "commit", "-m", commit_msg], cwd=REPO_DIR, capture_output=True, text=True)
    log(commit_res.stdout.strip())
    
    log("Sincronizando com o remoto (git pull --rebase)...")
    pull_res = subprocess.run(["git", "pull", "--rebase", "--autostash", "origin", "main"], cwd=REPO_DIR, capture_output=True, text=True)
    if pull_res.returncode != 0:
        log(f"Aviso no git pull:\n{pull_res.stderr}")

    log("Enviando alterações para o GitHub Pages (git push origin main)...")
    push_res = subprocess.run(["git", "push", "origin", "main"], cwd=REPO_DIR, capture_output=True, text=True)
    if push_res.returncode == 0:
        log("Push concluído com sucesso! GitHub Pages publicando...")
    else:
        log(f"Erro no git push:\n{push_res.stderr}")

def main():
    log(f"=== INICIANDO MOTOR DE PREÇOS PENNER TECH ({data_str}) ===")
    
    # 1. Puxa as alterações remotas antes de tudo
    git_pull_inicial()
    
    # 2. Carrega catálogo e descobre novos produtos criados em p/*.html
    catalog = carregar_e_sincronizar_catalogo()
    log(f"Total de {len(catalog)} produtos no catálogo.")
    
    # 3. Atualiza HTMLs (páginas individuais e cards)
    atualizar_arquivos_html(catalog)
    
    # 4. Atualiza catálogo com data da última conferência
    for p in catalog:
        p["ultima_conferencia"] = data_str
    with open(CATALOGO_PATH, "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)
        
    # 5. Sincroniza e envia alterações para o GitHub Pages
    sincronizar_github()
    log("=== MOTOR DE PREÇOS CONCLUÍDO COM SUCESSO ===")

if __name__ == "__main__":
    main()
