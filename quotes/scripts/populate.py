import random
from quotes.models import Quote
from collections import Counter

def run():
    sources = ["Сопрано", "Бойцовский клуб", "Большой куш", "Субмарина", "Гарри Поттер", "Бриллиантовая рука", "Самогонщики", "Москва слезам не верит", "Унесенные ветром", "Брат"]
    MAX_PER_SOURCE = 3
    TOTAL_QUOTES = 30

    counts = Counter()
    for q in Quote.objects.all():
        counts[q.source] += 1

    i = 0
    while i < TOTAL_QUOTES:
        available = [s for s in sources if counts[s] < MAX_PER_SOURCE]
        if not available:
            break
        source = random.choice(available)
        text = f"Тестовая цитата #{i+1} из '{source}'"
        weight = random.randint(1, 10)
        views = random.randint(0,50)
        likes = random.randint(0,50)
        try:
            Quote.objects.create(source=source, text=text, weight=weight, views=views, likes=likes)
            counts[source] += 1
            i += 1
        except:
            continue

    print(f"{i} test quotes created!")