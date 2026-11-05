"""Adiciona o Patinete Elétrico 350W IPX4 com Suporte a 150kg ao site renatopenner.com.br (GitHub Pages)."""
import io
import json
import os
import re
import shutil
from PIL import Image, ImageFilter

BASE = r"C:\Users\renat\SitesGithub\site-renato-penner"
BASE_ALT = r"C:\Users\renat\site-renato-penner"
FOTO_ORIG = r"C:\Users\renat\.gemini\antigravity\brain\2eee2922-62e9-43b5-95e2-9e021ba4195b\.user_uploaded\media_1793897558721_60386449.jpg"
SLUG = "patinete-eletrico-dobravel-350w"
DATA = "05/11/2026"
MARCA_W, MARCA_H = 1120, 840

PRODUTO = {
    "slug": SLUG,
    "titulo_card": "Patinete Elétrico 350W Dobrável com App Bluetooth",
    "h1": "Patinete Elétrico 350W Dobrável com App Bluetooth, Resistência à Água IPX4 e Suporte até 150 kg",
    "meta_desc": "Patinete elétrico 350W dobrável com certificação de resistência à água IPX4 contra chuva e poças, bateria de 42V 10.5Ah com autonomia de até 30 km, velocidade até 25 km/h, chassi reforçado para 150 kg, app Bluetooth com trava antifurto e bolsa de brinde.",
    "cat_badge": "Mercado Livre · Mais Vendido · 4º em Elétricos",
    "cat_css": "auto",
    "categoria_nome": "Automotivo e Mobilidade",
    "sub": "Resistente à Água IPX4 · Motor 350W · Até 25 km/h · Autonomia 30 km · Suporta 150 kg · Brinde Bolsa",
    "resumo": "Destaque total para a resistência à água IPX4 contra respingos e garoa, motor potente de 350W, autonomia estendida de até 30 km e estrutura reforçada que aguenta até 150 kg. Acompanha bolsa para patinete de brinde e app via Bluetooth.",
    "link": "https://meli.la/1zdtX1P",
    "preco_de": "R$ 1.999,90",
    "preco_por": "R$ 1.035,40",
    "preco_cartao": "ou R$ 1.089,90 em outros meios / até 10x",
    "desconto": "48% OFF",
    "porque": "Um dos maiores receios de quem adota o patinete elétrico para o dia a dia — seja para ir ao trabalho, faculdade ou integração com o transporte público — é a imprevisibilidade do clima. A maioria dos modelos de entrada queima com facilidade em poças ou garoas, mas este modelo vem de fábrica com <strong>certificação de proteção IPX4</strong>, blindando o compartimento da bateria e os circuitos eletrônicos contra respingos d'água multidirecionais e chuva leve.<br><br>Além da segurança contra água, ele se destaca pelo <strong>chassi robusto que suporta até 150 kg</strong> (muito superior aos concorrentes comuns que limitam em 100 kg ou 120 kg), pela <strong>super autonomia de até 30 km</strong> garantida pela bateria de lítio de 42V 10.5Ah, freio duplo (disco + elétrico) e aplicativo Bluetooth para travar pelo celular. Para fechar com chave de ouro, vem com uma <strong>bolsa para patinete de brinde</strong>.",
    "destaques": [
        ("Resistência à Água com Proteção IPX4", "Certificação de segurança contra respingos d'água em qualquer ângulo, permitindo rodar em pista molhada, garoa e asfalto com poças sem danificar os componentes elétricos."),
        ("Capacidade Reforçada para até 150 kg", "Estrutura robusta em liga metálica de alta resistência, ideal para suportar com folga condutores mais pesados ou transporte com mochila."),
        ("Super Autonomia de até 30 km", "Equipado com bateria de lítio de alta capacidade (42V 10.5Ah), perfeita para cobrir trajetos de ida e volta sem necessidade de recarga intermediária."),
        ("Motor de 350W Ágil (até 25 km/h)", "Excelente torque para arrancadas urbanas ágeis e boa força para enfrentar subidas leves com aceleração suave e controlada."),
        ("Brinde Exclusivo: Bolsa para Patinete", "Acompanha bolsa rígida para guidão inclusa, facilitando levar carteira, chaves, celular e ferramentas com praticidade."),
        ("App Bluetooth com Trava Antifurto", "Controle total no smartphone: ajuste modos de pilotagem, trave/destrave o motor eletronicamente, controle a iluminação LED e acompanhe a telemetria em tempo real."),
        ("Sistema de Freio Duplo Seguro", "Combinação de freio a disco traseiro ventilado com freio motor elétrico dianteiro, garantindo frenagens rápidas, estáveis e seguras em qualquer piso."),
        ("Design Dobrável em 1 Passo", "Mecanismo rápido e intuitivo para dobrar a coluna de direção e carregar no porta-malas do carro, metrô ou guardar no canto da sala."),
    ],
    "ficha": [
        "Marca / Modelo: Patinete Elétrico Dobrável 350W Smart Bluetooth",
        "Potência do motor: 350W com resposta progressiva",
        "Velocidade máxima: até 25 km/h",
        "Autonomia da bateria: até 25 a 30 km por carga (conforme peso e inclinação)",
        "Grau de proteção contra água: IPX4 (resistente a respingos e chuva leve)",
        "Bateria: Lítio de alta capacidade 42V 10.5Ah",
        "Tempo de recarga completa: aproximadamente 5 a 6 horas (bivolt 110V/220V)",
        "Capacidade de peso suportado: até 150 kg",
        "Pneus: 8,5 polegadas (50/75-6.1) com desenho para escoamento de água e absorção de impactos",
        "Sistema de freios: Freio a disco mecânico traseiro + Freio elétrico",
        "Iluminação: Farol dianteiro em LED de alta luminosidade e luz traseira de freio em LED",
        "Conectividade: Bluetooth integrado compatível com aplicativo para iOS e Android",
        "Suspensão: Pneus de 8,5 polegadas (sem amortecedor mecânico independente)",
        "Brinde incluso: 1x Bolsa de transporte para fixação no patinete",
    ],
    "pros": [
        "Classificação IPX4 comprovada: resistência a respingos d'água e chuva urbana, evitando queimas acidentais",
        "Suporta até 150 kg de peso, sendo um dos mais fortes e resistentes da categoria",
        "Super autonomia de até 30 km com bateria parruda de 42V 10.5Ah",
        "Freio duplo (disco + elétrico) que entrega alta segurança e frenagem firme mesmo em pista úmida",
        "Aplicativo Bluetooth completo com bloqueio eletrônico antifurto e modos de velocidade",
        "Acompanha bolsa de brinde prática para transporte de pertences no guidão",
        "Avaliação 4.8 estrelas no Mercado Livre com mais de 1.000 unidades vendidas e 48% OFF no Pix",
    ],
    "contras": [
        "Não possui amortecedor independente dedicado (a absorção de vibração depende da calibragem e dos pneus de 8,5 polegadas)",
        "A autonomia máxima varia de acordo com o peso do condutor e relevo do trajeto",
    ],
    "para_quem": "Profissionais e estudantes que buscam escapar do trânsito diário e economizar com transporte, que precisam de um veículo elétrico robusto para encarar o asfalto da cidade e dias de chuva com segurança e tranquilidade.",
}


