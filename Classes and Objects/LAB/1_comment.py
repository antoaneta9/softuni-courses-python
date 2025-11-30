class Comment:
    def __init__(self, username, content, likes = 0):
        self.username = username
        self.content = content
        self.likes = likes

person1 = Comment('user1', 'I like this book')
print(person1.username, person1.content, person1.likes)