#psudocode
def pseudo(m,k):
    k=0
    for i in range(1,m+1):
        for j in range(i):
            k+=1
    return k
m=int(input('M:'))
k=int(input('K:'))
print(pseudo(m,k))


#permutasi
