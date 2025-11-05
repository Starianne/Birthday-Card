from django.urls import path
from . import views

app_name = 'cards'
urlpatterns = [
    path('', views.cards_list, name="list"),
    path('<slug:slug>', views.card_page, name="page"),
]