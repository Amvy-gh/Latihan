print(f"Hallo dunia !")
print(f"Saya sedang belajar pythons !")

a =  2
b = 4
c = 10
d = 100

print(f"Hasil penjumlahan {a} dan {b} adalah {a+b}")
print(f"Hasil pengurangan {b} dan {c} adalah {b+c}")
print(f"Hasil pembagian {c} dan {d} adalah {c/d}")
print(f"Hasil perkalian {d} dan {a} adalah {d*a}")

nama = input("Namamu : ")
umur = int(input ("Umurmu : "))

print(f"Halo, {nama}! Tahun depan usiamu akan menjadi {umur+1}")

print(f"Saya sedang belajar perulangan!")
print(f"Index awal untuk start (diikuti) dan diakhiri index yang tidak diikuti")

i = 1;
while i < 10 :
    print(i)
    i += 1

for g in range(0, 10):
    print(g)

for i in range (0, 11, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)

angka = int(input("Masukkan angka : "))

if angka == 0:
    print(f"{angka} adalah angka nol")
elif angka % 2 == 0:
    print(f"{angka} adalah angka genap")
else:
    print(f"{angka} adalah angka ganjil")