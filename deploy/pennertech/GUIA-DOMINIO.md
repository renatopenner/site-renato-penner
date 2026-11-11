# Domínio próprio: pennertech.com.br/loja

O site (repo `site-renato-penner`) continua sendo publicado pelo GitHub Pages como sempre
(o motor de preços, o guardião e os hooks não mudam). O que entra é uma **camada na frente do
domínio** que decide o que cada caminho serve:

```
pennertech.com.br/loja/*   ->  GitHub Pages (renatopenner.github.io/site-renato-penner)
pennertech.com.br/         ->  portal provisório (raiz reservada para os serviços futuros)
www.pennertech.com.br      ->  301 para pennertech.com.br
```

Canonical, Open Graph, JSON-LD e `sitemap.xml` do site **já apontam** para
`https://pennertech.com.br/loja/...` (commit `ff52d79`). Falta só ligar o domínio.

> **Por que não dá só no GitHub Pages?** O Pages de projeto publica em
> `renatopenner.github.io/site-renato-penner/`; com domínio próprio ele iria para a **raiz**
> (`pennertech.com.br/`), não para `/loja`. Para manter a raiz livre para os serviços, o caminho
> é um roteador na borda — a opção recomendada é o Cloudflare Worker abaixo (grátis, TLS e CDN
> inclusos, sem servidor para manter).

---

## Caminho recomendado — Cloudflare (grátis)

### 1. Registrar o domínio

No Registro.br, com o domínio ativo e pago.

### 2. Colocar o domínio no Cloudflare

1. Crie a conta em <https://dash.cloudflare.com/sign-up> (plano Free).
2. **Add a site** → `pennertech.com.br` → plano Free.
3. O Cloudflare mostra **dois nameservers** (ex.: `ana.ns.cloudflare.com` e `bob.ns.cloudflare.com`).

### 3. Trocar os nameservers no Registro.br

Painel do Registro.br → domínio → **DNS** → *Utilizar outros servidores DNS* → informe os dois
nameservers do Cloudflare → salvar. Propagação costuma levar de minutos a algumas horas
(consulte com `nslookup -type=NS pennertech.com.br`).

### 4. Criar os registros DNS no Cloudflare

Na aba **DNS → Records** (o proxy laranja deve ficar **ligado** nos dois):

| Tipo | Nome | Conteúdo | Proxy |
|---|---|---|---|
| A | `@` | `192.0.2.1` | Proxied (laranja) |
| CNAME | `www` | `pennertech.com.br` | Proxied (laranja) |

O `192.0.2.1` é só um endereço de preenchimento: quem responde em `pennertech.com.br/*` é o
Worker. (Quando um serviço real assumir a raiz, troque esse registro pelo destino dele.)

### 5. Publicar o Worker

**Pelo painel (mais simples):**

1. **Workers & Pages → Create → Worker** → dê o nome `pennertech-router` → **Deploy**.
2. **Edit code** → apague o exemplo, cole todo o conteúdo de
   [`deploy/pennertech/worker.js`](./worker.js) → **Deploy**.
3. Volte para o Worker → **Settings → Triggers → Add route**, com a zona
   `pennertech.com.br`:
   - `pennertech.com.br/*`
   - `www.pennertech.com.br/*`

**Por linha de comando (opcional):**

```bash
cd deploy/pennertech
npx wrangler login
npx wrangler deploy          # usa o wrangler.toml desta pasta
```

### 6. SSL/TLS

- **SSL/TLS → Overview**: modo **Full (strict)**.
- **SSL/TLS → Edge Certificates**: **Always Use HTTPS** ligado.

### 7. Conferir

```powershell
curl.exe -sI https://pennertech.com.br/loja/                        # 200 (HTML da home)
curl.exe -sI https://pennertech.com.br/loja/p/patinete-eletrico-gm5.html  # 200
curl.exe -sI https://pennertech.com.br/loja/img/patinete-gm5-p1.jpg       # 200 (image/jpeg)
curl.exe -s  https://pennertech.com.br/loja/ | Select-String canonical    # https://pennertech.com.br/loja/
curl.exe -sI https://www.pennertech.com.br/loja/                    # 301 -> apex
curl.exe -sI https://pennertech.com.br/                             # 200 (portal provisório)
```

### 8. Google Search Console

1. Adicionar propriedade `pennertech.com.br` (verificação por DNS TXT no Cloudflare).
2. **Sitemaps** → enviar `https://pennertech.com.br/loja/sitemap.xml`.
3. As páginas antigas em `renatopenner.github.io/site-renato-penner/` continuam no ar como origem;
   o canonical já aponta para o domínio novo, então o Google consolida sozinho.

### 9. Quando os serviços da raiz entrarem

A raiz hoje é o portal provisório do Worker. Para colocar um serviço de verdade:

- **Cloudflare Tunnel** (recomendado para o pennerserver, sem abrir porta no roteador):
  Tunnel → Public Hostname `pennertech.com.br` → serviço local; **e troque a rota
  `pennertech.com.br/*` do Worker por `pennertech.com.br/loja*`** (senão o Worker continua
  interceptando a raiz). O `/loja` não muda.
- **Subdomínios** (`crm.pennertech.com.br`, `storage.pennertech.com.br`, ...): crie cada um como
  hostname do Tunnel/registro próprio; o Worker atual não os afeta.

---

## Alternativa A — GitHub Pages nativo (sem Cloudflare)

Dá o mesmo `pennertech.com.br/loja`, mas a **raiz passa a ser uma página estática do GitHub**
(serviços futuros ficariam em subdomínios). Passos:

1. Criar o repositório `renatopenner.github.io` (site de usuário) com `CNAME` contendo
   `pennertech.com.br` e uma `index.html` (portal da raiz). Ligar Pages nele.
2. **Renomear** o repositório `site-renato-penner` para `loja` — com domínio próprio no site de
   usuário, o Pages de projeto passa a ser servido em `pennertech.com.br/loja/`.
   (Guarde um repo `site-renato-penner` com uma página de redirect para não quebrar links antigos.)
3. DNS no Registro.br (ou Cloudflare em modo DNS only):
   - `A @ 185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - `CNAME www renatopenner.github.io`
4. Marcar **Enforce HTTPS** no repositório do site de usuário.

Limitação: a raiz fica presa ao GitHub Pages (nada de app dinâmico na raiz).

## Alternativa B — HostGator (arquivos estáticos)

Publicar os arquivos em `public_html/loja/` da hospedagem e apontar o DNS para a HostGator.
Funciona, mas **quebra o fluxo atual** (hoje é só `git push`; passaria a exigir deploy FTP/SFTP
a cada atualização de preço) — só vale a pena se você quiser PHP/banco na raiz.

---

## O que NÃO fazer

- **Não** adicionar arquivo `CNAME` no repo `site-renato-penner`: ele passaria a reivindicar a
  raiz do domínio e brigaria com os serviços futuros.
- **Não** apontar o apex direto para `renatopenner.github.io` sem o site de usuário configurado
  (o resultado seria 404 na raiz e caminhos errados).
- **Não** remover o Worker/rota enquanto a raiz não tiver outro destino — sem ele,
  `pennertech.com.br/loja` deixa de responder.
