import socket
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

def authenticate_server(server_socket, client_private_key):
    # Receive server's public key
    server_public_key = server_socket.recv(1024)

    # Send the client's public key to the server
    client_socket.sendall(client_public_pem)

    # Receive the encrypted challenge from the server
    encrypted_challenge = server_socket.recv(1024)

    # Decrypt the challenge with the client's private key
    decrypted_challenge = client_private_key.decrypt(
        encrypted_challenge,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Encrypt the challenge and send it back to the server
    encrypted_response = server_public_key.encrypt(
        decrypted_challenge,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    server_socket.sendall(encrypted_response)

    # Receive the authentication result from the server
    result = server_socket.recv(1024)

    if result == b"Authenticated":
        return True
    else:
        return False

# Generate key pair for the client
client_private_key, client_private_pem, client_public_pem = generate_key_pair()

# Save the client's private key to a file (to be used for decryption)
with open("client_private_key.pem", "wb") as f:
    f.write(client_private_pem)

# Create a socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("192.168.0.105", 8888))

# Authenticate the client with the server
authenticated = authenticate_server(client_socket, client_private_key)

# Print authentication result
if authenticated:
    print("Authenticated with the server")
else:
    print("Authentication failed")

# Close the connection
client_socket.close()