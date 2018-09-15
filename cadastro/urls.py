from django.urls import path
from . import views


app_name = 'cadastro'
urlpatterns = [
    # post views
    path('', views.cadastro, name='cadastro'),
]
