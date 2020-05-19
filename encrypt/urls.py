from django.urls import path
from . import views

app_name='encrypt'

urlpatterns=[
    path('encrypt/',views.encrypt,name='encrypt'),

]
