from django.shortcuts import render, redirect
from .models import Cards
from django.contrib.auth.decorators import login_required
from . import forms #importing forms.py file inside this folder

# Create your views here.
def cards_list(request):
    cards = Cards.objects.all().order_by('-date')
    return render(request, 'cards/cards_list.html', {'cards': cards})

def card_page(request, slug):
    card = Cards.objects.get(slug=slug)
    return render(request, 'cards/card_page.html', {'card': card})

@login_required(login_url="/userLogin/login/")
def card_new(request):
    if request.method == 'POST':
        form = forms.CreateCard(request.POST, request.FILES)
        if form.is_valid():
            #saves card made by user
            newcard = form.save(commit=False)
            newcard.author = request.user
            newcard.save()
            return redirect('cards:list')
    else:
        form = forms.CreateCard()
    return render(request, 'cards/card_new.html', { 'form': form })