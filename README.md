# MAJOR_PROJECT_NETWORK_DEVIICE_IDENTITY_MANAGEMENT_USING_CRYPTOGRAPHY_Jishnu_Nair
# Network Device Identity Management: Enhancing Security through Cryptographic Techniques

## Introduction
The "Network Device Identity Management using Cryptography" project addresses the security challenges arising from the increasing adoption of smart IoT and wearable devices. These devices possess sensors and Internet connectivity, which introduces new vulnerabilities and necessitates robust authentication and encryption mechanisms.

## Authenticated Encryption Techniques
Authenticated encryption techniques, a subset of symmetric key cryptographic algorithms, are employed to ensure the confidentiality and integrity of data. Confidentiality prevents unauthorized disclosure, while authenticity guarantees data integrity and verifies its source. This project recognizes the need for authentication of specific data components, such as packet headers, which require protection without encryption.

## Proposed Framework
The primary objective of this project is to mitigate identity-based attacks on network devices by implementing an advanced algorithm for user identification during network device access attempts. The proposed framework utilizes cryptography to secure network devices from fraudulent activities.

The framework incorporates a dynamic key generation model that produces multiple random keys, increasing randomness and enhancing security. During the exchange of secret seed pairs by the Authentication server, two functions, A and B, perform logical and bitwise operations to generate unique random secrets. These secrets serve as input to the SHA256 hashing algorithm, producing a 256-bit hash.

The utilization of dynamic key generation and the SHA256 hashing algorithm strengthens the security of network devices, offering a more resilient identity management system.

## Conclusion
By adopting the advanced cryptographic approach outlined in this project, the security of network devices can be significantly fortified, thereby reducing the risk of identity-based attacks. The combination of dynamic key generation and the SHA256 hashing algorithm contributes to a robust and secure identity management system for network devices.


This repository contains an src folder in which a network and authentication file is uploaded...



