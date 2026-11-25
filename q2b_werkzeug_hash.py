from werkzeug.security import generate_password_hash, check_password_hash

password = "MySecurePassword123"
hash1 = generate_password_hash(password)
hash2 = generate_password_hash(password)

print("Hash 1:", hash1)
print("Hash 2:", hash2)
print("Are hashes identical?", hash1 == hash2)
print("Verify Hash 1:", check_password_hash(hash1, password))
print("Verify Wrong Password:", check_password_hash(hash1, "wrongpass"))
