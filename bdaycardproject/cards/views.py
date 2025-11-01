from django.shortcuts import render

# Create your views here.
def cards_list(request):
    return render(request, 'cards/cards_list.html')