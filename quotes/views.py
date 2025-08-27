from django.shortcuts import render
from django.template.defaultfilters import random

from .models import Quote


# Create your views here.

def quotes_list(request):

    quotes = Quote.objects.all()

    return render(request, 'quotes/quotes_list.html', {'quotes': quotes})




def random_quote(request):
    q = Quote.objects.order_by('?').first()
    context = {'quote': q}
    return render(request,'quotes/random_quote.html', context)