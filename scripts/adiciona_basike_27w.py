"""Adiciona o Basike 27W (venda direta, R$ 36, Belém) ao site."""
import io
import json
import os
import re
import urllib.parse

from PIL import Image, ImageFilter

BASE = r"C:\Users\renat\SitesGithub\site-renato-penner"
FOTO = r"C:\Users\renat\AppData\Roaming\Hermes\composer-images\image_9ceaa6.png"
SLUG = "basike-27w-direto"
TITULO = "Carregador Basike 27W com cabo USB-C"
DATA = "28/10/2026"
WPP = "5591991455001"
WPP_EXIBE = "(91) 99145-5001"
PRECO = "R$ 36,00"
MENSAGEM = ("Olá, Renato! Vi o carregador Basike 27W no seu site e quero comprar "
            "por R$ 36 (entrega em Belém).")
LINK_WPP = f"https://wa.me/{WPP}?text={urllib.parse.quote(MENSAGEM)}"

SUB = "27 W · 1 porta USB-C · cabo USB-C de 67 W incluso · ANATEL homologado"
RESUMO = ("Carregador rápido de 27 W com cabo USB-C já na caixa: carrega celular e fone "
          "em pouco mais de uma hora e sobra cabo para outro aparelho. Vendo direto comigo "
          "em Belém, entrega combinada pelo WhatsApp.")
META = ("Carregador Basike MD-CAR271C de 27 W com porta USB-C e cabo USB-C de 67 W incluso, "
        "homologado pela ANATEL. Venda direta em Belém por R$ 36, entrega combinada pelo WhatsApp.")

DESTAQUES = [
    ("27 W de carga rápida", "Carrega celular e fone em pouco mais de uma hora; atende também tablet mais simples"),
    ("Cabo de 67 W na caixa", "Já vem com cabo USB-C de 67 W — serve para o carregador e para qualquer outra fonte"),
    ("Compacto e leve", "Ocupa menos que um carregador de notebook na tomada e vai fácil no bolso da mochila"),
    ("ANATEL homologado", "Etiqueta ANATEL 00133-26-13866 no produto, dentro da norma brasileira"),
]
FICHA = [
    "Modelo: Basike MD-CAR271C",
    "Potência: 27 W",
    "Portas: 1x USB-C (Power Delivery)",
    "Cabo incluso: USB-C de 67 W",
    "Certificação: ANATEL 00133-26-13866 · VAF 379518756",
    "Compatível: Android, iPhone (com cabo adequado) e fones USB-C",
]
PROS = [
    "Sai mais barato que qualquer 20 W de marca nas lojas",
    "Já vem com cabo — não precisa comprar separado",
    "27 W dão conta de celular com carga rápida e fone TWS ao mesmo tempo",
]
CONTRAS = [
    "Tem uma porta só: para carregar dois aparelhos juntos, o ideal é o Basike 65 W",
    "Venda apenas presencial em Belém, com entrega combinada — não envio para fora",
]
PORQUE = ("É o carregador que eu uso no dia a dia: 27 W, compacto e com cabo na caixa por R$ 36. "
          "Nas lojas, um 20 W só o plugue custa perto disso — e sem cabo. Vendo direto porque "
          "compro em quantidade e repasso o preço, com entrega combinada aqui em Belém.")


