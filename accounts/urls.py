from django.contrib.auth import views as auth
from django.urls import path,include
from accounts import views



app_name='accounts'

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',auth.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logut/',auth.LogoutView.as_view(),name='logout'),

]
