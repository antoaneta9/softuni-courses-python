import re
from colorama import init, Fore, Style
init(autoreset=True)

timestamp_regex = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$'
level_regex = r'^(ERROR|WARNING|INFO|DEBUG)$'
message_regex = r'^[A-Za-z0-9 ,.:!?_/-]{5,120}$'
user_regex = r'^[A-Za-z][A-Za-z0-9_]{2,19}$'
ip_regex = r'^((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$'

logs={}
invalid_logs = {}

error_count = 0
warning_count = 0
info_count = 0
debug_count = 0

ip_count = {}
unique_users = set()
max_message = ''

timestamp_first_valid_log = ''
timestamp_last_valid_log = ''
first_log_set = False
while True:
    command = input()
    if command == 'end':
        break

    timestamp, level, message, user, ip = command.split(' :: ')

    errors = []
    if not re.match(timestamp_regex, timestamp):
        errors.append('Wrong timestamp! Time stamp must be in the format YYYY-MM-DD HH:MM:SS')
    if not re.match(level_regex, level):
        errors.append('Wrong level! Level must be in the format A-Z')
    if not re.match(message_regex, message):
        errors.append('Wrong message! Message must be not contain special characters other than ",.!?_/-" and should not be longer than 120chars or shorter than 5chars.')
    if not re.match(user_regex, user):
        errors.append('Wrong user! User must be between 2 and 19 chars. No special chars rather than "_".')
    if not re.match(ip_regex, ip):
        errors.append('Wrong ip! IP must be between 1 and 255 devided between them with dots. Format: IPv4')

    if not errors:
        logs[timestamp] = {
            'level': level,
            'message': message,
            'user': user,
            'ip': ip
        }

        if not first_log_set:
            timestamp_first_valid_log = timestamp
            first_log_set = True
        timestamp_last_valid_log = timestamp


        ip_count[ip] = ip_count.get(ip, 0) + 1
        unique_users.add(user)

        if len(message) > len(max_message):
            max_message = message

        if level == 'ERROR':
            error_count += 1
        if level == 'WARNING':
            warning_count += 1
        if level == 'INFO':
            info_count += 1
        if level == 'DEBUG':
            debug_count += 1
    else:
        invalid_logs[timestamp] = errors

# print('VALIDS:')
# print(logs)
# print('<----------------------------------------->')
# print('INVALIDS:')
# print(invalid_logs)
# print('<----------------------------------------->')
# print('ERROR:', error_count)
# print('WARNING:', warning_count)
# print('INFO:', info_count)
# print('DEBUG:', debug_count)
# print('LONGEST MESSAGE:', max_message)
# print('UNIQUE USERS:', len(unique_users))
# print('IP:', ip_count)
print(Fore.GREEN + 'VALIDS:')
print(logs)
print(Fore.MAGENTA + '<----------------------------------------->')
print(Fore.RED + 'INVALIDS:')
print(invalid_logs)
print(Fore.MAGENTA + '<----------------------------------------->')

print(Fore.RED + 'ERROR:', error_count)
print(Fore.YELLOW + 'WARNING:', warning_count)
print(Fore.CYAN + 'INFO:', info_count)
print(Fore.BLUE + 'DEBUG:', debug_count)
print(Fore.GREEN + 'LONGEST MESSAGE:', max_message)
print(Fore.MAGENTA + 'UNIQUE USERS:', len(unique_users))
print(Fore.LIGHTBLUE_EX + 'IP:', ip_count)
print(Fore.GREEN + 'FIRST TIMESTAMP:', timestamp_first_valid_log)
print(Fore.CYAN + 'LAST TIMESTAMP:', timestamp_last_valid_log)


