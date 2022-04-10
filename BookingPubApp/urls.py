from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('restaurants/', views.restaurants_page),
    path('restaurants/' + '<int:id>', views.single_restaurant_page)
]