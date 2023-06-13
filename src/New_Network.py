import socket
import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def generate_key_pair():
    # Generate RSA key pair
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    # Serialize the keys to PEM format
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return private_key, private_pem, public_pem

def authenticate_client(client_socket, server_private_key):
    # Receive client's public key
    client_public_key = client_socket.recv(1024)

    # Generate a random challenge
    challenge = os.urandom(16)

    # Encrypt the challenge with the client's public key
    public_key = serialization.load_pem_public_key(client_public_key)
    encrypted_challenge = public_key.encrypt(
        challenge,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Send the encrypted challenge to the client
    client_socket.sendall(encrypted_challenge)

    # Receive the response from the client
    encrypted_response = client_socket.recv(1024)

    # Decrypt the response with the server's private key
    decrypted_response = server_private_key.decrypt(
        encrypted_response,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Check if the response matches the challenge
    if decrypted_response == challenge:
        return True
    else:
        return False

# Generate key pair for the server
server_private_key, server_private_pem, server_public_pem = generate_key_pair()

# Save the server's private key to a file (to be used for decryption)
with open("server_private_key.pem", "wb") as f:
    f.write(server_private_pem)

# Create a socket and listen for incoming connections
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("Ip Address of the Server", #port number))
server_socket.listen(1)

print("Authentication Server is listening for connections...")

while True:
    # Accept a connection from a client
    client_socket, addr = server_socket.accept()
    print("Client connected:", addr)

    # Authenticate the client
    authenticated = authenticate_client(client_socket, server_private_key)

    # Send authentication result to the client
    if authenticated:
        client_socket.sendall(b"Authenticated")
        print("Client authenticated")
    else:
        client_socket.sendall(b"Authentication Failed")
        print("Client authentication failed")

    # Close the connection
    client_socket.close()
