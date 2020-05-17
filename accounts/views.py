from django.shortcuts import render,redirect
from django.views.generic import CreateView,TemplateView
from .forms import UserForm,keyForm
from django.contrib.auth import login,authenticate
from .models import keyid
from django.contrib.auth.models import User
# Create your views here.
def signup(request):
    form = UserForm(request.POST)
    form2=keyForm(request.POST)
    if form.is_valid():
            user = User.objects.get_or_create(username=request.POST['username'],email=request.POST['email'],password=request.POST['password1'])[0]
            form = keyid.objects.get_or_create(user=user,keys='23456')[0]
            user=form.save()
        # username=form.cleaned_data.get('username')
        # password = form.cleaned_data.get('password1')
        # user=authenticate(username=username,password=password)
        # login(request,user)
            return redirect('home')
    else:
        (form.errors,form2.errors)

    return render(request, 'accounts/signup.html',{'form':form,'form2':form2})

class home(TemplateView):
    template_name='accounts/home.html'
