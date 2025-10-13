
people =input().split(' ')
step = int(input())
idx = 0
dead_ppl = []
while people:
    idx = (idx + step - 1) % len(people)
    dead_ppl.append(people[idx])
    people.pop(idx)


print(f"[{','.join(dead_ppl)}]")

