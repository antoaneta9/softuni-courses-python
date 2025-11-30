shelf = input().split('&')

while True:
    command = input()
    if command == 'Done':
        break

    parts = command.split(' | ')
    action = parts[0]

    if action == 'Add Book':
        book = parts[1]
        if book not in shelf:
            shelf.insert(0, book)
        else:
            continue

    elif action == 'Take Book':
        book = parts[1]
        if book in shelf:
            shelf.remove(book)
        else:
            continue

    elif action == 'Swap Books':
        book_1 = parts[1]
        book_2 = parts[2]

        if book_1 in shelf and book_2 in shelf:
            index_1 = shelf.index(book_1)
            index_2 = shelf.index(book_2)
            shelf[index_1], shelf[index_2] = shelf[index_2], shelf[index_1]
        else:
            continue

    elif action == 'Insert Book':
        book = parts[1]
        if book not in shelf:
            shelf.append(book)
        else:
            continue

    elif action == 'Check Book':
        index = int(parts[1])
        if 0 <= index < len(shelf):
            print(shelf[index])

print(', '.join(shelf))