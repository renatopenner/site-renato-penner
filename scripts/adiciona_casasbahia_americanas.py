import os
import sys
import json
import re
from PIL import Image, ImageDraw, ImageFont, ImageFilter

REPO = r"C:\Users\renat\SitesGithub\site-renato-penner"
IMG_DIR = os.path.join(REPO, "img")
P_DIR = os.path.join(REPO, "p")
DADOS_DIR = os.path.join(REPO, "dados")
CATALOGO_PATH = os.path.join(DADOS_DIR, "produtos.json")
SITEMAP_PATH = os.path.join(REPO, "sitemap.xml")

PRODUTOS = [
    {
        "slug": "smart-tv-50-samsung-crystal-uhd-4k-du7700",
        "titulo_card": 'Smart TV 50" Crystal UHD 4K Samsung 50DU7700',
        "h1": 'Smart TV 50" Crystal UHD 4K Samsung 50DU7700 com Gaming Hub, Processador Crystal 4K e Design sem Bordas',
        "meta_desc": 'Smart TV 50 polegadas Samsung Crystal UHD 4K 50DU7700 com Gaming Hub (Xbox Game Pass sem console), HDR, visual livre de cabos, Wi-Fi, Bluetooth e sistema Tizen.',
        "cat_badge": "Casas Bahia · Oferta Oficial",
        "cat_css": "casa",
        "categoria_nome": "Casa e Eletrodomésticos",
        "sub": "4K Real · Gaming Hub integrado · Processador Crystal 4K · Design Slim sem Bordas · HDR",
        "resumo": "Smart TV 50 polegadas com resolução 4K real, processador Crystal 4K com upscaling inteligente, Gaming Hub integrado (jogue Xbox Game Pass direto na TV sem videogame), design Slim sem bordas e sistema Tizen com todos os apps de streaming.",
        "link": "https://www.awin1.com/cread.php?awinmid=85979&awinaffid=3169987&ued=https%3A%2F%2Fwww.casasbahia.com.br%2Fsmart-tv-50-crystal-uhd-4k-samsung-50du7700-2024-processador-crystal-4k-gaming-hub-design-sem-bordas-visual-livre-de-cabos-tela-sem-limites%2Fp%2F55064972",
        "preco_de": "R$ 2.699,00",
        "preco_por": "R$ 2.199,00",
        "preco_cartao": "em até 10x de R$ 219,90 sem juros",
        "desconto": "18% OFF",
        "loja_nome": "Casas Bahia",
        "cor_marca": (0, 70, 190), # Azul Casas Bahia
        "texto_imagem": "SAMSUNG 50\" 4K",
        "sub_imagem": "Crystal UHD · Gaming Hub · Slim",
        "porque": "A linha Crystal UHD DU7700 da Samsung é a melhor escolha custo-benefício em TVs 50 polegadas. O processador Crystal 4K realiza upscaling eficiente de qualquer conteúdo para resolução próxima ao 4K, enquanto o Gaming Hub integrado permite jogar títulos da biblioteca do Xbox Game Pass via nuvem diretamente na TV, precisando apenas de uma assinatura e um controle Bluetooth emparelhado, sem necessidade de console físico.",
        "destaques": [
            ("Processador Crystal 4K", "Upscaling inteligente que converte qualquer sinal para próximo da resolução 4K real com cores vivas e nitidez precisa"),
            ("Samsung Gaming Hub", "Acesso nativo a serviços de jogos na nuvem como Xbox Game Pass e GeForce Now sem necessidade de videogame"),
            ("Design Slim sem Bordas", "Estrutura moderna e minimalista de 3 lados sem bordas com canaletas para ocultar os cabos"),
            ("Sistema Tizen OS Atualizado", "Navegação ágil com suporte completo a Netflix, Disney+, Prime Video, Max, YouTube e Globoplay"),
            ("Som em Movimento Virtual & Sincronia Sonora", "Áudio que acompanha os objetos em cena com suporte a soundbars externas integradas"),
            ("Conectividade Completa", "3x HDMI, 1x USB, Wi-Fi 5 de alta velocidade, Bluetooth 5.2 e porta Ethernet LAN"),
        ],
        "ficha": [
            "Marca: Samsung",
            "Modelo: UN50DU7700GXZD (Linha 2024/2025)",
            "Tamanho da tela: 50 polegadas",
            "Resolução: 4K Ultra HD (3.840 x 2.160 pixels)",
            "Frequência da tela: 60 Hz",
            "Processador: Crystal 4K",
            "HDR: HDR10+ / HLG",
            "Sistema Operacional: Tizen™ Smart TV",
            "Recursos Gamer: Samsung Gaming Hub, HGiG, ALLM (Modo Automático de Baixa Latência)",
            "Conexões: 3x HDMI, 1x USB-A, 1x Ethernet LAN, 1x Saída de Áudio Óptica, Wi-Fi 5, Bluetooth 5.2",
            "Voltagem: Bivolt Automático (100-240V)",
            "Conteúdo da embalagem: 1x Smart TV Samsung 50DU7700, 1x Controle Remoto SolarCell, 1x Cabo de força, Pés de suporte e Manual",
        ],
        "pros": [
            "Excelente custo-benefício para Smart TV 4K de 50 polegadas",
            "Gaming Hub integrado dispensa console para jogar jogos modernos",
            "Design ultrafino sem bordas aparentes",
            "Controle SolarCell recarregável por luz ambiente (sem necessidade de pilhas)",
            "Sistema Tizen maduro e repleto de aplicativos",
        ],
        "contras": [
            "Painel de 60Hz nativo (não é 120Hz para consoles competitivos)",
        ],
        "para_quem": "Famílias e entusiastas que querem uma tela grande de 50 polegadas com excelente qualidade de imagem 4K, suporte completo a todos os apps de streaming e capacidade de jogar videogames modernos na nuvem com baixo custo de investimento.",
    },
    {
        "slug": "air-fryer-mondial-family-4l-afn-40-bi",
        "titulo_card": "Fritadeira Elétrica Air Fryer Mondial Family 4 Litros AFN-40-BI",
        "h1": "Fritadeira Sem Óleo Air Fryer Mondial Family 4L AFN-40-BI Inox 1500W com Antiaderente Duraflon",
        "meta_desc": "Fritadeira Elétrica Air Fryer Mondial Family 4 Litros 1500W modelo AFN-40-BI com acabamento em inox, cuba antiaderente Duraflon, timer de 60 minutos e controle de temperatura até 200°C.",
        "cat_badge": "Americanas · Oferta Oficial",
        "cat_css": "casa",
        "categoria_nome": "Casa e Eletrodomésticos",
        "sub": "4 Litros · 1500W Potência · Antiaderente Duraflon · Timer 60 Minutos · Painel em Inox",
        "resumo": "A Air Fryer mais vendida do Brasil na versão Family 4L com 1500W de potência. Cesto quadrado com revestimento antiaderente Duraflon de alta durabilidade, controle de temperatura de até 200°C e timer sonoro de 60 minutos para refeições rápidas e saudáveis sem óleo.",
        "link": "https://www.awin1.com/cread.php?awinmid=22193&awinaffid=3169987&ued=https%3A%2F%2Fwww.americanas.com.br%2Fproduto%2F3149842521",
        "preco_de": "R$ 349,90",
        "preco_por": "R$ 249,90",
        "preco_cartao": "em até 6x de R$ 41,65 sem juros",
        "desconto": "28% OFF",
        "loja_nome": "Americanas",
        "cor_marca": (225, 0, 0), # Vermelho Americanas
        "texto_imagem": "MONDIAL FAMILY 4L",
        "sub_imagem": "Air Fryer 1500W · Inox · Duraflon",
        "porque": "A Mondial domina a preferência nacional de fritadeiras sem óleo pela confiabilidade térmica e facilidade de limpeza. O modelo AFN-40-BI de 4 Litros entrega o equilíbrio ideal de espaço interno (cesto quadrado espaçoso que acomoda peças inteiras de carne, tortas e porções generosas para até 4 pessoas) e potência consistente de 1500W que assa e frita com rapidez.",
        "destaques": [
            ("Capacidade Family 4 Litros", "Cesto quadrado amplo que aproveita melhor o espaço útil interno para preparar refeições para toda a família"),
            ("Potência Real de 1500W", "Aquecimento rápido e circulação de ar quente uniforme para receitas douradas por fora e suculentas por dentro"),
            ("Antiaderente Duraflon Exclusivo", "Revestimento que não gruda alimentos e facilita a higienização diária na pia ou lava-louças"),
            ("Controle de Temperatura até 200°C", "Ajuste preciso de temperatura para carnes, batatas, legumes, massas, bolos e salgados"),
            ("Timer Sonoro de 60 Minutos com Desligamento Automático", "Praticidade para programar o preparo sem risco de queimar os pratos"),
            ("Acabamento Frontal em Aço Inox", "Design moderno e resistente que combina perfeitamente com qualquer bancada de cozinha"),
        ],
        "ficha": [
            "Marca: Mondial",
            "Modelo: AFN-40-BI Family Inox",
            "Capacidade total: 4 Litros",
            "Potência: 1500W",
            "Temperatura máxima: De 80°C a 200°C",
            "Timer: 60 minutos com aviso sonoro e desligamento automático",
            "Cuba e Cesto: Removíveis com revestimento antiaderente Duraflon",
            "Acabamento: Polipropileno resistente com painel frontal em aço inoxidável escovado",
            "Lâmpadas piloto: Indicadoras de funcionamento e aquecimento",
            "Dimensões: 29,5 cm (A) x 28,5 cm (L) x 36,5 cm (P)",
            "Peso aproximado: 4,0 Kg",
            "Conteúdo da embalagem: 1x Fritadeira Air Fryer Mondial AFN-40-BI 4L, 1x Cuba com cesto removível, Livro de receitas e Manual",
        ],
        "pros": [
            "A Air Fryer com a maior rede de assistência e peças de reposição do Brasil",
            "Cuba quadrada de 4L que aproveita muito melhor a área útil que as cubas redondas",
            "Antiaderente Duraflon de alta resistência a riscos quando lavado adequadamente",
            "Preço altamente competitivo com ótimo custo-benefício",
            "Acabamento em inox elegante e fácil de limpar",
        ],
        "contras": [
            "Painel com comandos manuais analógicos (não é painel digital touchscreen)",
        ],
        "para_quem": "Quem busca uma rotina alimentar mais saudável e prática sem óleo, estudantes, casais e famílias que precisam de uma fritadeira confiável, potente e espaçosa de 4 litros sem pagar preços exorbitantes.",
    }
]

