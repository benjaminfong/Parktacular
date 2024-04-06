from django.urls import path
from . import views

## URL Configuration
urlpatterns = [
    # use path() to create an url object
    path('hello/', views.say_hello),
    path('api/', views.parking_facility_list),
]