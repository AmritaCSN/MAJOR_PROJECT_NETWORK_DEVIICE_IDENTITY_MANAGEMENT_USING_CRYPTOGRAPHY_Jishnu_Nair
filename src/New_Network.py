import socket
import time
from random import randint, randrange
import hashlib
import sys
import random

# Global Variables
fnb_output = []
fna_output = []
BITS = 8
Authentication_SERVER = '192.168.162.68'
port = 5900
session_counter = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Internet protocol settings
s.connect((Authentication_SERVER, port))  # Connect to Authentication_SERVER by sending NETWORK_DEVICE_ID


# Custom defined functions
def sha(data):
    sha_obj = hashlib.sha256()
    sha_obj.update(data.encode('utf-8'))
    return sha_obj.hexdigest()


def fna(data, key):
    return sha(data + key)


def fnb(data, key):
    return sha(key + data)


def send_request_to_auth_server(data):
    global session_counter
    session_counter += 1
    if session_counter >= 1000:
        session_counter = 0
    data = str(session_counter) + "|" + data
    s.send(str.encode(data))


def get_response_from_auth_server():
    response = s.recv(1024)
    return response.decode('utf-8')


def authentication_system():
    global fna_output, fnb_output
    send_request_to_auth_server('REQUEST:AUTHENTICATION')
    authentication_server_response = get_response_from_auth_server()
    if authentication_server_response == 'SEND:PUBLIC_KEY':
        public_key = str(randrange(10 ** 5, 10 ** 6))
        send_request_to_auth_server('PUBLIC_KEY:' + public_key)
        authentication_server_response = get_response_from_auth_server()
        if authentication_server_response == 'SEND:DATA':
            data = 'authentication-request-data'
            fna_output = fna(data, public_key)
            send_request_to_auth_server('FNA_OUTPUT:' + fna_output)
            authentication_server_response = get_response_from_auth_server()
            if authentication_server_response == 'SEND:DATA':
                data = 'authentication-response-data'
                fnb_output = fnb(data, public_key)
                send_request_to_auth_server('FNB_OUTPUT:' + fnb_output)
                authentication_server_response = get_response_from_auth_server()
                if authentication_server_response    == 'SUCCESS:AUTHENTICATION':
                    return True
    return False


def main():
    global fna_output, fnb_output
    if authentication_system():
        print("Authentication successful.")
    else:
        print("Authentication failed.")


if __name__ == "__main__":
    main()
