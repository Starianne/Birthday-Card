from django.shortcuts import render
from .models import Cards

# Create your views here.
def cards_list(request):
    cards = Cards.objects.all().order_by('-date')
    return render(request, 'cards/cards_list.html', {'cards': cards})

def card_page(request, slug):
    card = Cards.objects.get(slug=slug)
    return render(request, 'cards/card_page.html', {'card': card})