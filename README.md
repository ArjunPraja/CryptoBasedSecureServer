# Crypto-Based Secure Server

This project demonstrates a secure server implementation using Python's cryptography concepts, specifically focusing on RSA encryption and decryption. The server leverages Flask as a web framework, MongoDB for key storage, and REST APIs for communication. Public and private keys are generated based on user emails and stored securely in MongoDB. The server encrypts and decrypts data using the RSA algorithm, ensuring data security.

## Features
- **RSA Encryption/Decryption**: The server encrypts and decrypts data using RSA algorithms.
- **Email-based Key Storage**: Public and private keys are generated and stored in MongoDB, associated with user emails.
- **REST API**: Provides a RESTful interface for interacting with the secure server.
- **Flask Framework**: Handles the server-side logic, routing, and API management.
- **MongoDB Integration**: Manages public and private key storage for users.

## Technologies Used
- **Python**: Core language for the server and cryptographic operations.
- **Flask**: Web framework to create the server and RESTful APIs.
- **MongoDB**: NoSQL database used to store the public and private keys.
- **cryptography Library**: Python library used for implementing RSA encryption and decryption.

## Project Setup

### Prerequisites
- Python 3
- Flask
- MongoDB
- cryptography library

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ArjunPraja/CryptoBasedSecureServer.git
   cd CryptoBasedSecureServer
   ```

2. Install the required Python packages:
   ```bash
   pip install [Package Name]
   ```

3. Set up MongoDB:
   - Ensure MongoDB is running locally or in your preferred environment.
   - Update the MongoDB connection URI in the Flask application.

4. Run the Flask server:
   ```bash
   python Server.py
   ```

## API Endpoints

### 1. Register User
**Endpoint**: `/takeuser`  
**Method**: POST  
**Description**: Registers a user and generates RSA public and private keys based on the provided email. The keys are stored in MongoDB.

### 2. Get key
**Endpoint**: `/get_keys/{Email}`  
**Method**: GET 
**Description**: Get The Public And Private Key Of That Perticular Mail.

### 3. Encrypt Data
**Endpoint**: `/encrypt/{Email}`  
**Method**: POST  
**Description**: Encrypts data using the user's public key.

### 4. Decrypt Data
**Endpoint**: `/decrypt/{Email}`  
**Method**: POST  
**Description**: Decrypts data using the user's private key.

## How It Works

1. **User Registration**: When a user registers via their email, the system generates an RSA key pair (public and private keys). These keys are stored securely in MongoDB, associated with the user's email.

2. **Data Encryption**: The user can send data to be encrypted via the REST API. The server retrieves the user's public key from MongoDB and encrypts the data.

3. **Data Decryption**: The user can decrypt the data by sending a decryption request. The server retrieves the corresponding private key and decrypts the data.

## Security Considerations
- Keys are stored securely in MongoDB.
- Communication between the client and the server can be secured using HTTPS.
- RSA encryption ensures that sensitive data is protected.


