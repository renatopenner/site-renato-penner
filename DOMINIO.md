# Domínio — loja.pennertech.com.br

**Decisão (11/11/2026):** a loja fica no subdomínio `loja.pennertech.com.br`; `pennertech.com.br`
(raiz) fica **inteiro** para os serviços futuros. Nada de proxy nem de Worker: o GitHub Pages serve
a loja direto, com CDN, TLS e cache dele.

```
https://loja.pennertech.com.br/              -> loja (este repositório)
https://loja.pennertech.com.br/p/<slug>.html -> páginas de produto
https://pennertech.com.br/                   -> livre para os serviços futuros
```

Canonical, Open Graph, JSON-LD, `sitemap.xml` e `robots.txt` já apontam para
`https://loja.pennertech.com.br/...` (commit de migração de 11/11/2026).

## O que falta (2 passos)

### 1. DNS no Registro.br

No painel do domínio → **DNS** → *Adicionar registro*:

| Tipo | Nome | Valor | TTL |
|---|---|---|---|
| **CNAME** | `loja` | `renatopenner.github.io` | padrão (3600) |

- **Não** crie registro `A` para `loja` (o CNAME já resolve).
- **Não** mexa na raiz (`@`): ela fica sem registro até você decidir o serviço dela. Sem A/CNAME na
  raiz, `pennertech.com.br` simplesmente não responde — e a loja continua funcionando no subdomínio.

Conferir a propagação:

```powershell
nslookup -type=CNAME loja.pennertech.com.br
# deve responder algo como: loja.pennertech.com.br canonical name = renatopenner.github.io
```

### 2. Ligar o domínio no GitHub (depois que o DNS responder)

Repo → **Settings → Pages → Custom domain**: digite `loja.pennertech.com.br` → **Save**.
Isso cria o arquivo `CNAME` no repositório. Aguarde a emissão do certificado (1–15 min) e marque
**Enforce HTTPS**.

> **Por que o `CNAME` ainda não está no repositório:** quando o `CNAME` entra no repo, o GitHub
> passa a redirecionar `renatopenner.github.io/site-renato-penner` para o domínio novo. Se o DNS
> ainda não estiver propagado, a loja fica fora do ar nesse intervalo. Então a ordem é: DNS → testar
> → só então ligar o domínio no GitHub (ou eu ligo para você quando confirmar a propagação).

## Conferência final

```powershell
curl.exe -sI https://loja.pennertech.com.br/                                  # 200 html
curl.exe -sI https://loja.pennertech.com.br/p/bicicleta-eletrica-cavalletta-c12.html  # 200
curl.exe -sI https://loja.pennertech.com.br/img/bicicleta-eletrica-cavalletta-c12.jpg # 200 imagem
curl.exe -s  https://loja.pennertech.com.br/ | Select-String 'rel="canonical"'       # loja.pennertech.com.br/
curl.exe -sI https://renatopenner.github.io/site-renato-penner/                # 301 -> domínio novo
```

## Depois: serviços na raiz

A raiz está livre. Quando for publicar um serviço:

- **Cloudflare Tunnel no pennerserver** (sem abrir porta no roteador): aponte `pennertech.com.br`
  para o tunnel; a loja no subdomínio **não é afetada**.
- **Subdomínios de serviços** (`crm.pennertech.com.br`, `storage.pennertech.com.br`, ...): cada um
  é um registro próprio; a loja continua independente.
- **Página institucional na raiz**: pode ser um GitHub Pages de usuário (`renatopenner.github.io`
  com `CNAME pennertech.com.br`) — mas aí a raiz fica estática; apps continuam em subdomínios.

## Google Search Console

1. Adicionar propriedade `loja.pennertech.com.br` (prefixo de URL; verificação por TXT no DNS).
2. **Sitemaps** → enviar `https://loja.pennertech.com.br/sitemap.xml`.
3. O canonical já aponta para o subdomínio, então a migração de indexação é automática — o
   `github.io/site-renato-penner` redireciona para cá depois do passo 2.

## O que NÃO fazer

- Não criar `CNAME` no repo antes do DNS responder (ver aviso acima).
- Não criar registro `A` ou `AAAA` em `loja` (CNAME cobre).
- Não usar o mesmo `CNAME` do repo para a raiz: a raiz precisa ficar livre.
