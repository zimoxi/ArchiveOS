@echo off
echo Starting OpenFDAMS Development Environment...
echo.
start "OpenFDAMS Backend" cmd /c "cd /d %~dp0 && call start_backend.bat"
timeout /t 3 /nobreak >nul
start "OpenFDAMS Frontend" cmd /c "cd /d %~dp0 && call start_frontend.bat"
echo.
echo Both services started:
echo   Backend:  http://127.0.0.1:8000
echo   Frontend: http://localhost:5173
