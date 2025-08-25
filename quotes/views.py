from django.shortcuts import render
from .models import Quote


# Create your views here.

def quotes_list(request):

    quotes = Quote.objects.all()

    return render(request, 'quotes/quotes_list.html', {'quotes': quotes})




def random_quote(request):
    return render(request,'quotes/random_quote.html')