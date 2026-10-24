// =========================================================================
// Penner Tech - Motor Unificado de Rastreamento & Tráfego Pago
// Compatível com Google Ads, GA4, Meta Ads (Facebook/Instagram) e GTM
// =========================================================================

(function() {
  'use strict';

  // Configuração opcional de IDs (basta preencher quando tiver os IDs de campanha):
  window.PENNER_TRACKING_CONFIG = window.PENNER_TRACKING_CONFIG || {
    ga4_id: '',          // Ex: 'G-XXXXXXXXXX'
    gtm_id: '',          // Ex: 'GTM-XXXXXXX'
    meta_pixel_id: '',   // Ex: '123456789012345'
    google_ads_id: ''    // Ex: 'AW-XXXXXXXXX'
  };

  // Inicializa dataLayer padrão da indústria
  window.dataLayer = window.dataLayer || [];
  function gtag(){ window.dataLayer.push(arguments); }
  window.gtag = window.gtag || gtag;

  // 1. Captura e persistência de parâmetros de tráfego pago (UTMs, GCLID, FBCLID)
  function capturarParametrosCampanha() {
    var params = new URLSearchParams(window.location.search);
    var campaignData = {};
    var chaves = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content', 'gclid', 'fbclid', 'ttclid'];
    var encontrou = false;

    chaves.forEach(function(chave) {
      var val = params.get(chave);
      if (val) {
        campaignData[chave] = val;
        encontrou = true;
      }
    });

    if (encontrou) {
      try {
        sessionStorage.setItem('penner_campaign', JSON.stringify(campaignData));
        localStorage.setItem('penner_last_campaign', JSON.stringify({
          data: campaignData,
          timestamp: new Date().toISOString()
        }));
      } catch (e) {}
    } else {
      try {
        var salvo = sessionStorage.getItem('penner_campaign');
        if (salvo) campaignData = JSON.parse(salvo);
      } catch (e) {}
    }

    return campaignData;
  }

  var campanhaAtual = capturarParametrosCampanha();

  // 2. Disparo de visualização de página com dados da campanha
  window.dataLayer.push({
    'event': 'penner_page_view',
    'page_path': window.location.pathname,
    'page_title': document.title,
    'page_url': window.location.href,
    'campaign_data': campanhaAtual,
    'device': /Mobile|Android|iPhone/i.test(navigator.userAgent) ? 'mobile' : 'desktop'
  });

  // 3. Monitoramento inteligente de cliques (Afiliados e Redes)
  document.addEventListener('click', function(ev) {
    var a = ev.target && ev.target.closest ? ev.target.closest('a') : null;
    if (!a) return;

    var href = a.href || '';
    var destino = '';
    var tipo = '';

    if (href.indexOf('mercadolivre.com.br') >= 0 || href.indexOf('meli.la') >= 0) {
      destino = 'mercadolivre';
      tipo = 'afiliado';
    } else if (href.indexOf('amazon.com.br') >= 0 || href.indexOf('amzn.to') >= 0 || href.indexOf('link.amazon') >= 0) {
      destino = 'amazon';
      tipo = 'afiliado';
    } else if (href.indexOf('wa.me') >= 0 || href.indexOf('whatsapp.com') >= 0) {
      destino = 'whatsapp';
      tipo = 'contato';
    } else if (href.indexOf('youtube.com') >= 0 || href.indexOf('youtu.be') >= 0) {
      destino = 'youtube';
      tipo = 'social';
    } else if (href.indexOf('instagram.com') >= 0) {
      destino = 'instagram';
      tipo = 'social';
    }

    if (!destino) return;

    // Identificar produto se o clique veio de um card
    var card = a.closest('.card') || a.closest('article');
    var nomeProduto = '';
    if (card) {
      var h3 = card.querySelector('h3');
      if (h3) nomeProduto = h3.innerText.trim();
    }

    var eventoClique = {
      'event': 'outbound_click',
      'destino': destino,
      'tipo': tipo,
      'produto': nomeProduto || document.title,
      'url_destino': href,
      'origem_pagina': window.location.pathname,
      'campaign_data': campanhaAtual,
      'timestamp': new Date().toISOString()
    };

    console.log('[Analytics] Clique registrado:', destino, nomeProduto);
    window.dataLayer.push(eventoClique);

    if (typeof window.gtag === 'function') {
      window.gtag('event', 'select_promotion', {
        'promotion_id': destino,
        'promotion_name': nomeProduto || destino,
        'items': [{ 'item_name': nomeProduto || document.title }]
      });
    }
  }, true);

  console.log('[Penner Tech] Analytics & Tráfego Pago carregado com sucesso.');
})();
