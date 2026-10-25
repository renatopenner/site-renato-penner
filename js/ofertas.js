/* Cliques em oferta -> evento no GA4 (funciona no GitHub Pages, sem servidor).
   Só dispara depois do aceite do banner de cookies (localStorage consent = 'ok'). */
(function () {
  function lojaDe(href) {
    var h = (href || '').toLowerCase();
    if (h.indexOf('mercadolivre') >= 0 || h.indexOf('meli.la') >= 0) return 'mercadolivre';
    if (h.indexOf('amazon') >= 0) return 'amazon';
    if (h.indexOf('wa.me') >= 0 || h.indexOf('whatsapp') >= 0) return 'whatsapp';
    if (h.indexOf('youtu') >= 0) return 'youtube';
    return '';
  }

  function produtoDa(href, pagina) {
    var m = (href || '').match(/\/MLB-?(\d+)/);
    if (m) return 'MLB' + m[1];
    var p = (pagina || '').match(/\/p\/([a-z0-9-]+)\.html/);
    if (p) return p[1];
    try {
      var u = new URL(href);
      var seg = u.pathname.split('/').filter(Boolean).pop() || '';
      return seg.slice(0, 60);
    } catch (e) { return ''; }
  }

  function consentido() {
    try { return localStorage.getItem('consent') === 'ok'; } catch (e) { return false; }
  }

  document.addEventListener('click', function (ev) {
    var a = ev.target && ev.target.closest ? ev.target.closest('a') : null;
    if (!a) return;
    var loja = lojaDe(a.href);
    if (!loja) return;
    if (loja === 'youtube') return;            // vídeo não é clique de compra
    if (!consentido() || typeof window.gtag !== 'function') return;
    window.gtag('event', 'click_oferta', {
      loja: loja,
      produto: produtoDa(a.href, location.pathname),
      pagina: location.pathname,
      posicao: (a.closest('.card') ? 'card' : (a.closest('.btns') ? 'botao' : 'outro')),
      destino: a.href.slice(0, 180)
    });
  }, true);

  /* clique no botão de compra da página de produto = intenção mais forte */
  document.addEventListener('click', function (ev) {
    var a = ev.target && ev.target.closest ? ev.target.closest('a') : null;
    if (!a) return;
    var loja = lojaDe(a.href);
    if (!loja || loja === 'youtube') return;
    if (!consentido() || typeof window.gtag !== 'function') return;
    if (a.closest('.prod') || document.querySelector('.prod')) {
      window.gtag('event', 'clique_comprar', {
        loja: loja,
        produto: produtoDa(a.href, location.pathname),
        pagina: location.pathname
      });
    }
  }, true);
})();
