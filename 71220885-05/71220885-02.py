matkul = int(input("Masukkan jumlah matkul = "))
list_nilai = []
jumlah_nilai = 0
for i in range(matkul):
    nilai = (input(f"Masukkan matkul {i+1} = "))
    list_nilai.append(nilai)
for i in range(matkul):
    if list_nilai[i] == 'A':
        jumlah_nilai = jumlah_nilai + 4
    elif list_nilai[i] == 'B':
        jumlah_nilai = jumlah_nilai + 3
    elif list_nilai[i] == 'C':
        jumlah_nilai = jumlah_nilai + 2
    elif list_nilai[i] == 'D':
        jumlah_nilai = jumlah_nilai + 1

print(f"IPS-nya yaitu : {round((((jumlah_nilai*3)/matkul)/3),2)}")