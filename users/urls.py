from django.urls import path
from django.conf.urls import url , include
from . import views

urlpatterns = [
    #path("" , views.index , name="index"),
    #path("login" , views.login_view , name="login"),
    #path("logout" ,views.logout_view , name="logout" ),
    url("dashboard", views.dashboard, name="dashboard"),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^register/", views.register, name="register"),
]