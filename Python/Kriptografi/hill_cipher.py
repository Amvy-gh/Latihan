import numpy as np
import math

MODULO = 26
MATRIX_SIZE = 3

# Fungsi untuk membersihkan teks dari karakter non-alfabet
def clean_text(text):
    return ''.join([char.upper() for char in text if char.isalpha()])

# Fungsi untuk membuat matriks kunci
def create_hill_matrix(key):
    key_elements = key.split()  # Pisahkan input berdasarkan spasi jika angka
    
    if all(k.isalpha() for k in key_elements):  # Jika huruf
        key_elements = ''.join(key_elements).upper()
        key_elements = [ord(char) - ord('A') for char in key_elements]
    else:  # Jika angka
        key_elements = [int(k) for k in key_elements]
        if any(num < 0 or num > 25 for num in key_elements):
            raise ValueError("Angka dalam kunci harus dalam rentang 0-25!")

    # Pastikan panjang kunci adalah 9 karakter
    if len(key_elements) < 9:
        key_elements += [25] * (9 - len(key_elements))  # Tambah 'Z' jika kurang
    elif len(key_elements) > 9:
        key_elements = key_elements[:9]  # Jka lebih maka mengambil 9 karakter pertama

    matrix = np.array(key_elements).reshape(3, 3)
    return matrix

# Fungsi enkripsi Hill Cipher
def hill_encrypt(plaintext, key):
    matrix = create_hill_matrix(key)
    plaintext = clean_text(plaintext)

    # Tambahkan padding 'X' jika panjang plainteks bukan kelipatan 3
    while len(plaintext) % MATRIX_SIZE != 0:
        plaintext += 'X'

    ciphertext = ""
    for i in range(0, len(plaintext), MATRIX_SIZE):
        block = np.array([ord(c) - ord('A') for c in plaintext[i:i+MATRIX_SIZE]])
        encrypted_block = np.dot(matrix, block) % MODULO
        ciphertext += ''.join([chr(int(val) + ord('A')) for val in encrypted_block])

    return ciphertext

# Fungsi untuk mencari invers modular determinan di mod 26
def mod_inverse(matrix, mod):
    det = int(round(np.linalg.det(matrix))) % mod  # Hitung determinan
    if math.gcd(det, mod) != 1:  # Pastikan determinan punya invers di mod 26
        raise ValueError("Kunci tidak memiliki invers modulo 26, gunakan kunci lain!")

    det_inv = pow(det, -1, mod)  # Cari invers modular dari determinan

    # Hitung matriks kofaktor
    cofactors = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            minor = np.delete(np.delete(matrix, i, axis=0), j, axis=1)  # Matriks minor
            cofactors[i, j] = ((-1) ** (i + j)) * int(round(np.linalg.det(minor)))

    # Matriks adjugate = transpose dari matriks kofaktor
    adjugate = cofactors.T % mod
    inverse_matrix = (det_inv * adjugate) % mod

    return inverse_matrix.astype(int)

# Fungsi dekripsi Hill Cipher
def hill_decrypt(ciphertext, key):
    matrix = create_hill_matrix(key)
    inverse_matrix = mod_inverse(matrix, MODULO)

    plaintext = ""
    for i in range(0, len(ciphertext), MATRIX_SIZE):
        block = np.array([ord(c) - ord('A') for c in ciphertext[i:i+MATRIX_SIZE]])
        decrypted_block = np.dot(inverse_matrix, block) % MODULO
        plaintext += ''.join([chr(int(val) + ord('A')) for val in decrypted_block])

    return plaintext

def main():
    print("Silahkan Pilih:")
    print("1. Enkripsi")
    print("2. Dekripsi")

    operation_choice = input("Masukkan pilihan (1/2): ")

    if operation_choice == '1':
        filename = input("Masukkan nama file plainteks: ")
        key = input("Masukkan kunci (9 huruf atau 9 angka dipisah spasi): ")

        with open(filename, "r") as file:
            content = file.read().strip()

        ciphertext = hill_encrypt(content, key)
        with open("ciphertext.txt", "w") as file:
            file.write(ciphertext)

        print("Enkripsi selesai. File disimpan sebagai 'ciphertext.txt'.")
        print("Ciphertext:", ciphertext)

    elif operation_choice == '2':
        filename = input("Masukkan nama file cipherteks: ")
        key = input("Masukkan kunci (9 huruf atau 9 angka dipisah spasi): ")

        with open(filename, "r") as file:
            content = file.read().strip()

        try:
            plaintext = hill_decrypt(content, key)
            with open("decrypted.txt", "w") as file:
                file.write(plaintext)

            print("Dekripsi selesai. File disimpan sebagai 'decrypted.txt'.")
            print("Plaintext:", plaintext)
        except ValueError as e:
            print(f"Kesalahan: {e}")

    else:
        print("Pilihan operasi tidak valid.")

if __name__ == "__main__":
    main()
