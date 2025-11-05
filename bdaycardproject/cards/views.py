from django.shortcuts import render
from .models import Cards
from django.http import HttpResponse

# Create your views here.
def cards_list(request):
    cards = Cards.objects.all().order_by('-date')
    return render(request, 'cards/cards_list.html', {'cards': cards})

def card_page(request, slug):
    return HttpResponse(slug)