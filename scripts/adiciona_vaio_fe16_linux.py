"""Adiciona o Notebook Vaio FE16 AMD Ryzen 7 5825U Linux ao site renatopenner.github.io/site-renato-penner."""
import json
import os
import re
from PIL import Image

BASE = r"C:\Users\renat\SitesGithub\site-renato-penner"
BASE_ALT = r"C:\Users\renat\site-renato-penner"
FOTO_ORIG = r"C:\Users\renat\.gemini\antigravity\brain\f5473a48-b285-40d0-a684-f6a965c4b894\.user_uploaded\media_1793898104668_2f64c761.png"
SLUG = "vaio-fe16-ryzen7-linux"
DATA = "05/11/2026"
MARCA_W, MARCA_H = 1120, 840

PRODUTO = {
    "slug": SLUG,
    "titulo_card": "Notebook Vaio FE16 (Linux Debian 12)",
    "h1": "Notebook Vaio FE16 AMD Ryzen 7 5825U · Linux Debian 12 · 8 GB RAM · 512 GB SSD · Wi-Fi 6 · Tela 16\" IPS WUXGA Antirreflexo",
    "meta_desc": "Notebook Vaio FE16 com AMD Ryzen 7 5825U (8 núcleos / 16 threads), 8 GB RAM expansível até 64 GB, SSD 512 GB, tela 16\" IPS WUXGA 16:10, Wi-Fi 6 e sistema operacional Linux Debian 12 de fábrica.",
    "cat_badge": "Mercado Livre · ⚠️ SISTEMA LINUX DEBIAN 12",
    "cat_css": "notebooks",
    "categoria_nome": "Notebooks",
    "sub": "AMD Ryzen 7 5825U (8C/16T) · 8 GB RAM (Exp. até 64GB) · SSD 512 GB · 16\" IPS WUXGA (16:10) · Wi-Fi 6 · LINUX DEBIAN 12",
    "resumo": "Potência de sobra para programação, multitarefa e produtividade: processador AMD Ryzen 7 5825U de 8 núcleos e 16 threads, tela ampla de 16 polegadas IPS WUXGA (1920x1200) com proporção 16:10 produtiva, Wi-Fi 6, porta de rede Gigabit e total capacidade de upgrade (suporta até 64 GB de RAM e troca de SSD). Vem de fábrica com Linux Debian 12, entregando excelente desconto por não incluir licença proprietária de Windows.",
    "link": "https://meli.la/1Rf6Uvn",
    "preco_de": "R$ 5.099,00",
    "preco_por": "R$ 3.229,05",
    "preco_cartao": "ou R$ 3.399 em até 10x sem juros",
    "desconto": "36% OFF",
    "porque": "A linha Vaio FE16 com o AMD Ryzen 7 5825U entrega uma das melhores relações de custo por núcleo do mercado. São 8 núcleos reais e 16 threads capazes de compilar códigos pesados, rodar containers Docker, máquinas virtuais e multitarefa com folga. Diferente de concorrentes ultrafinos com memória 100% soldada, este Vaio conta com 2 slots SODIMM que permitem upgrade de memória RAM até impressionantes 64 GB e slot M.2 para expansão do SSD. Além disso, a tela IPS de 16 polegadas em proporção 16:10 (1920x1200) oferece muito mais área vertical para leitura de código e documentos do que painéis 16:9 convencionais. Por vir com o Linux Debian 12 de fábrica, você não paga o custo da licença do Windows — garantindo economia direta de centenas de reais.",
    "destaques": [
        ("Aviso Importante: Sistema Linux Debian 12", "Sai de fábrica com a estável distribuição Linux Debian 12. Não acompanha o Microsoft Windows de fábrica. Se preferir usar o Windows, você poderá instalar sua própria licença posteriormente sem complicações."),
        ("Processador AMD Ryzen 7 5825U (8C / 16T)", "8 núcleos e 16 threads com clock turbo de até 4,5 GHz e 16 MB de cache L3 — desempenho de ponta para programação pesada, compilação, virtualização e multitarefa"),
        ("Tela 16\" IPS WUXGA (1920 x 1200) Antirreflexo", "Resolução nítida em proporção 16:10 produtiva, que exibe mais linhas de código, planilhas e páginas web com fidelidade de cores e ângulos de visão confortáveis do painel IPS"),
        ("Totalmente Aberto a Upgrades (RAM e SSD)", "Possui 2 slots de memória RAM DDR4 com suporte a até 64 GB e slot M.2 NVMe para expansão ou troca de SSD — longevidade garantida sem peças soldadas"),
        ("Conectividade Wi-Fi 6 e Rede Gigabit RJ-45", "Conexão sem fio ultrarrápida Wi-Fi 6 com menor latência, além da tradicional porta física Ethernet RJ-45 para conexão cabeada ultraestável"),
        ("Teclado Ergonômico com Pad Numérico", "Digitação confortável com teclado numérico dedicado integrado, ideal para produtividade, programação e inserção ágil de números"),
        ("Bateria de Longa Duração e Chassi Grafite", "Autonomia declarada de até 10 horas de uso moderado, carregador prático e acabamento sóbrio e elegante em Cinza Grafite"),
    ],
    "ficha": [
        "Marca: VAIO (fabricado sob licença oficial pela Positivo Tecnologia no Brasil)",
        "Modelo: Vaio FE16 VJFE69F11XB0321H",
        "Processador: AMD Ryzen 7 5825U (8 núcleos / 16 threads, 2.0 GHz base, até 4.5 GHz Max Boost, 16 MB L3 Cache)",
        "Placa de Vídeo Integrada: AMD Radeon Graphics (Vega 8)",
        "Memória RAM: 8 GB DDR4 (expansível até 64 GB em 2 slots SODIMM — permite upgrade)",
        "Armazenamento: 512 GB SSD M.2 NVMe PCIe (permite upgrade)",
        "Sistema Operacional: Linux Debian 12 (⚠️ Atenção: Não vem com Microsoft Windows)",
        "Tela: 16\" IPS WUXGA (1920 x 1200 px), proporção 16:10, antirreflexo, 60 Hz",
        "Conectividade sem fio: Wi-Fi 6 (802.11ax) Dual Band + Bluetooth",
        "Portas e Conexões: 1x USB-C, 1x USB 3.2, 1x USB 3.0, 1x USB 2.0, 1x HDMI, 1x Porta Ethernet RJ-45 Gigabit, 1x leitor de cartão de memória SD, saída para fones de ouvido P2/P3",
        "Teclado: Padrão ABNT2 com teclado numérico dedicado integrado",
        "Bateria: 4,78 Ah / Íon de Lítio (autonomia estimada de até 10 horas)",
        "Cor: Cinza Grafite",
        "Homologação Anatel: 2581402198",
    ],
    "pros": [
        "Processador AMD Ryzen 7 5825U potente com 8 núcleos e 16 threads reais",
        "Permite upgrade de memória RAM até 64 GB em 2 slots SODIMM (nada de RAM soldada)",
        "Permite upgrade e troca fácil do SSD M.2 NVMe",
        "Tela de 16 polegadas IPS WUXGA (1920x1200) em proporção 16:10 antirreflexo",
        "Excelente economia de preço por não incluir o custo da licença do Windows",
        "Wi-Fi 6 moderno + porta física de rede Ethernet RJ-45",
        "Teclado completo com teclado numérico integrado",
    ],
    "contras": [
        "⚠️ VEM COM LINUX DEBIAN 12: requer instalação manual do Windows caso o comprador necessite do sistema da Microsoft",
        "Vem de fábrica com 8 GB em canal único (adicionar um segundo pente de memória ativa Dual Channel e melhora ainda mais o desempenho)",
        "Não possui leitor biométrico de impressão digital",
    ],
    "para_quem": "Desenvolvedores, engenheiros de software, administradores de sistemas, estudantes de TI e entusiastas que já usam Linux no dia a dia ou que desejam o máximo de poder de processamento (Ryzen 7 8C/16T) com tela grande de 16\" e facilidade de upgrade pagando menos pelo fato de não embutir a licença do Windows.",
}


