import re
usernames = input().split(', ')
for username in usernames:
    if re.match("^[A-Za-z0-9_-]*$", username):
        if 3 <= len(username) <= 16:
            print(f"{username}")

