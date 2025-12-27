@echo off
echo ==========================================
echo      MODO DE DIAGNOSTICO MAGIC
echo ==========================================

echo.
echo 1. Verificando Python...
py --version || python --version

echo.
echo 2. Instalando requisitos (verbose)...
py -m pip install -r requirements.txt || python -m pip install -r requirements.txt

echo.
echo 3. Tentando gerar o site...
echo ------------------------------------------
py build.py
if %errorlevel% neq 0 (
    echo.
    echo ------------------------------------------
    echo [ERRO FATAL] O "runas" falhou. 
    echo LEIA O ERRO ACIMA.
    echo ------------------------------------------
     python build.py
) else (
    echo.
    echo [SUCESSO] Site gerado sem erros!
)

echo.
echo Pressione qualquer tecla para fechar...
pause
