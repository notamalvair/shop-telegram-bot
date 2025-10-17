#!/bin/bash

echo "========================================"
echo "    Установка Telegram Shop Bot"
echo "========================================"
echo

echo "[1/4] Проверка Python..."
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo "ОШИБКА: Python не найден!"
        echo "Установите Python с https://www.python.org/downloads/"
        exit 1
    else
        PYTHON_CMD="python"
    fi
else
    PYTHON_CMD="python3"
fi

$PYTHON_CMD --version

echo
echo "[2/4] Установка зависимостей..."
$PYTHON_CMD -m pip install -r requirements-windows.txt
if [ $? -ne 0 ]; then
    echo "ОШИБКА: Не удалось установить зависимости!"
    exit 1
fi

echo
echo "[3/4] Создание конфигурации..."
if [ ! -f config.txt ]; then
    cp config.example.txt config.txt
    echo "Создан файл config.txt"
else
    echo "Файл config.txt уже существует"
fi

echo
echo "[4/4] Создание необходимых папок..."
mkdir -p src/backups
echo "Папка backups создана"

echo
echo "========================================"
echo "        Установка завершена!"
echo "========================================"
echo
echo "СЛЕДУЮЩИЕ ШАГИ:"
echo "1. Откройте config.txt и заполните:"
echo "   - BOT_TOKEN (получите у @BotFather)"
echo "   - ADMIN_ID (получите у @userinfobot)"
echo
echo "2. Запустите бота командой:"
echo "   cd src"
echo "   $PYTHON_CMD main.py"
echo
echo "Подробные инструкции: LOCAL_SETUP.md"
echo