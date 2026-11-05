"""Adiciona a Caixa de Som JBL PartyBox Stage 320 ao site renatopenner.com.br (GitHub Pages)."""
import json
import os
import re
from PIL import Image

BASE = r"C:\Users\renat\SitesGithub\site-renato-penner"
BASE_ALT = r"C:\Users\renat\site-renato-penner"
FOTO_ORIG = r"C:\Users\renat\.gemini\antigravity\brain\c2981a2d-1cca-4d31-8e56-1057c8f5b0d1\.user_uploaded\media_1793897929865_f0804b74.png"
SLUG = "jbl-partybox-stage-320"
DATA = "05/11/2026"
MARCA_W, MARCA_H = 1120, 840

PRODUTO = {
    "slug": SLUG,
    "titulo_card": "Caixa de Som JBL PartyBox Stage 320 Bluetooth 240W RMS",
    "h1": "Caixa de Som Bluetooth JBL PartyBox Stage 320 Portátil 240W RMS com Show de Luzes, Rodas e IPX4",
    "meta_desc": "Caixa de som Bluetooth JBL PartyBox Stage 320 com 240W RMS de potência, som JBL Pro Sound, até 18 horas de bateria, alça telescópica e rodas largas, show de luzes dinâmico, classificação IPX4 à prova de respingos e entradas para microfone e instrumento.",
    "cat_badge": "Mercado Livre · Mais Vendido · 2º em Caixas Acústicas",
    "cat_css": "casa",
    "categoria_nome": "Casa e áudio",
    "sub": "240W RMS · Bateria até 18h · Rodas e Alça Telescópica · Show de Luzes · IPX4 · Entradas Mic/Violão",
    "resumo": "Potência avassaladora de 240W RMS com a lendária assinatura acústica JBL Pro Sound, graves profundos, bateria para até 18 horas, rodinhas reforçadas com alça telescópica, show de luzes estroboscópico sincronizado e proteção IPX4 contra respingos d'água.",
    "link": "https://meli.la/1xs6YGm",
    "preco_de": "R$ 5.000,00",
    "preco_por": "R$ 2.570,00",
    "preco_cartao": "em até 21x de R$ 122,38 sem juros",
    "desconto": "48% OFF",
    "porque": "A JBL PartyBox Stage 320 é a evolução máxima da linha PartyBox para quem busca som de alta performance sem abrir mão de mobilidade prática. Seus <strong>240W RMS reais</strong> entregam pressão sonora limpa e envolvente através de dois woofers de 6,5 polegadas e dois tweeters de alta precisão de 25 mm, garantindo graves que estremecem o ambiente sem embolar médios e agudos.<br><br>O grande diferencial da Stage 320 frente aos modelos anteriores está na sua engenharia de transporte: equipada com <strong>rodas largas de rolagem suave e alça telescópica retrátil</strong> estilo mala de viagem, mover os seus 16,5 kg entre a sala, o quintal ou o porta-malas do carro é extremamente suave. A <strong>bateria interna oferece até 18 horas de autonomia</strong> (e conta com slot removível para troca rápida caso deseje estender a festa), carga rápida de 10 min para 2h de som, <strong>certificação IPX4 contra respingos</strong> na piscina, conectividade <strong>Bluetooth 5.4 com Auracast</strong> e entradas P10 com ganho dedicado para microfone e violão.",
    "destaques": [
        ("Potência Real de 240W RMS JBL Pro Sound", "Dois woofers de 6,5 polegadas de alta sensibilidade e dois tweeters de cúpula de 25 mm proporcionam fidelidade acústica cristalina com graves profundos e impacto sonoro de alto nível."),
        ("Máxima Mobilidade com Rodas e Alça Telescópica", "Projetada com rodas largas reforçadas e alça retrátil robusta, permitindo conduzir a caixa facilmente como uma mala de viagem em pisos, gramados e calçadas."),
        ("Bateria de até 18 Horas com Troca Rápida", "Autonomia prolongada para acompanhar qualquer festa do início ao fim. Conta com compartimento para bateria substituível e recarga rápida onde 10 minutos na tomada garantem até 2 horas de reprodução."),
        ("Proteção IPX4 à Prova de Respingos", "Estrutura blindada contra respingos d'água em qualquer ângulo, ideal para churrascos, festas na piscina ou áreas externas sem receio de chuva leve."),
        ("Show de Luzes Dinâmico e Efeitos DJ", "LEDs multicoloridos integrados que pulsam em sincronia perfeita com a batida musical, com estroboscópios e padrões visuais customizáveis pelo aplicativo JBL PartyBox."),
        ("Entradas para Microfone e Guitarra/Violão", "Duas entradas P10 com ajustes independentes de volume e ganho para transformar qualquer momento em show ao vivo ou sessão de karaokê."),
        ("Bluetooth 5.4 com Tecnologia Auracast", "Conexão sem fio estável e moderna capaz de sincronizar múltiplas caixas JBL compatíveis em estéreo ou modo festa sem cabos e com zero latência."),
    ],
    "ficha": [
        "Marca: JBL / Harman",
        "Modelo: JBL PartyBox Stage 320 (JBLPBSTAGE320BR)",
        "Potência de saída: 240 W RMS",
        "Transdutores: 2x woofers de 6,5 pol (165 mm) + 2x tweeters de 1 pol (25 mm)",
        "Resposta de frequência: 40 Hz – 20 kHz (-6 dB)",
        "Relação sinal-ruído: > 80 dB",
        "Autonomia da bateria: até 18 horas (conforme volume e efeitos de luz)",
        "Tempo de carregamento: 4 horas",
        "Alimentação / Voltagem: 100 – 240 V ~ 50/60 Hz (Bivolt automático)",
        "Tipo de bateria: Bateria de íons de lítio recarregável e removível (68 Wh)",
        "Conectividade sem fio: Bluetooth 5.4 (A2DP V1.4, AVRCP V1.6) com suporte a Auracast",
        "Conexões físicas: Entrada auxiliar P2 3,5 mm, Entrada USB-A (leitura e carregador portátil), 2x Entradas P10 (Mic 1 e Mic 2/Guitarra) com ganho",
        "Grau de proteção: IPX4 resistente a respingos d'água",
        "Dimensões (L x A x P): 33,5 cm x 67,0 cm x 38,5 cm",
        "Peso: 16,5 kg",
        "Homologação Anatel: 219732307120",
        "Itens inclusos: 1x JBL PartyBox Stage 320, 1x Cabo de força AC, 1x Guia de início rápido, 1x Cartão de garantia",
    ],
    "pros": [
        "Potência sonora expressiva de 240W RMS com a nitidez e graves profundos da tecnologia JBL Pro Sound",
        "Rodas largas integradas e alça telescópica retrátil que facilitam totalmente o deslocamento dos 16,5 kg",
        "Bateria de até 18 horas com suporte a bateria removível e carregamento rápido (10 min = 2h de som)",
        "Proteção IPX4 certificada contra respingos d'água, ideal para beira de piscina e áreas abertas",
        "Show de luzes dinâmico imersivo com controle total de iluminação e som pelo app JBL PartyBox",
        "Duas entradas P10 para microfone e instrumento musical com controles analógicos de ganho",
        "Excelente oportunidade com 48% de desconto e parcelamento em até 21x sem juros no Mercado Pago",
    ],
    "contras": [
        "Caixa de porte avantajado com 67 cm de altura e 16,5 kg (embora as rodinhas amenizem o transporte no plano, requer esforço ao subir escadas)",
    ],
    "para_quem": "Entusiastas de som de alta qualidade, famílias que adoram confraternizações e churrascos à beira da piscina, músicos para voz e violão em apresentações acústicas e quem quer uma caixa de som potente, moderna e portátil sem precisar ficar preso a fios ou tomadas.",
}


