#suhu = float(input("Masukkan suhu = "))

#if suhu >= 38:
#    print("Anda demam")
#else :
#    print("Anda tidak demam")

#if suhu < 34:
#    print("mati kedinginan")
#elif 34 <= suhu <= 37:
#    print("aman")
#elif 38 <= suhu <= 40:
#    print("demam")
#else :
#    print("mati kepanasan")

#bilangan = int(input("Masukkan sebuah bilangan = "))

#if bilangan > 0:
#    print("Positif")
#elif bilangan < 0:
#    print("Negatif")
#else :
#    print("Nol")

#a = int(input("A = "))
#b = int(input("B = "))
#c = int(input("C = "))

#if a > b and a > c:
#    print("Yang terbesar adalah A")
#elif b > a and b > c:
#    print("Yang terbesar adalah B")
#else :
#    print("Yang terbesar adalah C")

#cigars = int(input("Masukkan jumlah cigars : "))
#is_weekend = str(input("Apakah weekend? [Y/N] : "))

#if is_weekend == "Y" and cigars >= 40:
#    print("Success")
#elif is_weekend == "Y" and 40 <= cigars <= 60:
#    print("Success")
#else :
#    print("Failed")

#if is_weekend == True and cigars >= 40:
#    return True
#  elif is_weekend == False and 40 <= cigars <= 60:
#    return True
#  else :
#    return False

nama1 = str(input("Masukkan nama 1 = "))
nama2 = str(input("Masukkan nama 2 = "))
nama3 = str(input("Masukkan nama 3 = "))

if len(nama1) >= len(nama2) and len(nama1) >= len(nama2):
    print("Nama yang paling panjang adalah",nama1)
elif len(nama2) >= len(nama1) and len(nama2) >= len(nama3):
    print("Nama yang paling panjang adalah",nama2)
else :
    print("Nama yang paling panjang adalah",nama3)