def encrypt_rail_fence(text, key):
rail = [['\n' for i in range(len(text))] for j in range(key)]
direction_down = False
row, col = 0, 0
for i in range(len(text)):
if row == 0 or row == key - 1:
direction_down = not direction_down
rail[row][col] = text[i]
col += 1
row += 1 if direction_down else -1
result = []
for i in range(key):
for j in range(len(text)):
if rail[i][j] != '\n':
result.append(rail[i][j])

return "".join(result)

def decrypt_rail_fence(cipher, key):
rail = [['\n' for i in range(len(cipher))] for j in range(key)]
direction_down = None
row, col = 0, 0
for i in range(len(cipher)):
if row == 0:
direction_down = True
if row == key - 1:
direction_down = False
rail[row][col] = '*'
col += 1
row += 1 if direction_down else -1
index = 0
for i in range(key):
for j in range(len(cipher)):
if rail[i][j] == '*' and index < len(cipher):
rail[i][j] = cipher[index]
index += 1

result = []
row, col = 0, 0
for i in range(len(cipher)):
if row == 0:
direction_down = True
if row == key - 1:
direction_down = False
if rail[row][col] != '\n':
result.append(rail[row][col])
col += 1
row += 1 if direction_down else -1
return "".join(result)

while True:
print("1. Encrypt ")
print("2. Decrypt ")
print("3. Exit")
choice = input("Enter your choice: ")
if choice == '1':
text = input("Enter the text to encrypt: ")
key = int(input("Enter the key (number of rails): "))
encrypted_text = encrypt_rail_fence(text, key)
print(f"Encrypted text: {encrypted_text}\n")
elif choice == '2':
cipher = input("Enter the cipher text to decrypt: ")
key = int(input("Enter the key (number of rails): "))
decrypted_text = decrypt_rail_fence(cipher, key)
print(f"Decrypted text: {decrypted_text}\n")
elif choice == '3':
print("Exiting...")
break
else:
print("Invalid choice, please try again.\n")
