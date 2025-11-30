import re

invalid_users = {}
valid_users = {}

name_regex = r'^[A-Z][a-z]+\s[A-Z][a-z]+$'
email_regex = r'^[a-z0-9]+[a-z0-9\.\_\-]*@[a-z\-]+\.[a-z\.]{2,}$'
website_regex = r'^www\.(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'
phone_regex = r'^\d{10}$'

while True:
    command = input()
    if command == 'end':
        break

    name, email, website, phone = command.split('-')
    errors = {}
    if not re.match(name_regex, name):
        errors['name'] = 'Invalid name'
    if not re.match(email_regex, email):
        errors['email'] = 'Invalid email'
    if not re.match(website_regex, website):
        errors['website'] = 'Invalid website'
    if not re.match(phone_regex, phone):
        errors['phone'] = 'Invalid phone'

    if not errors:
        valid_users[name] = {
            "email": email,
            "website": website,
            "phone": phone
        }
    else:
        invalid_users[name] = errors

print(valid_users)
print(invalid_users)



