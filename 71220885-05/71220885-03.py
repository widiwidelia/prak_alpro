def ganjil(atas,bawah):
    if bawah > atas:
        for i in range(bawah,atas+1,-1):
            if i % 2 != 0:
                if i == atas or i == atas - 1:
                    print(i)
                else:
                    print(i, end=", ")

    else:
        for i in range(bawah,atas+1,1):
            if i % 2 != 0:
                if i == atas or i == atas - 1:
                    print(i)
                else:
                    print(i, end = ", ")

ganjil(82,97)