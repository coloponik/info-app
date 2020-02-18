from django.urls import path
from . import views
# from calculator import views as Calc

urlpatterns = [
    path('calculator/', views.calculator)
]