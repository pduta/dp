import random




def read_file(file_name):
   try:
       with open(file_name, 'r') as f:
           items = f.readlines()
           items = [item.strip() for item in items]
           return items
   except FileNotFoundError:
       print(f"Error: {file_name} not found.")
       return []




def generate_combination(item_list, count=4):
   if not item_list:
       return None
   combination = ''.join(random.choice(item_list) for _ in range(count))
   return combination




file_name = input("Enter the file name: ")
data = read_file(file_name)


if data:
   num_items = int(input("Enter the number of words/items for the combination: "))
   result = generate_combination(data, count=num_items)


   if result:
       print(f"Generated Combination: {result}")
   else:
       print("Could not generate a combination.")
else:
   print("Error reading the file.")
