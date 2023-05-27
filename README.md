# MAJOR_PROJECT_NETWORK_DEVIICE_IDENTITY_MANAGEMENT_USING_CRYPTOGRAPHY_Jishnu_Nair

## Introduction
The "Network Device Identity Management using Cryptography" project seeks to provide solutions for the security issues brought on by the growing use of wearable and smart IoT devices. Due to the sensors and Internet connectivity found in these devices, there is a need for strong authentication and encryption procedures.

## Authenticated Encryption Techniques
To guarantee the confidentiality and integrity of data, authenticated encryption techniques, a subset of symmetric key cryptographic algorithms, are used. Authenticity ensures data integrity and validates its origins, while confidentiality prohibits unauthorised dissemination. This project acknowledges the requirement for authentication of some data elements, such as packet headers, which call for protection without encryption.

## Proposed Framework
By developing a algorithm for user identification during network device access attempts, this project's main goal is to reduce identity-based assaults on network devices. To protect network devices from fraudulent operations, the suggested framework makes use of cryptography.

A dynamic key generation approach that generates numerous random keys, improving randomness and boosting security, is incorporated into the framework. The Authentication server uses two functions, A and B, to execute logical and bitwise operations to create distinct random secrets during the exchange of secret seed pairs. The SHA256 hashing algorithm uses these secrets as input to create a 256-bit hash.

The SHA256 hashing technique and dynamic key generation are used to increase the security of network devices and provide a more robust identity management system.

## Conclusion
The security of network devices can be greatly strengthened by implementing the sophisticated cryptographic strategy described in this research, lowering the danger of identity-based assaults. The SHA256 hashing algorithm and dynamic key generation work together to create a reliable and secure identity management system for network devices.

## Steps to execute the code

1. Begin by ensuring that both connecting devices, such as your laptop and the Raspberry Pi, are connected to the same network.

2. You will find two source files that have been provided: "Network.py" and "Authentication.py". "Network.py" functions as the server, while "Authentication.py" serves as the client. To establish a secure connection, it is necessary to specify the IP address and port number.

3. The IP address of the Raspberry Pi should be indicated within the code of "Network.py" which will be executed on the laptop. Similarly, the IP address of the laptop should be mentioned within the code of "Authentication.py" to be executed on the Raspberry Pi.

4. Once the IP addresses have been appropriately specified, begin by executing the "Network.py" program on the laptop. Following that, run the "Authentication.py" code on the Raspberry Pi.

Please note that these steps should be followed in the sequence provided to ensure the proper execution of the code.


This repository contains an src folder in which a network and authentication file is uploaded...



