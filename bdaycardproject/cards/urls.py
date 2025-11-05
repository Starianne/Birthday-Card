from django.urls import path
from . import views

urlpatterns = [
    path('', views.cards_list, name="cards"),
    path('<slug:slug>', views.card_page, name="page"),
]