from . import list
import random
# id = input('enter id : ')
# password = input('enter Hash : ')

def valid(x,y):
    if len(y)==84:
        return True
    else:
        return False

def decode(x):
    i=0
    while(x!='decode'):
        if(i>78):
            return '``'
        for j in range(1,1265):
            if x==list.List[i][j]:
                x='decode'
                return list.List[i][0]
        i+=1

def validid(id,password):
    x=''
    for i in range(60,77,4):
        code=''
        for j in range(4):
            code+= password[i+j]
        x+=decode(code)
    if x==id:
        return True
    else:
        return False

def length(password):
    x=''
    for i in range(80,84):
        x+=password[i]
    y=decode(x)
    d=int(y,16)
    return d

def realpass(decoded,length):
    realpass=''
    for i in range(0,length*4,4):
        x=''
        for j in range(0,4):
            x+=decoded[i+j]
        y = decode(x)
        realpass+=y
    return(realpass)

def change(password):
    passw=''
    for i in range(0,82,4):
        p=''
        for j in range(0,4):
            p+=password[i+j]
        y= decode(p)
        passw+=y
    if '``' in passw:
        return False
    else:
        return True


def hashcode(id,password):
    if valid(id,password) and validid(id,password):
        if change(password):
            decoded_len = ''
            real = length(password)
            for i in range((15-(real))*4,61):
                decoded_len+=password[i]
            y=realpass(decoded_len,real)
            return y
        else:
            return('invalid hash')
    else:
        return('invalid hash')
