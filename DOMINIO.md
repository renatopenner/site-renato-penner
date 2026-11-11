# Domínio — pennertech.com.br (ATIVO)

**Status em 11/11/2026, 14:32:** no ar e com HTTPS forçado nos dois hostnames.

```
https://loja.pennertech.com.br/                -> loja (GitHub Pages, repo site-renato-penner)
https://loja.pennertech.com.br/p/<slug>.html   -> páginas de produto
https://pennertech.com.br/                     -> redirect para a loja (página do repo renatopenner.github.io)
https://www.pennertech.com.br/                 -> 301 para pennertech.com.br (GitHub Pages)
http://…                                       -> 301 para https
https://renatopenner.github.io/site-renato-penner/  -> 301 para https://loja.pennertech.com.br/
```

## Como ficou

| Peça | Onde | Config |
|---|---|---|
| Loja | repo `site-renato-penner` | custom domain `loja.pennertech.com.br`, `Enforce HTTPS` ligado, arquivo `CNAME` no repo |
| Raiz | repo `renatopenner.github.io` (site de usuário) | custom domain `pennertech.com.br`, `Enforce HTTPS` ligado, `CNAME` no repo + página de redirect |
| DNS | Registro.br (nameservers `d.sec.dns.br` / `e.sec.dns.br`) | 4 A no apex → IPs do GitHub Pages; CNAME `loja` e `www` → `renatopenner.github.io` |

Certificados Let's Encrypt emitidos pelo GitHub e aprovados para os dois hostnames.

## Verificação (11/11/2026 14:32)

```
200  https://loja.pennertech.com.br/
200  https://loja.pennertech.com.br/p/bicicleta-eletrica-cavalletta-c12.html
200  https://loja.pennertech.com.br/img/patinete-gm5-p1.webp     (image/webp)
200  https://loja.pennertech.com.br/sobre.html
200  https://loja.pennertech.com.br/robots.txt
200  https://loja.pennertech.com.br/sitemap.xml                  (53 URLs)
200  https://pennertech.com.br/                                  (página de redirect)
301  https://www.pennertech.com.br/   -> https://pennertech.com.br/
301  http://loja.pennertech.com.br/   -> https://loja.pennertech.com.br/
301  https://renatopenner.github.io/site-renato-penner/ -> https://loja.pennertech.com.br/
```

## Pendências e próximos passos

1. **Google Search Console**: criar propriedade `loja.pennertech.com.br`, verificar (arquivo HTML no repo
   ou TXT no DNS) e enviar `https://loja.pennertech.com.br/sitemap.xml`.
2. **Serviços na raiz**: quando existirem, trocar o apontamento do apex (ex.: Cloudflare Tunnel no
   pennerserver) e **remover o custom domain** do repo `renatopenner.github.io` (Settings → Pages →
   apagar Custom domain), senão o GitHub continua reivindicando o apex. A loja no subdomínio não muda.
3. O `github.io` antigo continuará **redirecionando** (301) para a loja — links de vídeos e posts
   seguem funcionando.

## Regras para não quebrar

- **Não remover** o arquivo `CNAME` do repo da loja (é o que mantém `loja.pennertech.com.br`).
- **Não** apontar o apex para outro serviço sem antes remover o custom domain do site de usuário.
- Ao mexer no DNS, manter os 4 A do apex e o CNAME da `loja`; `www` é opcional.
- Se a zona voltar a não publicar no painel do Registro.br, o plano B é migrar os nameservers para o
  Cloudflare e recriar os mesmos registros — a ativação no GitHub já está feita e não muda.
