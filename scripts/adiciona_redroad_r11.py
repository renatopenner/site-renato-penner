"""Adiciona o Robô Aspirador Passa Pano Redroad R11 ao site loja.pennertech.com.br."""
import json
import os
import re
from PIL import Image

BASE = r"C:\Users\renat\SitesGithub\site-renato-penner"
FOTO_ORIG = r"C:\Users\renat\.gemini\antigravity\brain\a7825e10-5c25-4b7b-be18-1c00467a9e4f\.user_uploaded\media_1794869349707_41862611.jpg"
SLUG = "robo-aspirador-redroad-r11"
DATA = "16/11/2026"
DATA_ISO = "2026-11-16"
MARCA_W, MARCA_H = 1120, 840

PRODUTO = {
    "slug": SLUG,
    "titulo_card": "Robô Aspirador Redroad R11 20.000 Pa com Base Autolimpante e LiDAR",
    "h1": "Robô Aspirador Passa Pano Redroad R11 3 em 1 com Sucção de 20.000 Pa, Mapeamento LiDAR e Base Autolimpante (127V)",
    "meta_desc": "Robô aspirador Redroad R11 (9º mais vendido no Mercado Livre, nota 4.8 em 529 opiniões). Sucção de 20.000 Pa, navegação a laser LDS (até 4 mapas), base autolimpante (até 90 dias), escova extensível e passa pano 3 em 1. 127V, Anatel 083842617632.",
    "cat_badge": "Black Friday · 9º Mais Vendido · Nota 4.8 ★★★★★ (529)",
    "cat_css": "casa",
    "categoria_nome": "Casa e áudio",
    "sub": "20.000 Pa · Base Autolimpante (90 dias) · Laser LDS (4 mapas) · Passa Pano 240 ml · 127V",
    "resumo": "Robô aspirador e passa pano 3 em 1 com 20.000 Pa de sucção e estação autolimpante para até 90 dias sem esvaziar manualmente. Mapeamento a laser LDS (armazena até 4 mapas), escova lateral extensível para cantos, Wi-Fi 2.4G/5G com Alexa/Google Home e autonomia de até 156 min.",
    "link": "https://meli.la/1c4saDQ",
    "preco_de": "R$ 1.999,99",
    "preco_por": "R$ 1.404,00",
    "preco_cartao": "15x R$ 93,60 sem juros cartão Mercado Pago · R$ 12,02 cashback Meli Dólar",
    "desconto": "29% OFF",
    "porque": "A maioria dos robôs aspiradores de entrada bate nos móveis de forma aleatória e exige que você esvazie a gavetinha de pó quase todo dia. O Redroad R11 entrega pacote de topo de linha por R$ 1.404 na Black Friday: mapeamento a laser LDS (que desenha a planta da casa, evita colisões e guarda até 4 mapas), sucção de 20.000 Pa com escova lateral extensível para cantos e uma base autolimpante que suga a sujeira do robô automaticamente por até 90 dias.",
    "destaques": [
        ("Sucção de 20.000 Pa (4 níveis)", "Potência de 20 kPa para remover poeira fina, migalhas e pelos de animais em pisos frios, madeira e tapetes"),
        ("Estação autolimpante (até 90 dias)", "Base com saco coletor de grande capacidade que esvazia o robô automaticamente após a limpeza"),
        ("Mapeamento a laser LDS / LiDAR", "Mapeia em tempo real, armazena até 4 ambientes/andares distintos e permite criar paredes virtuais e zonas restritas no app"),
        ("Escova lateral extensível mecânica", "Alcança cantos e rodapés aumentando em 30% a cobertura, com sistema antiemaranhamento para pelos"),
        ("Sistema 3 em 1 com pano eletrônico", "Aspira, varre e passa pano com reservatório de água de 240 ml e controle eletrônico em 3 estágios"),
        ("Wi-Fi 2.4G/5G, Alexa e Google Home", "Agendamento para até 7 dias, ajuste de sucção/água por cômodo, retomada automática e homologação Anatel nº 083842617632"),
    ],
    "ficha": [
        "Marca / Modelo: Redroad R11 (Linha Robot · Cor: Branco)",
        "Voltagem da estação: 127V",
        "Potência elétrica: 36 W · Pressão de sucção máxima: 20.000 Pa (20 kPa)",
        "Navegação: Laser LDS (LiDAR) com armazenamento de até 4 mapas",
        "Modos de limpeza: Combinado (varrição + esfregão), Varrição pura e Esfregão puro",
        "Reservatório de pó: 290 ml no robô · Saco da base autolimpante (3 L / 4 L conforme especificação do anúncio, até 90 dias)",
        "Reservatório de água: 240 ml com controle eletrônico de fluxo em 3 estágios",
        "Bateria: 3,2 Ah (3.200 mAh) · Carregamento automático (tempo de carga: ~4 h)",
        "Autonomia por modo: Silencioso 156 min · Padrão 133 min · Alta 87 min · Extra alta 60 min",
        "Transposição de obstáculos: ≥ 20 mm (sem módulo de água) / ≥ 15 mm (com água)",
        "Sensores e filtros: Sensor de obstáculos, sensor antiqueda e filtro HEPA incluso",
        "Conectividade: Wi-Fi 2.4 GHz / 5 GHz · Compatível com Alexa e Google Home",
        "Dimensões: Robô 321,5 × 321,5 × 100 mm · Base 239 × 157 × 255 mm",
        "Homologação Anatel Nº: 083842617632",
    ],
    "pros": [
        "9º lugar em Robôs Aspiradores no Mercado Livre com nota 4.8 de 5 em 529 avaliações",
        "29% OFF na Black Friday: de R$ 1.999,99 por R$ 1.404,00 em até 15x sem juros no cartão Mercado Pago",
        "Combo raro nessa faixa de preço: 20.000 Pa + LiDAR (4 mapas) + base autolimpante + escova lateral extensível",
        "Suporte a Wi-Fi 2.4G/5G, Alexa, Google Home e programação semanal por cômodo",
        "Homologado pela Anatel (nº 083842617632) e indicado para tapetes e pelos de pets",
    ],
    "contras": [
        "Atenção à voltagem: este anúncio específico é 127V (exige transformador caso sua tomada seja 220V)",
        "Altura de 10 cm (100 mm) por conta da torre do laser LDS: verifique se passa sob sofás ou camas muito baixas",
        "Base autolimpante utiliza sacos coletores descartáveis para reposição periódica",
    ],
    "para_quem": "Casas e apartamentos com pets, pisos frios, madeira ou tapetes onde você quer automatizar a limpeza diária com mapeamento inteligente e ficar semanas sem precisar esvaziar o reservatório de pó.",
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
    busca = re.sub(r"[^a-z0-9 ]", " ", (p["titulo_card"] + " " + p["sub"] + " " + p["slug"] + " robo aspirador redroad lidar").lower())
    busca = re.sub(r"\s+", " ", busca).strip()
    return f'''<article class="card" data-cat="{p['cat_css']}" data-busca="{busca}">
      <div class="thumbwrap"><a class="thumb" href="{p['link']}" target="_blank" rel="sponsored nofollow noopener"><span class="badge">Black Friday · 29% OFF</span><picture><source srcset="img/{p['slug']}.webp" type="image/webp"><img width="1120" height="840" src="img/{p['slug']}.jpg" alt="{p['titulo_card']}" loading="lazy"></picture></a></div>
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
    cabeca = re.sub(r'<meta name="build" content="[^"]*">', f'<meta name="build" content="{DATA_ISO} 19:50">', cabeca)

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
            "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.8", "reviewCount": "529"},
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
