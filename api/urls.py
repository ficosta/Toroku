from django.urls import path
from . import views


app_name = 'api'
urlpatterns = [
    # post views
    path('print/', views.Print, name='print'),
    path('print/<int:pk>/', views.PrintVisitante, name='print'),
]
