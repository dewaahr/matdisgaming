def rekurensi_min(a1,a0,n,k1,k2):
    if n!=0:
        c=a1
        a2=(k1*a1)-(k2*a0)
        a0=c
        return rekurensi_min(a2,a0,n-1,k1,k2)
    else:
        return (k1*a1)-(k2*a0)

def rekurensi_plus(a1,a0,n,k1,k2):
    if n!=0:
        c=a1
        a2=(k1*a1)+(k2*a0)
        a0=c
        return rekurensi_plus(a2,a0,n-1,k1,k2)
    else:
        return (k1*a1)+(k2*a0)
    
def rekurensi_pangkat(a0,n,k1,k2,n_2=0): 
    if n!=0:
        a1=k1*a0+(k2**(n_2))
        n_2+=1
        return rekurensi_pangkat(a1,n-1,k1,k2,n_2)
    else:
        return k1*a0+(k2**(n_2))
    
    
a0=int(input('a_0:'))
a1=int(input('a_1:'))   
n=int(input('a_n (yang di tanya):'))
k1=int(input('koefisien pertama:'))
k2=int(input('koefisien kedua:'))
# a0=1
# n=5
# k1=8
# k2=10
print(rekurensi_plus(a1,a0,n-2,k1,k2))
print(rekurensi_min(a1,a0,n-2,k1,k2))
print(rekurensi_pangkat(a0,n-1,k1,k2))
