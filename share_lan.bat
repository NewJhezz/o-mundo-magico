@echo off
echo ==========================================
echo      COMPARTILHAMENTO DE VARINHAS (LAN)
echo ==========================================
echo.
echo Obtendo seu endereco IP local...
ipconfig | findstr "IPv4"
echo.
echo ------------------------------------------
echo AGORA EM SEU CELULAR (Mesma Wi-Fi):
echo Digite o endereco IP acima que comece com 192.168...
echo seguido de :8000
echo Exemplo: 192.168.0.15:8000
echo ------------------------------------------
echo.
echo Pressione Ctrl+C para encerrar o site.
echo.
py -m http.server 8000 --bind 0.0.0.0 || python -m http.server 8000 --bind 0.0.0.0
pause
