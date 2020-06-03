from django.shortcuts import render,redirect
from django.views.generic import CreateView,TemplateView
from .forms import UserForm,keyForm
from django.contrib.auth import login,authenticate
from .models import keyid
from django.contrib.auth.models import User
from django.contrib import messages
import random
# Create your views here.
def signup(request):
    form = UserForm(request.POST)
    form2=keyForm(request.POST)
    if form.is_valid():
            user = User.objects.create_user(username=request.POST['username'],email=request.POST['email'],password=request.POST['password1'])
            def id():
                key = generate()
                if keyid.objects.filter(keys=key).exists():
                    return id()
                else:
                    return key
            form = keyid.objects.get_or_create(user=user,keys=id())[0]
            user=form.save()
            messages.info(request,'Signed up successfully')
            return redirect('accounts:signup')
    else:
        (form.errors,form2.errors)

    return render(request, 'accounts/signup.html',{'form':form,'form2':form2})

def generate():
    id=''
    for i in range(4):
        a=random.randrange(65,91)
        c=chr(a)
        id+=c
    d=random.randrange(0,10)
    id+=str(d)
    return id


class home(TemplateView):
    template_name='accounts/home.html'

class conditions(TemplateView):
    template_name='accounts/t&c.html'
