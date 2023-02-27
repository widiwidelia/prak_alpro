#def seleksi_kkn(sks):
    #return True: jika sks >= 110
    #return False jika sks < 110
#    if sks >= 110:
#        return True
#    else:
#        return False
    
#program utama
#sks = int(input("Masukkan jumlah sks yang sudah ditempuh : "))
#hasil_seleksi = seleksi_kkn(sks)
#output
#if hasil_seleksi == True:
#    print("Boleh mengambil KKN")
#else:
#    print("Belum boleh mengambil KKN")

#optional argument, argumen bisa hanya satu
#def hitung_belanja(belanja, diskon=0):
#    bayar = belanja - (belanja * diskon)/100
#    return bayar

#menukar dua nilai
#def tukar(a,b):
#    temp = b #temporary sebagai storage tambahan
#    b = a
#    a = temp
#    return a,b

#a = int(input("Masukkan nilai A = "))
#b = int(input("Masukkan nilai B = "))
#print(f"Sebelum ditukar, nilai A adalah {a} dan nilai B adalah {b}")
#a,b = tukar(a,b)
#print(f"Setelah ditukar, nilai A adalah {a} dan nilai B adalah {b}")

#variabel yang ada dalam fungsi tidak berkaitan dengan variable yang ada di program utama
#nilai variabel dalam fungsi terisolasi
#variable dalam fungsi dinamakan variable lokal
#menggunakan struktur data yang bernama Tuple = kumpulan nilai
#jumlah tuple harus sama (a,b = dua hasil)

#Tuple
#c = 10
#d = 15
#a,b = b,a
#print(a)
#print(b) 

#def tagihan_listrik(pemakaian, golongan=3):
#print(tagihan_listrik(130)) #optional argument (golongan=3)
#print(tagihan_listrik(80,4)) #ternary operator
#print(tagihan_listrik(golongan=1, pemakaian=175)) #named argument

#buatlah fungsi cek(a,b,c) yg menentukan apakah digit paling kiri sama
#def cek(a,b,c):
#    if a ** 2 + b ** 2 == c ** 2:
#        print(f"{a} ** 2 + {b} ** 2 = {c} ** 2")
#        return True
#    elif a ** 2 + c ** 2 == b ** 2:
#        print(f"{a} ** 2 + {c} ** 2 = {b} ** 2")
#        return True
#    elif b ** 2 + c ** 2 == a ** 2:
#        print(f"{b} ** 2 + {c} ** 2 = {a} ** 2")
#        return True
#    else:
#        return False
    #pass #artinya 'lewati' (jika belum menulis fungsi)

#a = int(input("Masukkan a = "))
#b = int(input("Masukkan b = "))
#c = int(input("Masukkan c = "))

#cek(a,b,c)

#def runner_up(a,b,c,d,e):
#    data = [a,b,c,d,e]
#    data = sorted(data) atau data.sort()
#    return data[1]

#print(runner_up(a,b,c,d,e))

def n_hari_berikutnya(nama, n):
    n = n % 7
    #hari = ["senin","selasa","rabu","kamis","jumat","sabtu","minggu"]
    #bobot = hari.index(nama)
    #bobot = (bobot + n) % 7
    #print(hari[bobot])
    '''
    senin = 0
    selasa = 1
    rabu = 2
    kamis = 3
    jumat = 4
    sabtu = 5
    minggu = 6
    '''
    bobot = 0
    if nama == "selasa":
        bobot = 1
    elif nama == "rabu":
        bobot = 2
    elif nama == "kamis":
        bobot = 3
    elif nama == "jumat":
        bobot = 4
    elif nama == "sabtu":
        bobot = 5
    elif nama == "minggu":
        bobot = 6
    
    total = (bobot + n) % 7
    if total == 0:
        print("senin")
    elif total == 1:
        print("selasa")
    elif total == 2:
        print("rabu")
    elif total == 3:
        print("kamis")
    elif total == 4:
        print("jumat")
    elif total == 5:
        print("sabtu")
    elif total == 6:
        print("minggu")   

nama = input("Masukkan hari = ")
n = int(input("Berapa hari kemudian? = "))
n_hari_berikutnya(nama,n)