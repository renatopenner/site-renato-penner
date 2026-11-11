# Instala a proteção de produtos neste clone do site
# Uso:  powershell -ExecutionPolicy Bypass -File scripts\instalar_protecao.ps1
$ErrorActionPreference = 'Stop'
$repo = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$py = 'C:\Users\renat\AppData\Local\Programs\Python\Python314\python.exe'
if (-not (Test-Path $py)) { $py = (Get-Command python).Source }

Write-Host "Clone: $repo"
git -C $repo config core.hooksPath .githooks
Write-Host "Hook pre-commit ativado (core.hooksPath = .githooks)."

& $py (Join-Path $repo 'scripts\protege_produtos.py') --gerar
& $py (Join-Path $repo 'scripts\protege_produtos.py') --backup
& $py (Join-Path $repo 'scripts\protege_produtos.py') --verificar
if ($LASTEXITCODE -ne 0) { throw "Verificacao da protecao falhou." }
Write-Host "Protecao de produtos instalada e verificada."
