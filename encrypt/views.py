from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import encoded
from .forms import encodeForm
from accounts.models import keyid
from django.contrib.auth.models import User
from .hash.encode import encode
from django.contrib.auth.decorators import login_required
from django.utils import timezone
# Create your views here.
@login_required
def encrypt(request):
    encrpyt_form=encodeForm(request.POST)
    if encrpyt_form.is_valid():
        b = keyid.objects.get(user_id=request.user)
        encodes = encode(id=b.keys,password=request.POST['password'])
        hash = encoded()
        hash.name = request.POST['name']
        hash.date= timezone.datetime.now()
        hash.enc = encodes
        hash.hasher = request.user
        if hash.enc!='password maximum length is 15':
            hash.save()
        return HttpResponse(encodes)
        # redirect('encrpyt')
    return render(request,'encode/encode.html',{'encrpyt_form':encrpyt_form})
