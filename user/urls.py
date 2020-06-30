from django.urls import path, re_path, include
from . import views
from InfoApp import settings
from django.contrib.auth import views as authViews

urlpatterns = [
    # path('account/', include('django.contrib.auth.urls')),
    re_path(r'^account/profile/notes/', views.notes),
    re_path(r'^account/profile/settings/', views.settings),
    re_path(r'^account/profile/$', views.profile),
    re_path(r'^account/login/$', views.LoginView.as_view(), name="account_login"),
    re_path(r'^account/signup/$', views.SignupView.as_view(), name="account_signup"),
    re_path(r'^account/logout/$', authViews.LogoutView.as_view(), name='account_logout')
]