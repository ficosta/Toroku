from django.urls import path
from . import views


app_name = 'cadastro'
urlpatterns = [
    # post views
    path('cadastro/', views.cadastro, name='cadastro'),
    path('', views.home, name='home'),
]
