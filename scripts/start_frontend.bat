@echo off
cd /d "%~dp0..\\frontend"
if not exist "node_modules" (
    echo Installing dependencies...
    npm install
)
echo Starting OpenFDAMS Frontend on http://localhost:5173
npm run dev
pause
