# PMPC Secure Messaging System

## Description
This project implements a hybrid cryptographic system combining a custom Prime Mirror Polyalphabetic Cipher (PMPC) with AES-GCM encryption to provide secure text and file communication.

## Features
- Custom PMPC encryption and decryption
- AES-GCM encryption for confidentiality and integrity
- Case-preserving encryption
- File encryption and decryption support
- Secure key derivation using SHA-256
- Portable encrypted files with embedded nonce
- Error handling for wrong key and tampering

## How It Works
Plaintext → PMPC → AES-GCM → Ciphertext  
Ciphertext → AES-GCM Decrypt → PMPC Decrypt → Plaintext  

## Security Features
- AES-GCM ensures confidentiality and integrity
- Random nonce prevents pattern attacks
- Authentication tag prevents tampering
- SHA-256 strengthens weak keys

## Technologies Used
- Python
- Flask
- Cryptography Library

## How to Run
1. Install dependencies  
   pip install flask cryptography  

2. Run the application  
   python app.py  

3. Open browser  
   http://127.0.0.1:5000  

## Author
Pooja
