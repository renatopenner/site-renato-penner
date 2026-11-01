"""Adiciona as Luvas Isolantes para Eletricistas CW 400V ao site renatopenner.com.br (GitHub Pages)."""
import io
import json
import os
import re
from PIL import Image

BASE = r"C:\Users\renat\SitesGithub\site-renato-penner"
FOTO_ORIG = r"C:\Users\renat\.gemini\antigravity\brain\4290ec98-4c09-4db7-97da-cb925e6e813d\.user_uploaded\media_1793557855779_2e1c4ce5.png"
SLUG = "luva-isolante-eletricista-400v"
DATA = "01/11/2026"
MARCA_W, MARCA_H = 1120, 840

PRODUTO = {
    "slug": SLUG,
    "titulo_card": "Luvas Isolantes para Eletricista CW 400V Antiderrapante",
    "h1": "Luvas Isolantes para Eletricistas CW Suportam Tensão até 400V com Palma Antiderrapante",
    "meta_desc": "Luvas isolantes para eletricistas CW com proteção contra choque elétrico até 400V. Palma emborrachada antiderrapante, dorso respirável, flexibilidade e alta sensibilidade tátil para manutenção elétrica e instalações.",
    "cat_badge": "Mercado Livre · +1000 Vendidos · Nota 4.6 ★★★★½",
    "cat_css": "perifericos",
    "categoria_nome": "Periféricos e acessórios",
    "sub": "Proteção até 400V · Palma emborrachada antiderrapante · Dorso respirável · +1000 vendidos",
    "resumo": "EPI indispensável para quem mexe com eletricidade, fontes, quadros de distribuição e fiação: protege as mãos contra choques de até 400V sem perder a sensibilidade tátil nem a flexibilidade para segurar parafusos, fios e ferramentas. Palma emborrachada com excelente aderência.",
    "link": "https://meli.la/2D5RWdM",
    "preco_de": "",
    "preco_por": "R$ 59,99",
    "preco_cartao": "4x R$ 15,00 sem juros · R$ 1,80 de cashback Meli Dólar",
    "desconto": "",
    "porque": "Trabalhar com manutenção elétrica, quadros de luz, tomadas ou fontes sem luva adequada é um risco desnecessário. A maioria das luvas de alta tensão grossas de borracha tiram todo o tato e tornam impossível parafusar ou decapar um fio com precisão. O par da CW resolve justamente isso: suporta até 400V para a rotina diária de baixa tensão (110V/220V) e mantém a pegada firme e ágil com palma antiderrapante e dorso respirável que não esquenta a mão.",
    "destaques": [
        ("Isolamento elétrico até 400V", "Projetada para trabalhos em baixa tensão residencial e comercial, redes de 110V/127V, 220V e 380V"),
        ("Sensibilidade tátil preservada", "Formato anatômico justo aos dedos que permite manusear fios finos, parafusos pequenos e bornes sem precisar tirar a luva"),
        ("Palma emborrachada antiderrapante", "Camada isolante com alta aderência para segurar chaves de fenda, alicates, tubos e conduítes sem escorregar"),
        ("Dorso ventilado e elástico", "Tecido respirável no dorso e punho ajustável que evitam o suor excessivo nas mãos durante trabalhos prolongados"),
        ("Resistência mecânica", "Protege a pele contra choques, abrasão, lascas, rebarbas de calhas e cortes leves de fios"),
        ("+1000 unidades vendidas e nota 4.6", "Item amplamente aprovado com 263 opiniões reais de compradores no Mercado Livre"),
    ],
    "ficha": [
        "Marca: CW",
        "Modelo: Luva Isolante de Proteção Elétrica 400V",
        "Tensão de isolamento: Até 400 Volts (baixa tensão)",
        "Material da palma: Revestimento isolante emborrachado flexível de alta densidade",
        "Material do dorso: Tecido elástico respirável e punho com acabamento reforçado",
        "Cor: Preto e cinza",
        "Aplicações: Instalações elétricas, troca de disjuntores, tomadas, iluminação, manutenção de computadores, nobreaks e equipamentos industriais leves",
        "Conteúdo da embalagem: 1x Par de luvas isolantes CW 400V",
    ],
    "pros": [
        "Mais de 1.000 unidades vendidas no Mercado Livre e avaliação 4.6 com 263 opiniões reais",
        "Permite manuseio fino de ferramentas e parafusos, ao contrário das luvas de borracha rígidas",
        "Palma com excelente aderência mesmo com peças lisas ou cabos oleosos",
        "Parcelamento em até 4x sem juros e cashback no Mercado Pago",
    ],
    "contras": [
        "Destinada para tensões de até 400V (não deve ser utilizada em redes de média ou alta tensão acima de 400V/1000V sem luvas classe 0/00 específicas)",
    ],
    "para_quem": "Eletricistas prediais e residenciais, técnicos de informática e redes, instaladores de ar-condicionado e CFTV, instaladores de energia solar e hobbistas que valorizam segurança e conforto nas instalações.",
}


def prepara_imagem():
    im = Image.open(FOTO_ORIG).convert("RGB")
    alvo_h = 800
    escala = alvo_h / im.height
    novo = im.resize((int(im.width * escala), alvo_h), Image.Resampling.LANCZOS)
    tela = Image.new("RGB", (MARCA_W, MARCA_H), "white")
    tela.paste(novo, ((MARCA_W - novo.width) // 2, (MARCA_H - alvo_h) // 2))
    destino = os.path.join(BASE, "img", f"{SLUG}.png")
    tela.save(destino, optimize=True)
    print("Imagem gerada:", destino, tela.size)


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
      <div class="thumbwrap"><a class="thumb" href="{p['link']}" target="_blank" rel="sponsored nofollow noopener"><span class="badge">Mercado Livre · +1000 Vendidos</span><img src="img/{p['slug']}.png" alt="{p['titulo_card']}" loading="lazy"></a></div>
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
    cabeca = re.sub(r'<meta name="build" content="[^"]*"', f'<meta name="build" content="2026-11-01 15:35">', cabeca)

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
    <div class="foto"><a href="{p['link']}" target="_blank" rel="sponsored nofollow noopener" title="Ver oferta no Mercado Livre"><img src="../img/{p['slug']}.png" alt="{p['titulo_card']}"></a></div>
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
          f'"brand": {{"@type": "Brand", "name": "CW"}}, '
          f'"offers": {{"@type": "Offer", "url": "{p["link"]}", "price": "{preco_num}", '
          f'"priceCurrency": "BRL", "availability": "https://schema.org/InStock"}}, '
          f'"aggregateRating": {{"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": "263"}}}}</script>')
    cauda = re.sub(r'<script type="application/ld\+json">.*?</script>', ld, cauda, count=1, flags=re.S)
    return cabeca + corpo + cauda


def main():
    p = PRODUTO
    prepara_imagem()

    # 1. Página de detalhes p/luva-isolante-eletricista-400v.html
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
    paginas = ["index.html", "perifericos.html"]
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
