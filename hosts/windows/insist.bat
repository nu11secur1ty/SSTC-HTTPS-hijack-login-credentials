@echo off

SET NEWLINE=^& echo.

FIND /C /I "ns1.intranet.de" %WINDIR%\system32\drivers\etc\hosts
IF %ERRORLEVEL% NEQ 0 ECHO %NEWLINE%^0.0.0.0 ns1.intranet.de>>%WINDIR%\System32\drivers\etc\hosts


