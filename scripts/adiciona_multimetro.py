"""Adiciona o Multímetro Digital Portátil DT830B ao site renatopenner.com.br (GitHub Pages)."""
import io
import json
import os
import re
from PIL import Image, ImageFilter

BASE = r"C:\Users\renat\SitesGithub\site-renato-penner"
FOTO_ORIG = r"C:\Users\renat\.gemini\antigravity\brain\4290ec98-4c09-4db7-97da-cb925e6e813d\.user_uploaded\media_1793557783959_98e36a84.jpg"
SLUG = "multimetro-digital-portatil-dt830b"
DATA = "01/11/2026"
MARCA_W, MARCA_H = 1120, 840

PRODUTO = {
    "slug": SLUG,
    "titulo_card": "Multímetro Digital Portátil DT830B com Bateria e Pontas de Prova",
    "h1": "Multímetro Digital Portátil DT830B para Teste de Continuidade, Tensão e Medição com Bateria Inclusa",
    "meta_desc": "Multímetro digital portátil DT830B com visor LCD, pontas de prova e bateria de 9V inclusa. Mede tensão AC/DC até 1000V, corrente até 10A, resistência, transistores hFE e teste de diodo/continuidade. Ideal para bancada de TI e eletrônica.",
    "cat_badge": "Mercado Livre · Mais Vendido · Nota 4.8 ★★★★★",
    "cat_css": "perifericos",
    "categoria_nome": "Periféricos e acessórios",
    "sub": "Visor LCD · Tensão AC/DC até 1000V · Corrente até 10A · Teste de Diodo e hFE · Bateria 9V inclusa",
    "resumo": "Multímetro digital indispensável para bancada de TI e eletrônica: mede tensão contínua e alternada, corrente DC, resistência e continuidade para testar fontes de PC/notebook, tomadas, pilhas, placas e cabos. Compacto, robusto e já pronto para uso com pontas de prova e bateria inclusas.",
    "link": "https://meli.la/2B9JKNY",
    "preco_de": "R$ 39,99",
    "preco_por": "R$ 20,90",
    "preco_cartao": "R$ 0,62 de cashback em Meli Dólar com cartão Mercado Pago",
    "desconto": "47% OFF",
    "porque": "Multímetro é a ferramenta número 1 de qualquer técnico de informática, eletricista ou entusiasta de hardware. Seja para testar se uma fonte de computador está entregando os 12V/5V corretos, identificar um cabo rompido com o teste de continuidade ou testar pilhas e baterias de placa-mãe (CR2032), o modelo DT830B é o padrão mais consagrado do mercado. Por cerca de vinte reais e já vindo com bateria e pontas de teste na caixa, é o custo-benefício imbatível para ter sempre na bancada ou na mochila.",
    "destaques": [
        ("Medição de Tensão Contínua (DCV)", "Escalas de 200mV até 1000V com alta precisão para testar fontes ATX, fontes de bancada, baterias de notebook e células de lítio"),
        ("Medição de Tensão Alternada (ACV)", "Escalas de 200V e 750V para aferir tomadas residenciais de 110V/127V ou 220V, nobreaks e estabilizadores"),
        ("Corrente Contínua (DCA) até 10A", "Mede de microampères (200µA) até 10A em escala dedicada sem fusível para circuitos de carga"),
        ("Resistência e Teste de Diodo/Continuidade", "Mede resistores de 200Ω a 2000kΩ (2 MΩ) e testa semicondutores, diodos, LEDs e integridade de trilhas e fios"),
        ("Teste de Ganho de Transistores (hFE)", "Soquete frontal próprio para medição direta de fator de amplificação hFE em transistores NPN e PNP"),
        ("Kit Completo Pronto para Usar", "Acompanha o par de cabos com pontas de prova (vermelha e preta isoladas) e a bateria de 9V necessária já instalada/inclusa"),
    ],
    "ficha": [
        "Modelo: DT830B Digital Multimeter (Chrome Technology)",
        "Display: LCD de 3 ½ dígitos com leitura máxima de 1999",
        "Alimentação: Bateria de 9V (já inclusa no pacote)",
        "Dimensões aproximadas: 12,6 × 7,0 × 2,4 cm · Peso: aprox. 150 g",
        "Escalas de Tensão DC: 200mV, 2000mV, 20V, 200V, 1000V",
        "Escalas de Tensão AC: 200V, 750V",
        "Escalas de Corrente DC: 200µA, 2000µA, 20mA, 200mA, 10A (entrada 10A máx. 10s)",
        "Escalas de Resistência: 200Ω, 2000Ω, 20kΩ, 200kΩ, 2000kΩ (2MΩ)",
        "Funções adicionais: Teste de Diodo/Continuidade e soquete para transistor hFE (NPN/PNP)",
        "Conteúdo da embalagem: 1x Multímetro Digital DT830B, 1x Par de cabos com pontas de prova (vermelho/preto), 1x Bateria 9V, 1x Manual",
    ],
    "pros": [
        "Item Mais Vendido do Mercado Livre (13º no ranking geral de Multímetros) com nota 4.8 de 5 baseada em avaliações de compradores",
        "Preço imbatível: de R$ 39,99 por R$ 20,90 (47% de desconto real)",
        "Já vem com bateria de 9V e pontas de teste — só tirar da caixa e começar a medir",
        "Resolve a rotina diária de manutenção em bancada de computadores, eletrodomésticos e eletrônica",
        "Formato super compacto e leve, fácil de transportar na maleta de ferramentas",
    ],
    "contras": [
        "Seleção manual de escala: é necessário girar o botão rotativo para a faixa de medição adequada antes de testar",
        "Entrada de 10A sem proteção por fusível: medições de corrente elevada exigem cuidado e limite de 10 segundos contínuos",
    ],
    "para_quem": "Técnicos de TI e suporte de informática, estudantes de cursos técnicos e engenharia, eletricistas, hobbistas e makers que precisam de um multímetro confiável para diagnosticar tensões, fontes, pilhas e cabos sem gastar muito.",
}


