from . import list
import random
# id = input('enter id : ')
# password = input('enter password : ')

def valid(x,y):
    if len(x)==5 and len(y)<16:
        return True
    else:
        return False

def length(id,password):
    hash=password
    salt=''
    size=15
    if len(password)<15:
        for i in range(15-len(password)):
            x=random.randrange(97,123)
            salt+=chr(x)
            size-=1
    salt+=hash
    salt+=str(id)
    hash=salt
    hash+=(hex(size))[2]
    return hash



def encode(id,password):
    if valid(id,password):
        encode=''
        hash = length(id,password)
        i=0
        k=0
        x=21
        while(x>0):
            if i>78:
                return('password maximum length is 15')
            if hash[k]==list.List[i][0]:
                a=random.randrange(1,1265)
                encode+=list.List[i][a]
                k+=1
                x-=1
                i=0
            else:
                i+=1
        return(encode)
    else:
        return('password maximum length is 15')






# encode(id,password)
