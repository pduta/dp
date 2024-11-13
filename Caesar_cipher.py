def caesar_cipher(text, shift, mode):
result = ""
if mode == 'decrypt':
shift = -shift
for i in range(len(text)):
char = text[i]
if char.isupper():
result += chr((ord(char) + shift - 65) % 26 + 65)
elif char.islower():
result += chr((ord(char) + shift - 97) % 26 + 97)
else:
result += char
return result

while True:
print("1. Encrypt")
print("2. Decrypt")
print("3. Exit")
choice = input("Enter your choice: ")
if choice == '1':
text = input("Enter the text to encrypt: ")
shift = int(input("Enter the shift value: "))
encrypted_text = caesar_cipher(text, shift, 'encrypt')
print(f"Encrypted text: {encrypted_text}\n")
elif choice == '2':
text = input("Enter the text to decrypt: ")
shift = int(input("Enter the shift value: "))
decrypted_text = caesar_cipher(text, shift, 'decrypt')
print(f"Decrypted text: {decrypted_text}\n")
elif choice == '3':
print("Exiting...")
break
else:
print("Invalid choice, please try again.\n")