def prepara_imagem():
    im = Image.open(FOTO_ORIG).convert("RGB")
    fundo = im.resize((MARCA_W, MARCA_H), Image.Resampling.LANCZOS).filter(ImageFilter.GaussianBlur(28))
    alvo_h = MARCA_H
    scale = alvo_h / im.height
    alvo_w = int(im.width * scale)
    novo = im.resize((alvo_w, alvo_h), Image.Resampling.LANCZOS)

    mask = Image.new("L", (alvo_w, alvo_h), 255)
    feather = 60
    for x in range(feather):
        val = int(255 * (x / feather))
        for y in range(alvo_h):
            mask.putpixel((x, y), val)
            mask.putpixel((alvo_w - 1 - x, y), val)

    offset_x = (MARCA_W - alvo_w) // 2
    fundo.paste(novo, (offset_x, 0), mask)

    destino = os.path.join(BASE, "img", f"{SLUG}.png")
    fundo.save(destino, optimize=True)
    print("Imagem gerada:", destino, fundo.size)


def bloco_preco(p):
    html = '<div class="preco">'
    if p["preco_de"]:
        html += f'<span class="de">de {p["preco_de"]}</span>'
    html += f'<span class="por">por {p["preco_por"]}</span>'
    if p["preco_cartao"]:
        html += f'<span class="cartao">{p["preco_cartao"]}</span>'
    nota = f'preço conferido em {DATA}'
    if p["desconto"]:
        nota += f' · {p["desconto"]}'
    html += f"<small>{nota}</small></div>"
    return html


def gera_card(p):
    busca = re.sub(r"[^a-z0-9 ]", " ", (p["titulo_card"] + " " + p["sub"] + " " + p["slug"]).lower())
    busca = re.sub(r"\s+", " ", busca).strip()
    return f'''<article class="card" data-cat="{p['cat_css']}" data-busca="{busca}">
      <div class="thumbwrap"><a class="thumb" href="{p['link']}" target="_blank" rel="sponsored nofollow noopener"><span class="badge">Mercado Livre · Mais Vendido</span><img src="img/{p['slug'].replace('.html', '')}.png" style="object-fit:cover;padding:0" alt="{p['titulo_card']}" loading="lazy"></a></div>
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

    cabeca = re.sub(r"<title>.*?</title>", f"<title>{p['titulo_card']} — Renato Penner</title>", cabeca, flags=re.S)
    cabeca = re.sub(r'<meta name="description" content="[^"]*"', f'<meta name="description" content="{p["meta_desc"]}"', cabeca)
    cabeca = re.sub(r'<link rel="canonical" href="[^"]*"', f'<link rel="canonical" href="https://www.renatopenner.com.br/p/{p["slug"]}.html"', cabeca)
    cabeca = re.sub(r'<meta property="og:title" content="[^"]*"', f'<meta property="og:title" content="{p["titulo_card"]} — Renato Penner"', cabeca)
    cabeca = re.sub(r'<meta property="og:description" content="[^"]*"', f'<meta property="og:description" content="{p["meta_desc"]}"', cabeca)
    cabeca = re.sub(r'<meta property="og:url" content="[^"]*"', f'<meta property="og:url" content="https://www.renatopenner.com.br/p/{p["slug"]}.html"', cabeca)
    cabeca = re.sub(r'<meta name="build" content="[^"]*"', f'<meta name="build" content="2026-11-01 15:30">', cabeca)

    # Marca menu ativo em periféricos
    cabeca = cabeca.replace('class="link on"', 'class="link "')
    cabeca = cabeca.replace(f'class="link " href="../{p["cat_css"]}.html"', f'class="link on" href="../{p["cat_css"]}.html"')

    destaques = "".join(f"<li class=\"dt\"><strong>{t}:</strong> {d}</li>" for t, d in p["destaques"])
    ficha = "".join(f'<li class="dt">{x}</li>' for x in p["ficha"])
    pros = "".join(f'<li class="ok">{x}</li>' for x in p["pros"])
    contras = "".join(f'<li class="no">{x}</li>' for x in p["contras"])

    corpo = f'''<main class="wrap">
  <div class="migalha"><a href="../index.html">Início</a> /
    <a href="../{p['cat_css']}.html">{p['categoria_nome']}</a> / {p['titulo_card']}</div>
  <section class="prod">
    <div class="foto foto-cheia"><a href="{p['link']}" target="_blank" rel="sponsored nofollow noopener" title="Ver oferta no Mercado Livre"><img src="../img/{p['slug']}.png" alt="{p['titulo_card']}"></a></div>
    <div>
      <span class="cat" style="color:#38bdf8;font-size:11px;font-weight:800;letter-spacing:.1em">{p['cat_badge']}</span>
      <h1>{p['h1']}</h1>
      <div class="pmeta">{p['sub']}</div>
      {bloco_preco(p)}
      <div class="btns" style="margin-top:18px">
        <a class="btn" href="{p['link']}" target="_blank" rel="sponsored nofollow noopener">Ver oferta no Mercado Livre →</a>
      </div>
      <div class="box"><h4>Por que eu recomendo</h4><p style="color:#c6d5e2;font-size:14.5px">{p['porque']}</p></div>
      <div class="box"><h4>Destaques e Funções</h4><ul>{destaques}</ul></div>
      <div class="box"><h4>Ficha Técnica e Conteúdo</h4><ul>{ficha}</ul></div>
      <div class="box"><h4>Prós</h4><ul>{pros}</ul><h4 style="margin-top:14px">Contras</h4><ul>{contras}</ul></div>
      <div class="box"><h4>Para quem serve</h4><p style="color:#c6d5e2;font-size:14.5px">{p['para_quem']}</p></div>
    </div>
  </section>
