import itertools
import string
import time




def brute_force_attack(password):
   characters = string.ascii_letters + string.digits
   attempts = 0
   start_time = time.time()


   for length in range(1, len(password) + 1):
       for guess_tuple in itertools.product(characters, repeat=length):
           attempts += 1
           guess = ''.join(guess_tuple)


           if attempts % 100000 == 0:
               print(f"Attempt {attempts}: Current guess is '{guess}'")


           if guess == password:
               end_time = time.time()
               print(
                   f"\nPassword '{password}' cracked after {attempts} attempts in {end_time - start_time:.2f} seconds.")
               return guess


   print("Failed to crack the password.")
   return None




password = input("Enter the password to crack: ")
brute_force_attack(password)

