@echo off
echo ========================================
echo      Запуск Telegram Shop Bot
echo ========================================
echo.

if not exist config.txt (
    echo ОШИБКА: Файл config.txt не найден!
    echo Сначала запустите install.bat
    pause
    exit /b 1
)

if not exist "src\backups" mkdir "src\backups"

echo Запуск бота...
cd src
python main.py

echo.
echo Бот остановлен.
pause