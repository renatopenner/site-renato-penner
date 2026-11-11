/**
 * pennertech.com.br — roteador de borda (Cloudflare Worker)
 *
 *   pennertech.com.br/loja/*  -> GitHub Pages (renatopenner.github.io/site-renato-penner)
 *   www.pennertech.com.br     -> redireciona 301 para o apex
 *   pennertech.com.br/        -> portal provisório (raiz livre para os serviços futuros)
 *
 * Para publicar: Cloudflare Dashboard > Workers & Pages > Create > Worker,
 * cole este arquivo, Deploy, e em Settings > Triggers > Routes adicione
 *   pennertech.com.br/*  e  www.pennertech.com.br/*
 * Guia completo: GUIA-DOMINIO.md (nesta pasta).
 *
 * Quando os serviços da raiz entrarem (Cloudflare Tunnel, VPS etc.):
 * troque a rota "pennertech.com.br/*" por rotas específicas (ex.: /loja*)
 * e aponte a raiz para o novo destino. O /loja continua funcionando.
 */

const UPSTREAM = 'https://renatopenner.github.io/site-renato-penner';
const SITE = 'https://pennertech.com.br';
const PREFIXO = '/loja';

const PORTAL = `<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Penner Tech</title>
<meta name="description" content="Penner Tech — loja de recomendações e futuros serviços.">
<meta name="theme-color" content="#050a12">
<style>
*{box-sizing:border-box}
body{margin:0;min-height:100vh;display:flex;align-items:center;justify-content:center;
  background:#050a12;color:#dbe7f3;font:16px/1.6 'Segoe UI',system-ui,sans-serif;padding:32px}
.wrap{max-width:560px;width:100%}
h1{font-size:34px;margin:0 0 4px;letter-spacing:.02em}
h1 em{color:#38bdf8;font-style:normal}
p{color:#8fa6bb;margin:0 0 28px}
a.card{display:flex;align-items:center;gap:16px;text-decoration:none;color:inherit;
  background:#0c1724;border:1px solid #1e3448;border-radius:16px;padding:18px 20px;margin:0 0 12px;
  transition:border-color .15s,transform .15s}
a.card:hover{border-color:#38bdf8;transform:translateY(-2px)}
a.card .ico{font-size:26px}
a.card b{display:block;font-size:16px}
a.card span{color:#8fa6bb;font-size:13.5px}
small{display:block;color:#5b7183;font-size:12.5px;margin-top:24px}
</style>
</head>
<body>
<div class="wrap">
  <h1>Penner <em>Tech</em></h1>
  <p>Recomendações testadas e, em breve, os serviços do domínio.</p>
  <a class="card" href="/loja/"><span class="ico">🛒</span><span><b>Loja</b><span>Notebooks, SSD, acessórios e mobilidade elétrica — com link direto para a oferta</span></span></a>
  <a class="card" href="https://www.youtube.com/@renatopenner2037" target="_blank" rel="noopener"><span class="ico">▶</span><span><b>YouTube</b><span>Vídeos de análise e montagem</span></span></a>
  <small>© Penner Tech — novos serviços em breve neste endereço.</small>
</div>
</body>
</html>`;

export default {
  async fetch(request) {
    const url = new URL(request.url);

    // www -> apex (mantém caminho e query)
    if (url.hostname === 'www.pennertech.com.br') {
      return Response.redirect(SITE + url.pathname + url.search, 301);
    }

    // /loja -> /loja/
    if (url.pathname === PREFIXO) {
      return Response.redirect(SITE + PREFIXO + '/' + url.search, 301);
    }

    // /loja/* -> GitHub Pages, preservando query string (cache busting ?v=...)
    if (url.pathname.startsWith(PREFIXO + '/')) {
      const destino = UPSTREAM + url.pathname.slice(PREFIXO.length) + url.search;
      const resposta = await fetch(destino, {
        method: request.method,
        headers: request.headers,
        redirect: 'follow',
        cf: { cacheEverything: false }
      });
      const headers = new Headers(resposta.headers);
      headers.set('x-pennertech-rota', 'loja');
      const corpo = request.method === 'HEAD' ? null : resposta.body;
      return new Response(corpo, {
        status: resposta.status,
        statusText: resposta.statusText,
        headers
      });
    }

    // raiz: portal provisório
    if (url.pathname === '/' || url.pathname === '') {
      return new Response(PORTAL, {
        headers: {
          'content-type': 'text/html; charset=utf-8',
          'cache-control': 'public, max-age=120'
        }
      });
    }

    return new Response('Não encontrado', {
      status: 404,
      headers: { 'content-type': 'text/plain; charset=utf-8' }
    });
  }
};
