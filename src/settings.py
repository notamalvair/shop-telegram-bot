from simple_config import config
import sqlite3

class Settings:
    def __init__(self):
        pass
    
    # main_settings
    def get_token(self):
        token = config.get('BOT_TOKEN')
        if not token:
            print("❌ Ошибка: Токен бота не найден в config.txt!")
            print("📋 Проверьте файл config.txt в корневой папке проекта")
            exit(1)
        return token
    
    def set_token(self, value):
        # Для простого конфига не реализуем изменение через код
        print("⚠️ Для изменения токена отредактируйте файл config.txt")
        
    def is_debug(self):
        return config.get_bool('DEBUG', False)
        
    def set_debug(self, value):
        print("⚠️ Для изменения режима отладки отредактируйте файл config.txt")
    
    def get_main_admin_id(self):
        admin_id = config.get('ADMIN_ID')
        if not admin_id:
            print("❌ Ошибка: ID администратора не найден в config.txt!")
            exit(1)
        return int(admin_id)
    
    def set_main_admin_id(self, value):
        print("⚠️ Для изменения ID администратора отредактируйте файл config.txt")
    
    # shop_settings
    def get_shop_name(self):
        return config.get('SHOP_NAME', 'Мой магазин')
    
    def set_shop_name(self, value):
        print("⚠️ Для изменения названия магазина отредактируйте файл config.txt")
    
    def get_greeting(self):
        return config.get('GREETING', 'Добро пожаловать!')
    
    def set_greeting(self, value):
        print("⚠️ Для изменения приветствия отредактируйте файл config.txt")
    
    def get_refund_policy(self):
        return config.get('REFUND_POLICY', 'Политика возврата не указана')
    
    def set_refund_policy(self, value):
        print("⚠️ Для изменения политики возврата отредактируйте файл config.txt")
    
    def get_contacts(self):
        return config.get('CONTACTS', 'Контакты не указаны')
    
    def set_contacts(self, value):
        print("⚠️ Для изменения контактов отредактируйте файл config.txt")
    
    def is_image_enabled(self):
        return config.get_bool('ENABLE_IMAGE', True)
    
    def set_image_enabled(self, value):
        print("⚠️ Для изменения настроек изображений отредактируйте файл config.txt")
    
    def is_sticker_enabled(self):
        return config.get_bool('ENABLE_STICKER', False)
    
    def set_sticker_enabled(self, value):
        print("⚠️ Для изменения настроек стикеров отредактируйте файл config.txt")
    
    def is_phone_number_enabled(self):
        return config.get_bool('ENABLE_PHONE_NUMBER', False)
    
    def set_phone_number_enabled(self, value):
        print("⚠️ Для изменения настроек номера телефона отредактируйте файл config.txt")
    
    def is_delivery_enabled(self):
        return config.get_bool('ENABLE_DELIVERY', False)
    
    def set_delivery_enabled(self, value):
        print("⚠️ Для изменения настроек доставки отредактируйте файл config.txt")
    
    def get_delivery_price(self):
        return config.get_float('DELIVERY_PRICE', 0.0)
    
    def set_delivery_price(self, value):
        print("⚠️ Для изменения цены доставки отредактируйте файл config.txt")
    
    # stats_settings (заглушки для совместимости)
    def get_bar_color(self):
        return "3299ff"  # Синий цвет по умолчанию
    
    def set_bar_color(self, value):
        print("⚠️ Настройки статистики больше не используются")
    
    # database methods (сохраняем для совместимости)
    def create_database(self):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            first_name TEXT,
            last_name TEXT,
            phone_number TEXT,
            registration_date TEXT
        )""")
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS items (
            item_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            image_path TEXT,
            category TEXT
        )""")
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            items TEXT,
            total_price REAL,
            order_date TEXT,
            status TEXT,
            delivery_address TEXT,
            phone_number TEXT
        )""")
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS categories (
            category_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )""")
        
        conn.commit()
        conn.close()
    
    def remove_database(self):
        try:
            from os import remove
            remove("../database.db")
            return True
        except:
            return False