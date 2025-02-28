import socket
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import random

# DNA bases
bases = ['A', 'C', 'G', 'T']

# Encode data into DNA sequence
def encode_data(data):
    dna_seq = ""
    for byte in data:
        # Convert byte to binary and pad with zeros
        binary = bin(byte)[2:].zfill(8)
        # Encode each bit into a DNA base
        for bit in binary:
            if bit == '0':
                dna_seq += random.choice(['A', 'C'])
            else:
                dna_seq += random.choice(['G', 'T'])
    return dna_seq

# AES encryption
def encrypt_data(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    return cipher.iv + ct_bytes

def start_server():
    # Define server address and port
    server_address = ('127.0.0.1', 65432)
    
    # Create socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(server_address)
        server_socket.listen()

        print("Server is listening on", server_address)
        
        # Wait for a client connection
        connection, client_address = server_socket.accept()
        with connection:
            print("Connected by", client_address)
            da = input("Enter the data: ")
            data = da.encode('utf-8')
            
            # Generate a random key for AES encryption
            key = get_random_bytes(16)
            encrypted_data = encrypt_data(data, key)
            dna_seq = encode_data(encrypted_data)
            print("Sending Encoded DNA sequence:", dna_seq)
            
            # Send encoded DNA sequence to client
            connection.sendall(dna_seq.encode('utf-8') )
            connection.sendall(da.encode('utf-8'))

if __name__ == "__main__":
    start_server()
