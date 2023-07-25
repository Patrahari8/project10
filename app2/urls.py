from django.urls import path
from app2.views import *
app_name='two'

urlpatterns=[
    path('third/',thrid,name='third'),
    path('fourth/',fourth,name='fourth'),
    path('string2/',string2, name='string2')
]