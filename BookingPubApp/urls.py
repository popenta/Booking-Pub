from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.main_page)
]