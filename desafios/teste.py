reminders = 5
for i in range(reminders):
    print(f"Sending reminder email #{i + 1}")
orders = ['Order #1', 'Order #2', 'Order #3']
for order in orders:
    print(f"Processing {order}")
    
for o in range(0, len(orders)):
    print('Processing {}'.format(orders[o]))

user_profile = {'name': 'Alice', 'age': 30, 'email': None}    
print(user_profile.items())
for key, value in user_profile.items():
    print(f"{key.capitalize()}: {value}")
    
room_sizes = [100, 150, 200]
square_footage = [size * size for size in room_sizes]
print(f"Square footages: {square_footage}")

inventory = ['apple', 'banana', 'cherry']
item_to_find = 'orange'
for item in inventory:
    if item == item_to_find:
        print(f"{item_to_find} found in inventory")
        break
else:
    print(f"{item_to_find} not found, adding to inventory")
    inventory.append(item_to_find)
print(inventory)

rows = range(1, 4)
columns = ['A', 'B', 'C']
for row in rows:
    for column in columns:
        print(f"Assigning seat: {row}{column}")
        
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)
    
x = 0
y = 0
while x < 3 and y < 3:
    print(f"x = {x}, y = {y}")
    x += 1
    y += 1