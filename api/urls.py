from django.urls import path
from . import views

urlpatterns = [
    path("symbols/", views.get_symbols, name="symbols"),
    path("convert/", views.convert_currency, name="convert"),
]