def prepara_imagem():
    im = Image.open(FOTO_ORIG).convert("RGB")
    # Bounding box do produto: (19, 42, 505, 986)
    cropped = im.crop((19, 42, 505, 986))
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
        (p["titulo_card"] + " " + p["sub"] + " " + p["slug"] + " jbl partybox stage 320 caixa de som bluetooth portatil 240w").lower(),
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
<meta name="build" content="2026-11-05 14:05">
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

      <div class="box" style="border-left:4px solid #38bdf8;background:rgba(56,189,248,0.06);padding:14px 18px;border-radius:10px;margin:20px 0;">
        <h4 style="color:#38bdf8;display:flex;align-items:center;gap:8px;margin-bottom:6px;">
          <span>🔊</span> 240W RMS com JBL Pro Sound &amp; Rodas Reforçadas
        </h4>
        <p style="color:#dbe7f3;font-size:14.5px;margin:0;line-height:1.55;">
          A combinação definitiva entre <strong>potência real para festas de grande porte</strong> e <strong>facilidade de transporte</strong>. Com alça retrátil estilo mala, rodinhas emborrachadas, certificação IPX4 contra respingos de piscina e até 18 horas de bateria contínua.
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
<script type="application/ld+json">{{"@context": "https://schema.org", "@type": "Product", "name": "{p['titulo_card']}", "description": "{p['meta_desc']}", "brand": {{"@type": "Brand", "name": "JBL"}}, "offers": {{"@type": "Offer", "url": "{p['link']}", "price": "{preco_num}", "priceCurrency": "BRL", "availability": "https://schema.org/InStock", "seller": {{"@type": "Organization", "name": "Mercado Livre"}}}}, "aggregateRating": {{"@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "10635"}}}}</script>

<footer><div class="wrap">
  <img class="marca" src="../img/lockup-rodape.png?v=462caf9a" alt="Renato Penner — Engenharia da Computação">
  <div class="aviso"><strong>Aviso de afiliado:</strong> os links deste site são de afiliado.
  Se você comprar por eles, eu recebo uma comissão da loja — <strong>sem nenhum custo a mais para você</strong>.
  Preços e disponibilidade são da data indicada em cada produto e podem mudar sem aviso.
  Última verificação dos links: 05/11/2026.</div>

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

        paginas = ["casa.html", "index.html", "promocoes.html"]
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
