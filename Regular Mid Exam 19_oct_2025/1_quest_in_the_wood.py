days = int(input())
num_adventurers = int(input())
total_energy = float(input())

water_per_person_per_day = float(input())
food_per_person_per_day = float(input())


total_food = (days * food_per_person_per_day)  * num_adventurers
total_water = (days * water_per_person_per_day)  * num_adventurers

for day in range(1, days + 1):
    daily_energy_loss = float(input())
    total_energy -= daily_energy_loss

    if total_energy <= 0:
        print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
        break

    if day % 2 == 0:
        total_water *= 0.70
        total_energy *= 1.05


    if day % 3 == 0:
        total_energy *= 1.10
        total_food -= total_food / num_adventurers

else:
    print(f"You are ready for the quest. You will be left with {total_energy:.2f} energy!")
