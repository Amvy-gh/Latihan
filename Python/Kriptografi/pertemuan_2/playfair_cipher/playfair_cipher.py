import numpy as np

def create_playfair_matrix(key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    key = "".join(dict.fromkeys(key.upper() + alphabet))
    matrix = [list(key[i:i+6]) for i in range(0, 36, 6)]
    return matrix

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None

def playfair_encrypt(text, key):
    matrix = create_playfair_matrix(key)
    text = text.upper().replace(" ", "")
    if len(text) % 2 != 0:
        text += 'X'
    
    encrypted_text = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)
        
        if row_a == row_b:
            encrypted_text += matrix[row_a][(col_a+1)%6] + matrix[row_b][(col_b+1)%6]
        elif col_a == col_b:
            encrypted_text += matrix[(row_a+1)%6][col_a] + matrix[(row_b+1)%6][col_b]
        else:
            encrypted_text += matrix[row_a][col_b] + matrix[row_b][col_a]
    
    return encrypted_text

def playfair_decrypt(text, key):
    matrix = create_playfair_matrix(key)
    dekripsi_text = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)
        
        if row_a == row_b:
            dekripsi_text += matrix[row_a][(col_a-1)%6] + matrix[row_b][(col_b-1)%6]
        elif col_a == col_b:
            dekripsi_text += matrix[(row_a-1)%6][col_a] + matrix[(row_b-1)%6][col_b]
        else:
            dekripsi_text += matrix[row_a][col_b] + matrix[row_b][col_a]
    
    return dekripsi_text

def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read().strip()

def write_to_file(filename, text):
    with open(filename, 'w') as file:
        file.write(text)

key = input("Masukkan key")
plaintext = read_from_file("plaintext.txt")
ciphertext = playfair_encrypt(plaintext, key)
write_to_file("ciphertext.txt", ciphertext)
print("Enkripsi selesai! Hasil disimpan di ciphertext.txt")

ciphertext = read_from_file("ciphertext.txt")
dekripsi_text = playfair_decrypt(ciphertext, key)
write_to_file("dekripsi.txt", dekripsi_text) 
print("Dekripsi selesai! Hasil disimpan di dekripsi.txt")