import re
from datetime import datetime

TIMESTAMP = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$'
LEVEL = r'^(ERROR|WARNING|INFO|DEBUG)$'
MESSAGE = r'^[A-Za-z0-9 ,.:!?_/-]{5,200}$'
USER = r'^[A-Za-z][A-Za-z0-9_]{2,19}$'
IP = r'^((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$'

def parse_line(line):
    parts = line.split('::')
    if len(parts) != 5:
        return None, ['Wrong format']

    parts = [p.strip() for p in parts]
    timestamp, level, message, user, ip = parts
    errors = []

    if not re.match(TIMESTAMP, timestamp):
        errors.append('Timestamp must be in format YYYY-MM-DD HH:MM:SS')
    if not re.match(MESSAGE, message):
        errors.append('Message must be in format "A-Za-z0-9 ,.:!?_/-" and between 5 and 200 chars')
    if not re.match(USER, user):
        errors.append('User should be between 2 and 19 chars long and no special chars other than "_"')
    if not re.match(IP, ip):
        errors.append('IP address should be in format IPv4')

    if errors:
        return None, errors

    parsed_time = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
    return {
        'timestamp': parsed_time,
        'level': level,
        'message': message,
        'user': user,
        'ip': ip
    }, None

