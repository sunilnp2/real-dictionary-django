from django.urls import path
from word.views import *
app_name = 'word'

urlpatterns = [
    path('', home, name='home'),
    path('search', search, name='search'),
    
]
