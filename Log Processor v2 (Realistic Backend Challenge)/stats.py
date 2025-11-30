from collections import Counter

def compute_stats(valid_logs):
    levels = Counter()
    ips = Counter()
    users = Counter()

    if not valid_logs:
        return {}

    longest_msg = ''
    timestamps = []

    for log in valid_logs:
        levels[log['level']] += 1
        ips[log['ip']] += 1
        users[log['user']] += 1

        if len(log['message']) > len(longest_msg):
            longest_msg = log['message']
        timestamps.append(log['timestamp'])

    return {
        'valid_count': len(valid_logs),
        'most_common_user': users.most_common(),
        'top_5_ips': ips.most_common(5),
        'levels': dict(levels),
        'longest_msg': longest_msg,
        'first_timestamps': min(timestamps),
        'last_timestamp': max(timestamps),
        'unique_users': len(users.keys()),
    }

