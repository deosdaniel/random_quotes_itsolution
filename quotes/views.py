from django.shortcuts import render, redirect
from django.template.defaultfilters import random
from django.db.models import F

from .forms import QuoteForm
from .models import Quote
from .utils import get_random_quote


# Create your views here.

def quotes_list(request):

    quotes = Quote.objects.all()

    return render(request, 'quotes/quotes_list.html', {'quotes': quotes})


def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_quote")
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})

def random_quote(request):
    q = get_random_quote()
    return render(request,'quotes/random_quote.html', {'quote': q})