#def perkalian(a,b):
#    hasil = 0
#    print(f"{a} x {b} = ")
#    for i in range(a):
#        print(f"{b}", end = '+')

#print(perkalian(6,5))

def perkalian(a,b):
    hasil = 0
    print(f"{a} x {b} = ", end="")
    for i in range(1, a+1):
        if i == a:
            print(f"{b} = ", end = "")
        else:
            print(f"{b} + ", end = "")
        hasil += b
    print(f"{hasil}")

perkalian(6,5)

def ganjil(atas,bawah):
    if bawah > atas:
        atas, bawah = bawah, atas
        
    for i in range(bawah,atas+1):
        if i % 2 != 0:
            if i == atas or i == atas - 1:
                print(i)
            else:
                print(i, end=", ")

ganjil(82,97)