def gerar_imagem(prod):
    w, h = 1120, 840
    im = Image.new("RGB", (w, h), (13, 17, 24))
    draw = ImageDraw.Draw(im)

    # Gradiente e halo
    cor = prod["cor_marca"]
    halo = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    hdraw = ImageDraw.Draw(halo)
    hdraw.ellipse([(150, 100), (970, 740)], fill=(cor[0], cor[1], cor[2], 120))
    halo = halo.filter(ImageFilter.GaussianBlur(100))
    im.paste(halo, (0, 0), halo)

    # Moldura e card central
    draw = ImageDraw.Draw(im)
    draw.rounded_rectangle([(70, 60), (1050, 780)], radius=24, outline=(255, 255, 255, 30), width=2)

    # Badge de topo
    badge_bg = (cor[0], cor[1], cor[2])
    draw.rounded_rectangle([(110, 100), (420, 148)], radius=12, fill=badge_bg)
    
    # Fontes
    try:
        f_badge = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 22)
        f_tit = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 44)
        f_sub = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 26)
        f_preco = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 52)
        f_cond = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 24)
        f_loja = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 28)
    except:
        f_badge = ImageFont.load_default()
        f_tit = ImageFont.load_default()
        f_sub = ImageFont.load_default()
        f_preco = ImageFont.load_default()
        f_cond = ImageFont.load_default()
        f_loja = ImageFont.load_default()

    draw.text((130, 112), f"★ {prod['loja_nome'].upper()} OFICIAL", font=f_badge, fill=(255, 255, 255))

    # Título estilizado na arte
    draw.text((110, 210), prod["texto_imagem"], font=f_tit, fill=(255, 255, 255))
    draw.text((110, 275), prod["sub_imagem"], font=f_sub, fill=(180, 205, 235))

    # Divisor suave
    draw.line([(110, 340), (1010, 340)], fill=(255, 255, 255, 40), width=2)

    # Detalhe visual de destaques
    destaque_y = 380
    for i, (d_tit, _) in enumerate(prod["destaques"][:3]):
        draw.text((120, destaque_y), f"✔  {d_tit}", font=f_sub, fill=(220, 235, 250))
        destaque_y += 50

    # Área de preço no rodapé da arte
    draw.rounded_rectangle([(110, 580), (1010, 740)], radius=16, fill=(18, 24, 38))
    draw.text((140, 605), f"de {prod['preco_de']} por", font=f_cond, fill=(140, 160, 185))
    draw.text((140, 640), prod["preco_por"], font=f_preco, fill=(56, 189, 248))
    draw.text((540, 658), f"({prod['desconto']})", font=f_cond, fill=(74, 222, 128))
    draw.text((140, 702), prod["preco_cartao"], font=f_cond, fill=(180, 200, 220))
    draw.text((760, 650), f"Oferta {prod['loja_nome']} →", font=f_loja, fill=(255, 255, 255))

    # Salva em JPG e WebP
    slug = prod["slug"]
    jpg_path = os.path.join(IMG_DIR, f"{slug}.jpg")
    webp_path = os.path.join(IMG_DIR, f"{slug}.webp")
    im.save(jpg_path, "JPEG", quality=90, optimize=True)
    im.save(webp_path, "WEBP", quality=90)
    print(f"[IMAGEM] Gerada {jpg_path} e {webp_path}")

