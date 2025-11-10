from django.urls import path
from . import views

app_name = 'cards'
urlpatterns = [
    path('', views.cards_list, name="list"),
    path('new-card/', views.card_new, name="new-card"),
    path('<slug:slug>', views.card_page, name="page"),
]