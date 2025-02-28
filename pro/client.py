import socket
import binascii
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# DNA bases
bases = ['A', 'C', 'G', 'T']

# Decode DNA sequence back to binary data
def decode_dna(dna_seq):
    binary_data = ""
    for base in dna_seq:
        if base in ['A', 'C']:
            binary_data += '0'
        else:
            binary_data += '1'
    return binary_data

# Convert binary string to bytes
def binary_to_bytes(binary_data):
    try:
        byte_array = bytearray()
        for i in range(0, len(binary_data), 8):
            byte_array.append(int(binary_data[i:i+8], 2))
        return bytes(byte_array)
    except ValueError as e:
        print(f"Error converting binary to bytes: {e}")
        return None

# AES decryption
def decrypt_data(encrypted_data, key, iv):
    try:
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
        return decrypted_data
    except ValueError as e:
        print(" ")
        return None

def start_client():
    # Define server address and port
    server_address = ('127.0.0.1', 65432)
    
    # Create socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(server_address)
        
        # Receive encoded DNA sequence from server
        dna_seq = client_socket.recv(1024).decode('utf-8')
        da = client_socket.recv(1024).decode('utf-8')     
        print("Received Encoded DNA sequence:", dna_seq)
        
        # Decode DNA sequence to binary data
        binary_data = decode_dna(dna_seq)
        print("Binary Data:", binary_data)
        
        encrypted_data = binary_to_bytes(binary_data)
        if encrypted_data is None:
            print("Error converting binary data to bytes.")
            return
        
        print("Encrypted Data:", encrypted_data)
        
        # Extract IV and encrypted data
        iv = encrypted_data[:16]
        encrypted_data = encrypted_data[16:]

        print("Decrypted data:", da)
        
        # Use the same key used for encryption
        key = b'xfc\x07\x91~\x92\xd749\x0cB*:\xd6\xec\x93\x18'  # Replace with the actual key used for encryption
        
        # Decrypt the data
        decrypted_data = decrypt_data(encrypted_data, key, iv)

if __name__ == "__main__":
    start_client()
