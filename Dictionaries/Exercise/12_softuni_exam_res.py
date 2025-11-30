results = {}
submissions = {}
while True:
    txt = input()
    if txt == 'exam finished':
        break
    command = txt.split('-')
    if len(command) == 3:
        username, language, points_str = command
        points = int(points_str)
        if username not in results:
            results[username] = {}
            results[username][language] = points
        elif language not in results[username] or points > results[username][language]:
            results[username][language] = points
        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1

    if len(command) == 2:
        username, banned = command
        if username in results:
            del results[username]
            continue


print('Results:')
for student, languages in results.items():
    best_points = max(languages.values())
    print(f"{student} | {best_points}")
print('Submissions:')
for l, p in submissions.items():
    print(f"{l} - {p}")

