# MAJOR_PROJECT_NETWORK_DEVIICE_IDENTITY_MANAGEMENT_USING_CRYPTOGRAPHY_Jishnu_Nair

## Introduction
The "Network Device Identity Management using Cryptography" project seeks to provide solutions for the security issues brought on by the growing use of wearable and smart IoT devices. Due to the sensors and Internet connectivity found in these devices, there is a need for strong authentication and encryption procedures.

## Authenticated Encryption Techniques
To guarantee the confidentiality and integrity of data, authenticated encryption techniques, a subset of symmetric key cryptographic algorithms, are used. Authenticity ensures data integrity and validates its origins, while confidentiality prohibits unauthorised dissemination. This project acknowledges the requirement for authentication of some data elements, such as packet headers, which call for protection without encryption.

## Proposed Framework
By developing a algorithm for user identification during network device access attempts, this project's main goal is to reduce identity-based assaults on network devices. To protect network devices from fraudulent operations, the suggested framework makes use of cryptography.

A dynamic key generation approach that generates numerous random keys, improving randomness and boosting security, is incorporated into the framework. The Authentication server uses two functions, A and B, to execute logical and bitwise operations to create distinct random secrets during the exchange of secret seed pairs. 

The SHA256 hashing technique and dynamic key generation are used to increase the security of network devices and provide a more robust identity management system.

## Conclusion
By using the complex cryptographic technique presented in this research, network device security may be significantly increased, reducing the risk of identity-based attacks. A trustworthy and secure identity management system for network devices is created using dynamic key generation.

## Steps to execute the code

1. Begin by ensuring that both connecting devices, such as your laptop and the Raspberry Pi, are connected to the same network.

2. You will find two source files that have been provided: "Net.py" and "Client.py". "Net.py" functions as the server, while "Client.py" serves as the client. To establish a secure connection, it is necessary to specify the IP address and port number.

3. The IP address of the Raspberry Pi should be indicated within the code of "Net.py" which will be executed on the laptop. Similarly, the IP address of the laptop should be mentioned within the code of "Client.py" to be executed on the Raspberry Pi.

4. Once the IP addresses have been appropriately specified, begin by executing the "Net.py" program on the laptop. Following that, run the "Client.py" code on the Raspberry Pi.

Please note that these steps should be followed in the sequence provided to ensure the proper execution of the code.


This repository contains an src folder in which a network and authentication file is uploaded...



