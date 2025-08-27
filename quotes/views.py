from django.shortcuts import render, redirect
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

def quote_detail(request, pk):
    q = Quote.objects.get(pk=pk)
    return render(request, 'quotes/quote_detail.html', {'quote': q})

def random_quote(request):
    q = get_random_quote()
    Quote.objects.filter(pk=q.id).update(views=F('views')+1)
    return redirect('quote_detail', pk=q.pk)

def like_quote(request, pk):
    Quote.objects.filter(id=pk).update(likes=F('likes')+1)
    return redirect("quote_detail", pk=pk)

def dislike_quote(request, pk):
    q = Quote.objects.get(pk=pk)
    if q.likes > 0:
        Quote.objects.filter(pk=pk).update(likes=F("likes") - 1)
    return redirect("quote_detail", pk=pk)