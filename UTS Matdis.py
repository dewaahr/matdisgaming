import math
while True:
    print("\n================Silahkan Pilih Mode============\n")
    print("1. Chinese Reminder Theorem")
    print("2. Enkripsi")
    print("3. gcd dan lcm")
    print("4. Himpunan")
    print("5. exit")
    pilihan=int(input('\nMasukan Pilihan: '))

    if pilihan==1:
        print('\n====================chinese reminder theorem===============\n')
        a= int(input('masukkan x1      : '))
        a1= int(input('hasil modulus x1 : '))
        b= int(input('masukkan x2      : '))
        b2= int(input('hasil modulus x2 : '))
        c= int(input('masukkan x3      : '))
        c3= int(input('hasil modulus x3 : '))

        #proses y1
        m = a*b*c
        rumus1 = (a*b*c)//a
        # print(rumus1)
        y1 = 1
        while (rumus1 * y1) % a != 1:
            y1 += 1

        print('maka nilai y1 adalah ',y1)
        #proses y2
        rumus2 = (a*b*c)//b
        y2 = 1
        while (rumus2 * y2) % b != 1:
            y2 += 1

        print('maka nilai y2 adalah ',y2)
        #proses y3
        rumus3 = (a*b*c)//c
        y3 = 1
        while (rumus3 * y3) % c != 1:
            y3 += 1

        print('maka nilai y3 adalah ',y3)
        #rumus x
        x=(rumus1*y1)*a1+(rumus2*y2)*b2+(rumus3*y3)*c3
        hasil = x % (a*b*c)
        print('maka nilai yang x yang memenuhi syarat adalah ',hasil)
        print('')
        print(f'prosesnya x mod {a} = {a1}, x mod {b} = {b2}, x mod {c} = {c3}')
        print(f'm = {m}')
        print(f'm1 = {a}x{b}x{c}//{a} = {b}x{c}x y1')
        print(f'm2 = {a}x{b}x{c}//{b} = {a}x{c}x y2')
        print(f'm3 = {a}x{b}x{c}//{c} = {a}x{b}x y3')
        print(f'y1 =({rumus1} x y1) mod {a} = 1 ==> {y1}')
        print(f'y2 =({rumus2} x y2) mod {b} = 1 ==> {y2}')
        print(f'y3 =({rumus3} x y3) mod {c} = 1 ==> {y3}')
        print(f'x =({rumus1} x {y1}) x {a1} + ({rumus2} x {y2}) x {b2} + ({rumus3} x {y3}) x {c3}')
        print(f'x = {x} mod {m}')
        print(f'x = {hasil}')

    elif pilihan==2:

        print('\n================enkripsi kata==================\n')
        kalimat = input('masukkan kalimat : ').upper() # input "SUKA"
        n1= int(input('masukkan n1 : ')) # input 3 (teman p)
        n2= int(input('masukkan n2 : ')) # input 11 (+)
        n3= int(input('masukkan n3 : ')) # input 26 (mod)

        kata="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".upper()
        kata_list=kata.split(",")

        print('\n======proses======\n')
        for karakter in kalimat:
            posisi=kata_list.index(karakter)
            rumus = (((n1 * (posisi)) + n2) % n3)

            print(f'jadi dari kata {kalimat}, kita masukkan dalam rumus ({n1} x {posisi} + {n2} mod {n3}) = {rumus} == {kata_list[rumus]}')
        print('\nmaka hasilnya adalah :======================>',end=' ')
        for karakter in kalimat:
                posisi=kata_list.index(karakter)
                rumus = (((n1 * (posisi)) + n2) % n3)
                print(kata_list[rumus],end="")

    elif pilihan==3:
        print('\n================ GCD and LCM ==================\n')
    
        a = int(input('masukkan a : '))
        b = int(input('masukkan b : '))

        gcd = math.gcd(a, b)
        lcm = (a*b)/gcd
        def prime_factors(n):
            i = 2
            factors = []
            while i * i <= b:
                if n % i:
                    i += 1
                else:
                    n //= i
                    factors.append(i)
            if n > 1:
                factors.append(b)
            return factors

        print(f'faktorisasi prima dan berbeda dari {a} = {prime_factors(a)}') 
        print(f'faktorisasi prima dan berbeda dari {b} = {prime_factors(b)}') 

        print(f'kalikan bilangan dengan pangkat yang terkecil ')

        print(f'hasil gcd nya adalah ==================================== {gcd}')

        #lcm 

        print(f'hasil lcm nya adalah ==================================== {(a*b)//gcd}')



    elif pilihan == 4:
        print('\n===================Silahkan Upgrade ke Pro we pantat====================\n')

    else:
        print('\n============ Hub wa darkoboy and noid1622 only in github.com =============\n')
        break
