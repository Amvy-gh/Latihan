nama = input("Masukan namamu = ")
umur = int(input("Masukan umurmu = "))
           
if umur >= 18 and umur <60:
    print(f"Selamat, {nama}! Anda sudah cukup umur untuk memulai tantangan permainan.")
elif umur <18 or umur > 60:
    print(f"Maaf permainan ini terlalu berat untuk umurmu wahai {anjes} yang berumur {umur} tahun")