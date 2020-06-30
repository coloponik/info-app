from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include('weather.urls')),
    re_path(r'^', include('calculator.urls')),
    re_path(r'^', include('user.urls')),
    re_path(r'^account/', include("account.urls")),
    re_path(r'^', views.index)
]
