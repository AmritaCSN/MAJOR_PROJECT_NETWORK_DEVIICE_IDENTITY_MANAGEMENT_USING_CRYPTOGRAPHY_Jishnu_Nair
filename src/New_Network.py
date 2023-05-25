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
def or_operator(binary_characters_1, binary_characters_2):
    return '{0:0{1}b}'.format(int(binary_characters_1, 2) | int(binary_characters_2, 2), 8)


def left_logical_shift_operator(binary: list) -> list:
    result = []
    for digit in binary:
        val = int(digit) & ((1 << 8) - 1)
        result.append('{0:08b}'.format(int(val)))
    return result


def right_logical_shift_operator(binary: list) -> list:
    result = []
    for digit in binary:
        val = int(digit, 2)
        bin_format = val >> 1 if val >= 0 else (val + 0x10000000) >> 1
        result.append('{0:08b}'.format(int(bin_format)))
    return result


def left_circular_shift_operator(binary: list) -> list:
    result = []
    for bin_val in binary:
        val = bin_val[1:] + bin_val[0]
        result.append(val)
    return result


def right_circular_shift_operator(binary: list) -> list:
    result = []
    for digit in binary:
        temp = digit[-1] + digit[0:-1]
        result.append(temp)
    return result


def convert_to_binary_system(input: str) -> list:
    proc_val = ' '.join(format(ord(char), 'b') for char in input).split()
    result = []
    for entry in proc_val:
        zeros = 0
        zeros += (8 - len(entry))
        result.append((zeros * '0') + entry)
    return result


def binary_to_decimal_system(binary):
    decimal, i = 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


def convert_to_ascii_system(input: list) -> str:
    binary = ""
    for i in input:
        binary += i
    str_data = ""
    for i in range(0, len(binary), 8):
        temp_data = int(binary[i:i + 8])
        decimal_data = binary_to_decimal_system(temp_data)
        str_data = str_data + chr(decimal_data)
    return str_data


def div_binary_into_n_parts_system(a, n):
    k, m = divmod(len(a), n)
    four_parts_temp = list((a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n)))
    max_length = max(len(part) for part in four_parts_temp)
    for i in range(len(four_parts_temp)):
        if len(four_parts_temp[i]) < max_length:
            four_parts_temp[i].append("11111111")
    return four_parts_temp


def complex_xor_logic(binary_list_one, binary_list_two):
    length1 = len(binary_list_one)
    length2 = len(binary_list_two)
    xored_binary = []
    i = 0
    while i < length1 and i < length2:
        binary_val_1 = binary_list_one[i]
        binary_val_2 = binary_list_two[i]
        xor_result = or_operator(binary_val_1, binary_val_2)
        xored_binary.append(xor_result)
        i += 1
    return xored_binary


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
