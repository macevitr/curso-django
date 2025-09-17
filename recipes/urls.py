from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="recipes-home"),  # Home
    path("recipe/<int:id>/", views.recipe, name="recipes-detail"),  # Recipe Detail
]
