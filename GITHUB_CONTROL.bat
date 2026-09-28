@echo off
title CONTROL DE GITHUB Y CLASES - DAVID C
:MENU
cls
echo ====================================================
echo           ASISTENTE DOCENTE - DAVID C
echo ====================================================
echo.
echo   [1] SUBIR cambios a GitHub (Compu Personal / Casa)
echo   [2] DESCARGAR cambios de GitHub (Compu Colegio)
echo   [3] VER ESTADO / Archivos modificados o pendientes
echo   [4] ABRIR PLANIFICACION DE LA SEMANA ACTUAL
echo   [5] SALIR
echo.
echo ====================================================
set /p opcion=Selecciona una opcion (1 a 5) y presiona ENTER: 

if "%opcion%"=="1" goto SUBIR
if "%opcion%"=="2" goto DESCARGAR
if "%opcion%"=="3" goto ESTADO
if "%opcion%"=="4" goto ABRIR_PLAN
if "%opcion%"=="5" goto SALIR

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

:ESTADO
cls
echo ====================================================
echo     ESTADO ACTUAL DEL REPOSITORIO (GIT STATUS)
echo ====================================================
echo.
git status
echo.
echo ====================================================
pause
goto MENU

:ABRIR_PLAN
cls
echo ====================================================
echo     ABRIENDO PLANIFICACION DE LA SEMANA 2
echo ====================================================
echo.
start "" "03_PLANIFICACION_SEMANAL\SEMANA_02\README_INDICE.md"
echo Planificacion abierta en tu editor predeterminado.
timeout /t 2 >nul
goto MENU

:SALIR
exit
