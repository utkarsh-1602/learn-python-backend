from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.myview01, name='myview01')
]