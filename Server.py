from flask import Flask, request, jsonify, redirect, url_for
from pymongo import MongoClient
from key_generation import RSAKeyGenerator
from encrypt_decrypt import RSASecurity

app = Flask(__name__)

# MongoDB Setup
client = MongoClient("mongodb://localhost:27017/")
db = client['INSSERVER']
users_collection = db['users']

@app.route('/')
def home():
    return "Hello, This Is The BackEnd Server Which Can Help You Use Encrypt And Decrypt Features"

@app.route('/takeuser', methods=['POST'])
def takeuser():
    data = request.get_json()
    email = data.get('Email')

    # if email not in users_collection.find({email:email}):
    #     return "Bhosdike Kuch Aur enter Kar Lawde"
    
    if not email:
        return jsonify({"error": "Email is required"}), 400
    
    # Generate RSA Keys
    key_gen = RSAKeyGenerator()
    key_gen.generate_keys()
    
    # Serialize Keys
    private_key_pem = key_gen.serialize_private_key().decode('utf-8')
    public_key_pem = key_gen.serialize_public_key().decode('utf-8')
    
    # Store in MongoDB
    user_data = {
        "email": email,
        "public_key": public_key_pem,
        "private_key": private_key_pem
    }
    users_collection.insert_one(user_data)
    
    return redirect(url_for('get_keys', email=email))

@app.route('/get_keys/<email>', methods=['GET'])
def get_keys(email):
    user = users_collection.find_one({"email": email})
    
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    return jsonify({
        "email": user["email"],
        "public_key": user["public_key"],
        "private_key": user["private_key"]
    })

@app.route('/encrypt/<email>', methods=['POST'])
def encrypt(email):
    data = request.get_json()
    plaintext = data.get('plaintext')
    
    if not plaintext:
        return jsonify({"error": "Plaintext is required"}), 400
    
    user = users_collection.find_one({"email": email})
    
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    public_key_pem = user['public_key']
    rsa_security = RSASecurity(public_key_pem=public_key_pem)
    
    ciphertext = rsa_security.encrypt(plaintext)
    
    return jsonify({"ciphertext": ciphertext.hex()})

@app.route('/decrypt/<email>', methods=['POST'])
def decrypt(email):
    data = request.get_json()
    ciphertext_hex = data.get('ciphertext')
    
    if not ciphertext_hex:
        return jsonify({"error": "Ciphertext is required"}), 400
    
    user = users_collection.find_one({"email": email})
    
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    private_key_pem = user['private_key']
    rsa_security = RSASecurity(private_key_pem=private_key_pem)
    
    ciphertext = bytes.fromhex(ciphertext_hex)
    plaintext = rsa_security.decrypt(ciphertext)
    
    return jsonify({"plaintext": plaintext})

if __name__ == '__main__':
    app.run(debug=True)
