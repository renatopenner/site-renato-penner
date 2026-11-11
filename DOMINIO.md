# Domínio — pennertech.com.br

**Decisão (11/11/2026):**

```
https://loja.pennertech.com.br/               -> loja (este repositório, GitHub Pages)
https://loja.pennertech.com.br/p/<slug>.html  -> páginas de produto
https://pennertech.com.br/                    -> redireciona para a loja (por enquanto)
```

A raiz fica com um redirecionamento **provisório** para a loja. Quando os serviços existirem, troca-se
só o apontamento da raiz — a loja no subdomínio não é afetada.

Canonical, Open Graph, JSON-LD, `sitemap.xml` e `robots.txt` já apontam para
`https://loja.pennertech.com.br/...` (commit de migração de 11/11/2026).

## Como está montado

| Peça | Onde | O que faz |
|---|---|---|
| Loja | repo `site-renato-penner` + Pages custom domain `loja.pennertech.com.br` | serve o site |
| Raiz | repo `renatopenner.github.io` (site de usuário) + Pages custom domain `pennertech.com.br` | página de redirect instantâneo para a loja |
| DNS | Registro.br (`a.auto.dns.br` / `b.auto.dns.br`) | CNAME da loja + A da raiz |

## Registros DNS no Registro.br

Painel → `pennertech.com.br` → **DNS** → *Configurar endereçamento* → **Modo Avançado** →
**Configurar Zona DNS** → *Nova entrada*:

| Tipo | Nome | Nome do servidor / Valor | TTL |
|---|---|---|---|
| **CNAME** | `loja` | `renatopenner.github.io` | 3600 |
| **A** | *(em branco — raiz)* | `185.199.108.153` | 3600 |
| **A** | *(em branco)* | `185.199.109.153` | 3600 |
| **A** | *(em branco)* | `185.199.110.153` | 3600 |
| **A** | *(em branco)* | `185.199.111.153` | 3600 |
| CNAME *(opcional)* | `www` | `renatopenner.github.io` | 3600 |

Conferir (use um resolvedor público; o DNS corporativo do Banpará cacheia):

```powershell
Resolve-DnsName loja.pennertech.com.br -Type CNAME -Server 8.8.8.8   # renatopenner.github.io
Resolve-DnsName pennertech.com.br -Type A -Server 8.8.8.8            # os 4 IPs do GitHub
```

## Ordem de ativação (importante)

1. DNS adicionado e propagado (os dois comandos acima respondem).
2. Ligar o **custom domain da raiz** (`pennertech.com.br` no repo `renatopenner.github.io`).
3. Ligar o **custom domain da loja** (`loja.pennertech.com.br` no repo `site-renato-penner`).
4. Aguardar os certificados e marcar **Enforce HTTPS** nos dois.

> **Nunca ligue o custom domain da raiz antes do DNS responder.** Quando `pennertech.com.br` é
> configurado no site de usuário, o GitHub passa a redirecionar
> `renatopenner.github.io/site-renato-penner` para `pennertech.com.br/site-renato-penner`. Se o DNS
> ainda não resolver, a loja fica fora do ar nesse intervalo. Foi por isso que o domínio da raiz foi
> temporariamente desligado em 11/11/2026 enquanto os registros não existiam.

## Quando os serviços chegarem

A raiz hoje é o redirect. Para colocar um serviço de verdade:

- **Cloudflare Tunnel** no pennerserver (sem abrir porta no roteador): aponte `pennertech.com.br`
  para o tunnel e remova o custom domain da raiz do repo `renatopenner.github.io` (ou mantenha o
  repo só como redirect de *fallback*). A loja em `loja.pennertech.com.br` **não é afetada**.
- **Subdomínios** (`crm.pennertech.com.br`, `storage.pennertech.com.br`, ...): cada um é um registro
  próprio; nada na loja muda.

## Google Search Console

1. Propriedade `loja.pennertech.com.br` (prefixo de URL).
2. Enviar `https://loja.pennertech.com.br/sitemap.xml`.
3. O canonical já aponta para o subdomínio; depois da ativação, o `github.io` redireciona para cá.

## O que NÃO fazer

- Não ligar custom domain antes do DNS (ver aviso acima).
- Não criar registro `A` para `loja` (o CNAME cobre).
- Não usar o `CNAME` do repo da loja para a raiz: são sites diferentes de propósito.
