# Toy Password Cracker (SHA-256 Demo)

A tiny, safe, academic demo showing how brute-force password cracking works using SHA-256.
Perfect for learning and portfolio use.

## How It Works

hash_password.py → takes a password, hashes it with SHA-256, saves it.

cracker.py → brute-forces all lowercase combinations (a–z, up to 4 characters) until the hash matches.

This shows why short, simple passwords get cracked instantly and why strong, long passwords matter.

## Usage
1) Hash a password
python hash_password.py

2) Run the brute-force cracker
python cracker.py


If the password is short + lowercase, you’ll see something like:

SUCCESS! Password found: cat
Attempts: 327
Time taken: 0.0032 seconds

## Disclaimer

This project is for learning only.
Do not use it on any system or account you do not own.

## Made by Srijoni Ghosh
