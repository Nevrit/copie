from . import views
from django.urls import path # type: ignore

urlpatterns = [
    path('', views.index, name='accueil'),
    path('product/<slug:slug>/', views.products_description, name='products_description'),
]