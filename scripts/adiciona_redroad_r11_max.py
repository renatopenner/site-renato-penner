"""Adiciona o Robô Aspirador Redroad R11 Max 36000Pa ao site loja.pennertech.com.br."""
import json
import os
import re
from PIL import Image

BASE = r"C:\Users\renat\SitesGithub\site-renato-penner"
FOTO_ORIG = r"C:\HermesKit\projects\video_redroad_r11_max\ml_product_hq.webp"
SLUG = "robo-aspirador-redroad-r11-max"
DATA = "27/11/2026"
DATA_ISO = "2026-11-27"
MARCA_W, MARCA_H = 1120, 840

PRODUTO = {
    "slug": SLUG,
    "titulo_card": "Robô Aspirador Redroad R11 Max 36.000 Pa com Base Autolimpante",
    "h1": "Robô Aspirador e Passa Pano Redroad R11 Max 3 em 1 com Sucção de 36.000 Pa, Sobe até 20 mm, LiDAR e Base Autolimpante",
    "meta_desc": "Robô aspirador Redroad R11 Max topo de linha com 36.000 Pa de sucção, superação de obstáculos de até 20 mm de altura, navegação a laser LiDAR, estação autolimpante (até 60 dias) e 3 em 1 completo (varre, aspira e passa pano).",
    "cat_badge": "Black Friday · 36.000 Pa · Nota 4.9 ★★★★★ (+100 vendidos)",
    "cat_css": "casa",
    "categoria_nome": "Casa e áudio",
    "sub": "36.000 Pa · Sobe até 20 mm · Base Autolimpante (60 dias) · Laser LiDAR · 3 em 1",
    "resumo": "Robô aspirador topo de linha 3 em 1 com monstruosa sucção de 36.000 Pa e suspensão inteligente para subir soleiras e carpetes de até 20 mm. Mapeamento laser LiDAR em tempo real via app, estação autolimpante para até 60 dias sem tocar em sujeira e controle eletrônico de água.",
    "link": "https://meli.la/1Uwdz2V",
    "preco_de": "R$ 2.499,99",
    "preco_por": "R$ 1.605,18",
    "preco_cartao": "18x R$ 95,89 sem juros cartão Mercado Pago · R$ 13,63 cashback Meli Dólar",
    "desconto": "35% OFF (R$ 1.492,82 com cupom)",
    "porque": "Enquanto robôs aspiradores comuns entregam 3.000 ou 4.000 Pa, o Redroad R11 Max atinge impressionantes 36.000 Pa de poder de sucção, arrancando poeira fina e pelos profundos de qualquer piso. Outro grande trunfo é a suspensão articulada para transpor obstáculos e degraus de até 20 mm de altura, subindo em tapetes altos e soleiras sem travar. Acompanha base de auto-esvaziamento para você ficar até 2 meses sem encostar na sujeira.",
    "destaques": [
        ("Sucção Monstruosa de 36.000 Pa", "Pressão colossal de sucção para limpeza pesada em pisos de madeira, porcelanato e carpetes densos"),
        ("Transposição de Obstáculos de 20 mm", "Suspensão dinâmica projetada para subir desníveis, soleiras de portas e tapetes de até 2 cm sem empacar"),
        ("Estação Autolimpante (até 60 dias)", "A base suga os resíduos do compartimento do robô automaticamente ao final de cada ciclo"),
        ("Mapeamento Laser LiDAR 3D", "Mapeamento milimétrico em tempo real pelo aplicativo com suporte a paredes virtuais e divisão por cômodos"),
        ("Sistema 3 em 1 Inteligente", "Varre, aspira e passa pano com reservatório de água controlado eletronicamente"),
        ("Controle Total pelo Smartphone", "Agendamento semanal, personalização de potência e nível de água por ambiente e comandos remotos"),
    ],
    "ficha": [
        "Marca / Modelo: Redroad R11 Max (Linha Premium · Cor: Preto)",
        "Pressão de sucção máxima: 36.000 Pa (36 kPa)",
        "Capacidade de superação de obstáculos: até 20 mm (2 cm de altura)",
        "Navegação: Sensor a Laser LiDAR de alta precisão 360°",
        "Modos de operação: Varrição, Sucção e Mop (Passa Pano) integrado",
        "Estação de auto-esvaziamento: Inclusa (capacidade para até 60 dias de resíduos)",
        "Conectividade: Wi-Fi com aplicativo dedicado e controle por mapa",
        "Sensores: Antiqueda, anticolisão inteligente e mapeamento de superfície",
        "Filtragem: Sistema com filtro de alta eficiência HEPA",
    ],
    "pros": [
        "Monstruosa sucção de 36.000 Pa, uma das maiores potências do mercado mundial",
        "Capacidade real de subir obstáculos de 20 mm, ideal para casas com tapetes grossos e soleiras",
        "35% OFF de Black Friday: de R$ 2.499,99 por R$ 1.605,18 (ou R$ 1.492,82 ativando o cupom)",
        "Até 18x de R$ 95,89 sem juros no cartão Mercado Pago com R$ 13,63 de cashback Meli Dólar",
        "Estação autolimpante completa que elimina a necessidade de esvaziamento manual diário",
    ],
    "contras": [
        "A base de auto-esvaziamento ocupa um espaço dedicado no piso próximo à tomada",
        "Uso de sacos descartáveis na base para retenção higiênica dos resíduos",
    ],
    "para_quem": "Quem busca o que há de mais potente e autônomo em robôs aspiradores, com força de sobra para pets e tapetes pesados e sem o estresse de ver o robô empacando em soleiras ou desníveis.",
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
    busca = re.sub(r"[^a-z0-9 ]", " ", (p["titulo_card"] + " " + p["sub"] + " " + p["slug"] + " robo aspirador redroad r11 max 36000pa").lower())
    busca = re.sub(r"\s+", " ", busca).strip()
    return f'''<article class="card" data-cat="{p['cat_css']}" data-busca="{busca}">
      <div class="thumbwrap"><a class="thumb" href="{p['link']}" target="_blank" rel="sponsored nofollow noopener"><span class="badge">Black Friday · 35% OFF</span><picture><source srcset="img/{p['slug']}.webp" type="image/webp"><img width="1120" height="840" src="img/{p['slug']}.jpg" alt="{p['titulo_card']}" loading="lazy"></picture></a></div>
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
    cabeca = re.sub(r'<meta name="build" content="[^"]*">', f'<meta name="build" content="{DATA_ISO} 08:00">', cabeca)

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
            "brand": {"@type": "Brand", "name": "Redroad"},
            "offers": {
                "@type": "Offer",
                "url": p["link"],
                "price": preco_num,
                "priceCurrency": "BRL",
                "availability": "https://schema.org/InStock",
                "itemCondition": "https://schema.org/NewCondition",
            },
            "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "100"},
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
            "cupom": "R$ 1.492,82 com cupom",
            "ultima_conferencia": DATA,
        })
        with open(caminho_json, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
        print("produtos.json atualizado com", SLUG)

    card_html = gera_card(p)
    for nome in ["index.html", "casa.html", "promocoes.html"]:
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