def gerar_pagina_produto(prod):
    slug = prod["slug"]
    destaques_html = "".join([f'<li class="dt"><strong>{tit}:</strong> {desc}</li>\n' for tit, desc in prod["destaques"]])
    ficha_html = "".join([f'<li class="dt">{item}</li>\n' for item in prod["ficha"]])
    pros_html = "".join([f'<li>{p}</li>\n' for p in prod["pros"]])
    contras_html = "".join([f'<li>{c}</li>\n' for c in prod["contras"]])

    preco_num = prod["preco_por"].replace("R$", "").replace(".", "").replace(",", ".").strip()

    html = f"""<!doctype html>
<html lang="pt-BR">
<head>
<script>(function(){{try{{var m=document.cookie.match(/(?:^|;\s*)pt_tema=(escuro|claro)/);document.documentElement.setAttribute("data-tema",m?m[1]:"claro")}}catch(e){{document.documentElement.setAttribute("data-tema","claro")}}}})();</script>
<meta charset="utf-8">
<meta http-equiv="Cache-Control" content="no-store">
<meta name="build" content="2026-11-28 16:30">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{prod['titulo_card']} — Penner Tech</title>
<meta name="description" content="{prod['meta_desc']}">
<link rel="canonical" href="https://loja.pennertech.com.br/p/{slug}.html">
<meta property="og:type" content="product">
<meta property="og:site_name" content="Penner Tech">
<meta property="og:title" content="{prod['titulo_card']} — Penner Tech">
<meta property="og:description" content="{prod['meta_desc']}">
<meta property="og:url" content="https://loja.pennertech.com.br/p/{slug}.html">
<meta property="og:locale" content="pt_BR">
<meta name="theme-color" content="#f7fafc">
<meta property="og:image" content="https://loja.pennertech.com.br/img/{slug}.jpg">
<meta property="og:image:width" content="1120">
<meta property="og:image:height" content="840">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{prod['titulo_card']} — Penner Tech">
<meta name="twitter:description" content="{prod['meta_desc']}">
<meta name="twitter:image" content="https://loja.pennertech.com.br/img/{slug}.jpg">
<link rel="icon" type="image/png" sizes="64x64" href="../img/favicon-64.png?v=9fb83174">
<link rel="icon" type="image/png" sizes="192x192" href="../img/icon-192.png?v=c11102d6">
<link rel="apple-touch-icon" href="../img/apple-touch-icon.png?v=8f32fdca">
<link rel="stylesheet" href="../css/style.css?v=4cf08b7c">
<script>
addEventListener('load',function(){{try{{var u='https://renatopennersoares1783016458000.0871043.meusitehostgator.com.br/c.php?p='+encodeURIComponent(location.pathname)+'&o='+encodeURIComponent(location.hostname);
  if(navigator.sendBeacon){{navigator.sendBeacon(u);}}else{{fetch(u,{{keepalive:true}});}}}}catch(e){{}}}});
document.addEventListener('click',function(ev){{var a=ev.target&&ev.target.closest?ev.target.closest('a'):null;if(!a)return;
  var h=a.href||'',d='';
  if(h.indexOf('mercadolivre')>=0||h.indexOf('meli.la')>=0)d='mercadolivre';
  else if(h.indexOf('amazon')>=0)d='amazon';
  else if(h.indexOf('casasbahia')>=0)d='casasbahia';
  else if(h.indexOf('americanas')>=0)d='americanas';
  else if(h.indexOf('awin1.com')>=0)d='awin';
  else if(h.indexOf('wa.me')>=0||h.indexOf('whatsapp')>=0)d='whatsapp';
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
  document.addEventListener('scroll', carrega, {{once:true, passive:true}});
  document.addEventListener('click', carrega, {{once:true}});
  document.addEventListener('keydown', carrega, {{once:true}});
  setTimeout(carrega, 4000);
}})();
</script>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "{prod['titulo_card']}",
  "image": "https://loja.pennertech.com.br/img/{slug}.jpg",
  "description": "{prod['meta_desc']}",
  "brand": {{
    "@type": "Brand",
    "name": "{prod['loja_nome']}"
  }},
  "offers": {{
    "@type": "Offer",
    "url": "{prod['link']}",
    "priceCurrency": "BRL",
    "price": "{preco_num}",
    "priceValidUntil": "2027-12-31",
    "itemCondition": "https://schema.org/NewCondition",
    "availability": "https://schema.org/InStock",
    "seller": {{
      "@type": "Organization",
      "name": "{prod['loja_nome']}"
    }}
  }}
}}
</script>
</head>
<body>
<header class="header"><div class="wrap">
  <div class="logo"><a href="../index.html">Penner Tech</a> <span class="tag">Curadoria Oficial</span></div>
  <nav class="nav">
    <a href="../index.html">Início</a>
    <a href="../casa.html">Casa</a>
    <a href="../promocoes.html">Promoções</a>
    <a href="../sobre.html">Sobre</a>
  </nav>
  <button id="btn-tema" class="btn-tema" type="button" aria-label="Alternar tema claro/escuro" title="Alternar tema claro/escuro">
    <span class="icone-sol" aria-hidden="true">☀️</span><span class="icone-lua" aria-hidden="true">🌙</span>
  </button>
</div></header>

<main class="wrap">
  <div class="migalha"><a href="../index.html">Início</a> / <a href="../casa.html">{prod['categoria_nome']}</a> / {prod['titulo_card']}</div>
  <section class="prod">
    <div class="foto"><a href="{prod['link']}" target="_blank" rel="sponsored nofollow noopener" title="Ver oferta na {prod['loja_nome']}"><picture><source srcset="../img/{slug}.webp" type="image/webp"><img width="1120" height="840" fetchpriority="high" src="../img/{slug}.jpg" alt="{prod['titulo_card']}"></picture></a></div>
    <div>
      <span class="cat" style="color:var(--acento);font-size:11px;font-weight:800;letter-spacing:.1em">{prod['cat_badge']}</span>
      <h1>{prod['h1']}</h1>
      <div class="pmeta">{prod['sub']}</div>
      <div class="preco"><span class="de">de {prod['preco_de']}</span><span class="por">por {prod['preco_por']}</span><span class="cartao">{prod['preco_cartao']}</span><small>preço conferido em 28/11/2026 · {prod['desconto']}</small></div>
      <div class="btns" style="margin-top:18px">
        <a class="btn" href="{prod['link']}" target="_blank" rel="sponsored nofollow noopener">Ver oferta na {prod['loja_nome']} →</a>
      </div>
      <div class="box"><h2>Por que eu recomendo</h2><p style="color:var(--texto-corpo);font-size:14.5px">{prod['porque']}</p></div>

      <div class="box"><h3>Destaques Principais</h3><ul>
        {destaques_html}
      </ul></div>

      <div class="box"><h3>Ficha Técnica Oficial</h3><ul>
        {ficha_html}
      </ul></div>

      <div class="box"><h3>Pontos Fortes e Atenção</h3>
        <p style="color:var(--texto-corpo);font-size:14px;margin-bottom:6px"><strong>Prós:</strong></p>
        <ul style="margin-bottom:12px">{pros_html}</ul>
        <p style="color:var(--texto-corpo);font-size:14px;margin-bottom:6px"><strong>Ponto de atenção:</strong></p>
        <ul>{contras_html}</ul>
      </div>

      <div class="box"><h3>Para quem é indicado</h3><p style="color:var(--texto-corpo);font-size:14.5px">{prod['para_quem']}</p></div>
    </div>
  </section>
</main>

<footer class="footer"><div class="wrap">
  <p>© 2026 Renato Penner · Engenheiro da Computação · Loja Penner Tech</p>
  <div class="aviso"><strong>Aviso de afiliado:</strong> Participamos dos programas de parceiros oficiais da Awin (Casas Bahia e Americanas), Mercado Livre e Amazon. Ao comprar através dos nossos links, você apoia nosso trabalho independente sem pagar nenhum centavo a mais pelo produto.</div>
</div></footer>
<script src="../js/tema.js"></script>
</body>
</html>
"""
    p_path = os.path.join(P_DIR, f"{slug}.html")
    with open(p_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[PÁGINA] Gerada {p_path}")

def gerar_card_html(prod):
    slug = prod["slug"]
    busca_text = f"{prod['titulo_card'].lower()} {prod['sub'].lower()} {prod['loja_nome'].lower()} {prod['cat_css']}"
    busca_clean = re.sub(r'[^a-z0-9 ]', ' ', busca_text)
    busca_clean = re.sub(r'\s+', ' ', busca_clean).strip()

    return f"""    <article class="card" data-cat="{prod['cat_css']}" data-busca="{busca_clean}">
      <div class="thumbwrap"><a class="thumb" href="{prod['link']}" target="_blank" rel="sponsored nofollow noopener"><span class="badge">{prod['cat_badge']}</span><picture><source srcset="img/{slug}.webp" type="image/webp"><img width="1120" height="840" src="img/{slug}.jpg" alt="{prod['titulo_card']}" loading="lazy"></picture></a></div>
      <div class="body">
        <span class="cat">{prod['categoria_nome']}</span>
        <h3><a href="p/{slug}.html" style="color:inherit">{prod['titulo_card']}</a></h3>
        <span class="sub">{prod['sub']}</span>
        <p class="resumo">{prod['resumo']}</p>
        <div class="preco"><span class="de">de {prod['preco_de']}</span><span class="por">por {prod['preco_por']}</span><span class="cartao">{prod['preco_cartao']}</span><small>preço conferido em 28/11/2026 · {prod['desconto']}</small></div>
        <div class="btns">
          <a class="btn" href="{prod['link']}" target="_blank" rel="sponsored nofollow noopener">Ver na {prod['loja_nome']} →</a><a class="btn ghost" href="p/{slug}.html">Detalhes</a>
        </div>
      </div>
    </article>"""

def atualizar_htmls():
    pages = ["index.html", "casa.html", "promocoes.html"]
    for page in pages:
        path = os.path.join(REPO, page)
        if not os.path.exists(path):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        cards_to_insert = []
        for p in PRODUTOS:
            if f"p/{p['slug']}.html" not in content:
                cards_to_insert.append(gerar_card_html(p))

        if cards_to_insert:
            bloco = "\n".join(cards_to_insert)
            # Insere no inicio do <div class="grid">
            if '<div class="grid">' in content:
                content = content.replace('<div class="grid">', f'<div class="grid">\n{bloco}')
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"[CARDS] Inseridos {len(cards_to_insert)} cards em {page}")
        else:
            print(f"[CARDS] {page} já possui os cards.")

