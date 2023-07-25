from django.urls import path
from app1.views import *
app_name='one'

urlpatterns=[
    path('first/',first,name='first'),
    path('second/',second,name='second'),
    path('string1/',string1,name='string1'),
    
]