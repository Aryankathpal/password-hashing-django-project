from django.shortcuts import render,redirect
from django.views.generic import CreateView,TemplateView
from .forms import UserForm,keyForm
from django.contrib.auth import login,authenticate
from .models import keyid
from django.contrib.auth.models import User
import random
# Create your views here.
def signup(request):
    form = UserForm(request.POST)
    form2=keyForm(request.POST)
    if form.is_valid():
            user = User.objects.create_user(username=request.POST['username'],email=request.POST['email'],password=request.POST['password1'])
            form = keyid.objects.get_or_create(user=user,keys=generate())[0]
            user=form.save()
            return redirect('home')
    else:
        (form.errors,form2.errors)

    return render(request, 'accounts/signup.html',{'form':form,'form2':form2})

def generate():
    id=''
    for i in range(5):
        a=random.randrange(0,10)
        id+=str(a)
    return id


class home(TemplateView):
    template_name='accounts/home.html'