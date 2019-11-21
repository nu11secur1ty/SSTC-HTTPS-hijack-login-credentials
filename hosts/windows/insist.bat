@echo off

set hostspath=%windir%\System32\drivers\etc\hosts

echo 127.0.0.1           facesbook.com >> %hostspath%
echo 127.0.0.1           www.facesbook.com >> %hostspath%
exit
