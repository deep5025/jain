from Crypto.Cipher import AES
import base64

# Set the secret key and the initialization vector
secret_key = b'\xbfN\x0f\x17\x9bG\xe6\xa6\x1di\xb5\xaa\xe2\xb0\xe3\xba
iv = b'\xbe\xc5\x03\x14g\xfd\xac\xf2\xbc9\\!\xb5\xdahN:\xbd~\xd9\xe02?A\xc7\xe9\x12p%JiG'

# Set the message to be encrypted
message = b'This is a secret message!'

# Pad the message to a multiple of 16 bytes
padding_length = 16 - (len(message) % 16)
message += bytes([padding_length]) * padding_length

# Create a new AES cipher object
cipher = AES.new(secret_key, AES.MODE_CBC, iv)

# Encrypt the message
encrypted_message = cipher.encrypt(message)

# Encode the encrypted message in base64
encoded_message = base64.b64encode(encrypted_message)

# Print the encoded message
print(encoded_message.decode())
