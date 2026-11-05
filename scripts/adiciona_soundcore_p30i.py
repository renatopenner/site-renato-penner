"""Adiciona o Fone de Ouvido Anker Soundcore P30i ao site renatopenner.com.br (GitHub Pages)."""
import io
import json
import os
import re
import shutil
from PIL import Image

BASE = r"C:\Users\renat\SitesGithub\site-renato-penner"
BASE_ALT = r"C:\Users\renat\site-renato-penner"
FOTO_ORIG = r"C:\Users\renat\.gemini\antigravity\brain\29295e98-da51-459e-ad07-56f9e77383ae\.user_uploaded\media_1793896394439_9358f85d.png"
SLUG = "soundcore-p30i-anker"
DATA = "05/11/2026"
MARCA_W, MARCA_H = 1120, 840

PRODUTO = {
    "slug": SLUG,
    "titulo_card": "Fone de Ouvido Bluetooth Anker Soundcore P30i",
    "h1": "Fone de Ouvido Sem Fio Anker Soundcore P30i com Cancelamento de Ruído Adaptativo (ANC 42dB) e Suporte para Celular",
    "meta_desc": "Fone de Ouvido Bluetooth Anker Soundcore P30i com Cancelamento Ativo de Ruído ANC 42dB, Bluetooth 5.4 multiponto, bateria para até 45 horas, drivers de 10 mm e estojo 2 em 1 com suporte para celular.",
    "cat_badge": "Mercado Livre · Loja Oficial · Mais Vendido",
    "cat_css": "casa",
    "categoria_nome": "Casa e áudio",
    "sub": "ANC Adaptativo 42 dB · Bluetooth 5.4 Conexão Dupla · Bateria 45h · Estojo Suporte 2 em 1 · IP54",
    "resumo": "O fone intra-auricular que une som imersivo e máxima praticidade: cancelamento ativo de ruído inteligente de até 42 dB, drivers dinâmicos de 10 mm com graves marcantes, conexão multiponto para alternar entre notebook e celular sem perder tempo, bateria para até 45 horas totais e estojo 2 em 1 que funciona como suporte de mesa para smartphone.",
    "link": "https://meli.la/28zv85J",
    "preco_de": "R$ 389,00",
    "preco_por": "R$ 196,00",
    "preco_cartao": "em até 6x R$ 32,66 sem juros",
    "desconto": "50% OFF",
    "porque": "A Anker acertou em cheio no Soundcore P30i ao entregar recursos de fones topo de linha por uma fração do preço. O cancelamento de ruído adaptativo de 42 dB silencia com eficiência ruídos de trânsito, metrô e conversas ao redor no trabalho. A conexão dupla inteligente (multiponto) permite que você participe de reuniões no notebook e atenda chamadas no celular sem precisar desconectar. Além disso, a bateria absurda de até 45 horas e o estojo com apoio integrado para apoiar o celular na mesa tornam este fone o parceiro definitivo para produtividade, jogos e viagens.",
    "destaques": [
        ("Cancelamento de Ruído Adaptativo (ANC)", "Tecnologia inteligente que detecta o ambiente e atenua ruídos indesejados em até 42 dB para imersão total no trabalho, transporte ou descanso"),
        ("Bluetooth 5.4 e Conexão Dupla", "Alterne suavemente entre o notebook e o celular sem precisar reconectar; áudio sem perdas e baixíssima latência para jogos e streaming"),
        ("Graves Potentes com Drivers de 10 mm", "Drivers dinâmicos de 10 mm combinados com tecnologia exclusiva Soundcore para graves encorpados, médios presentes e agudos equilibrados"),
        ("Bateria para até 45 Horas", "Até 10 horas de reprodução contínua com uma única carga e até 45 horas totais com o estojo de carregamento"),
        ("Estojo Inovador 2 em 1 com Suporte", "Design funcional que traz um suporte articulado oculto no estojo para apoiar o smartphone na vertical ou horizontal enquanto assiste aulas ou vídeos"),
        ("Chamadas Claras com 4 Microfones IA", "Quatro microfones com algoritmo de inteligência artificial que filtram o barulho externo e mantêm a voz cristalina em chamadas"),
        ("Resistência IP54 e Conforto Ergonômico", "Proteção contra poeira e respingos de suor/chuva leve e encaixe leve com 3 tamanhos de ponteiras de silicone"),
    ],
    "ficha": [
        "Marca: Soundcore by Anker",
        "Modelo: Soundcore P30i (A3959)",
        "Tipo: Fone de ouvido intra-auricular True Wireless Stereo (TWS)",
        "Conectividade: Bluetooth 5.4 com suporte a Conexão Multiponto (2 aparelhos simultâneos)",
        "Cancelamento de Ruído: ANC Adaptativo de até 42 dB com modo Transparência",
        "Drivers: Dinâmicos de 10 mm com tecnologia BassUp",
        "Autonomia da bateria: Até 10 horas por carga / até 45 horas totais com o estojo",
        "Carregamento: USB Tipo-C (cabo incluso) com recarga rápida",
        "Microfones: 4 microfones direcionais com cancelamento de ruído assistido por IA",
        "Certificação de proteção: IP54 (resistente a poeira e respingos de água)",
        "Conteúdo da embalagem: 1x Par de fones Soundcore P30i, 1x Estojo de carregamento 2 em 1 com suporte, 1x Cabo USB-C, 3x Pares de pontas de silicone (P/M/G), Manual e garantia",
    ],
    "pros": [
        "Cancelamento de ruído ativo adaptativo de 42 dB muito eficiente nesta faixa de valor",
        "Conexão multiponto real: alterna automaticamente entre chamadas no celular e vídeos no notebook",
        "Estojo 2 em 1 inteligente com suporte articulado para apoiar o smartphone na mesa",
        "Autonomia espetacular: até 10 horas nos fones e 45 horas no total",
        "Qualidade de som Anker reconhecida mundialmente, com aplicativo Soundcore e equalizador customizável",
        "Excelente custo-benefício com 50% de desconto e parcelamento em 6x sem juros",
    ],
    "contras": [
        "Não possui carregamento sem fio por indução Qi no estojo (apenas USB Tipo-C com fio)",
    ],
    "para_quem": "Profissionais e estudantes que passam o dia em reuniões ou estudando e precisam alternar entre notebook e celular, quem pega transporte público e quer silêncio com cancelamento de ruído, gamers que buscam baixa latência e quem quer um fone resistente e confiável para o dia a dia sem gastar valores abusivos.",
}


