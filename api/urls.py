from django.urls import path
from . import views


app_name = 'api'
urlpatterns = [
    # post views
    path('print/', views.PrintViewSet.as_view(), name='print'),
]
