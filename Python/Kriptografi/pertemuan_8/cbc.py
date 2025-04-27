import itertools

# --------------------------------------------
# 1. Konversi teks ke blok 4-bit
# --------------------------------------------
def text_to_4bit_blocks(plaintext: str) -> list[list[int]]:
    """
    Ubah string ASCII (tanpa spasi) ke blok-4bit.
    Contoh: 'h' -> 01101000 -> [0,1,1,0] dan [1,0,0,0]
    """
    blocks = []
    for ch in plaintext.replace(' ', ''):
        byte = ord(ch)
        bits8 = [(byte >> i) & 1 for i in reversed(range(8))]
        # pecah 8-bit menjadi dua 4-bit
        blocks.append(bits8[:4])
        blocks.append(bits8[4:])
    return blocks

# --------------------------------------------
# 2. Generate keystream LFSR 4-bit
# --------------------------------------------
def generate_lfsr_keystream(
    seed: list[int], taps: list[int], length: int
) -> list[list[int]]:
    """
    LFSR 4-bit dengan seed (list of 4 bits), tap positions, dan jumlah output.
    taps = [0, 2] untuk polinomial x^4 + x^2 + 1.
    """
    state = seed.copy()
    stream = []
    for _ in range(length):
        stream.append(state.copy())
        # feedback = XOR dari semua tap bits
        fb = 0
        for t in taps:
            fb ^= state[t]
        # shift right dan masukkan feedback di MSB
        state = [fb, state[0], state[1], state[2]]
    return stream

# --------------------------------------------
# 3. Fungsi wrapping (rotasi kanan)
# --------------------------------------------
def rotate_right(bits: list[int], r: int) -> list[int]:
    """Rotasi kanan r bit untuk list bit kecil (contoh 4-bit)"""
    n = len(bits)
    r %= n
    return bits[-r:] + bits[:-r]

# --------------------------------------------
# 4. Enkripsi CBC per blok 4-bit
# --------------------------------------------
def encrypt_cbc(
    plain_blocks: list[list[int]],
    keystream: list[list[int]],
    iv: list[int],
    rotate: int = 2
) -> list[list[int]]:
    """
    Enkripsi CBC:
      C_0 = IV
      C_i = RotR( (P_i xor C_{i-1}) xor K_i )
    """
    cipher_blocks = []
    prev = iv.copy()
    for i, p in enumerate(plain_blocks):
        inter = [p[j] ^ prev[j] for j in range(4)]
        xored = [inter[j] ^ keystream[i][j] for j in range(4)]
        c = rotate_right(xored, rotate)
        cipher_blocks.append(c)
        prev = c
    return cipher_blocks

# --------------------------------------------
# 5. Gabungkan blok cipher jadi hex string
# --------------------------------------------
def blocks_to_hex(cipher_blocks: list[list[int]]) -> str:
    bits = ''.join(''.join(str(b) for b in blk) for blk in cipher_blocks)
    hex_str = ''
    # split setiap 8 bit
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        hex_str += f"{int(byte, 2):02x}"
    return hex_str

# --------------------------------------------
# Contoh Input dan Cara Panggil (per tahap)
# --------------------------------------------
if __name__ == '__main__':
    # Input dasar:
    plaintext = 'hello world'
    seed       = [1, 0, 1, 0]    # U0 = 1010
    taps       = [0, 2]          # polinomial x^4 + x^2 + 1
    iv         = [0, 0, 1, 1]    # IV = 0011

    # 1. Konversi teks → blok 4-bit
    plain_blocks = text_to_4bit_blocks(plaintext)
    print('Blok 4-bit:', plain_blocks)

    # 2. Generate keystream sebanyak len(plain_blocks)
    ks = generate_lfsr_keystream(seed, taps, len(plain_blocks))
    print('Keystream:', ks)

    # 3. Enkripsi CBC
    cipher_blocks = encrypt_cbc(plain_blocks, ks, iv, rotate=2)
    print('Blok Cipher:', cipher_blocks)

    # 4. Output hex
    cipher_hex = blocks_to_hex(cipher_blocks)
    print('Cipher (hex):', cipher_hex)
