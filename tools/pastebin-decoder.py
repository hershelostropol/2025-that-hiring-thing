
import binascii
import base64
import json

def xor_encrypt(text: bytes):
    """XOR encrypt/decrypt (same operation)"""
    XOR_KEY = b"!!!HappyPenguin1950!!!"
    encrypted_text = bytearray()
    for i in range(len(text)):
        encrypted_text.append(text[i] ^ XOR_KEY[i % len(XOR_KEY)])
    return bytes(encrypted_text)

def decode(encoded: str) -> str:
    """Decode exactly like tsunami malware does"""
    encoded_bytes = binascii.unhexlify(encoded)
    encoded_bytes = xor_encrypt(encoded_bytes)  # xor_decrypt is same as xor_encrypt
    encoded = base64.b64decode(encoded_bytes).decode()
    return encoded[::-1]

def decrypt_payload(input: str):
    """Decrypt the payload using tsunami's decode function"""

    # Read the JSON payload
    payload = json.loads(input)

    # Extract hex message
    hex_message = payload['message']

    # Decode using tsunami's method
    decrypted = decode(hex_message)

    return decrypted

def defang_url(url: str) -> str:
    """Defang the URL"""
    return url.replace('.', '[.]')

if __name__ == "__main__":
    with open("NAME_OF_RAW_PASTEBIN_CONTENT_FILE", 'r') as f:
        json_payload = binascii.unhexlify(f.read())
        payload = decrypt_payload(json_payload)
        print(defang_url(payload))