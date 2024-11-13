import hashlib
def hash_password(password: str) -> str:
encoded_password = password.encode('utf-8')
hash_object = hashlib.sha256()
hash_object.update(encoded_password)
return hash_object.hexdigest()
# Example usage
password = input("Enter the password: ")
hashed_password = hash_password(password)
print(f"SHA-256 hashed password: {hashed_password}")
