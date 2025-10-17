import item as itm
import re

excluded_words = ["без", "в", "для", "до", "за", "из", "к", "под", "а", "о", "над", "на", "о", "об", "от", "перед", "по", "под", "при", "про", "с", "у"]

# Простые правила для русской морфологии (базовые окончания)
def get_normal_forms(word):
    """Простая нормализация слов без pymorphy2"""
    word = word.lower().strip()
    
    # Убираем знаки препинания
    word = re.sub(r'[^\w\s]', '', word)
    
    if len(word) < 3:
        return {word}
    
    # Простые правила для русских слов
    forms = {word}
    
    # Убираем распространенные окончания
    endings = ['ов', 'ев', 'ей', 'ам', 'ям', 'ах', 'ях', 'ми', 'ами', 'ями', 
               'ы', 'и', 'а', 'я', 'у', 'ю', 'е', 'о', 'ом', 'ем', 'ой', 'ей']
    
    for ending in endings:
        if word.endswith(ending) and len(word) > len(ending) + 2:
            forms.add(word[:-len(ending)])
    
    return forms
    

class Query:
    def __init__(self, results):
        self.results = results

    def __get_items(self):
        return list(map(itm.Item, self.results.keys()))[::-1][:90]

    def match(self):
        return self.__get_items()

    def price(self):
        return sorted(list(map(itm.Item, self.results.keys()))[::-1], key=lambda item: item.get_price())

    def popular(self):
        pass

# Система очков для поиска:
# Точное совпадение в названии: 5 очков
# Частичное совпадение в названии: 3 очка  
# Точное совпадение в описании: 2 очка
# Частичное совпадение в описании: 1 очко
def search_item(query):
    points = dict()
    query_lower = query.lower()
    
    for item in itm.get_item_list():
        points[item.get_id()] = 0
        item_name = item.get_name().lower()
        item_desc = item.get_desc().lower()
        
        # Поиск по отдельным словам
        for word in list(filter(lambda word: word not in excluded_words, query.split())):
            word_forms = get_normal_forms(word)
            
            # Поиск в названии
            for word_title in item_name.split():
                title_forms = get_normal_forms(word_title)
                
                # Точное совпадение форм
                if word_forms & title_forms:
                    points[item.get_id()] += 5
                # Частичное совпадение (одно слово содержит другое)
                elif any(w in word_title or word_title in w for w in word_forms):
                    points[item.get_id()] += 3
            
            # Поиск в описании
            for word_desc in item_desc.split():
                desc_forms = get_normal_forms(word_desc)
                
                # Точное совпадение форм
                if word_forms & desc_forms:
                    points[item.get_id()] += 2
                # Частичное совпадение
                elif any(w in word_desc or word_desc in w for w in word_forms):
                    points[item.get_id()] += 1
        
        # Дополнительные очки за полное совпадение фразы
        if query_lower in item_name:
            points[item.get_id()] += 10
        elif query_lower in item_desc:
            points[item.get_id()] += 5
            
        # Удаляем товары без совпадений
        if points[item.get_id()] == 0:
            points.pop(item.get_id())
    
    return Query(dict(sorted(points.items(), key=lambda item: item[1], reverse=True)))
