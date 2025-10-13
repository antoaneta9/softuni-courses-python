objects = input().split(', ')

while True:
    command = input().split(':')
    method = command[0]

    if method == 'course start':
        break

    if method == "Add":
        obj = command[1]
        if obj not in objects:
            objects.append(obj)
    elif method == "Insert":
        obj = command[1]
        index = int(command[2])
        if obj not in objects:
            objects.insert(index, obj)
    elif method == "Remove":
        obj = command[1]
        if obj in objects:
            objects.remove(obj)
        exercise = f"{obj}-Exercise"
        if exercise in objects:
            objects.remove(exercise)
    elif method == 'Swap':
        obj = command[1]
        lesson_1 = command[1]
        lesson_2 = command[2]
        if lesson_1 in objects and lesson_2 in objects:
            index_1 = objects.index(lesson_1)
            index_2 = objects.index(lesson_2)
            objects[index_1], objects[index_2] = objects[index_2], objects[index_1]

            lesson1_ex = f"{lesson_1}-Exercise"
            lesson2_ex = f"{lesson_2}-Exercise"

            if lesson1_ex in objects:
                objects.remove(lesson1_ex)
                new_index1 = objects.index(lesson_1)
                objects.insert(new_index1 + 1, lesson1_ex)

            if lesson2_ex in objects:
                objects.remove(lesson2_ex)
                new_index2 = objects.index(lesson_2)
                objects.insert(new_index2 + 1, lesson2_ex)
    elif method == "Exercise":
        obj = command[1]
        exercise = f"{obj}-Exercise"
        if obj in objects:
            lesson_index = objects.index(obj)
            if exercise not in objects:
                objects.insert(lesson_index+1, exercise)
        else:
            objects.append(obj)
            objects.append(exercise)

iterations = 0
for obj in objects:
    iterations += 1
    print(f"{iterations}.{obj}")
