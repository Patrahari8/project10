from django.urls import path
from app3.views import *
app_name='three'

urlpatterns=[
    path('fifth/',fifth, name='fifth'),
    path('sixth/',sixth,name='sixth'),
    path('string3/',string3,name='string3'),
]