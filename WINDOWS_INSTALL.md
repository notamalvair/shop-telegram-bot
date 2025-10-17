# Установка на Windows

## Проблема с pymorphy2
Библиотека `pymorphy2` требует компиляции C++ кода и может не устанавливаться на Windows без дополнительных инструментов.

## Решение 1: Использование упрощенной версии (рекомендуется)

```bash
# Установите упрощенные зависимости
pip install -r requirements-windows.txt

# Или установите вручную:
pip install aiogram==2.25.1 phonenumbers==8.13.26 pyparsing==3.1.1
```

Бот будет работать с упрощенным поиском без морфологического анализа.

## Решение 2: Установка Visual Studio Build Tools

Если нужна полная функциональность поиска:

1. Скачайте и установите [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
2. Установите Python Development workload
3. Перезапустите командную строку
4. Попробуйте установить полные зависимости:

```bash
pip install -r requirements.txt
```

## Решение 3: Использование предкомпилированных пакетов

```bash
# Попробуйте установить из conda-forge
conda install -c conda-forge pymorphy2

# Или используйте готовые wheel файлы
pip install --only-binary=all pymorphy2
```

## Запуск бота

```bash
cd src
python main.py
```

## Функциональность поиска

- **С pymorphy2**: Полный морфологический анализ русских слов
- **Без pymorphy2**: Упрощенный поиск с базовыми правилами склонения

Обе версии работают корректно для большинства случаев использования.