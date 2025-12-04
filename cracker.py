# cracker.py
import hashlib
import time
import itertools
import string

# Load stored hash
with open("hashed_password.txt", "r") as f:
    # .strip() is crucial to remove any invisible "newlines"
    stored_hash = f.read().strip() 

charset = string.ascii_lowercase 
max_length = 4 

print(f"Target Hash: {stored_hash}")
print("Starting brute-force attack (SHA-256)...")

start = time.time()

def crack():
    count = 0
    for length in range(1, max_length + 1):
        for guess in itertools.product(charset, repeat=length):
            count += 1
            
            # 1. Create the guess string
            guess_str = "".join(guess)
            
            # 2. Hash the guess using SHA-256
            guess_hash = hashlib.sha256(guess_str.encode('utf-8')).hexdigest()

            # 3. Compare directly (String match)
            if guess_hash == stored_hash:
                return guess_str, count

    return None, count

result, attempts = crack()
end = time.time()

if result:
    print(f"\nSUCCESS! Password found: {result}")
    print(f"Attempts: {attempts}")
    print(f"Time taken: {end - start:.4f} seconds")
else:
    print("\nPassword not found within limits.")