import re
auth_pattern = re.compile(
    r"^AUTH\s+(?P<username>[A-Za-z0-9]+)\s+(?P<ip>(?:25[0-5]|2[0-4]\d|1?\d{1,2})\."
    r"(?:25[0-5]|2[0-4]\d|1?\d{1,2})\.(?:25[0-5]|2[0-4]\d|1?\d{1,2})\."
    r"(?:25[0-5]|2[0-4]\d|1?\d{1,2}))\s+(?P<status>SUCCESS|FAIL)$"
)

file_pattern = re.compile(
    r"^FILE\s+(?P<username>[A-Za-z0-9]+)\s+(?P<filename>\S+)\s+"
    r"(?P<action>READ|WRITE|DELETE)$"
)

sys_pattern = re.compile(
    r"^SYS\s+(?P<component>[A-Z]+):(?P<code>\d+)\s*-\s*(?P<message>.+)$"
)

auth_logs = {}
file_logs = []
system_logs = {}

while True:
    line = input()
    if line == "Analyze":
        break

    m = auth_pattern.match(line)
    if m:
        data = m.groupdict()
        user = data["username"]
        ip = data["ip"]
        status = data["status"]

        if status == "FAIL":
            if user not in auth_logs:
                auth_logs[user] = {}
            if ip not in auth_logs[user]:
                auth_logs[user][ip] = 0
            auth_logs[user][ip] += 1
        continue

    m = file_pattern.match(line)
    if m:
        file_logs.append(m.groupdict())
        continue

    m = sys_pattern.match(line)
    if m:
        comp = m.group("component")
        code = int(m.group("code"))

        if comp not in system_logs:
            system_logs[comp] = []
        system_logs[comp].append(code)
        continue

brute_force_results = []
priv_access_results = []
sys_failure_results = []

for user, ips in auth_logs.items():
    for ip, fails in ips.items():
        if fails >= 5:
            brute_force_results.append((user, ip, fails))

brute_force_results.sort(key=lambda x: x[0])

for entry in file_logs:
    user = entry["username"]
    filename = entry["filename"]

    if filename.startswith("root_") and user != "root":
        priv_access_results.append((user, filename))

priv_access_results.sort(key=lambda x: x[1])

for component, codes in system_logs.items():
    errors = [c for c in codes if c >= 500]
    if len(errors) >= 3:
        sys_failure_results.append((component, len(errors)))

sys_failure_results.sort(key=lambda x: x[0])

if not brute_force_results and not priv_access_results and not sys_failure_results:
    print("No threats detected")
    exit()
for user, ip, fails in brute_force_results:
    print(f"BRUTE_FORCE {user} {ip} {fails}")
for user, filename in priv_access_results:
    print(f"PRIV_ACCESS {user} {filename}")
for comp, count in sys_failure_results:
    print(f"SYS_FAILURE {comp} {count}")


