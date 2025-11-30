# ===============================
# Python List Slicing Cheat Sheet
# ===============================

numbers = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Original list:", numbers)
print()

# 1️⃣ Slice from index 1 to 4 (inclusive start, exclusive stop)
print("numbers[1:5] ->", numbers[1:5])

# 2️⃣ Slice from start to index 4
print("numbers[:5] ->", numbers[:5])

# 3️⃣ Slice from index 5 to end
print("numbers[5:] ->", numbers[5:])

# 4️⃣ Slice the whole list
print("numbers[:] ->", numbers[:])

# 5️⃣ Slice with step
print("numbers[1:8:2] ->", numbers[1:8:2])

# 6️⃣ Reverse the list
print("numbers[::-1] ->", numbers[::-1])

# 7️⃣ Negative indexes
print("numbers[-3:] -> last 3 items:", numbers[-3:])
print("numbers[:-3] -> all but last 3 items:", numbers[:-3])

# 8️⃣ Example for SoftUni Treasure Hunt
chest = ['Gold', 'Silver', 'Bronze', 'Cup']
print("\nChest:", chest)

count = 2
stolen = chest[-count:]
chest = chest[:-count]

print(f"Steal last {count} items:", stolen)
print("Remaining chest:", chest)

# 9️⃣ Slice everything after first element (Loot command)
command_parts = ['Loot', 'Gold', 'Silver', 'Coins']
items_to_add = command_parts[1:]
print("\nCommand parts:", command_parts)
print("Items to add:", items_to_add)


