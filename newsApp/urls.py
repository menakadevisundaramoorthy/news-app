from django.urls import path

from . import views

app_name = 'newsApp'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
]
