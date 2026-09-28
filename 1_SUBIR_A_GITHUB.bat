@echo off
echo ====================================================
echo     SUBIR CAMBIOS A GITHUB (COMPU PERSONAL/CASA)
echo ====================================================
echo.

echo 1. Configurando usuario David C...
git config user.name "David C"
git config user.email "davidc@example.com"

echo.
echo 2. Agregando archivos modificados...
git add -A

echo.
echo 3. Guardando cambios (Commit)...
git commit -m "Actualizacion automatica de clases - %date% %time%"

echo.
echo 4. Subiendo a GitHub (Push)...
git push origin main

echo.
echo ====================================================
echo   !LISTO! Cambios subidos exitosamente a GitHub.
echo ====================================================
pause
