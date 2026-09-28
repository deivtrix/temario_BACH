@echo off
title CONTROL DE GITHUB - DAVID C
:MENU
cls
echo ====================================================
echo           ASISTENTE GITHUB - DAVID C
echo ====================================================
echo.

git status -s > %temp%\git_st.txt 2>nul
set "git_changes="
for /f "tokens=*" %%a in (%temp%\git_st.txt) do set "git_changes=%%a"

if defined git_changes (
    echo   ESTADO: [ ! CAMBIOS PENDIENTES / MODIFICADO ! ]
) else (
    echo   ESTADO: [  ACTUALIZADO / SIN CAMBIOS PENDIENTES  ]
)

echo.
echo ====================================================
echo.
echo   [1] SUBIR cambios a GitHub (Compu Personal / Casa)
echo   [2] DESCARGAR cambios de GitHub (Compu Colegio)
echo   [3] SALIR
echo.
echo ====================================================
set /p opcion=Selecciona una opcion (1, 2 o 3) y presiona ENTER: 

if "%opcion%"=="1" goto SUBIR
if "%opcion%"=="2" goto DESCARGAR
if "%opcion%"=="3" goto SALIR

echo.
echo Opcion invalida. Intenta de nuevo...
timeout /t 2 >nul
goto MENU

:SUBIR
cls
echo ====================================================
echo     SUBIENDO CAMBIOS A GITHUB...
echo ====================================================
echo.
git config user.name "David C"
git config user.email "davidc@example.com"
git add -A
git commit -m "Actualizacion automatica de clases"
git push origin main
echo.
echo ====================================================
echo   !EXITO! Todos los cambios han sido subidos.
echo ====================================================
pause
goto MENU

:DESCARGAR
cls
echo ====================================================
echo     DESCARGANDO CAMBIOS DE GITHUB...
echo ====================================================
echo.
git pull origin main
echo.
echo ====================================================
echo   !EXITO! Tu carpeta esta 100%% actualizada.
echo ====================================================
pause
goto MENU

:SALIR
exit
