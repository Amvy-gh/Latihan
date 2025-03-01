from collections import Counter
import string
import os

# Perbaiki path file dengan raw string
input_file_path = r"C:\laragon\www\Latihan\Python\Kriptografi\pertemuan_3\ciphertext.txt"
output_file_path = r"C:\laragon\www\Latihan\Python\Kriptografi\pertemuan_3\decrypted.txt"

# Cek apakah file ada
if not os.path.exists(input_file_path):
    print("File tidak ditemukan! Pastikan path benar.")
    exit()

# Baca isi file
with open(input_file_path, "r", encoding="utf-8") as file:
    ciphertext = file.read()

# Hilangkan karakter non-huruf dan ubah menjadi huruf kecil
ciphertext_clean = "".join(filter(lambda x: x in string.ascii_letters, ciphertext.lower()))

# Cek apakah ciphertext kosong
if not ciphertext_clean:
    print("Ciphertext kosong! Periksa file input.")
    exit()

# Fungsi untuk mendekripsi Vigenere Cipher
def vigenere_decrypt(ciphertext, key):
    decrypted_text = []
    key_length = len(key)
    alphabet = string.ascii_lowercase

    for i, char in enumerate(ciphertext):
        if char in alphabet:
            shift = ord(key[i % key_length]) - ord('a')
            new_index = (alphabet.index(char) - shift) % 26
            decrypted_text.append(alphabet[new_index])
        else:
            decrypted_text.append(char)

    return "".join(decrypted_text)

# Dekripsi dengan kunci "warlord"
decrypted_text_vigenere = vigenere_decrypt(ciphertext_clean, "warlord")

# Simpan hasil dekripsi ke file
with open(output_file_path, "w", encoding="utf-8") as file:
    file.write(decrypted_text_vigenere)

# Menampilkan pesan sukses dan letak hasil dekripsi
print(f"Hasil dekripsi telah disimpan di: {output_file_path}")
