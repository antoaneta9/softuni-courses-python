# filters.py

def get_logs_by_level(logs, level):
    return [l for l in logs if l["level"] == level]

def get_logs_by_user(logs, user):
    return [l for l in logs if l["user"] == user]

def get_logs_by_ip(logs, ip):
    return [l for l in logs if l["ip"] == ip]

def get_logs_in_timerange(logs, start, end):
    return [l for l in logs if start <= l["timestamp"] <= end]


# Sorting
def sort_logs_by_timestamp(logs):
    return sorted(logs, key=lambda x: x["timestamp"])

def sort_logs_by_user(logs):
    return sorted(logs, key=lambda x: x["user"])

def sort_logs_by_level(logs):
    return sorted(logs, key=lambda x: x["level"])
