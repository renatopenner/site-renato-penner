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
    
    if cupom:
        bloco = (
            f'<div class="preco tem-cupom">'
            f'<span class="de">de {de}</span>'
            f'<span class="por">por {por}</span>'
            f'<span class="cartao">{cartao}</span>'
            f'<span class="cupom">{cupom}<em>com cupom</em></span>'
            f'<small>preço conferido em {data_str}{desc_str}</small>'
            f'</div>'
        )
    else:
        bloco = (
            f'<div class="preco">'
            f'<span class="de">de {de}</span>'
            f'<span class="por">por {por}</span>'
            f'<span class="cartao">{cartao}</span>'
            f'<small>preço conferido em {data_str}{desc_str}</small>'
            f'</div>'
        )
    return bloco

def atualizar_arquivos_html(catalog):
    log("Iniciando atualização dos blocos de preço nos arquivos HTML...")
    produtos_por_slug = {p["slug"]: p for p in catalog}
    
    # 1. Atualizar páginas em p/*.html
    for prod in catalog:
        slug = prod["slug"]
        page_path = os.path.join(REPO_DIR, "p", f"{slug}.html")
        if not os.path.exists(page_path):
            continue
        
        with open(page_path, "r", encoding="utf-8", errors="ignore") as f:
            c = f.read()
        
        novo_bloco = montar_bloco_preco(prod)
        # Substituir bloco de preço na página individual
        c_novo = re.sub(r'<div class="preco[^"]*">.*?</div>', novo_bloco, c, count=1, flags=re.DOTALL)
        
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
        
        for slug, prod in produtos_por_slug.items():
            link_p = f"p/{slug}.html"
            if link_p in content:
                # Localizar o card do produto correspondente
                card_pattern = re.compile(r'(<article[^>]*>.*?href="' + re.escape(link_p) + r'".*?</article>)', re.DOTALL)
                match = card_pattern.search(content)
                if match:
                    card_html = match.group(1)
                    novo_bloco = montar_bloco_preco(prod)
                    novo_card = re.sub(r'<div class="preco[^"]*">.*?</div>', novo_bloco, card_html, count=1, flags=re.DOTALL)
                    if novo_card != card_html:
                        content = content.replace(card_html, novo_card)
                        modificado = True

        if modificado:
            with open(hf, "w", encoding="utf-8") as f:
                f.write(content)
            log(f"  Cards atualizados em {fname}!")

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
    
    log("Enviando alterações para o GitHub Pages (git push origin main)...")
    push_res = subprocess.run(["git", "push", "origin", "main"], cwd=REPO_DIR, capture_output=True, text=True)
    if push_res.returncode == 0:
        log("Push concluído com sucesso! GitHub Pages publicando...")
    else:
        log(f"Erro no git push:\n{push_res.stderr}")

def main():
    log(f"=== INICIANDO MOTOR DE PREÇOS PENNER TECH ({data_str}) ===")
    if not os.path.exists(CATALOGO_PATH):
        log(f"ERRO: Catálogo não encontrado em {CATALOGO_PATH}")
        sys.exit(1)
        
    with open(CATALOGO_PATH, "r", encoding="utf-8") as f:
        catalog = json.load(f)
        
    log(f"Total de {len(catalog)} produtos carregados do catálogo.")
    
    # Atualizar HTMLs
    atualizar_arquivos_html(catalog)
    
    # Atualizar catálogo com última conferência
    for p in catalog:
        p["ultima_conferencia"] = data_str
    with open(CATALOGO_PATH, "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)
        
    # Enviar para o GitHub
    sincronizar_github()
    log("=== MOTOR DE PREÇOS CONCLUÍDO COM SUCESSO ===")

if __name__ == "__main__":
    main()
