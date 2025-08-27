import random
from .models import Quote

def get_random_quote():
    quotes = list(Quote.objects.all())
    if not quotes:
        return None
    weights = [q.weight if q.weight > 0 else 1 for q in quotes]
    return random.choices(quotes, weights=weights, k=1)[0]