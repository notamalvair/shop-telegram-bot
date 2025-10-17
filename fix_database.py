# -*- coding: utf-8 -*-
"""
Скрипт для исправления структуры базы данных
"""
import os
import sys

# Переходим в папку src
os.chdir('src')
sys.path.append('.')

from settings import Settings

print("🔧 Исправление структуры базы данных...")

try:
    settings = Settings()
    
    # Создаем базу данных
    settings.create_database()
    
    # Выполняем миграцию
    settings.migrate_database()
    
    print("✅ База данных исправлена!")
    
    # Проверяем структуру
    import sqlite3
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    
    cursor.execute("PRAGMA table_info(users)")
    columns = cursor.fetchall()
    
    print(f"📊 Структура таблицы users ({len(columns)} колонок):")
    for i, col in enumerate(columns):
        print(f"  {i+1}. {col[1]} ({col[2]})")
    
    conn.close()
    
except Exception as e:
    print(f"❌ Ошибка: {e}")
    import traceback
    traceback.print_exc()

print("\n🚀 Теперь можно запускать бота!")