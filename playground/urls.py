from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('hello_playground/', views.say_hello_fromstore)
    
]
