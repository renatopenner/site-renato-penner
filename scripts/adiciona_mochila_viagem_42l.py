"""Adiciona a Mochila Impermeável Reforçada 30-42L para Notebook e Viagem ao site renatopenner.com.br (GitHub Pages)."""
import json
import os
import re
from PIL import Image

BASE = r"C:\Users\renat\SitesGithub\site-renato-penner"
BASE_ALT = r"C:\Users\renat\site-renato-penner"
FOTO_ORIG = r"C:\Users\renat\.gemini\antigravity\brain\3a42011e-1095-4bdc-8513-d502c0799e9a\.user_uploaded\media_1793898431587_f71439d5.png"
SLUG = "mochila-viagem-notebook-impermeavel-42l"
DATA = "05/11/2026"
MARCA_W, MARCA_H = 1120, 840

PRODUTO = {
    "slug": SLUG,
    "titulo_card": "Mochila Impermeável Reforçada 30-42L para Notebook e Viagem",
    "h1": "Mochila Unissex Impermeável e Reforçada 30-42L Expansível para Notebook 15.6\" e Viagem",
    "meta_desc": "Mochila unissex impermeável de alta capacidade expansível de 30 a 42L, compartimento acolchoado para notebook até 15.6\", porta USB integrada, alça para mala de bordo, tecido náilon/PVC resistente e acabamento ergonômico reforçado.",
    "cat_badge": "Mercado Livre · Mais Vendido · 6º em Mochilas",
    "cat_css": "moda",
    "categoria_nome": "Moda e Viagem",
    "sub": "Capacidade 30-42L Expansível · Notebook até 15.6\" · Impermeável · Porta USB · Alça para Mala",
    "resumo": "Mochila executiva e de viagem unissex com capacidade ajustável de 30 a 42 litros, compartimento exclusivo acolchoado contra impactos para notebook de 15.6 polegadas, tecido impermeável em náilon e PVC, porta USB externa e cinta traseira para fixação em malas de bordo.",
    "link": "https://meli.la/16Y65Ur",
    "preco_de": "R$ 216,00",
    "preco_por": "R$ 94,00",
    "preco_cartao": "em até 5x de R$ 18,80 sem juros",
    "desconto": "56% OFF",
    "porque": "Para quem atua na área de TI, engenharia ou viaja com frequência, uma mochila confiável precisa cumprir três papéis indispensáveis: proteger equipamentos caros, aguentar chuva urbana repentina e se adaptar ao volume de carga sem parecer uma mala desajeitada. Essa mochila modelo 9248 entrega exatamente essa tríade com maestria.<br><br>Seu grande trunfo é o <strong>fole expansível com fivelas de compressão laterais</strong>: no dia a dia no escritório, ela permanece compacta em 30 litros; quando surge uma viagem de negócios ou fim de semana, expande para <strong>42 litros reais</strong>, acomodando roupas, calçados e necessaire sem necessidade de mala adicional. O compartimento traseiro conta com <strong>acolchoamento reforçado antichoque para notebooks de até 15.6 polegadas</strong>, o acabamento externo em náilon e PVC repele água com facilidade, a porta USB integrada viabiliza carregar o celular em trânsito e a faixa posterior permite encaixá-la diretamente no puxador retrátil da mala de bordo em aeroportos.",
    "destaques": [
        ("Capacidade Expansível de 30 a 42 Litros", "Sistema com zíper expansor e presilhas laterais de compressão rápida, permitindo ajustar o tamanho para o dia a dia compacto ou expandir para bagagem completa de viagem."),
        ("Compartimento Acolchoado Antichoque para Notebook", "Divisória exclusiva e acolchoada para acomodar com segurança notebooks de até 15.6 polegadas e tablets contra impactos e quedas acidentais."),
        ("Acabamento Impermeável em Náilon e PVC", "Tecido denso e repelente a líquidos que protege documentos, roupas e eletrônicos contra respingos e chuvas repentinas no trajeto urbano."),
        ("Conexão USB Integrada e Saída de Fone", "Porta USB externa pass-through que permite ligar um powerbank interno para recarregar smartphones em movimento mantendo as mãos livres."),
        ("Cinta Traseira para Acoplar em Malas", "Faixa transversal ergonômica que se fixa firmemente na haste retrátil de malas de bordo, facilitando a circulação em aeroportos e terminais."),
        ("Ergonomia e Costuras Reforçadas", "Alças de ombro respiráveis e acolchoadas com formato ergonômico em S, alça de mão reforçada e peso vazio de apenas 900 g para máximo conforto."),
        ("Design Unissex Sóbrio e Versátil", "Acabamento preto fosco minimalista e profissional que transita com elegância entre reuniões de trabalho, ambiente acadêmico e viagens de lazer."),
    ],
    "ficha": [
        "Marca: Jiesipote Fashion",
        "Modelo: 9248 (Mochila Executiva e Viagem Expansível)",
        "Capacidade volumétrica: ajustável de 30 a 42 Litros",
        "Compatibilidade de notebook: laptops de até 15.6 polegadas",
        "Material: Náilon de alta densidade + revestimento em PVC impermeável",
        "Dimensões aproximadas: 45 cm (altura) x 30 cm (largura) x 24 cm (profundidade)",
        "Peso vazio: aproximadamente 900 g",
        "Tipo de fechamento: Zíperes reforçados bidirecionais",
        "Conectividade integrada: 1x Entrada USB externa pass-through + 1x Saída para fone de ouvido",
        "Alças e suporte: Alças de ombro acolchoadas respiráveis, alça de mão almofadada e cinta para haste de mala de bordo",
        "Gênero / Estilo: Sem gênero (unissex) / Executivo, urbano, trabalho e viagem",
        "Classificação Mercado Livre: 6º lugar em Mochilas (+10 mil unidades vendidas, avaliação 4.9 de 5 estrelas)",
        "Itens inclusos: 1x Mochila Executiva Expansível 30-42L Modelo 9248 Cor Preta com cabo USB interno",
    ],
    "pros": [
        "Excelente custo-benefício por R$ 94,00 com 56% de desconto em produto com nota 4.9 e mais de 10.000 vendas",
        "Fole expansível de 30L a 42L com presilhas de compressão que se adapta perfeitamente do trabalho diário a viagens curtas",
        "Proteção impermeável eficiente que protege notebook e eletrônicos contra umidade e chuvas repentinas",
        "Compartimento traseiro bem acolchoado protegendo laptops de até 15.6 polegadas contra batidas",
        "Porta USB externa prática para carregar celular na rua sem precisar abrir a mochila",
        "Cinta de acoplamento na mala de bordo que poupa esforço físico em viagens e aeroportos",
        "Material leve (900g) e resistente com costuras firmes nas alças",
    ],
    "contras": [
        "Não acompanha bateria portátil (powerbank necessário para usar a porta de carga USB externa)",
        "Laptops gamers extragrandes de 17.3 polegadas não cabem no compartimento acolchoado dedicado",
    ],
    "para_quem": "Profissionais de TI, engenheiros, técnicos, estudantes universitários e qualquer pessoa que precise de uma mochila resistente, elegante e impermeável para levar notebook no dia a dia, com a flexibilidade de virar uma mala de bordo para viagens curtas de avião ou rodoviárias.",
}


