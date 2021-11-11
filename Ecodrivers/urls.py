from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.home, name='home'),
    path('menu1', views.menu, name='menu'),
    path('menu2', views.menu2, name='menu2'),
    path('menu3', views.menu3, name='menu3'),
    path("booktable", views.booktable, name='booktable'),
    path("contact", views.Contact1, name='contact'),
    path('Event', views.Event, name="Event"),
    path('blood', views.blood, name='blood'),
]