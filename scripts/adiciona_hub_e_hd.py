"""Adiciona os dois produtos novos (Hub 7 em 1 e HD Storage Orico) ao site estático."""
import io
import json
import os
import re
import urllib.request

from PIL import Image

BASE = r"C:\Users\renat\SitesGithub\site-renato-penner"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/156.0 Safari/537.36"}
DATA = "28/10/2026"
MARCA_W, MARCA_H = 1120, 840

PRODUTOS = [
    {
        "slug": "hub-7-em-1-usb-c-3a",
        "titulo_card": "Hub USB 7 em 1 Hrebos AD-227 (3 USB-A + 4 USB-C)",
        "h1": "Hub USB 7 em 1 Hrebos AD-227 com 3 USB-A, 4 USB-C e Botão por Porta",
        "meta_desc": "Hub USB 7 em 1 Hrebos AD-227 com 3 portas USB-A e 4 USB-C de 5 Gbps, botões individuais de energia, corpo em alumínio e cabo de 1 metro. Serve em Windows e macOS.",
        "cat": "Mercado Livre",
        "cat_css": "perifericos",
        "categoria_nome": "Periféricos",
        "sub": '3x USB-A + 4x USB-C · 5 Gbps · Botão liga/desliga em cada porta · Corpo de alumínio · Cabo 1 m',
        "resumo": "Transforma uma única porta do notebook em sete: três USB-A e quatro USB-C, com botão de energia em cada uma. É o hub certo para quem vive com pendrive, mouse, teclado, HD externo e leitor de cartão disputando espaço — e quer desligar o que não está usando sem ficar tirando cabo.",
        "link": "https://www.mercadolivre.com.br/hub-7-in-1-para-notebook-e-mac-com-3-usb-e-4-type-c-gbps-3a/p/MLB51860943?pdp_filters=item_id%3AMLB7726113448&matt_word=renatopenner&matt_tool=86394049",
        "preco_de": "R$ 208,99",
        "preco_por": "R$ 138,31",
        "preco_cartao": "12x R$ 13,67 com cartão Mercado Pago",
        "desconto": "33% OFF",
        "img_origem": "https://http2.mlstatic.com/D_NQ_NP_2X_661502-MLA99991260581_112025-F.webp",
        "porque": "Hub com botão individual por porta é o tipo de detalhe que parece frescura até você precisar: dá para deixar o HD externo conectado e desligado ao mesmo tempo, sem desmontar a mesa toda. Com 3 USB-A e 4 USB-C em corpo de alumínio e 5 Gbps, resolve o notebook que só tem duas portas e vive no limite.",
        "destaques": [
            ("7 portas de verdade", "3 USB-A e 4 USB-C simultâneas, com 5 Gbps em cada uma — o suficiente para pendrive, mouse, teclado, HD externo e leitor de cartão ao mesmo tempo"),
            ("Botão individual por porta", "Liga e desliga cada entrada separadamente, com LED indicando o que está ativo; nada de ficar plugando e desplugando cabo"),
            ("Corpo de alumínio", "Carcaça metálica que ajuda a dissipar calor e não parece plástico de brinquedo na mesa"),
            ("Proteção contra sobrecarga", "Cada porta tem proteção, o que protege notebook e dispositivos em caso de pico"),
            ("Plug and play", "Funciona em Windows e macOS sem instalar driver nenhum; cabo de 1 metro já embutido"),
        ],
        "ficha": [
            'Marca: Hrebos · Modelo: AD-227 (alfanumérico 227)',
            'Portas: 3x USB-A + 4x USB-C (7 no total)',
            'Velocidade: USB 3.0 · 5 Gbps',
            'Cor e material: cinza, liga de alumínio',
            'Cabo: 1 metro, integrado',
            'Compatibilidade: Windows e macOS',
            'Extras: botão liga/desliga e LED por porta, proteção contra sobrecarga',
            'Na caixa: 1 hub 7 em 1 e 1 fonte de alimentação',
        ],
        "pros": [
            "Sete portas com botão individual — controle real de quais dispositivos ficam ativos",
            "USB-A e USB-C no mesmo hub, sem precisar de adaptador avulso",
            "Corpo de alumínio, mais firme e com melhor dissipação que os hubs plásticos",
            "5 Gbps é o teto prático do USB 3.0: atende HD externo e pendrive rápido sem gargalo",
        ],
        "contras": [
            'Não é Thunderbolt nem USB 3.1/3.2 de 10 Gbps — para SSD NVMe externo de alta performance existe hub melhor (e mais caro)',
            "Precisa da fonte na tomada para alimentar as sete portas; não é hub de bolso",
        ],
        "para_quem": "Quem usa notebook com poucas portas e precisa ligar mouse, teclado, pendrive, HD externo e leitor de cartão ao mesmo tempo — e quer desligar o que não está em uso sem desmontar a estação de trabalho.",
    },
    {
        "slug": "hd-storage-5-baias-orico",
        "titulo_card": 'HD Storage 5 Baias Orico DS500U3 (USB 3.0, até 50 TB)',
        "h1": 'HD Storage Orico DS500U3 com 5 Baias SATA 3.5" e USB 3.0',
        "meta_desc": 'Gabinete externo Orico DS500U3 com 5 baias SATA de 3,5 polegadas, até 10 TB por disco, USB 3.0 de 5 Gbps, hibernação inteligente e troca de disco sem abrir o gabinete.',
        "cat": "Mercado Livre",
        "cat_css": "ssd",
        "categoria_nome": "SSD e armazenamento",
        "sub": '5 baias SATA 3,5" · até 10 TB por disco · USB 3.0 5 Gbps · Hibernação inteligente · Troca de disco a quente',
        "resumo": "Cinco HDs de desktop ligados ao mesmo tempo, num gabinete vertical com baia magnética que abre sem parafuso. É a solução para quem acumulou disco de backup, mídia e projeto e vive ligando case avulso — ou para montar um servidor de arquivos caseiro sem comprar NAS.",
        "link": "https://www.mercadolivre.com.br/hd-storage-5-baias-magneticas-usb-30-ds500u3-orico/p/MLB27745949?pdp_filters=item_id%3AMLB3875927703&matt_word=renatopenner&matt_tool=86394049",
        "preco_de": "",
        "preco_por": "R$ 1.498,90",
        "preco_cartao": "",
        "desconto": "",
        "img_origem": "https://http2.mlstatic.com/D_NQ_NP_2X_785208-MLA99500025580_112025-F.webp",
        "porque": "Quem trabalha com vídeo, foto ou backup de máquina sabe o problema: HD solto em cima da mesa, case que esquenta, cabo USB toda hora. Esse gabinete resolve com cinco baias verticais, cada uma com sua porta, e abertura magnética — troca de disco em segundos, sem desligar nada. Não é NAS (não tem rede), é o passo anterior, bem mais barato.",
        "destaques": [
            ("5 baias SATA de 3,5 polegadas", "Até 10 TB por disco, ou seja, até 50 TB no total — espaço de sobra para backup, mídia e arquivo morto"),
            ("Baia magnética, troca a quente", "A tampa abre por ímã e cada disco sai pela frente, sem parafuso e sem desligar o gabinete"),
            ("USB 3.0 de 5 Gbps", "Chip controlador dedicado; na prática é o limite do USB 3.0 e atende backup e edição de arquivos direto do disco"),
            ("Hibernação inteligente", "Depois de 30 minutos sem atividade os discos entram em repouso: menos consumo e mais vida útil"),
            ("Vertical e silencioso no dia a dia", "Ocupa pouco espaço na mesa e tem controle de rotação; o barulho aparece só quando os discos estão trabalhando"),
        ],
        "ficha": [
            "Marca: Orico · Modelo: DS500U3-BK",
            'Baias: 5, para discos SATA de 3,5" removíveis',
            "Capacidade máxima: 10 TB por disco",
            "Interface: USB 3.0 (5 Gbps) com chip controlador",
            'Discos de 2,5": exigem adaptador Orico 1125SS (não incluso)',
            "Hibernação automática: após 30 minutos sem atividade",
            "Clonagem: não tem função de clonar",
            "Importante: discos rígidos não acompanham o produto",
        ],
        "pros": [
            "Cinco discos acessíveis ao mesmo tempo, com troca a quente pela frente",
            "Cabeçalho magnético sem parafuso: manutenção de backup fica rápida",
            "Hibernação automática economiza energia e preserva os discos",
            "Custa bem menos que um NAS de 5 baias e atende quem só precisa do volume no PC",
        ],
        "contras": [
            "Não é NAS: não tem rede nem acesso remoto, precisa estar ligado a um computador por USB",
            'Discos de 2,5" só com adaptador 1125SS vendido à parte',
            "HDs não estão inclusos — o preço é só do gabinete",
        ],
        "para_quem": "Quem edita vídeo e foto, faz backup de várias máquinas ou tem pilha de HD de desktop na gaveta e quer tudo ligado num só gabinete — sem pagar o preço de um NAS.",
    },
]