def prepara_imagem():
    im = Image.open(FOTO_ORIG).convert("RGB")
    # Bounding box do produto: (110, 40, 816, 876)
    cropped = im.crop((110, 40, 816, 876))
    alvo_h = 760
    scale = alvo_h / cropped.height
    novo_w = int(cropped.width * scale)
    novo = cropped.resize((novo_w, alvo_h), Image.Resampling.LANCZOS)
    tela = Image.new("RGB", (MARCA_W, MARCA_H), (255, 255, 255))
    tela.paste(novo, ((MARCA_W - novo.width) // 2, (MARCA_H - alvo_h) // 2))

    for base_dir in [BASE, BASE_ALT]:
        if os.path.exists(base_dir):
            destino = os.path.join(base_dir, "img", f"{SLUG}.png")
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


def gera_card(p, cat_override=None, badge_override=None):
    cat_css = cat_override if cat_override else p["cat_css"]
    cat_nome = p["categoria_nome"]
    badge = badge_override if badge_override else p["cat_badge"]
    busca = re.sub(
        r"[^a-z0-9 ]",
        " ",
        (p["titulo_card"] + " " + p["sub"] + " " + p["slug"] + " mochila viagem notebook impermeavel 42l expansivel preta executiva jiesipote").lower(),
    )
    busca = re.sub(r"\s+", " ", busca).strip()
    return f'''<article class="card" data-cat="{cat_css}" data-busca="{busca}">
      <div class="thumbwrap"><a class="thumb" href="{p['link']}" target="_blank" rel="sponsored nofollow noopener"><span class="badge">{badge}</span><img src="img/{p['slug']}.png" alt="{p['titulo_card']}" loading="lazy"></a></div>
      <div class="body">
        <span class="cat">{cat_nome}</span>
        <h3><a href="p/{p['slug']}.html" style="color:inherit">{p['titulo_card']}</a></h3>
        <span class="sub">{p['sub']}</span>
        <p class="resumo">{p['resumo']}</p>
        {bloco_preco(p)}
        <div class="btns">
          <a class="btn" href="{p['link']}" target="_blank" rel="sponsored nofollow noopener">Ver oferta →</a><a class="btn ghost" href="p/{p['slug']}.html">Detalhes</a>
        </div>
      </div>
    </article>'''


def gera_pagina_completa(p):
    destaques = "".join(f'<li class="dt"><strong>{t}:</strong> {d}</li>' for t, d in p["destaques"])
    ficha = "".join(f'<li class="dt">{x}</li>' for x in p["ficha"])
    pros = "".join(f'<li class="ok">{x}</li>' for x in p["pros"])
    contras = "".join(f'<li class="no">{x}</li>' for x in p["contras"])
    preco_num = re.sub(r"[^\d,]", "", p["preco_por"]).replace(".", "").replace(",", ".")

    html = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta http-equiv="Cache-Control" content="no-store">
<meta name="build" content="2026-11-05 14:15">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{p['titulo_card']} — Renato Penner</title>
<meta name="description" content="{p['meta_desc']}">
<link rel="canonical" href="https://www.renatopenner.com.br/p/{p['slug']}.html">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Renato Penner">
<meta property="og:title" content="{p['titulo_card']} — Renato Penner">
<meta property="og:description" content="{p['meta_desc']}">
<meta property="og:url" content="https://www.renatopenner.com.br/p/{p['slug']}.html">
<meta property="og:locale" content="pt_BR">
<meta name="theme-color" content="#050a12">
<meta property="og:image" content="https://www.renatopenner.com.br/img/{p['slug']}.png">
<meta property="og:image:width" content="1120">
<meta property="og:image:height" content="840">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://www.renatopenner.com.br/img/{p['slug']}.png">
<link rel="icon" type="image/png" sizes="64x64" href="../img/favicon-64.png?v=300a8b34">
<link rel="icon" type="image/png" sizes="192x192" href="../img/icon-192.png?v=348692ee">
<link rel="apple-touch-icon" href="../img/apple-touch-icon.png?v=5bcd05bd">
<link rel="stylesheet" href="../css/style.css?v=4cf08b7c">
<script>
addEventListener('load',function(){{try{{var u='https://renatopennersoares1783016458000.0871043.meusitehostgator.com.br/c.php?p='+encodeURIComponent(location.pathname)+'&o='+encodeURIComponent(location.hostname);
  if(navigator.sendBeacon){{navigator.sendBeacon(u);}}else{{fetch(u,{{keepalive:true}});}}}}catch(e){{}}}});
document.addEventListener('click',function(ev){{var a=ev.target&&ev.target.closest?ev.target.closest('a'):null;if(!a)return;
  var h=a.href||'',d='';
  if(h.indexOf('mercadolivre')>=0||h.indexOf('meli.la')>=0)d='mercadolivre';
  else if(h.indexOf('amazon')>=0)d='amazon';
  else if(h.indexOf('wa.me')>=0||h.indexOf('whatsapp')>=0)d='whatsapp';
  else if(h.indexOf('youtu')>=0)d='youtube';
  if(!d)return;try{{var u='https://renatopennersoares1783016458000.0871043.meusitehostgator.com.br/c.php?e=c&d='+d+'&p='+encodeURIComponent(location.pathname)+'&o='+encodeURIComponent(location.hostname);
  if(navigator.sendBeacon){{navigator.sendBeacon(u);}}else{{fetch(u,{{keepalive:true}});}}}}catch(e){{}}}});
</script>

<script>
(function(){{
  var ID='G-T3M72SC18N', carregado=false;
  window.dataLayer=window.dataLayer||[];
  window.gtag=function(){{dataLayer.push(arguments);}};
  function carrega(){{
    if(carregado) return; carregado=true;
    var s=document.createElement('script'); s.async=true;
    s.src='https://www.googletagmanager.com/gtag/js?id='+ID;
    document.head.appendChild(s);
    gtag('js', new Date());
    gtag('consent','update',{{analytics_storage:'granted'}});
    gtag('config', ID, {{anonymize_ip:true}});
  }}
  window.__ga4Carrega=carrega;
  try{{ if(localStorage.getItem('consent')==='ok') carrega(); }}catch(e){{}}
}})();
</script>
<script defer src="../js/ofertas.js"></script>
</head>
<body>
<header><div class="wrap nav">
  <a href="../index.html" class="logo" aria-label="Renato Penner — início"><img src="../img/marca.png?v=e1cc9158" alt=""><span>RENATO PENNER<small>ENGENHEIRO DA COMPUTAÇÃO</small></span></a>
  <nav class="links"><a class="link " href="../index.html">Início</a><a class="link " href="../promocoes.html">Ofertas</a><a class="link " href="../notebooks.html">Notebooks</a><a class="link " href="../ssd.html">SSD</a><a class="link " href="../carregadores.html">Carregadores</a><a class="link " href="../saude.html">Saúde</a><a class="link " href="../casa.html">Casa</a><a class="link " href="../auto.html">Auto</a><a class="link " href="../perifericos.html">Periféricos</a><a class="link on" href="../moda.html">Moda</a></nav>
  <div class="dir"><a class="link" href="https://www.youtube.com/@renatopenner2037" target="_blank" rel="noopener">YouTube ↗</a></div>
</div></header>
<main class="wrap">
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

      <div class="box" style="border-left:4px solid #38bdf8;background:rgba(56,189,248,0.06);padding:14px 18px;border-radius:10px;margin:20px 0;">
        <h4 style="color:#38bdf8;display:flex;align-items:center;gap:8px;margin-bottom:6px;">
          <span>🎒</span> Fole Expansível 30L a 42L com Proteção Impermeável
        </h4>
        <p style="color:#dbe7f3;font-size:14.5px;margin:0;line-height:1.55;">
          Versatilidade total para o dia a dia e viagens: funciona compacta no trajeto de trabalho/estudo e expande com facilidade para até <strong>42 litros</strong> para acomodar roupas e calçados. Conta com <strong>tecido impermeável em náilon e PVC</strong>, porta USB pass-through e <strong>cinta para fixação no puxador da mala de bordo</strong>.
        </p>
      </div>

      <div class="box"><h4>Por que eu recomendo</h4><p style="color:#c6d5e2;font-size:14.5px">{p['porque']}</p></div>
      <div class="box"><h4>Destaques e Recursos</h4><ul>{destaques}</ul></div>
      <div class="box"><h4>Ficha Técnica e Conteúdo</h4><ul>{ficha}</ul></div>
      <div class="box"><h4>Prós</h4><ul>{pros}</ul><h4 style="margin-top:14px">Contras</h4><ul>{contras}</ul></div>
      <div class="box"><h4>Para quem serve</h4><p style="color:#c6d5e2;font-size:14.5px">{p['para_quem']}</p></div>
    </div>
  </section>
</main>
<script type="application/ld+json">{{"@context": "https://schema.org", "@type": "Product", "name": "{p['titulo_card']}", "description": "{p['meta_desc']}", "brand": {{"@type": "Brand", "name": "Jiesipote"}}, "offers": {{"@type": "Offer", "url": "{p['link']}", "price": "{preco_num}", "priceCurrency": "BRL", "availability": "https://schema.org/InStock", "seller": {{"@type": "Organization", "name": "Mercado Livre"}}}}, "aggregateRating": {{"@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "1837"}}}}</script>

<footer><div class="wrap">
  <img class="marca" src="../img/lockup-rodape.png?v=462caf9a" alt="Renato Penner — Engenharia da Computação">
  <div class="aviso"><strong>Aviso de afiliado:</strong> os links deste site são de afiliado.
  Se você comprar por eles, eu recebo uma comissão da loja — <strong>sem nenhum custo a mais para você</strong>.
  Preços e disponibilidade são da data indicada em cada produto e podem mudar sem aviso.
  Última verificação dos links: {DATA}.</div>

<div id="lgpd" style="display:none;position:fixed;left:16px;right:16px;bottom:16px;z-index:99;
max-width:560px;margin:0 auto;background:#111f2e;border:1px solid #1e3448;border-radius:14px;
padding:14px 16px;box-shadow:0 10px 30px rgba(0,0,0,.5);font:13.5px/1.45 'Segoe UI',system-ui,sans-serif;color:#dbe7f3">
  <p style="margin:0 0 10px">Uso o Google Analytics para entender o que você procura aqui e melhorar
  as recomendações. Isso grava cookies de medição, sem identificar você. Dá para recusar.</p>
  <div style="display:flex;gap:8px;flex-wrap:wrap">
    <button id="lgpd-ok" style="background:#38bdf8;color:#04121d;border:0;border-radius:8px;
    padding:8px 16px;font-weight:800;font-size:13px;cursor:pointer">Aceitar</button>
    <button id="lgpd-no" style="background:transparent;color:#8fa6bb;border:1px solid #1e3448;
    border-radius:8px;padding:8px 16px;font-weight:700;font-size:13px;cursor:pointer">Recusar</button>
  </div>
</div>
<script>
(function(){{
  var b=document.getElementById('lgpd'); if(!b) return;
  var escolha=''; try{{escolha=localStorage.getItem('consent')||'';}}catch(e){{}}
  if(!escolha) b.style.display='block';
  document.getElementById('lgpd-ok').onclick=function(){{
    try{{localStorage.setItem('consent','ok');}}catch(e){{}}
    if(window.__ga4Carrega) window.__ga4Carrega();
    b.style.display='none';
  }};
  document.getElementById('lgpd-no').onclick=function(){{
    try{{localStorage.setItem('consent','no');}}catch(e){{}}
    b.style.display='none';
  }};
}})();
</script>
</div></footer>
</body>
</html>
"""
    return html


def atualiza_paginas_html(p, novo_card):
    for base_dir in [BASE, BASE_ALT]:
        if not os.path.exists(base_dir):
            continue

        paginas = ["moda.html", "index.html", "promocoes.html"]
        for nome in paginas:
            caminho = os.path.join(base_dir, nome)
            if not os.path.exists(caminho):
                continue
            content = open(caminho, encoding="utf-8").read()

            if f"p/{SLUG}.html" in content:
                print(f"Card já existe em {base_dir}/{nome}")
                continue

            pos = content.find('<article class="card"')
            if pos >= 0:
                pos = content.rfind("\n", 0, pos) + 1
                content = content[:pos] + novo_card + "\n    " + content[pos:]
                print(f"Card inserido no topo em {base_dir}/{nome}")
                with open(caminho, "w", encoding="utf-8") as f:
                    f.write(content)
            else:
                print(f"Não achou ponto de inserção em {base_dir}/{nome}")


def atualiza_produtos_json(p):
    for base_dir in [BASE, BASE_ALT]:
        if not os.path.exists(base_dir):
            continue
        caminho_json = os.path.join(base_dir, "dados", "produtos.json")
        if not os.path.exists(caminho_json):
            continue

        dados = json.load(open(caminho_json, encoding="utf-8"))
        slugs = {item["slug"] for item in dados}

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
            print(f"produtos.json atualizado em {base_dir}")
        else:
            for item in dados:
                if item["slug"] == SLUG:
                    item["title"] = p["titulo_card"]
                    item["link"] = p["link"]
                    item["preco_de"] = p["preco_de"]
                    item["preco_por"] = p["preco_por"]
                    item["preco_cartao"] = p["preco_cartao"]
                    item["ultima_conferencia"] = DATA
            json.dump(dados, open(caminho_json, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
            print(f"produtos.json sincronizado com {SLUG} em {base_dir}")


def atualiza_sitemap():
    for base_dir in [BASE, BASE_ALT]:
        if not os.path.exists(base_dir):
            continue
        sm_path = os.path.join(base_dir, "sitemap.xml")
        if os.path.exists(sm_path):
            sm_content = open(sm_path, encoding="utf-8").read()
            if f"{SLUG}.html" not in sm_content:
                item = f"  <url><loc>https://www.renatopenner.com.br/p/{SLUG}.html</loc><lastmod>2026-11-05</lastmod></url>\n"
                sm_content = sm_content.replace("</urlset>", item + "</urlset>")
                with open(sm_path, "w", encoding="utf-8") as f:
                    f.write(sm_content)
                print(f"sitemap.xml atualizado em {base_dir}")


def main():
    p = PRODUTO
    prepara_imagem()

    # 1. Página de produto
    page_html = gera_pagina_completa(p)
    for base_dir in [BASE, BASE_ALT]:
        if os.path.exists(base_dir):
            page_path = os.path.join(base_dir, "p", f"{SLUG}.html")
            with open(page_path, "w", encoding="utf-8") as f:
                f.write(page_html)
            print("Página criada:", page_path)

    # 2. Atualizar dados/produtos.json
    atualiza_produtos_json(p)

    # 3. Inserir cards nas páginas HTML
    card = gera_card(p)
    atualiza_paginas_html(p, card)

    # 4. Atualizar sitemap.xml
    atualiza_sitemap()


if __name__ == "__main__":
    main()
