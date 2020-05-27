from django.shortcuts import render,redirect,get_object_or_404
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
    hashs=''
    hashsm=''
    hashsm1=''
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
            hashs=hash.enc
        else:
            hashsm = 'encryption support only !@.$#:%,&*;-_ these special charactors'
        # redirect('encrpyt')
    return render(request,'encode/encode.html',{'encrpyt_form':encrpyt_form,'hashs':hashs,'hashsm':hashsm})

@login_required
def enlist(request):
    hash=encoded.objects.filter(hasher_id=request.user)
    return render(request,'encode/enlist.html',{'hash':hash})

@login_required
def detail(request,hasher_id):
    hash=get_object_or_404(encoded,pk=hasher_id)
    return render(request,'encode/detail.html',{'hash':hash})

@login_required
def delete_it(request,hasher_id):
    hash=get_object_or_404(encoded,pk=hasher_id)
    if request.method=='POST':
        hash.delete()
        return redirect('encrypt:enlist')
    return render(request, 'encode/delete.html',{'hash':hash})
