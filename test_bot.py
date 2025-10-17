#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Тестовый скрипт для проверки бота
"""

import sys
import os

# Добавляем папку src в путь
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

print("🧪 Тестирование бота...")
print("📁 Текущая директория:", os.getcwd())
print("📂 Содержимое папки src:")
for item in os.listdir('src'):
    print(f"  - {item}")

print("\n🔧 Проверка конфигурации...")
try:
    # Переходим в папку src для правильной работы с конфигом
    os.chdir('src')
    from simple_config import config
    print("✅ Модуль simple_config загружен")
    
    token = config.get('BOT_TOKEN')
    if token:
        print(f"✅ Токен найден: {token[:10]}...")
    else:
        print("❌ Токен не найден!")
        
    admin_id = config.get('ADMIN_ID')
    if admin_id:
        print(f"✅ Admin ID найден: {admin_id}")
    else:
        print("❌ Admin ID не найден!")
        
except Exception as e:
    print(f"❌ Ошибка загрузки конфигурации: {e}")

print("\n🗄️ Проверка базы данных...")
try:
    import sqlite3
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    
    # Проверяем таблицы
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print(f"✅ Найдено таблиц: {len(tables)}")
    for table in tables:
        print(f"  - {table[0]}")
    
    conn.close()
except Exception as e:
    print(f"❌ Ошибка проверки базы данных: {e}")

print("\n🤖 Попытка запуска бота...")
try:
    print("📁 Уже в папке src")
    
    # Импортируем основные модули
    from settings import Settings
    print("✅ Settings загружен")
    
    settings = Settings()
    print("✅ Settings инициализирован")
    
    token = settings.get_token()
    print(f"✅ Токен получен: {token[:10]}...")
    
    print("\n🚀 Запуск main.py...")
    with open('main.py', 'r', encoding='utf-8') as f:
        exec(f.read())
    
except KeyboardInterrupt:
    print("\n⏹️ Остановлено пользователем")
except Exception as e:
    print(f"❌ Ошибка запуска: {e}")
    import traceback
    traceback.print_exc()