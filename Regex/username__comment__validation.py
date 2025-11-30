import re

username_regex = r'^[A-Za-z][A-Za-z0-9_]{2,19}$'
comment_regex = r'^[A-Za-z0-9 .,!?]{1,200}$'

valids = {}
not_valids = {}
while True:
    command = input()
    if command == 'end':
        break
    errors=[]
    parts = command.split(':', 1)
    if len(parts) != 2:
        not_valids[command] = ['Invalid format (missing ":")']
        continue
    username, comment = parts[0], parts[1].strip()
    if not re.match(username_regex, username):
        errors.append('Invalid username')
    if not re.match(comment_regex, comment):
        errors.append('Invalid comment')

    if '!!!!' in comment:
        errors.append('Too many exclamation marks')

    if not errors:
        valids[username] = comment
    else:
        not_valids[username] = errors
print(valids)
print(not_valids)


