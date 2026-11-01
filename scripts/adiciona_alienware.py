import os, sys, re, io
from PIL import Image, ImageFilter

BASE = r"C:\Users\renat\site-renato-penner"
FOTO = r"C:\Users\renat\.gemini\antigravity\brain\ac36df41-508a-400b-b520-a2b9bbb277eb\.user_uploaded\media_1793567313399_2cceba6a.png"
SLUG = "dell-alienware-16-aurora-ac16250"
TITULO = "Notebook Gamer Dell Alienware 16 Aurora AC16250"
SUB = "Intel Core 7 240H · 32 GB DDR5 · 512 GB SSD NVMe · RTX 3050 6GB · Tela 16\" · Wi-Fi 7 · Windows 11"
LINK_AFILIADO = "https://meli.la/2FutpuB"

# 1. Tratar a imagem
print("Tratando a imagem do produto...")
im = Image.open(FOTO).convert("RGBA")

# Fundo 1120x840 gradiente/dark
fundo = Image.new("RGBA", (1120, 840), (11, 16, 32, 255))
# Halo azul suave no fundo
halo = Image.new("RGBA", (1120, 840), (0, 0, 0, 0))
from PIL import ImageDraw
hdraw = ImageDraw.Draw(halo)
hdraw.ellipse([(200, 100), (920, 740)], fill=(28, 48, 80, 160))
halo = halo.filter(ImageFilter.GaussianBlur(90))
fundo = Image.alpha_composite(fundo, halo)

# Redimensionar imagem original mantendo aspect ratio
alvo_h = 760
escala = alvo_h / im.height
novo_w = int(im.width * escala)
novo = im.resize((novo_w, alvo_h), Image.Resampling.LANCZOS)

