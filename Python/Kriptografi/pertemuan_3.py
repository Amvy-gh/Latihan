import numpy as np

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Error: Tidak dapat membuka file {filename}")
        exit(1)

def write_to_file(filename, text):
    with open(filename, 'w') as file:
        file.write(text)

def encrypt_playfair(plaintext, key):
    # Implementasi Playfair Cipher di sini
    return "Encrypted Playfair Cipher Text"

def encrypt_hill(plaintext, key_matrix):
    # Implementasi Hill Cipher di sini
    return "Encrypted Hill Cipher Text"

def main():
    filename = input("Masukkan nama file plainteks: ")
    plaintext = read_file(filename)
    
    choice = int(input("Pilih algoritma enkripsi:\n1. Playfair Cipher\n2. Hill Cipher\nPilihan: "))
    
    encrypted_text = ""
    if choice == 1:
        key = input("Masukkan kunci Playfair Cipher: ")
        encrypted_text = encrypt_playfair(plaintext, key)
    elif choice == 2:
        print("Masukkan kunci Hill Cipher (3x3 matrix), dipisah dengan spasi:")
        key_matrix = []
        for _ in range(3):
            row = list(map(int, input().split()))
            key_matrix.append(row)
        key_matrix = np.array(key_matrix)
        encrypted_text = encrypt_hill(plaintext, key_matrix)
    else:
        print("Pilihan tidak valid!")
        return
    
    output_filename = input("Masukkan nama file output untuk menyimpan cipherteks: ")
    write_to_file(output_filename, encrypted_text)
    
    print(f"Enkripsi selesai! Hasil disimpan di {output_filename}")

if __name__ == "__main__":
    main()
