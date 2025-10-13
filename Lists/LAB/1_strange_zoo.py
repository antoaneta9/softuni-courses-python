tail = input()
body = input()
head = input()

dog = [tail, body, head]
dog[0], dog[2] = dog[2], dog[0]
print(dog)