import numpy as np

def generate_playfair_matrix(key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    key = "".join(dict.fromkeys(key.upper() + alphabet))
    matrix = [list(key[i:i+6]) for i in range(0, 36, 6)]
    return matrix

def find_position(matrix, letter):
    for i in range(6):
        for j in range(6):
            if matrix[i][j] == letter:
                return i, j
    return None

def playfair_encrypt(text, key):
    matrix = generate_playfair_matrix(key)
    text = text.upper().replace(" ", "")
    encrypted = ""
    
    if len(text) % 2 != 0:
        text += "X"
    
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)
        
        if r1 == r2:
            encrypted += matrix[r1][(c1 + 1) % 6] + matrix[r2][(c2 + 1) % 6]
        elif c1 == c2:
            encrypted += matrix[(r1 + 1) % 6][c1] + matrix[(r2 + 1) % 6][c2]
        else:
            encrypted += matrix[r1][c2] + matrix[r2][c1]
    
    return encrypted

def hill_encrypt(text, key_matrix):
    while len(text) % 3 != 0:
        text += 'X'
    
    text_vector = [ord(c) - ord('A') for c in text.upper()]
    key_matrix = np.array(key_matrix)
    encrypted = ""
    
    for i in range(0, len(text_vector), 3):
        block = np.array(text_vector[i:i+3]).reshape(3, 1)
        result = np.dot(key_matrix, block) % 26
        encrypted += ''.join(chr(int(c) + ord('A')) for c in result.flatten())
    
    return encrypted

if __name__ == "__main__":
    plaintext = input("Masukkan teks: ")
    playfair_key = input("Masukkan kunci Playfair: ")
    hill_key = [[6, 24, 1], [13, 16, 10], [20, 17, 15]]
    
    playfair_encrypted = playfair_encrypt(plaintext, playfair_key)
    hill_encrypted = hill_encrypt(plaintext, hill_key)
    
    print(f"Playfair Cipher Encrypted: {playfair_encrypted}")
    print(f"Hill Cipher Encrypted: {hill_encrypted}")
