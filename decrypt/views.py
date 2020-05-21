from django.shortcuts import render,redirect,get_object_or_404
from .models import decode
from django.contrib.auth.models import User
from accounts.models import keyid
from .forms import decrypt
from django.contrib.auth.decorators import login_required
from .hash.decode import hashcode
from encrypt.models import encoded

# Create your views here.
@login_required
def decoded(request):
    decrypt_form=decrypt(request.POST)
    hash=''
    if request.method=='POST':
        b=keyid.objects.get(user_id=request.user)
        key=b.keys
        if decrypt_form.is_valid():
            pas = hashcode(id=key,password=request.POST['encrypted_password'])
            hash=pas

    return render(request, 'decrypt/decrypt.html',{'decrypt_form':decrypt_form,'hash':hash})

@login_required
def endecrypt(request, hash_id):
     hash=get_object_or_404(encoded,pk=hash_id)
     b=keyid.objects.get(user_id=request.user)
     key=b.keys
     pas = hashcode(id=key,password=hash.enc)
     hash=pas
     return render(request,'decrypt/endecrypt.html',{'hash':hash})