def prepara_imagem():
    im = Image.open(FOTO_ORIG).convert("RGB")
    alvo_h = 780
    escala = alvo_h / im.height
    novo_w = int(im.width * escala)
    novo = im.resize((novo_w, alvo_h), Image.Resampling.LANCZOS)
    tela = Image.new("RGB", (MARCA_W, MARCA_H), (255, 255, 255))
    tela.paste(novo, ((MARCA_W - novo_w) // 2, (MARCA_H - alvo_h) // 2))

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


def gera_card(p):
    busca = re.sub(
        r"[^a-z0-9 ]",
        " ",
        (
            p["titulo_card"]
            + " "
            + p["sub"]
            + " "
            + p["slug"]
            + " vaio fe16 ryzen 7 5825u linux debian 12 notebook 16 ips wuxga ram ssd upgrade"
        ).lower(),
    )
    busca = re.sub(r"\s+", " ", busca).strip()
    return f'''<article class="card" data-cat="{p['cat_css']}" data-busca="{busca}">
      <div class="thumbwrap"><a class="thumb" href="{p['link']}" target="_blank" rel="sponsored nofollow noopener"><span class="badge" style="background:#f59e0b;color:#000;font-weight:900">⚠️ LINUX</span><img src="img/{p['slug']}.png" alt="{p['titulo_card']}" loading="lazy"></a></div>
      <div class="body">
        <span class="cat">{p['categoria_nome']}</span>
        <h3><a href="p/{p['slug']}.html" style="color:inherit">{p['titulo_card']}</a></h3>
        <span class="sub">{p['sub']}</span>
        <div style="background:rgba(245,158,11,0.12);border:1px solid #f59e0b;color:#fcd34d;padding:5px 9px;border-radius:7px;font-size:11.5px;font-weight:700;margin:6px 0 8px;display:flex;align-items:center;gap:6px"><span>⚠️</span> <span>Atenção: Sistema Operacional <strong>Linux Debian 12</strong> (não vem com Windows)</span></div>
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
<meta name="build" content="2026-11-05 14:10">
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
  <nav class="links"><a class="link " href="../index.html">Início</a><a class="link " href="../promocoes.html">Ofertas</a><a class="link on" href="../notebooks.html">Notebooks</a><a class="link " href="../ssd.html">SSD</a><a class="link " href="../carregadores.html">Carregadores</a><a class="link " href="../saude.html">Saúde</a><a class="link " href="../casa.html">Casa</a><a class="link " href="../auto.html">Auto</a><a class="link " href="../perifericos.html">Periféricos</a><a class="link " href="../moda.html">Moda</a></nav>
  <div class="dir"><a class="link" href="https://www.youtube.com/@renatopenner2037" target="_blank" rel="noopener">YouTube ↗</a></div>
</div></header>
<main class="wrap">
  <div class="migalha"><a href="../index.html">Início</a> /
    <a href="../notebooks.html">{p['categoria_nome']}</a> / {p['titulo_card']}</div>
  <section class="prod">
    <div class="foto"><a href="{p['link']}" target="_blank" rel="sponsored nofollow noopener" title="Ver oferta no Mercado Livre"><img src="../img/{p['slug']}.png" alt="{p['titulo_card']}"></a></div>
    <div>
      <span class="cat" style="color:#38bdf8;font-size:11px;font-weight:800;letter-spacing:.1em">{p['cat_badge']}</span>
      <h1>{p['h1']}</h1>
      <div class="pmeta">{p['sub']}</div>
      {bloco_preco(p)}

      <div style="background:rgba(245,158,11,0.12);border:2px solid #f59e0b;border-radius:12px;padding:14px 18px;margin:18px 0;color:#fef08a;font-size:14.5px;line-height:1.5">
        <div style="display:flex;align-items:center;gap:8px;font-size:15px;font-weight:800;color:#fbbf24;margin-bottom:6px">
          <span style="font-size:18px">⚠️</span> AVISO IMPORTANTE: SISTEMA OPERACIONAL LINUX DEBIAN 12
        </div>
        Este modelo sai de fábrica com o sistema operacional <strong>Linux (Debian 12)</strong> e <strong>não possui o Microsoft Windows pré-instalado</strong>. Trata-se de uma excelente economia para quem já utiliza Linux (desenvolvedores, estudantes e profissionais de TI) ou para quem deseja adquirir um hardware potente com Ryzen 7 Octa-Core gastando menos e instalar sua própria licença do Windows por conta própria.
      </div>

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
<script type="application/ld+json">{{"@context": "https://schema.org", "@type": "Product", "name": "{p['titulo_card']}", "description": "{p['meta_desc']}", "brand": {{"@type": "Brand", "name": "VAIO"}}, "offers": {{"@type": "Offer", "url": "{p['link']}", "price": "{preco_num}", "priceCurrency": "BRL", "availability": "https://schema.org/InStock"}}, "aggregateRating": {{"@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "1171"}}}}</script>

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

    # 1. Página de produto p/vaio-fe16-ryzen7-linux.html
    page_html = gera_pagina_completa(p)

    for base_dir in [BASE, BASE_ALT]:
        if os.path.exists(base_dir):
            page_path = os.path.join(base_dir, "p", f"{SLUG}.html")
            with open(page_path, "w", encoding="utf-8") as f:
                f.write(page_html)
            print("Página criada:", page_path)

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
    card_html = gera_card(p)

    for base_dir in [BASE, BASE_ALT]:
        if not os.path.exists(base_dir):
            continue

        paginas_config = [
            ("index.html", card_html),
            ("promocoes.html", card_html),
            ("notebooks.html", card_html),
        ]

        for nome, card_markup in paginas_config:
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
            content = content[:pos] + card_markup + "\n    " + content[pos:]
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
