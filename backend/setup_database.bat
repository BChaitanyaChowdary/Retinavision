@echo off
echo.
echo ========================================
echo  Setting up PostgreSQL Database
echo ========================================
echo.

REM Check if .env exists
if not exist ".env" (
    echo ERROR: .env file not found!
    echo Please create a .env file with your credentials.
    echo See .env.example for template.
    pause
    exit /b 1
)

echo.
echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Initializing database tables...
python init_database.py

echo.
echo ========================================
echo  Database setup complete!
echo ========================================
echo.
echo Next steps:
echo   1. Update your app.py to use database functions
echo   2. Run your Flask application
echo   3. Test the API endpoints
echo.
echo See DATABASE_INTEGRATION.md for detailed instructions
echo.
pause
