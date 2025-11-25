@echo off
echo ================================================
echo   Eye Disease Classification System
echo   Starting Full Stack Application
echo ================================================
echo.

REM Check if virtual environment exists
if not exist "backend\venv" (
    echo [1/5] Creating Python virtual environment...
    cd backend
    python -m venv venv
    cd ..
    echo Virtual environment created!
    echo.
) else (
    echo [1/5] Virtual environment already exists
    echo.
)

REM Install backend dependencies
echo [2/5] Installing backend dependencies...
cd backend
call venv\Scripts\activate
pip install -r requirements.txt --quiet
cd ..
echo Backend dependencies installed!
echo.

REM Install frontend dependencies
if not exist "frontend\node_modules" (
    echo [3/5] Installing frontend dependencies...
    cd frontend
    call npm install
    cd ..
    echo Frontend dependencies installed!
    echo.
) else (
    echo [3/5] Frontend dependencies already installed
    echo.
)

REM Start backend
echo [4/5] Starting Flask Backend...
start "Flask Backend" cmd /k "cd backend && venv\Scripts\activate && python app.py"
timeout /t 5 /nobreak > nul
echo Backend started on http://localhost:5000
echo.

REM Start frontend
echo [5/5] Starting React Frontend...
start "React Frontend" cmd /k "cd frontend && npm start"
echo Frontend starting on http://localhost:3000
echo.

echo ================================================
echo   Application Started Successfully!
echo ================================================
echo.
echo Backend:  http://localhost:5000
echo Frontend: http://localhost:3000
echo.
echo Press any key to close this window...
echo (Backend and Frontend will continue running)
pause > nul
