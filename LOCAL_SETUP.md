# 💻 Установка и запуск на локальном ПК

## 📋 Что вам понадобится

1. **Python 3.11 или новее** - [скачать с python.org](https://www.python.org/downloads/)
2. **Git** - [скачать с git-scm.com](https://git-scm.com/downloads)
3. **Токен Telegram бота** - получить у [@BotFather](https://t.me/BotFather)
4. **Ваш Telegram ID** - получить у [@userinfobot](https://t.me/userinfobot)

## 🚀 Пошаговая установка

### Шаг 1: Скачивание репозитория

Откройте командную строку (Windows) или терминал (Mac/Linux) и выполните:

```bash
# Клонируйте репозиторий
git clone https://github.com/notamalvair/shop-telegram-bot.git

# Перейдите в папку проекта
cd shop-telegram-bot
```

### Шаг 2: Установка Python зависимостей

```bash
# Установите все необходимые библиотеки
pip install -r requirements-windows.txt
```

**Примечание:** Могут появиться предупреждения о совместимости версий - это нормально.

### Шаг 3: Создание конфигурации

```bash
# Скопируйте пример конфига
copy config.example.txt config.txt    # Windows
# или
cp config.example.txt config.txt      # Mac/Linux
```

### Шаг 4: Настройка config.txt

Откройте файл `config.txt` в любом текстовом редакторе и заполните:

```ini
# Основные настройки бота
BOT_TOKEN = ВАШ_ТОКЕН_БОТА_ЗДЕСЬ
ADMIN_ID = ВАШ_TELEGRAM_ID_ЗДЕСЬ

# Настройки базы данных (можно оставить как есть)
DB_HOST = localhost
DB_PORT = 5432
DB_NAME = shop_bot
DB_USER = postgres
DB_PASSWORD = password

# Настройки платежей (опционально)
PAYMENT_TOKEN = 
QIWI_TOKEN = 
QIWI_PHONE = 

# Настройки уведомлений (опционально)
NOTIFICATION_CHAT_ID = 
```

**Обязательно заполните:**
- `BOT_TOKEN` - получите у [@BotFather](https://t.me/BotFather)
- `ADMIN_ID` - получите у [@userinfobot](https://t.me/userinfobot)

### Шаг 5: Создание необходимых папок

```bash
# Создайте папку для резервных копий
mkdir src\backups    # Windows
# или
mkdir -p src/backups # Mac/Linux
```

### Шаг 6: Запуск бота

```bash
# Перейдите в папку с исходным кодом
cd src

# Запустите бота
python main.py
```

## ✅ Проверка работы

Если всё настроено правильно, вы увидите:

```
🤖 Бот запущен успешно!
📱 Имя бота: @ваш_бот
👤 Администратор: ваше_имя (ID: ваш_id)
🔄 Ожидание сообщений...
```

Теперь найдите своего бота в Telegram и отправьте команду `/start`

## 🛠 Возможные проблемы и решения

### Проблема: "ModuleNotFoundError"
**Решение:** Убедитесь, что установили зависимости:
```bash
pip install -r requirements-windows.txt
```

### Проблема: "Invalid token"
**Решение:** Проверьте токен бота в config.txt - он должен выглядеть как `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`

### Проблема: "Permission denied"
**Решение:** Запустите командную строку от имени администратора (Windows)

### Проблема: Бот не отвечает
**Решение:** 
1. Проверьте, что бот запущен (не закрывайте окно с программой)
2. Убедитесь, что токен правильный
3. Проверьте интернет-соединение

## 🔄 Остановка и перезапуск

**Остановка бота:**
- Нажмите `Ctrl+C` в окне командной строки

**Перезапуск бота:**
```bash
cd shop-telegram-bot/src
python main.py
```

## 📁 Структура файлов

После установки у вас будет:

```
shop-telegram-bot/
├── config.txt          # Ваши настройки (НЕ делитесь этим файлом!)
├── config.example.txt   # Пример настроек
├── requirements-windows.txt # Зависимости
├── src/
│   ├── main.py         # Главный файл бота
│   ├── backups/        # Папка для резервных копий
│   └── ...             # Другие файлы бота
└── README.md           # Документация
```

## 🔒 Безопасность

⚠️ **ВАЖНО:**
- Никогда не делитесь файлом `config.txt` - в нём ваши секретные токены!
- Не публикуйте токен бота в интернете
- Регулярно делайте резервные копии данных

## 🆘 Нужна помощь?

1. **Создание бота:** [BOT_SETUP.md](BOT_SETUP.md)
2. **Проблемы с Windows:** [WINDOWS_INSTALL.md](WINDOWS_INSTALL.md)
3. **Приватность репозитория:** [MAKE_PRIVATE.md](MAKE_PRIVATE.md)

---

🎉 **Поздравляем! Ваш интернет-магазин на базе Telegram бота готов к работе!**