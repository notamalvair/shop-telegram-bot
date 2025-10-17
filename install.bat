@echo off
echo ========================================
echo    Установка Telegram Shop Bot
echo ========================================
echo.

echo [1/3] Проверка Python...
python --version
if %errorlevel% neq 0 (
    echo ОШИБКА: Python не найден!
    echo Скачайте Python с https://www.python.org/downloads/
    pause
    exit /b 1
)

echo.
echo [2/3] Установка зависимостей...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ОШИБКА: Не удалось установить зависимости!
    echo Попробуйте: pip install aiogram phonenumbers
    pause
    exit /b 1
)

echo.
echo [3/3] Создание конфигурации...
if not exist config.txt (
    copy config.example.txt config.txt
    echo Файл config.txt создан
) else (
    echo Файл config.txt уже существует
)

if not exist "src\backups" mkdir "src\backups"
echo Папка backups создана

echo.
echo ========================================
echo        Установка завершена!
echo ========================================
echo.
echo СЛЕДУЮЩИЕ ШАГИ:
echo 1. Откройте config.txt и заполните:
echo    - BOT_TOKEN (получите у @BotFather)
echo    - ADMIN_ID (получите у @userinfobot)
echo.
echo 2. Запустите бота командой:
echo    cd src
echo    python main.py
echo.
pause