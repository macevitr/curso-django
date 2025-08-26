from django.urls import path
from recipes.views import home, sobre, contato


urlpatterns = [
    path('sobre/', sobre),  # Sobre
    path('', home),     # Home
    path('contato/', contato),  # Contato
]
