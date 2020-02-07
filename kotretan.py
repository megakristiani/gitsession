ans=True
while ans:
    print(""" Main Menu
    1. Belajar
    2. Belanja
    3. Exit
    """)
    jwb=input("No. menu : ")
    if jwb=="1":
        print("""Oke, kita belajar! Kamu mau belajar apa?
        1. Luas Segitiga
        2. Luas Trapesium
        3. Exit
        """)
        jwba=(input("Masukin no pilihan kamu disini : "))
        if jwba=="1":
            a=int(input("Masukan panjang alas dalam cm : "))
            b=int(input("Masukan panjang tinggi dalam cm : "))
            luas_segitiga=((a*b)/2)
            print(f'Luas segitiga = {a} cm x {b} cm / 2 = {luas_segitiga} cm')
        elif jwba=="2":
            d=int(input("Masukan alas trapesium dalam cm : "))
            e=int(input("Masukan tinggi trapesium dalam cm : "))
            f=int(input("Masukan atap trapesium dalam cm : "))
            luas_trapesium=(e*(d+f))/2
            print(f'Luas Trapesium = ({e} cm *({d} cm + {f} cm))/2 = {luas_trapesium}')
        elif jwba=="3":
            break
        else:
            print("no. yang kamu masukan salah.")
    elif jwb=="2":
        print("""Mau belanja apa?
        1. Makanan
        2. Exit""")
        jwbn=(input("Masukan no. pilihan kamu disini : "))
        if jwbn=="1":
            print("Mau beli apa?")
            item1=int(input("Tempe mendoan (Rp.2000) : "))
            item2=int(input("Tahu sumedang (Rp.3000) : "))
            item3=int(input("Indomie ayam bawang (Rp.5000) : "))
            total=(2000*item1)+(3000*item2)+(5000*item3)
            print(f'total belanjaan kamu adalah Rp.{total}. Silakan kamu transfer ke virtual akun. Terimakasih')
        elif jwbn=="2":
            break
        else:
            print("no. yang kamu masukan salah.")
    elif jwb=="3":
        break
    else:
        print("no. yang kamu masukan salah.")
    
        
            
            