def imagem(slug, origem):
    b = urllib.request.urlopen(urllib.request.Request(origem, headers=UA), timeout=90).read()
    im = Image.open(io.BytesIO(b)).convert("RGB")
    im.thumbnail((MARCA_W - 40, MARCA_H - 40), Image.Resampling.LANCZOS)
    tela = Image.new("RGB", (MARCA_W, MARCA_H), "white")
    tela.paste(im, ((MARCA_W - im.width) // 2, (MARCA_H - im.height) // 2))
    destino = os.path.join(BASE, "img", f"{slug}.png")
    tela.save(destino, optimize=True)
    print("imagem:", destino, tela.size, "| origem", im.size)


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


def card(p):
    busca = re.sub(r"[^a-z0-9 ]", " ", p["titulo_card"].lower())
    busca = re.sub(r"\s+", " ", busca).strip()
    return f'''<article class="card" data-cat="{p['cat_css']}" data-busca="{busca} {p['slug'].replace('-', ' ')}">
      <div class="thumbwrap"><a class="thumb" href="{p['link']}" target="_blank" rel="sponsored nofollow noopener"><span class="badge">{p['cat']}</span><img src="img/{p['slug']}.png" alt="{p['titulo_card']}" loading="lazy"></a></div>
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


def pagina(p, template):
    ini = template.index('<main class="wrap">')
    fim = template.index('</main>') + len('</main>')
    cabeca = template[:ini]
    cauda = template[fim:]

    # cabeça
    cabeca = re.sub(r"<title>.*?</title>", f"<title>{p['titulo_card']} — Renato Penner</title>", cabeca, flags=re.S)
    cabeca = re.sub(r'<meta name="description" content="[^"]*"', f'<meta name="description" content="{p["meta_desc"]}"', cabeca)
    cabeca = re.sub(r'<link rel="canonical" href="[^"]*"', f'<link rel="canonical" href="https://www.renatopenner.com.br/p/{p["slug"]}.html"', cabeca)
    cabeca = re.sub(r'<meta property="og:title" content="[^"]*"', f'<meta property="og:title" content="{p["titulo_card"]} — Renato Penner"', cabeca)
    cabeca = re.sub(r'<meta property="og:description" content="[^"]*"', f'<meta property="og:description" content="{p["meta_desc"]}"', cabeca)
    cabeca = re.sub(r'<meta property="og:url" content="[^"]*"', f'<meta property="og:url" content="https://www.renatopenner.com.br/p/{p["slug"]}.html"', cabeca)
    cabeca = re.sub(r'<meta name="build" content="[^"]*"', '<meta name="build" content="2026-10-28 10:15">', cabeca)
    # menu ativo
    def marca_nav(m):
        href = m.group(1)
        on = " on" if f'href="../{p["cat_css"]}.html"' in m.group(0) else ""
        return m.group(0)
    # remove "on" de todos e aplica no atual
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
      <span class="cat" style="color:#38bdf8;font-size:11px;font-weight:800;letter-spacing:.1em">{p['cat']}</span>
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
          f'"offers": {{"@type": "Offer", "url": "{p["link"]}", "price": "{preco_num}", '
          f'"priceCurrency": "BRL", "availability": "https://schema.org/InStock"}}}}</script>')
    cauda = re.sub(r'<script type="application/ld\+json">.*?</script>', ld, cauda, count=1, flags=re.S)
    return cabeca + corpo + cauda


def main():
    caminho_json = os.path.join(BASE, "dados", "produtos.json")
    dados = json.load(open(caminho_json, encoding="utf-8"))
    slugs = {x["slug"] for x in dados}
    template = open(os.path.join(BASE, "p", "dock-station-dual-sata-clone.html"), encoding="utf-8").read()

    for p in PRODUTOS:
        imagem(p["slug"], p["img_origem"])
        with open(os.path.join(BASE, "p", f"{p['slug']}.html"), "w", encoding="utf-8") as fh:
            fh.write(pagina(p, template))
        print("página:", p["slug"])

        if p["slug"] not in slugs:
            dados.append({
                "slug": p["slug"], "title": p["titulo_card"], "file": f"{p['slug']}.html",
                "cat": p["cat"], "link": p["link"], "preco_de": p["preco_de"],
                "preco_por": p["preco_por"], "preco_cartao": p["preco_cartao"],
                "cupom": "", "ultima_conferencia": DATA,
            })

    json.dump(dados, open(caminho_json, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("produtos.json:", len(dados), "produtos")

    # cards nas páginas: nome -> slugs que entram
    mapa = {
        "index.html": [p["slug"] for p in PRODUTOS],
        "perifericos.html": [p["slug"] for p in PRODUTOS if p["cat_css"] == "perifericos"],
        "ssd.html": [p["slug"] for p in PRODUTOS if p["cat_css"] == "ssd"],
        "promocoes.html": [p["slug"] for p in PRODUTOS if p["desconto"]],
    }
    for nome, slugs_pagina in mapa.items():
        if not slugs_pagina:
            continue
        caminho = os.path.join(BASE, nome)
        h = open(caminho, encoding="utf-8").read()
        novos = [card(p) for p in PRODUTOS if p["slug"] in slugs_pagina]
        pos = h.find('<article class="card"')
        if pos < 0:
            continue
        # recua até o início da linha
        pos = h.rfind("\n", 0, pos) + 1
        h = h[:pos] + "\n".join(novos) + "\n    " + h[pos:]
        open(caminho, "w", encoding="utf-8").write(h)
        print(f"cards inseridos em {nome}: {len(novos)}")

    # sitemap
    sm = os.path.join(BASE, "sitemap.xml")
    s = open(sm, encoding="utf-8").read()
    for p in PRODUTOS:
        if f"{p['slug']}.html" in s:
            continue
        item = (f"  <url><loc>https://www.renatopenner.com.br/p/{p['slug']}.html</loc>"
                f"<lastmod>2026-10-28</lastmod></url>\n")
        s = s.replace("</urlset>", item + "</urlset>")
    open(sm, "w", encoding="utf-8").write(s)
    print("sitemap ok")


if __name__ == "__main__":
    main()