def prepara_imagem():
    im = Image.open(FOTO_ORIG).convert("RGB")
    bbox = (20, 35, 595, 995)
    cropped = im.crop(bbox)
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
    cat_nome = "Periféricos e acessórios" if cat_css == "perifericos" else p["categoria_nome"]
    badge = badge_override if badge_override else p["cat_badge"]
    busca = re.sub(r"[^a-z0-9 ]", " ", (p["titulo_card"] + " " + p["sub"] + " " + p["slug"] + " fone anker soundcore cancelamento de ruido tws sem fio").lower())
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
    destaques = "".join(f"<li class=\"dt\"><strong>{t}:</strong> {d}</li>" for t, d in p["destaques"])
    ficha = "".join(f'<li class="dt">{x}</li>' for x in p["ficha"])
    pros = "".join(f'<li class="ok">{x}</li>' for x in p["pros"])
    contras = "".join(f'<li class="no">{x}</li>' for x in p["contras"])
    preco_num = re.sub(r"[^\d,]", "", p["preco_por"]).replace(".", "").replace(",", ".")

    html = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta http-equiv="Cache-Control" content="no-store">
<meta name="build" content="2026-11-05 13:30">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{p['titulo_card']} — Renato Penner</title>
<meta name="description" content="{p['meta_desc']}">
<link rel="canonical" href="https://renatopenner.github.io/site-renato-penner/p/{p['slug']}.html">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Renato Penner">
<meta property="og:title" content="{p['titulo_card']} — Renato Penner">
<meta property="og:description" content="{p['meta_desc']}">
<meta property="og:url" content="https://renatopenner.github.io/site-renato-penner/p/{p['slug']}.html">
<meta property="og:locale" content="pt_BR">
<meta name="theme-color" content="#050a12">
<meta property="og:image" content="https://renatopenner.github.io/site-renato-penner/img/{p['slug']}.png">
<meta property="og:image:width" content="1120">
<meta property="og:image:height" content="840">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://renatopenner.github.io/site-renato-penner/img/{p['slug']}.png">
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
  <nav class="links"><a class="link " href="../index.html">Início</a><a class="link " href="../promocoes.html">Ofertas</a><a class="link " href="../notebooks.html">Notebooks</a><a class="link " href="../ssd.html">SSD</a><a class="link " href="../carregadores.html">Carregadores</a><a class="link " href="../saude.html">Saúde</a><a class="link on" href="../casa.html">Casa</a><a class="link " href="../auto.html">Auto</a><a class="link " href="../perifericos.html">Periféricos</a><a class="link " href="../moda.html">Moda</a></nav>
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
      <div class="box"><h4>Por que eu recomendo</h4><p style="color:#c6d5e2;font-size:14.5px">{p['porque']}</p></div>
      <div class="box"><h4>Destaques e Recursos</h4><ul>{destaques}</ul></div>
      <div class="box"><h4>Ficha Técnica e Conteúdo</h4><ul>{ficha}</ul></div>
      <div class="box"><h4>Prós</h4><ul>{pros}</ul><h4 style="margin-top:14px">Contras</h4><ul>{contras}</ul></div>
      <div class="box"><h4>Para quem serve</h4><p style="color:#c6d5e2;font-size:14.5px">{p['para_quem']}</p></div>
    </div>
  </section>
