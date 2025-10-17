"""
Простой парсер конфигурации из config.txt
"""
import os

class SimpleConfig:
    def __init__(self, config_path="config.txt"):
        self.config_path = config_path
        self.config = {}
        self.load_config()
    
    def load_config(self):
        """Загружает конфигурацию из файла"""
        if not os.path.exists(self.config_path):
            print(f"❌ Файл конфигурации не найден: {self.config_path}")
            print("📋 Создайте файл config.txt в папке src")
            exit(1)
        
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    # Пропускаем комментарии и пустые строки
                    if line.startswith('#') or not line or '=' not in line:
                        continue
                    
                    key, value = line.split('=', 1)
                    self.config[key.strip()] = value.strip()
        except Exception as e:
            print(f"❌ Ошибка чтения конфигурации: {e}")
            exit(1)
    
    def get(self, key, default=None):
        """Получает значение из конфига"""
        return self.config.get(key, default)
    
    def get_int(self, key, default=0):
        """Получает целое число из конфига"""
        try:
            return int(self.config.get(key, default))
        except (ValueError, TypeError):
            return default
    
    def get_float(self, key, default=0.0):
        """Получает число с плавающей точкой из конфига"""
        try:
            return float(self.config.get(key, default))
        except (ValueError, TypeError):
            return default
    
    def get_bool(self, key, default=False):
        """Получает булево значение из конфига"""
        value = self.config.get(key, '0')
        return value in ('1', 'true', 'True', 'yes', 'Yes')

# Глобальный экземпляр конфига
config = SimpleConfig()