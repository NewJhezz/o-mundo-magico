@echo off
echo ==========================================
echo      Tentando encontrar a Magia (Python)...
echo ==========================================

:: Tenta usar o comando 'py' (Launcher) que geralmente funciona melhor no Windows
py --version >nul 2>&1
if %errorlevel% equ 0 (
    echo Python encontrado! (Usando comando 'py')
    
    echo.
    echo Instalando Flask...
    py -m pip install -r requirements.txt
    
    echo.
    echo Gerando o site...
    py build.py
    
    goto :success
)

:: Se falhar, tenta o comando 'python' normal
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo Python encontrado! (Usando comando 'python')
    
    echo.
    echo Instalando Flask...
    python -m pip install -r requirements.txt
    
    echo.
    echo Gerando o site...
    python build.py
    
    goto :success
)

:: Se chegar aqui, não achou nada
echo.
echo [ERRO CRITICO] O Python nao foi detectado corretamente.
echo Voce precisa reinstalar o Python e marcar a caixinha:
echo "Add Python to PATH" (Adicionar Python ao PATH) no inicio da instalacao.

goto :end

:success
echo.
echo ==========================================
echo      SUCESSO! Site gerado.
echo ==========================================

:end
echo.
echo Pressione qualquer tecla para sair...
pause
