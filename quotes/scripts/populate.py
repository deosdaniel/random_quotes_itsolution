import random
from quotes.models import Quote
from collections import Counter

def run():
    sources = ["Movie A", "Book B", "Series C", "Movie D", "Book E", "Movie F", "Book G", "Movie H", "Book K", "Movie L"]
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
        text = f"Test quote #{i+1} from {source}"
        weight = random.randint(1, 10)
        try:
            Quote.objects.create(source=source, text=text, weight=weight)
            counts[source] += 1
            i += 1
        except:
            continue

    print(f"{i} test quotes created!")