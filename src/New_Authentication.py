import hashlib
import sys
import socket
import random
import time

BITS = 8

fnb_output = []
fna_output = []
session_counter = 0
address = []


def Authentication_SERVER():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((NETWORK_DEVICE_ID, port))
    except socket.error as message:
        print(message)
        return s

def right_circular_shift_OPERATOR(binary):
    result = []
    for digit in binary:
        temp = digit[-1] + digit[0:-1]
        result.append(temp)
    return result


def convert_to_binary_SYSTEM(input_str):
    proc_val = ' '.join(format(ord(char), 'b') for char in input_str).split()
    result = []
    for entry in proc_val:
        zeros = BITS - len(entry)
        result.append((zeros * '0') + entry)
    return result


def binary_to_decimal_SYSTEM(binary):
    decimal, i = 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


def convert_to_ascii_SYSTEM(input_list):
    binary = ""
    for i in input_list:
        binary += i
    str_data = ""
    for i in range(0, len(binary), BITS):
        temp_data = int(binary[i:i + BITS])
        decimal_data = binary_to_decimal_SYSTEM(temp_data)
        str_data = str_data + chr(decimal_data)
    return str_data


def div_binary_into_n_parts_SYSTEM(a, n):
    k, m = divmod(len(a), n)
    four_parts_temp = list((a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n)))
    max_length = max(len(part) for part in four_parts_temp)
    for i in range(len(four_parts_temp)):
        if len(four_parts_temp[i]) < max_length:
            four_parts_temp[i].append("0" * BITS)
    return four_parts_temp


def complex_xor_LOGIC(binary_list_one, binary_list_two):
    length1 = len(binary_list_one)
    length2 = len(binary_list_two)
    result = []
    num = min(length1, length2)
    max_val = max(length1, length2)
    for i in range(num):
        result.append(xor_OPERATOR(binary_list_one[i], binary_list_two[i]))
    if length1 > length2:
        for i in range(num, max_val):
            result.append(xor_OPERATOR(binary_list_one[i], "0" * BITS))
    elif length1 < length2:
        for i in range(num, max_val):
            result.append(xor_OPERATOR("0" * BITS, binary_list_two[i]))
    return result


def xor_OPERATOR(binary_1, binary_2):
    return '{0:0{1}b}'.format(int(binary_1, 2) ^ int(binary_2, 2), BITS)


def encrypt_string(input_string, key):
    binary_input = convert_to_binary_SYSTEM(input_string)
    binary_key = convert_to_binary_SYSTEM(key)
    binary_key_parts = div_binary_into_n_parts_SYSTEM(binary_key, 4)
    num_parts = len(binary_input)
    for i in range(num_parts):
        fnb_output.append(complex_xor_LOGIC(binary_input[i], binary_key_parts[i % 4]))
    encrypted_data = ""
    for i in fnb_output:
        encrypted_data += i
    return encrypted_data


def sha(input_string):
    return hashlib.sha256(input_string.encode()).hexdigest()


def main():
    global s
    global NETWORK_DEVICE_ID
    global port
    NETWORK_DEVICE_ID = '127.0.0.1'
    port = 65432
    s = Authentication_SERVER()
    conn = LINK_ESTABLISHED()
    Transmission_LINK(conn)


def Transmission_LINK(conn):
    global session_counter
    global address
    session_counter += 1
    if session_counter == 1:
        time.sleep(1)
        address = []
        address.append(socket.gethostbyname(socket.gethostname()))
        address.append(str(random.randint(50000, 60000)))
        print("Random IP address: {}".format(address[0]))
        print("Random Port: {}".format(address[1]))
        conn.send(str(address[0]).encode())
        time.sleep(1)
        conn.send(str(address[1]).encode())
        time.sleep(1)
        conn.send(str(session_counter).encode())
    else:
        if session_counter == 2:
            conn.send(str(address[0]).encode())
            time.sleep(1)
            conn.send(str(address[1]).encode())
            time.sleep(1)
            conn.send(str(session_counter).encode())
            time.sleep(1)
            encrypted_string = encrypt_string("Hello", "key")
            conn.send(encrypted_string.encode())
        else:
            print("Invalid Session")


if __name__ == "__main__":
    main()
