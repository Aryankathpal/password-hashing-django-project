from django.contrib.auth import views as auth
from django.urls import path,include
from accounts import views
from .views import verification,accountcreated,activated


app_name='accounts'

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',auth.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logut/',auth.LogoutView.as_view(),name='logout'),
    path('activate/<uidb64>/<token>',verification.as_view(),name='activate'),
    path('created/',accountcreated.as_view(),name='accountcreated'),
    path('activated/',activated.as_view(),name='activated'),
]
