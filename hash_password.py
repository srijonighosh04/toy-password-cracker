# hash_password.py
import hashlib

password = input("Enter a password to hash (for demo purposes): ")

# We use SHA-256 this time. It is very fast.
# encode() turns string into bytes, hexdigest() turns hash into readable string
hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

with open("hashed_password.txt", "w") as f:
    f.write(hashed_password)

print(f"Password '{password}' hashed (SHA-256) and saved to hashed_password.txt!")