</main>'''

    preco_num = re.sub(r"[^\d,]", "", p["preco_por"]).replace(".", "").replace(",", ".")
    ld = (f'<script type="application/ld+json">{{"@context": "https://schema.org", "@type": "Product", '
          f'"name": "{p["titulo_card"]}", "description": "{p["meta_desc"]}", '
          f'"brand": {{"@type": "Brand", "name": "Chrome Technology"}}, '
          f'"offers": {{"@type": "Offer", "url": "{p["link"]}", "price": "{preco_num}", '
          f'"priceCurrency": "BRL", "availability": "https://schema.org/InStock"}}, '
          f'"aggregateRating": {{"@type": "AggregateRating", "ratingValue": "4.8", "reviewCount": "26"}}}}</script>')
    cauda = re.sub(r'<script type="application/ld\+json">.*?</script>', ld, cauda, count=1, flags=re.S)
    return cabeca + corpo + cauda


def main():
    p = PRODUTO
    prepara_imagem()

    # 1. Página de detalhes p/multimetro-digital-portatil-dt830b.html
    template = open(os.path.join(BASE, "p", "dock-station-dual-sata-clone.html"), encoding="utf-8").read()
    page_html = gera_pagina(p, template)
    page_path = os.path.join(BASE, "p", f"{SLUG}.html")
    with open(page_path, "w", encoding="utf-8") as f:
        f.write(page_html)
    print("Página criada:", page_path)

    # 2. Atualizar dados/produtos.json
    caminho_json = os.path.join(BASE, "dados", "produtos.json")
    dados = json.load(open(caminho_json, encoding="utf-8"))
    slugs = {x["slug"] for x in dados}
    if SLUG not in slugs:
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
        json.dump(dados, open(caminho_json, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print("produtos.json atualizado com", SLUG)
    else:
        print("produtos.json já contém", SLUG)

    # 3. Inserir cards nas páginas HTML
    card_html = gera_card(p)
    paginas = ["index.html", "perifericos.html", "promocoes.html"]
    for nome in paginas:
        caminho = os.path.join(BASE, nome)
        content = open(caminho, encoding="utf-8").read()
        if f'p/{SLUG}.html' in content:
            print(f"Card já existe em {nome}")
            continue

        pos = content.find('<article class="card"')
        if pos < 0:
            print(f"Não achou card em {nome}")
            continue
        pos = content.rfind("\n", 0, pos) + 1
        content = content[:pos] + card_html + "\n    " + content[pos:]
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Card inserido com sucesso em {nome}")

    # 4. Sitemap.xml
    sm_path = os.path.join(BASE, "sitemap.xml")
    sm_content = open(sm_path, encoding="utf-8").read()
    if f"{SLUG}.html" not in sm_content:
        item = f"  <url><loc>https://www.renatopenner.com.br/p/{SLUG}.html</loc><lastmod>2026-11-01</lastmod></url>\n"
        sm_content = sm_content.replace("</urlset>", item + "</urlset>")
        with open(sm_path, "w", encoding="utf-8") as f:
            f.write(sm_content)
        print("Sitemap.xml atualizado!")


if __name__ == "__main__":
    main()
