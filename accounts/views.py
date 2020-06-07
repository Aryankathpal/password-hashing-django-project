from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import CreateView,TemplateView
from .forms import UserForm,keyForm
from django.contrib.auth import login,authenticate
from .models import keyid
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .utils import token_generator
import random
# Create your views here.
def signup(request):
    form = UserForm(request.POST)
    form2=keyForm(request.POST)
    if form.is_valid():
            user = User.objects.create_user(username=request.POST['username'],email=request.POST['email'].lower(),password=request.POST['password1'])
            user.is_active = False

            def id():
                key = generate()
                if keyid.objects.filter(keys=key).exists():
                    return id()
                else:
                    return key
            form = keyid.objects.get_or_create(user=user,keys=id())[0]

            uidb64=urlsafe_base64_encode(force_bytes(user.pk))
            domain=get_current_site(request).domain
            link=reverse('accounts:activate',kwargs={'uidb64':uidb64,'token':token_generator.make_token(user)})
            activate_url='http://'+domain+link

            email_subject='Activate your account'
            email_body='hi '+user.username+ '\nplease click on this link to actvate your account\n' + activate_url
            email = EmailMessage(
                email_subject,
                email_body,
                'kathlock.help@gmail.com',
                [user.email],
            )
            email.send(fail_silently=False)
            user1=user.username
            user=form.save()
            deactivate(user1)
            # active()
            #messages.info(request,'Signed up successfully')
            return redirect('accounts:accountcreated')
    else:
        (form.errors,form2.errors)

    return render(request, 'accounts/signup.html',{'form':form,'form2':form2})

def deactivate(user1):
    user=User.objects.get(username=user1)
    user.is_active=False
    user=user.save()

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

class verification(TemplateView):
    def get(self,request,uidb64,token):
        try:
            uid=urlsafe_base64_decode(force_text(uidb64))
            user=User.objects.get(pk=uid)

        except Exception as indentifiers:
            user=None
        if user is not None and token_generator.check_token(user,token):
            user.is_active=True
            user=user.save()
            print('help')
            return redirect('accounts:activated')
        return render(request, 'accounts/failed.html')

class accountcreated(TemplateView):
    template_name='accounts/inactive.html'

class activated(TemplateView):
    template_name='accounts/activated.html'
