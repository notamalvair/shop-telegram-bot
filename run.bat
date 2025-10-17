@echo off
chcp 65001 >nul
echo ========================================
echo      Telegram Shop Bot - Autostart
echo ========================================
echo.

echo [1/4] Checking Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo X Python not found! Install Python from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [2/4] Installing dependencies...
pip install -r requirements.txt >nul 2>&1
if %errorlevel% neq 0 (
    echo X Error installing dependencies!
    pause
    exit /b 1
)

echo [3/4] Checking configuration...
if not exist "src\config.txt" (
    if exist "src\config.example.txt" (
        copy "src\config.example.txt" "src\config.txt" >nul
        echo ! Created file src\config.txt
        echo CONFIGURE THE BOT:
        echo    - Open src\config.txt
        echo    - Insert bot token (get from @BotFather)
        echo    - Insert your admin ID (get from @userinfobot)
        echo.
        pause
        exit /b 0
    ) else (
        echo X Configuration file not found!
        pause
        exit /b 1
    )
)

echo [4/4] Starting bot...
cd src
python main.py

echo.
echo Bot stopped.
pause