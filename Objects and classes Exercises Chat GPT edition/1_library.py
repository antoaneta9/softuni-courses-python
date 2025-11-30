
class Library:
    __total_books = 0

    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, title):
        self.books.append(title)
        Library.__total_books += 1

    def add_member(self, username):
        if username not in self.members:
            self.members.append(username)
        else:
            pass

    def borrow(self, username, title):
        if title not in self.books:
            return f"{title} is not available in {self.name}."
        elif username not in self.members:
            return f"{username} is not a member of {self.name}."

        return f"{username} borrowed {title}."

    def get_info(self, what):
        result = ''
        if what == 'books':
            result+= f"Books in {self.name}: {', '.join(self.books)}\n"
        elif what == 'members':
            result+= f"Members in {self.name}: {', '.join(self.members)}\n"
        result += f"Total books: {Library.__total_books}"
        return result

library = Library(input())
lines = int(input())

for i in range(1, lines + 1):
    command = input().split(' ')

    if command[0] == 'add_book':
        library.add_book(command[1])
    elif command[0] == 'add_member':
        library.add_member(command[1])
    elif command[0] == 'borrow':
        print(library.borrow(command[1], command[2]))
    elif command[0] == 'get_info':
        print(library.get_info(command[1]))