def monta_imagem():
    im = Image.open(FOTO).convert("RGB")
    fundo = im.resize((1120, 840), Image.Resampling.LANCZOS).filter(ImageFilter.GaussianBlur(22))
    # escurece um pouco o fundo para o produto destacar
    escuro = Image.new("RGB", fundo.size, (10, 16, 26))
    fundo = Image.blend(fundo, escuro, 0.35)
    alvo_h = 800
    escala = alvo_h / im.height
    novo = im.resize((int(im.width * escala), alvo_h), Image.Resampling.LANCZOS)
    fundo.paste(novo, ((1120 - novo.width) // 2, (840 - alvo_h) // 2))
    destino = os.path.join(BASE, "img", f"{SLUG}.png")
    fundo.save(destino, optimize=True)
    print("imagem:", destino, fundo.size)


def card():
    return f'''<article class="card" data-cat="carregadores" data-busca="carregador basike 27w 27 w usb-c cabo pd direto belem">
      <div class="thumbwrap"><a class="thumb" href="{LINK_WPP}" target="_blank" rel="noopener"><span class="badge">Direto comigo</span><img src="img/{SLUG}.png" style="object-fit:cover;padding:0" alt="{TITULO}" loading="lazy"></a></div>
      <div class="body">
        <span class="cat">Carregadores</span>
        <h3><a href="p/{SLUG}.html" style="color:inherit">{TITULO}</a></h3>
        <span class="sub">{SUB}</span>
        <p class="resumo">{RESUMO}</p>
        <div class="preco"><span class="por">R$ 36,00</span><small>venda direta · somente em Belém</small></div>
        <div class="direta-card">Direto comigo: R$ 36 · entrega combinada em Belém</div>
        <div class="btns">
          <a class="btn wa" href="{LINK_WPP}" target="_blank" rel="noopener">WhatsApp · R$ 36</a><a class="btn ghost" href="p/{SLUG}.html">Detalhes</a>
        </div>
      </div>
    </article>'''


def pagina():
    template = open(os.path.join(BASE, "p", "basike-65w.html"), encoding="utf-8").read()
    ini = template.index('<main class="wrap">')
    fim = template.index('</main>') + len('</main>')
    cabeca, cauda = template[:ini], template[fim:]

    cabeca = re.sub(r"<title>.*?</title>", f"<title>{TITULO} — Renato Penner</title>", cabeca, flags=re.S)
    cabeca = re.sub(r'<meta name="description" content="[^"]*"', f'<meta name="description" content="{META}"', cabeca)
    cabeca = re.sub(r'<link rel="canonical" href="[^"]*"', f'<link rel="canonical" href="https://www.renatopenner.com.br/p/{SLUG}.html"', cabeca)
    cabeca = re.sub(r'<meta property="og:title" content="[^"]*"', f'<meta property="og:title" content="{TITULO} — Renato Penner"', cabeca)
    cabeca = re.sub(r'<meta property="og:description" content="[^"]*"', f'<meta property="og:description" content="{META}"', cabeca)
    cabeca = re.sub(r'<meta property="og:url" content="[^"]*"', f'<meta property="og:url" content="https://www.renatopenner.com.br/p/{SLUG}.html"', cabeca)
    cabeca = re.sub(r'<meta name="build" content="[^"]*"', '<meta name="build" content="2026-10-28 11:30">', cabeca)

    destaques = "".join(f'<li class="dt"><strong>{t}:</strong> {d}</li>' for t, d in DESTAQUES)
    ficha = "".join(f'<li class="dt">{x}</li>' for x in FICHA)
    pros = "".join(f'<li class="ok">{x}</li>' for x in PROS)
    contras = "".join(f'<li class="no">{x}</li>' for x in CONTRAS)

    corpo = f'''<main class="wrap">
  <div class="migalha"><a href="../index.html">Início</a> /
    <a href="../carregadores.html">Carregadores</a> / {TITULO}</div>
  <section class="prod">
    <div class="foto"><img src="../img/{SLUG}.png" alt="{TITULO}"></div>
    <div>
      <span class="cat" style="color:#3ddc84;font-size:11px;font-weight:800;letter-spacing:.1em">DIRETO COMIGO · BELÉM</span>
      <h1>{TITULO}</h1>
      <div class="pmeta">{SUB}</div>
      <div class="preco"><span class="por">R$ 36,00</span><small>venda direta comigo · somente em Belém</small></div>
      <div class="box direta" style="margin-top:18px">
        <h4>Venda direta comigo</h4>
        <div class="direta-preco">R$ 36<small>entrega combinada</small></div>
        <p class="direta-info">Somente em Belém: combino a entrega pelo WhatsApp, em bairros próximos ou ponto combinado.</p>
        <span class="direta-estoque">27 W · CABO USB-C INCLUSO</span>
        <div class="btns" style="margin-top:14px">
          <a class="btn wa" href="{LINK_WPP}" target="_blank" rel="noopener">Falar no WhatsApp · {WPP_EXIBE}</a>
        </div>
      </div>
      <div class="box"><h4>Por que eu recomendo</h4><p style="color:#c6d5e2;font-size:14.5px">{PORQUE}</p></div>
      <div class="box"><h4>Destaques</h4><ul>{destaques}</ul></div>
      <div class="box"><h4>Ficha técnica</h4><ul>{ficha}</ul></div>
      <div class="box"><h4>Prós</h4><ul>{pros}</ul><h4 style="margin-top:14px">Contras</h4><ul>{contras}</ul></div>
    </div>
  </section>
</main>'''

    ld = ('<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Product", '
          f'"name": "{TITULO}", "description": "{META}", '
          f'"offers": {{"@type": "Offer", "url": "{LINK_WPP}", "price": "36.00", '
          '"priceCurrency": "BRL", "availability": "https://schema.org/InStock"}}</script>')
    cauda = re.sub(r'<script type="application/ld\+json">.*?</script>', ld, cauda, count=1, flags=re.S)
    return cabeca + corpo + cauda


def main():
    monta_imagem()
    open(os.path.join(BASE, "p", f"{SLUG}.html"), "w", encoding="utf-8").write(pagina())
    print("página criada")

    caminho = os.path.join(BASE, "dados", "produtos.json")
    dados = json.load(open(caminho, encoding="utf-8"))
    if SLUG not in {x["slug"] for x in dados}:
        dados.append({
            "slug": SLUG, "title": TITULO, "file": f"{SLUG}.html", "cat": "Direto comigo",
            "link": LINK_WPP, "preco_de": "", "preco_por": PRECO, "preco_cartao": "",
            "cupom": "", "ultima_conferencia": DATA,
        })
        json.dump(dados, open(caminho, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("produtos.json:", len(dados))

    for nome in ("index.html", "carregadores.html"):
        p = os.path.join(BASE, nome)
        h = open(p, encoding="utf-8").read()
        if SLUG in h:
            print("já existe em", nome)
            continue
        pos = h.find('<article class="card"')
        pos = h.rfind("\n", 0, pos) + 1
        h = h[:pos] + card() + "\n    " + h[pos:]
        open(p, "w", encoding="utf-8").write(h)
        print("card inserido em", nome)

    sm = os.path.join(BASE, "sitemap.xml")
    s = open(sm, encoding="utf-8").read()
    if f"{SLUG}.html" not in s:
        s = s.replace("</urlset>",
                      f"  <url><loc>https://www.renatopenner.com.br/p/{SLUG}.html</loc><lastmod>2026-10-28</lastmod></url>\n</urlset>")
        open(sm, "w", encoding="utf-8").write(s)
        print("sitemap atualizado")


if __name__ == "__main__":
    main()
