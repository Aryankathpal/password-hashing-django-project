from django.urls import path
from . import views

app_name='decrypt'

urlpatterns=[
    path('decrypt/',views.decoded,name='decrypt'),
    path('<int:hash_id>',views.endecrypt,name='endecrypt'),

]
