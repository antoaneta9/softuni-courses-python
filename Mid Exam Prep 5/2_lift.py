waiting_list = int(input())
lift_cabins = list(map(int, input().split(' ')))
max_capacity = 4

for cabin in range(len(lift_cabins)):
    free_space = max_capacity - lift_cabins[cabin]

    if free_space > 0:
        people_to_load = min(free_space, waiting_list)
        lift_cabins[cabin] += people_to_load
        waiting_list -= people_to_load


if waiting_list == 0 and any(capacity < max_capacity for capacity in lift_cabins):
    print(f"The lift has empty spots!")

elif waiting_list > 0 and all(capacity == max_capacity for capacity in lift_cabins):
    print(f"There isn't enough space! {waiting_list} people in a queue!")
print(*lift_cabins)
