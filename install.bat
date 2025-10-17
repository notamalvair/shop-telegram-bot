@echo off
echo ========================================
echo    Установка Telegram Shop Bot
echo ========================================
echo.

echo [1/4] Проверка Python...
python --version
if %errorlevel% neq 0 (
    echo ОШИБКА: Python не найден!
    echo Скачайте Python с https://www.python.org/downloads/
    pause
    exit /b 1
)

echo.
echo [2/4] Установка зависимостей...
echo Попытка 1: Минимальные зависимости...
pip install -r requirements-minimal.txt
if %errorlevel% neq 0 (
    echo Попытка 2: Полные зависимости...
    pip install -r requirements-windows.txt
    if %errorlevel% neq 0 (
        echo Попытка 3: Только основные библиотеки...
        pip install aiogram==2.25.2 phonenumbers
        if %errorlevel% neq 0 (
            echo ОШИБКА: Не удалось установить зависимости!
            echo Попробуйте установить вручную: pip install aiogram phonenumbers
            pause
            exit /b 1
        )
    )
)

echo.
echo [3/4] Создание конфигурации...
if not exist config.txt (
    copy config.example.txt config.txt
    echo Создан файл config.txt
) else (
    echo Файл config.txt уже существует
)

echo.
echo [4/4] Создание необходимых папок...
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
echo Подробные инструкции: LOCAL_SETUP.md
echo.
pause