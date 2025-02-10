def caesar_encrypt(plaintext, shift):
    """
    Fungsi untuk mengenkripsi teks menggunakan Caesar Cipher.
    :param plaintext: Teks asli yang ingin dienkripsi.
    :param shift: Jumlah pergeseran huruf.
    :return: Teks terenkripsi (ciphertext).
    """
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():  # Hanya mengubah huruf, karakter lain tetap
            base = ord('a') if char.islower() else ord('A')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            ciphertext += new_char
        else:
            ciphertext += char  # Spasi dan karakter lainnya tetap sama
    return ciphertext

def caesar_decrypt(ciphertext, shift):
    """
    Fungsi untuk mendekripsi teks terenkripsi dengan Caesar Cipher.
    :param ciphertext: Teks terenkripsi.
    :param shift: Jumlah pergeseran huruf yang digunakan saat enkripsi.
    :return: Teks asli yang telah didekripsi.
    """
    return caesar_encrypt(ciphertext, -shift)  # Dekripsi cukup membalikkan shift

# Contoh penggunaan:
plaintext = "Anjes Bermana"
shift = 3  # Pergeseran huruf

# Enkripsi
ciphertext = caesar_encrypt(plaintext, shift)
print(f"Teks Asli    : {plaintext}")
print(f"Ciphertext   : {ciphertext}")

# Dekripsi
decrypted_text = caesar_decrypt(ciphertext, shift)
print(f"Teks Dekripsi: {decrypted_text}")

# Mencoba semua kemungkinan shift untuk brute-force dekripsi
print("\nMencoba semua kemungkinan kunci (brute-force dekripsi):")
ciphertext_unknown = "Dqmhv Ehupdqd"  # Teks terenkripsi yang ingin kita pecahkan
for k in range(1, 26):
    print(f"Shift {k}: {caesar_decrypt(ciphertext_unknown, k)}")
