from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Generate a 16-byte key
key = get_random_bytes(16)

# Create a cipher object using the key
cipher = AES.new(key, AES.MODE_EAX)

# Encrypt some data
# strin = input()
data = b"TGTCAGTAGCTTTATTAAAGTCTACCAGTTCAGAGCGTAGAAACGAAACGGAACATTAGTTCCGGTCAGGACCGTCCTCCCAACTCGAAGATAGTGCTATTGTTAAGCCTGTCTATATTATGACAGCGCATTTGCGTAGCTTAGGTAGGCCGAATGGACAACACCAGGTGCTCCGCATTCTAGCCATGATGTGCGCTTTTGGGCGCAGCCTTGCCATTAGGTTAATTGAGCCGAAACTGTGATACTGCAACATATG"
nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(data)

print(f'Key: {key}')
print(f'Nonce: {nonce}')
print(f'Ciphertext: {ciphertext}')
print(f'Tag: {tag}')
