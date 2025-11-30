books = {}

while True:
    cmd = input()
    if cmd == 'End':
        break
    book_name, author, quantity_str = cmd.split('|')
    quantity = int(quantity_str)
    books[book_name] = {'author': author, 'quantity': quantity}

while True:
    cmd = input()
    if cmd == 'Stop':
        break

    parts = cmd.split('|')
    if len(parts) != 2:
        print('Invalid format')
        continue
    action, info = parts
    
    if action == 'Borrow':
        book_name = info
        if book_name in books and books[book_name]['quantity'] > 0:
            books[book_name]['quantity'] -= 1
            print(f'You borrowed {book_name}')
        else:
            print(f'Sorry, "{book_name}" not available')
    elif action == 'Return':
        book_name = info
        if book_name in books:
            books[book_name]['quantity'] += 1
            print(f'You returned {book_name}')
        else:
            print(f'Sorry, "{book_name}" was not in the list before. You can not return something you have not borrowed.')
    elif action == 'Info':
        book_name = info
        if book_name in books:
            print(f'{book_name} by {books[book_name]["author"]}, available copies: {books[book_name]["quantity"]}')
        else:
            print(f'Sorry, "{book_name}" not available')
    else:
        print(f'Error')
for book_name, book in books.items():
    print(f'{book_name} by {book["author"]}, available copies: {book["quantity"]}')