def caesar_cipher_encrypt(input_string, key):
    encrypted_string = ""
    for char in input_string:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted_char = chr(((ord(char) - ord('a') + key) % 26) + ord('a'))
            if is_upper:
                shifted_char = shifted_char.upper()
            encrypted_string += shifted_char
        else:
            encrypted_string += char
    return encrypted_string

# Given string
input_string = "python"

# Encryption key
key = 3

# Encrypt the string using Caesar cipher
encrypted_string = caesar_cipher_encrypt(input_string, key)

print("Original string:", input_string)
print("Encrypted string:", encrypted_string)