# Centralizar
fundo.paste(novo, ((1120 - novo_w) // 2, (840 - alvo_h) // 2), novo)
img_dest = os.path.join(BASE, "img", f"{SLUG}.png")
fundo.convert("RGB").save(img_dest, optimize=True)
print(f"Imagem gerada em: {img_dest}")

# 2. Gerar pagina de produto em p/
print("Gerando pagina de produto p/...")
html_prod = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta http-equiv="Cache-Control" content="no-store">
<meta name="build" content="2026-11-01 18:00">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{TITULO} — Renato Penner</title>
<meta name="description" content="Notebook Gamer Dell Alienware 16 Aurora AC16250 com Intel Core 7 240H, 32 GB RAM DDR5, RTX 3050 6GB GDDR6 e Wi-Fi 7. Desempenho excepcional.">
<link rel="canonical" href="https://www.renatopenner.com.br/p/{SLUG}.html">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Renato Penner">
<meta property="og:title" content="{TITULO} — Renato Penner">
<meta property="og:description" content="Notebook Gamer Dell Alienware 16 Aurora AC16250 com Intel Core 7 240H, 32 GB RAM DDR5, RTX 3050 6GB e Wi-Fi 7.">
<meta property="og:url" content="https://www.renatopenner.com.br/p/{SLUG}.html">
<meta property="og:locale" content="pt_BR">
<meta name="theme-color" content="#050a12">
<meta property="og:image" content="https://www.renatopenner.com.br/img/{SLUG}.png">
<meta property="og:image:width" content="1120">
<meta property="og:image:height" content="840">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://www.renatopenner.com.br/img/{SLUG}.png">
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
    <a href="../notebooks.html">Notebooks</a> / Dell Alienware 16 Aurora</div>
  <section class="prod">
    <div class="foto"><a href="{LINK_AFILIADO}" target="_blank" rel="sponsored nofollow noopener" title="Ver oferta no Mercado Livre"><img src="../img/{SLUG}.png" alt="{TITULO}"></a></div>
    <div>
      <span class="cat" style="color:#38bdf8;font-size:11px;font-weight:800;letter-spacing:.1em">Mercado Livre · Oferta Oficial</span>
      <h1>{TITULO}</h1>
      <div class="pmeta">{SUB}</div>
      <div class="preco"><span class="por">Confira o preço e condições no Mercado Livre</span><span class="cartao">em até 10x ou 12x sem juros com frete grátis</span><small>preço conferido em 01/11/2026</small></div>

      <div class="btns" style="margin-top:18px">
        <a class="btn" href="{LINK_AFILIADO}" target="_blank" rel="sponsored nofollow noopener">Ver oferta no Mercado Livre →</a>
      </div>
      
      <div class="box"><h4>Descrição Geral</h4><p style="color:#c6d5e2;font-size:14.5px">Com o Dell Alienware 16 Aurora AC16250 você terá uma incrível experiência em um notebook com desempenho excepcional. Equipado com processadores Intel Core série H, fornece um desempenho poderoso para jogos de última geração, desenvolvimento pesado, renderização e multitarefa extrema.</p></div>
      
      <div class="box"><h4>Destaques e Vantagens</h4><ul>
        <li class="dt"><strong>Processador Intel® Core™ 7 240H:</strong> 10 núcleos, cache de 24 MB e frequência turbo de até 5.2 GHz para máxima resposta em tarefas pesadas.</li>
        <li class="dt"><strong>32 GB de Memória RAM DDR5 a 5600 MT/s:</strong> Configuração em Dual Channel (2x 16GB) para máxima largura de banda em emulação, compilação de código e jogos AAA.</li>
        <li class="dt"><strong>Placa de Vídeo Dedicada NVIDIA® GeForce RTX™ 3050 (6GB GDDR6):</strong> Suporte completo a Ray Tracing e DLSS com 6GB de VRAM dedicada.</li>
        <li class="dt"><strong>Conectividade Wi-Fi 7 Ultrarrápida:</strong> Placa de rede wireless MediaTek Wi-Fi 7 MT7925 com MU-MIMO 2x2 e Bluetooth de última geração.</li>
        <li class="dt"><strong>Construção Premium Alienware:</strong> Chassi robusto na tonalidade Azul Escuro com acabamento sofisticado e sistema térmico eficiente.</li>
        <li class="dt"><strong>Teclado Numérico Retroiluminado:</strong> Teclado retroiluminado na cor branca, no padrão ABNT2 em português do Brasil e com teclado numérico integrado.</li>
        <li class="dt"><strong>Áudio Imersivo Dolby Audio:</strong> Clareza sonora superior para jogos e chamadas de vídeo.</li>
      </ul></div>

      <div class="box"><h4>Especificações Técnicas Completas</h4><ul>
        <li class="dt"><strong>Cor:</strong> Azul escuro</li>
        <li class="dt"><strong>Processador:</strong> Intel® Core™ 7 240H (10-core, cache de 24MB, até 5.2 GHz)</li>
        <li class="dt"><strong>Armazenamento:</strong> SSD de 512GB PCIe NVMe M.2</li>
        <li class="dt"><strong>Memória RAM:</strong> 32GB DDR5 (2x16GB) 5600MT/s</li>
        <li class="dt"><strong>Placa de vídeo:</strong> NVIDIA® GeForce RTX™ 3050, GDDR6 de 6GB</li>
        <li class="dt"><strong>Teclado:</strong> Teclado retroiluminado na cor branca, numérico e em português</li>
        <li class="dt"><strong>Sistema Operacional:</strong> Windows 11 Home em Português (Brasil)</li>
        <li class="dt"><strong>Portas:</strong> 1 porta Type-C (USB 3.2 Gen 2, DisplayPort 1.4 para iGPU), 1 porta Type-C (USB 3.2 Gen 2 e DisplayPort 1.4 para iGPU); 2 portas USB 3.2 1ª geração Type-A</li>
        <li class="dt"><strong>Áudio:</strong> Dolby Audio</li>
        <li class="dt"><strong>Conectividade:</strong> MediaTek Wi-Fi 7 MT7925, 2x2, 802.11be, MU-MIMO, wireless com Bluetooth®</li>
        <li class="dt"><strong>Chipset:</strong> Chipset integrado com o processador</li>
        <li class="dt"><strong>Bateria:</strong> 3 células e 60 Wh (integrada)</li>
        <li class="dt"><strong>Dimensões:</strong> Altura: 35,69 cm | Largura: 1,86 cm | Profundidade: 2,27 cm</li>
        <li class="dt"><strong>Peso aproximado:</strong> 2,49 Kg</li>
        <li class="dt"><strong>Webcam:</strong> HD widescreen integrada com Dual Array Microphones</li>
        <li class="dt"><strong>Conteúdo da embalagem:</strong> Computador, cabo de força, manuais</li>
        <li class="dt"><strong>Aviso legal:</strong> A duração da bateria depende do uso que se dê ao produto.</li>
      </ul></div>

      <div class="box"><h4>Para quem é indicado</h4><p style="color:#c6d5e2;font-size:14.5px">Gamers, engenheiros, programadores e profissionais que precisam de uma estação de trabalho portátil extremamente potente com 32 GB de RAM DDR5 e GPU dedicada com alta durabilidade e confiabilidade da linha Alienware.</p></div>
    </div>
  </section>
</main>
<footer class="footer"><div class="wrap"><p>© 2026 Renato Penner · Engenheiro da Computação</p></div></footer>
</body>
</html>
"""

page_path = os.path.join(BASE, "p", f"{SLUG}.html")
with open(page_path, "w", encoding="utf-8") as f:
    f.write(html_prod)
print(f"Pagina de produto criada em: {page_path}")

# 3. Inserir card em notebooks.html
print("Atualizando notebooks.html...")
nb_path = os.path.join(BASE, "notebooks.html")
with open(nb_path, "r", encoding="utf-8") as f:
    nb_content = f.read()

card_html = f"""    <article class="card" data-cat="notebooks" data-busca="notebook gamer dell alienware 16 aurora ac16250 intel core 7 32gb rtx 3050 notebooks">
      <div class="thumbwrap"><a class="thumb" href="p/{SLUG}.html"><span class="badge">Mercado Livre</span><img src="img/{SLUG}.png" alt="{TITULO}" loading="lazy"></a></div>
      <div class="body">
        <span class="cat">Notebook Gamer</span>
        <h3><a href="p/{SLUG}.html">{TITULO}</a></h3>
        <p class="specs">Intel Core 7 240H · 32 GB RAM DDR5 · SSD 512 GB · RTX 3050 6GB · Wi-Fi 7</p>
        <div class="foot">
          <div class="preco"><span class="por">Ver oferta</span><small>Mercado Livre Oficial</small></div>
          <div class="botoes">
            <a class="btn-detalhes" href="p/{SLUG}.html">Análise</a>
            <a class="btn-comprar" href="{LINK_AFILIADO}" target="_blank" rel="sponsored nofollow noopener">Comprar</a>
          </div>
        </div>
      </div>
    </article>
"""

if f"p/{SLUG}.html" not in nb_content:
    nb_content = nb_content.replace('<div class="grid">', f'<div class="grid">\n{card_html}')
    with open(nb_path, "w", encoding="utf-8") as f:
        f.write(nb_content)
    print("notebooks.html atualizado com sucesso!")
else:
    print("notebooks.html ja continha o card.")

# 4. Atualizar sitemap.xml
sitemap_path = os.path.join(BASE, "sitemap.xml")
with open(sitemap_path, "r", encoding="utf-8") as f:
    sm_content = f.read()

nova_url = f"  <url><loc>https://www.renatopenner.com.br/p/{SLUG}.html</loc></url>\n"
if f"p/{SLUG}.html" not in sm_content:
    sm_content = sm_content.replace("</urlset>", f"{nova_url}</urlset>")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sm_content)
    print("sitemap.xml atualizado!")

print("=== CONCLUIDO CADASTRO NO SITE COM SUCESSO! ===")