def atualizar_catalogo():
    with open(CATALOGO_PATH, "r", encoding="utf-8") as f:
        catalogo = json.load(f)

    slugs_existentes = {p["slug"] for p in catalogo}
    adicionados = 0
    for p in PRODUTOS:
        if p["slug"] not in slugs_existentes:
            item = {
                "slug": p["slug"],
                "title": p["titulo_card"],
                "file": f"{p['slug']}.html",
                "cat": p["loja_nome"],
                "link": p["link"],
                "preco_de": p["preco_de"],
                "preco_por": p["preco_por"],
                "preco_cartao": p["preco_cartao"],
                "cupom": "",
                "ultima_conferencia": "28/11/2026"
            }
            catalogo.insert(0, item)
            adicionados += 1

    if adicionados > 0:
        with open(CATALOGO_PATH, "w", encoding="utf-8") as f:
            json.dump(catalogo, f, ensure_ascii=False, indent=2)
        print(f"[CATÁLOGO] Adicionados {adicionados} produtos em produtos.json")
    else:
        print("[CATÁLOGO] produtos.json já continha os produtos.")

def atualizar_sitemap():
    with open(SITEMAP_PATH, "r", encoding="utf-8") as f:
        sm = f.read()

    adicionados = 0
    for p in PRODUTOS:
        loc = f"<loc>https://loja.pennertech.com.br/p/{p['slug']}.html</loc>"
        if loc not in sm:
            bloco = f"  <url>\n    {loc}\n    <lastmod>2026-11-28</lastmod>\n    <changefreq>daily</changefreq>\n    <priority>0.8</priority>\n  </url>\n"
            sm = sm.replace("</urlset>", f"{bloco}</urlset>")
            adicionados += 1

    if adicionados > 0:
        with open(SITEMAP_PATH, "w", encoding="utf-8") as f:
            f.write(sm)
        print(f"[SITEMAP] Adicionados {adicionados} links no sitemap.xml")
    else:
        print("[SITEMAP] sitemap.xml já possui os links.")

if __name__ == "__main__":
    for prod in PRODUTOS:
        gerar_imagem(prod)
        gerar_pagina_produto(prod)
    atualizar_htmls()
    atualizar_catalogo()
    atualizar_sitemap()
    print("=== PROCESSO DE CRIAÇÃO CONCLUÍDO COM SUCESSO! ===")
