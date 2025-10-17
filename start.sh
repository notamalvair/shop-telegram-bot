#!/bin/bash

echo "========================================"
echo "      Запуск Telegram Shop Bot"
echo "========================================"
echo

if [ ! -f config.txt ]; then
    echo "ОШИБКА: Файл config.txt не найден!"
    echo "Сначала запустите ./install.sh"
    exit 1
fi

# Определяем команду Python
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "ОШИБКА: Python не найден!"
    exit 1
fi

mkdir -p src/backups

echo "Запуск бота..."
cd src
$PYTHON_CMD main.py

echo
echo "Бот остановлен."