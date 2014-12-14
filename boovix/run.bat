@echo ON
set PATH=C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Python34;C:\Python34\Scripts;

call static_analysis/static_analysis.bat
@if %ERRORLEVEL% neq 0 (
    set error_message="Static analysis returned error code: %ERRORLEVEL%"
    goto ERROR
)

python main.py
@goto EOF

:ERROR
@echo ----------------------------------ERROR----------------------------------
@echo %error_message%
@echo -------------------------------------------------------------------------
@goto EOF

:EOF
@cd %~dp0
