# 🔧 Решение проблем

## Проблемы с установкой зависимостей

### Ошибка: "Cannot install... conflicting dependencies"

**Проблема:** Конфликт версий между aiogram и aiohttp.

**Решение 1 (рекомендуется):**
```bash
pip install -r requirements-minimal.txt
```

**Решение 2:**
```bash
pip install aiogram==2.25.2 phonenumbers
```

**Решение 3 (если ничего не помогает):**
```bash
# Создайте виртуальное окружение
python -m venv bot_env
# Windows:
bot_env\Scripts\activate
# Linux/Mac:
source bot_env/bin/activate

# Установите зависимости
pip install aiogram phonenumbers
```

### Ошибка: "pip is looking at multiple versions"

**Решение:**
```bash
pip install --no-deps aiogram==2.25.2
pip install phonenumbers
pip install aiohttp>=3.8.0,<3.9.0
```

## Проблемы с запуском бота

### Ошибка: "config.txt не найден"

**Решение:**
1. Убедитесь, что файл `config.txt` находится в корневой папке проекта
2. Скопируйте `config.example.txt` в `config.txt`
3. Заполните все необходимые поля

### Ошибка: "Invalid token"

**Решение:**
1. Получите новый токен у @BotFather в Telegram
2. Убедитесь, что токен скопирован полностью без пробелов
3. Формат токена: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`

### Ошибка: "Permission denied" (Linux/Mac)

**Решение:**
```bash
chmod +x install.sh
chmod +x start.sh
```

## Проблемы с Python

### "Python не найден"

**Windows:**
1. Скачайте Python с python.org
2. При установке отметьте "Add Python to PATH"
3. Перезапустите командную строку

**Linux:**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

**Mac:**
```bash
brew install python3
```

### Проблемы с pip

**Обновление pip:**
```bash
python -m pip install --upgrade pip
```

**Установка pip (если отсутствует):**
```bash
python -m ensurepip --upgrade
```

## Дополнительная помощь

Если проблема не решена:
1. Проверьте версию Python: `python --version` (должна быть 3.11+)
2. Проверьте установленные пакеты: `pip list`
3. Попробуйте переустановить зависимости в виртуальном окружении
4. Обратитесь к документации aiogram: https://docs.aiogram.dev/