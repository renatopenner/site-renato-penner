# Proteção de produtos — Penner Tech

**Regra:** nenhum produto pode ser excluído do site. Página, card, catálogo, sitemap e imagem
de cada produto ficam travados por um guardião que **restaura** o que faltar.

## Por que isso existe (incidente real)

Em **05/11/2026** o produto *Patinete Elétrico GM5 P1* (o mesmo deste pedido) foi adicionado
com o link `https://meli.la/2tLEqgs`. No mesmo dia, o script `adiciona_patinete_350w.py`
sobrescreveu:

- `p/patinete-eletrico-gm5.html` → virou uma cópia da página do patinete 350W;
- `img/patinete-gm5-p1.png` → virou a foto do outro patinete;
- o card do GM5 em `index.html`, `auto.html` e `promocoes.html` → foi trocado pelo card do 350W;
- a entrada em `dados/produtos.json` → ficou apontando para o link do 350W (`meli.la/1zdtX1P`).

Resultado: o produto continuou existindo no repositório, mas **invisível na navegação** e
com página errada — exatamente o sintoma de "produto excluído do site".

## Como funciona

1. `dados/produtos_protegidos.json` (manifesto) lista cada produto publicado com: slug, título,
   link de afiliado, página, imagem, URL no sitemap e em quais páginas há card (`index.html`,
   página da categoria, `promocoes.html`), além de `fixado` (trava de hash da imagem).
2. `dados/produtos_backup/` guarda uma cópia do último estado saudável: páginas, cards,
   catálogo e (só nos produtos fixados) a imagem.
3. `scripts/protege_produtos.py` verifica os 5 pontos de cada produto e restaura o que faltar:

   | tratamento | verifica |
   |---|---|
   | `pagina_ausente` / `pagina_link_divergente` | `p/<slug>.html` existe e contém o link de afiliado |
   | `catalogo_ausente` / `catalogo_link_divergente` | entrada em `dados/produtos.json` com o mesmo link |
   | `card_ausente` | `<article class="card">` dentro do `<div class="grid">` de cada página |
   | `sitemap_ausente` | `<url><loc>…/p/<slug>.html</loc></url>` |
   | `imagem_ausente` / `imagem_trocada` | arquivo em `img/` (hash conferido nos `fixado`) |

4. **Três camadas de garantia:**
   - **motor de preços** (`scripts/motor_precos.py`, todo dia 08:00): restaura antes de mexer,
     revalida depois e **aborta o push** se algo protegido continuar faltando;
   - **hook pre-commit** (`.githooks/pre-commit`): bloqueia qualquer commit que remova/corrompa
     produto protegido, inclusive os feitos por outro agente;
   - **GitHub Actions** (opcional): o robô que confere o repositório remoto depois de cada push e
     restaura sozinho está pronto em `scripts/protecao-produtos.workflow.yml` — falta só copiar
     para `.github/workflows/` (veja "Ativar o robô do GitHub" abaixo).

## Comandos

```powershell
cd C:\Users\renat\SitesGithub\site-renato-penner
python scripts\protege_produtos.py --verificar    # relatório (código 1 = tem problema)
python scripts\protege_produtos.py --restaurar    # conserta o que faltar
python scripts\protege_produtos.py --gerar        # registra páginas novas de p/*.html
python scripts\protege_produtos.py --backup       # refaz o backup do estado saudável
python scripts\protege_produtos.py --rotina       # restaurar + gerar + backup + conferir
python scripts\protege_produtos.py --atualizar SLUG   # aceita o estado atual como novo padrão
python scripts\protege_produtos.py --refixar SLUG     # refaz a trava/hash da imagem
```

## Produto novo (fluxo obrigatório)

1. Página `p/<slug>.html` copiada de outra página-modelo (com ld+json `Product`).
2. Imagem JPEG ~120–200 KB em `img/<slug>.jpg` (ou PNG só com transparência/arte chapada).
3. Card em `index.html`, na página da categoria e em `promocoes.html` (se houver desconto),
   dentro do `<div class="grid">`, copiando o markup do card vizinho.
4. Entrada em `dados/produtos.json` (link de afiliado, preços, data).
5. `<url>` no `sitemap.xml`.
6. `python scripts\protege_produtos.py --rotina` → registra no manifesto e no backup.
7. Commit + push (o hook pre-commit confere antes).

## Ativar o robô do GitHub (opcional, recomendado)

O token que está no `origin` deste repositório **não tem o escopo `workflow`**, então o GitHub
recusa o push de arquivos dentro de `.github/workflows/`. O robô está pronto, só não pode ser
ligado por esse token. Duas formas de ativar:

1. **Pelo navegador (mais simples):** no GitHub, *Add file → Create new file*, caminho
   `.github/workflows/protecao-produtos.yml`, cole o conteúdo de
   `scripts/protecao-produtos.workflow.yml` e commite.
2. **Por linha de comando:** gere um token com escopo `workflow` (classic: `workflow`;
   fine-grained: *Workflows: Read and write*), atualize o remote e então:

   ```powershell
   New-Item -ItemType Directory .github\workflows -Force
   Copy-Item scripts\protecao-produtos.workflow.yml .github\workflows\protecao-produtos.yml
   git add .github ; git commit -m "Ativa robo de protecao de produtos" ; git push
   ```

Enquanto o robô não estiver ligado, a proteção continua valendo pelas outras duas camadas:
o motor diário (08:00) restaura e republica, e o hook pre-commit bloqueia remoções.

## Remover um produto de propósito (manutenção)

Exclusão é decisão consciente e exige três passos:

1. apagar a página, os cards, a entrada do catálogo e o `<url>` do sitemap;
2. remover o produto de `dados/produtos_protegidos.json` **e** de `dados/produtos_backup/`
   (`paginas/`, `cartoes/`, `img/`);
3. commitar com a trava liberada: `PROTECAO_PERMITIR_EXCLUSAO=1 git commit ...`.

Sem isso, o guardião (e o robô do GitHub) recoloca o produto no ar — que é o comportamento
desejado: **produto descontinuado se oculta/desativa, não se apaga**.

## Clones

Existem dois clones locais do repositório:

- `C:\Users\renat\SitesGithub\site-renato-penner` (usado pela tarefa diária de preços);
- `C:\Users\renat\site-renato-penner` (clone secundário).

Edite e publique em **um** clone, rode `git pull --rebase` no outro antes de mexer nele.
Nunca use `git clean -fd` ou `git reset --hard` com produto novo ainda não commitado —
foi assim que arquivos do patinete 350W foram apagados em 05/11/2026.
Depois de clonar, rode **uma vez** em cada clone:

```powershell
git config core.hooksPath .githooks
powershell -ExecutionPolicy Bypass -File scripts\instalar_protecao.ps1
```
