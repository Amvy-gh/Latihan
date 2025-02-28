file_path = "C:\laragon\www\Latihan\Python\Kriptografi\pertemuan_3\ciphertext.txt"

# Membaca file dan menghitung huruf
letter_count = {}

with open(file_path, "r", encoding="utf-8") as file:
    text = file.read().lower()  # Baca dan ubah jadi huruf kecil

    for char in text:
        if char.isalpha():  # Hanya hitung huruf
            letter_count[char] = letter_count.get(char, 0) + 1

# Menampilkan hasil
for letter, count in sorted(letter_count.items()):
    print(f"{letter}: {count}")