def prepara_imagem():
    im = Image.open(FOTO_ORIG).convert("RGB")
    # Cria tela 1120x840
    # Fundo com blur da própria imagem preenchendo as laterais
    bg = im.resize((MARCA_W, MARCA_H), Image.Resampling.LANCZOS).filter(ImageFilter.GaussianBlur(30))
    # Imagem nítida 840x840 no centro
    fg = im.resize((MARCA_H, MARCA_H), Image.Resampling.LANCZOS)
    bg.paste(fg, ((MARCA_W - MARCA_H) // 2, 0))

    for base_dir in [BASE, BASE_ALT]:
        if os.path.exists(base_dir):
            img_dir = os.path.join(base_dir, "img")
            os.makedirs(img_dir, exist_ok=True)
            # Salva o novo arquivo
            p_out = os.path.join(img_dir, f"{SLUG}.png")
            bg.save(p_out, format="PNG", optimize=True)
            print(f"Imagem salva em {p_out}")
            # Atualiza também patinete-gm5-p1.png para manter compatibilidade
            gm5_out = os.path.join(img_dir, "patinete-gm5-p1.png")
            bg.save(gm5_out, format="PNG", optimize=True)
            print(f"Imagem compatível salva em {gm5_out}")


def bloco_preco(p):
    return (
        f'<div class="preco">'
        f'<span class="de">de {p["preco_de"]}</span>'
        f'<span class="por">por {p["preco_por"]}</span>'
        f'<span class="cartao">{p["preco_cartao"]}</span>'
        f'<small>preço conferido em {DATA} · {p["desconto"]}</small>'
        f'</div>'
    )


def gera_card(p, cat_override=None, badge_override=None):
    cat_css = cat_override if cat_override else p["cat_css"]
    cat_nome = "Mobilidade Urbana"
    badge = badge_override if badge_override else p["cat_badge"]
    busca = re.sub(
        r"[^a-z0-9 ]",
        " ",
        (p["titulo_card"] + " " + p["sub"] + " " + p["slug"] + " patinete eletrico 350w ipx4 agua chuva 150kg bluetooth app dobravel").lower(),
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
<meta name="build" content="2026-11-05 13:50">
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
  <nav class="links"><a class="link " href="../index.html">Início</a><a class="link " href="../promocoes.html">Ofertas</a><a class="link " href="../notebooks.html">Notebooks</a><a class="link " href="../ssd.html">SSD</a><a class="link " href="../carregadores.html">Carregadores</a><a class="link " href="../saude.html">Saúde</a><a class="link " href="../casa.html">Casa</a><a class="link on" href="../auto.html">Auto</a><a class="link " href="../perifericos.html">Periféricos</a><a class="link " href="../moda.html">Moda</a></nav>
  <div class="dir"><a class="link" href="https://www.youtube.com/@renatopenner2037" target="_blank" rel="noopener">YouTube ↗</a></div>
</div></header>
<main class="wrap">
  <div class="migalha"><a href="../index.html">Início</a> /
    <a href="../auto.html">Automotivo e Mobilidade</a> / {p['titulo_card']}</div>
  <section class="prod">
    <div class="foto"><a href="{p['link']}" target="_blank" rel="sponsored nofollow noopener" title="Ver oferta no Mercado Livre"><img src="../img/{p['slug']}.png" alt="{p['titulo_card']}"></a></div>
    <div>
      <span class="cat" style="color:#38bdf8;font-size:11px;font-weight:800;letter-spacing:.1em">{p['cat_badge']}</span>
      <h1>{p['h1']}</h1>
      <div class="pmeta">{p['sub']}</div>
      <div class="preco"><span class="de">de {p['preco_de']}</span><span class="por">por {p['preco_por']}</span><span class="cartao">{p['preco_cartao']}</span><small>preço conferido em {DATA} · {p['desconto']}</small></div>
      <div class="btns" style="margin-top:18px">
        <a class="btn" href="{p['link']}" target="_blank" rel="sponsored nofollow noopener">Ver oferta no Mercado Livre →</a>
      </div>

      <div class="box" style="border-left:4px solid #38bdf8;background:rgba(56,189,248,0.06);padding:14px 18px;border-radius:10px;margin:20px 0;">
        <h4 style="color:#38bdf8;display:flex;align-items:center;gap:8px;margin-bottom:6px;">
          <span>💧</span> Destaque: Certificação de Resistência à Água IPX4
        </h4>
        <p style="color:#dbe7f3;font-size:14.5px;margin:0;line-height:1.55;">
          Projetado especialmente para o clima urbano real: a <strong>classificação IPX4</strong> protege os circuitos elétricos, o motor de 350W e a bateria contra <strong>respingos d'água multidirecionais, asfalto molhado, poças e garoa</strong>. Você não fica na mão nem corre risco de queimar componentes essenciais no trajeto de volta para casa.
        </p>
      </div>

      <div class="box"><h4>Por que eu recomendo</h4><p style="color:#c6d5e2;font-size:14.5px">{p['porque']}</p></div>

      <div class="box"><h4>Destaques e Vantagens Confirmadas</h4><ul>{destaques}</ul></div>

      <div class="box"><h4>Ficha Técnica</h4><ul>{ficha}</ul></div>

      <div class="box"><h4>Prós</h4><ul>{pros}</ul><h4 style="margin-top:14px">Contras</h4><ul>{contras}</ul></div>

      <div class="box"><h4>Para quem serve</h4><p style="color:#c6d5e2;font-size:14.5px">{p['para_quem']}</p></div>
    </div>
  </section>
</main>
<script type="application/ld+json">{{"@context": "https://schema.org", "@type": "Product", "name": "{p['h1']}", "description": "{p['meta_desc']}", "brand": {{"@type": "Brand", "name": "Smart Mobility"}}, "offers": {{"@type": "Offer", "url": "{p['link']}", "price": "{preco_num}", "priceCurrency": "BRL", "availability": "https://schema.org/InStock", "seller": {{"@type": "Organization", "name": "Mercado Livre"}}}}, "aggregateRating": {{"@type": "AggregateRating", "ratingValue": "4.8", "reviewCount": "181"}}}}</script>

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
    # Substitui qualquer card anterior de patinete ou insere no topo
    for base_dir in [BASE, BASE_ALT]:
        if not os.path.exists(base_dir):
            continue

        for nome in ["auto.html", "index.html", "promocoes.html"]:
            caminho = os.path.join(base_dir, nome)
            if not os.path.exists(caminho):
                continue

            content = open(caminho, encoding="utf-8").read()

            # Procura por card existente de patinete (seja o gm5 antigo ou este novo)
            padrao_card = re.compile(r'<article class="card"[^>]*data-busca="[^"]*patinete.*?<\/article>', re.DOTALL)
            if padrao_card.search(content):
                content = padrao_card.sub(novo_card, content, count=1)
                print(f"Card de patinete substituído/atualizado em {base_dir}/{nome}")
            else:
                # Se não achou, insere no topo da grid
                pos = content.find('<article class="card"')
                if pos >= 0:
                    pos = content.rfind("\n", 0, pos) + 1
                    content = content[:pos] + novo_card + "\n    " + content[pos:]
                    print(f"Card de patinete inserido no topo em {base_dir}/{nome}")

            with open(caminho, "w", encoding="utf-8") as f:
                f.write(content)


def atualiza_produtos_json(p):
    for base_dir in [BASE, BASE_ALT]:
        if not os.path.exists(base_dir):
            continue
        caminho_json = os.path.join(base_dir, "dados", "produtos.json")
        if not os.path.exists(caminho_json):
            continue

        dados = json.load(open(caminho_json, encoding="utf-8"))
        # Remove ou atualiza se já existia patinete-eletrico-gm5 ou o novo SLUG
        dados_novos = []
        achou = False
        for item in dados:
            if item["slug"] in ["patinete-eletrico-gm5", SLUG]:
                dados_novos.append({
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
                achou = True
            else:
                dados_novos.append(item)

        if not achou:
            dados_novos.append({
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

        json.dump(dados_novos, open(caminho_json, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print(f"produtos.json atualizado em {base_dir}")


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

    # 1. Gera página completa do novo produto
    page_html = gera_pagina_completa(p)

    for base_dir in [BASE, BASE_ALT]:
        if os.path.exists(base_dir):
            page_path = os.path.join(base_dir, "p", f"{SLUG}.html")
            with open(page_path, "w", encoding="utf-8") as f:
                f.write(page_html)
            print("Página criada:", page_path)

            # Também atualiza patinete-eletrico-gm5.html como cópia para evitar 404 em acessos antigos
            legacy_path = os.path.join(base_dir, "p", "patinete-eletrico-gm5.html")
            with open(legacy_path, "w", encoding="utf-8") as f:
                f.write(page_html)
            print("Página legada atualizada:", legacy_path)

    # 2. Atualiza dados/produtos.json
    atualiza_produtos_json(p)

    # 3. Atualiza cards em auto.html, index.html e promocoes.html
    card = gera_card(p)
    atualiza_paginas_html(p, card)

    # 4. Atualiza sitemap.xml
    atualiza_sitemap()


if __name__ == "__main__":
    main()
