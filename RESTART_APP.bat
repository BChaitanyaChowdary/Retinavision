@echo off
echo.
echo ========================================
echo  Restarting Eye Disease Classification
echo ========================================
echo.

echo Stopping any running processes...
taskkill /F /IM python.exe /T 2>nul
taskkill /F /IM node.exe /T 2>nul

echo.
echo Starting Backend...
cd backend
start "Backend Server" cmd /k "python app.py"

timeout /t 3 /nobreak >nul

echo.
echo Starting Frontend...
cd ../frontend
start "Frontend Server" cmd /k "npm start"

echo.
echo ========================================
echo  Application Started!
echo ========================================
echo.
echo Backend: http://localhost:5000
echo Frontend: http://localhost:3000
echo.
echo Press any key to exit this window...
pause >nul
