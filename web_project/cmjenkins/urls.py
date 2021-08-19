from django.urls import path
from django.urls.resolvers import URLPattern
from cmjenkins import views

urlpatterns = [
    path("cmjenkins/hello_there",views.hello_there,name="hello_there"),
    path("",views.home,name="home")
]