from django.shortcuts import render
from .models import Cards

# Create your views here.
def cards_list(request):
    cards = Cards.object.all()
    return render(request, 'cards/cards_list.html', {'cards': cards})