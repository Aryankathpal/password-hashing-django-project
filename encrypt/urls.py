from django.urls import path
from . import views

app_name='encrypt'

urlpatterns=[
    path('encrypt/',views.encrypt,name='encrypt'),
    path('list/',views.enlist,name='enlist'),
    path('<int:hasher_id>/',views.detail,name='detail'),
    path('<int:hasher_id>/delete',views.delete_it,name='delete'),
]
