from django.urls import path

from . import views


urlpatterns =[
    path("", views.home, name="home"), 
    path("service/",views.service, name="service"),
    path("soft/",views.soft, name="soft"),
    path("hello/",views.hello, name="hello"),
    path("kitty/",views.kitty, name="kitty")
] 
