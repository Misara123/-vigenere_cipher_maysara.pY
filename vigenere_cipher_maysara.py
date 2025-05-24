# Vigenère Cipher Encryption
# Author: MAYSARA ESSAM

def vigenere_encrypt(plaintext, keyword):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    plaintext = plaintext.replace(" ", "").upper()
    keyword = keyword.upper()

    # Repeat the keyword to match the length of the plaintext
    key = (keyword * ((len(plaintext) // len(keyword)) + 1))[:len(plaintext)]

    ciphertext = ''
    for p, k in zip(plaintext, key):
        p_index = alphabet.index(p)
        k_index = alphabet.index(k)
        c_index = (p_index + k_index) % 26
        ciphertext += alphabet[c_index]

    return ciphertext

# Input data
plaintext = "DEFEND THE EAST WALL OF THE CASTLE"
keyword = "VIGENERECIPHER"

# Encrypt and output the result
encrypted = vigenere_encrypt(plaintext, keyword)
print("Encrypted text:", encrypted)
