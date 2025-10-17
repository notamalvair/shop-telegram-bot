@echo off
echo ========================================
echo      Telegram Shop Bot - Автозапуск
echo ========================================
echo.

echo [1/4] Проверка Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python не найден! Установите Python с https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [2/4] Установка зависимостей...
pip install -r requirements.txt >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Ошибка установки зависимостей!
    pause
    exit /b 1
)

echo [3/4] Проверка конфигурации...
if not exist "src\config.txt" (
    if exist "src\config.example.txt" (
        copy "src\config.example.txt" "src\config.txt" >nul
        echo ⚠️  Создан файл src\config.txt
        echo 📝 НАСТРОЙТЕ КОНФИГУРАЦИЮ:
        echo    - Откройте src\config.txt
        echo    - Вставьте токен бота (получите у @BotFather)
        echo    - Вставьте ваш ID администратора (получите у @userinfobot)
        echo.
        pause
        exit /b 0
    ) else (
        echo ❌ Файл конфигурации не найден!
        pause
        exit /b 1
    )
)

echo [4/4] Запуск бота...
cd src
python main.py

echo.
echo Бот остановлен.
pause