</main>
<script type="application/ld+json">{{"@context": "https://schema.org", "@type": "Product", "name": "{p['titulo_card']}", "description": "{p['meta_desc']}", "brand": {{"@type": "Brand", "name": "Soundcore by Anker"}}, "offers": {{"@type": "Offer", "url": "{p['link']}", "price": "{preco_num}", "priceCurrency": "BRL", "availability": "https://schema.org/InStock"}}, "aggregateRating": {{"@type": "AggregateRating", "ratingValue": "4.8", "reviewCount": "420"}}}}</script>

<footer><div class="wrap">
  <img class="marca" src="../img/lockup-rodape.png?v=462caf9a" alt="Renato Penner — Engenharia da Computação">
  <div class="aviso"><strong>Aviso de afiliado:</strong> os links deste site são de afiliado.
  Se você comprar por eles, eu recebo uma comissão da loja — <strong>sem nenhum custo a mais para você</strong>.
  Preços e disponibilidade são da data indicada em cada produto e podem mudar sem aviso.
  Última verificação dos links: 05/11/2026.</div>
  
<div id="lgpd" style="display:none;position:fixed;left:16px;right:16px;bottom:16px;z-index:99;
max-width:560px;margin:0 auto;background:#111f2e;border:1px solid #1e3448;border-radius:14px;
padding:14px 16px;box-shadow:0 10px 30px rgba(0,0,0,.5);font:13.5px/1.45 'Segoe UI',system-ui,sans-serif;color:#dbe7f3">
  <p style="margin:0 0 10px">Uso o Google Analytics para entender o que você procura aqui e melhorar as recomendações. Não guardo nem vendo seus dados. Você aceita?</p>
  <div style="display:flex;gap:10px;justify-content:flex-end">
    <button id="lgpd-recusar" style="background:transparent;border:1px solid #334d66;color:#94a8bd;padding:7px 14px;border-radius:8px;font:inherit;font-size:13px;cursor:pointer">Não, obrigado</button>
    <button id="lgpd-aceitar" style="background:#38bdf8;border:none;color:#050a12;padding:7px 16px;border-radius:8px;font:inherit;font-size:13px;font-weight:700;cursor:pointer">Aceitar</button>
  </div>
</div>
</div></footer>
</body>
</html>
"""
    return html


def main():
    p = PRODUTO
    prepara_imagem()

    # 1. Página de produto p/soundcore-p30i-anker.html
    page_html = gera_pagina_completa(p)

    for base_dir in [BASE, BASE_ALT]:
        if os.path.exists(base_dir):
            page_path = os.path.join(base_dir, "p", f"{SLUG}.html")
            with open(page_path, "w", encoding="utf-8") as f:
                f.write(page_html)
            print("Página criada com perfeição:", page_path)

    # 2. Atualizar dados/produtos.json
    for base_dir in [BASE, BASE_ALT]:
        if os.path.exists(base_dir):
            caminho_json = os.path.join(base_dir, "dados", "produtos.json")
            if os.path.exists(caminho_json):
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
                    print(f"produtos.json atualizado em {base_dir}")
                else:
                    # Atualiza item existente
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

    # 3. Inserir cards nas páginas HTML
    card_casa = gera_card(p, cat_override="casa")
    card_perifericos = gera_card(p, cat_override="perifericos")

    for base_dir in [BASE, BASE_ALT]:
        if not os.path.exists(base_dir):
            continue

        paginas_config = [
            ("index.html", card_casa),
            ("promocoes.html", card_casa),
            ("casa.html", card_casa),
            ("perifericos.html", card_perifericos),
        ]

        for nome, card_html in paginas_config:
            caminho = os.path.join(base_dir, nome)
            if not os.path.exists(caminho):
                continue
            content = open(caminho, encoding="utf-8").read()
            if f'p/{SLUG}.html' in content:
                print(f"Card já existe em {base_dir}/{nome}")
                continue

            pos = content.find('<article class="card"')
            if pos < 0:
                print(f"Não achou card em {base_dir}/{nome}")
                continue
            pos = content.rfind("\n", 0, pos) + 1
            content = content[:pos] + card_html + "\n    " + content[pos:]
            with open(caminho, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Card inserido com sucesso em {base_dir}/{nome}")

    # 4. Atualizar sitemap.xml
    for base_dir in [BASE, BASE_ALT]:
        if not os.path.exists(base_dir):
            continue
        sm_path = os.path.join(base_dir, "sitemap.xml")
        if os.path.exists(sm_path):
            sm_content = open(sm_path, encoding="utf-8").read()
            if f"{SLUG}.html" not in sm_content:
                item = f"  <url><loc>https://renatopenner.github.io/site-renato-penner/p/{SLUG}.html</loc><lastmod>2026-11-05</lastmod></url>\n"
                sm_content = sm_content.replace("</urlset>", item + "</urlset>")
                with open(sm_path, "w", encoding="utf-8") as f:
                    f.write(sm_content)
                print(f"sitemap.xml atualizado em {base_dir}")


if __name__ == "__main__":
    main()
