from django.shortcuts import render

import quotes


# Create your views here.

def quotes_list(request):
    return render(request, 'quotes/quotes_list.html')

def random_quote(request):
    return render(request,'quotes/random_quote.html')