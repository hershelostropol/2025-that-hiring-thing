#!/usr/bin/env python3
"""
Byte array decoder to defanged URL for malware analysis
"""

# Byte array from the malware sample
byte_array = [
    104, 116, 116, 112, 115, 58, 47, 47, 97, 112, 105, 46, 110, 112, 111, 105,
    110, 116, 46, 105, 111, 47, 50, 99, 52, 53, 56, 54, 49, 50, 51, 57, 99, 51,
    98, 50, 48, 51, 49, 102, 98, 57
]

# Decode the bytes to string
decoded_url = bytes(byte_array).decode('utf-8')

# Defanged version for safe display
defanged_url = decoded_url.replace('.', '[.]')
print(f"Defanged URL: {defanged_url}")