@echo off
title Atualizar Precos — Penner Tech
cd /d "%~dp0.."
python "%~dp0motor_precos.py"
echo.
echo ========================================================
echo Atualizacao concluida! Pressione qualquer tecla para sair...
echo ========================================================
pause >nul
