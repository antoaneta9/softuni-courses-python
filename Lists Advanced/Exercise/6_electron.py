electron = int(input())
shells = []
n = 1
while electron > 0:
    max_electrons = 2 * n ** 2
    if electron >= max_electrons:
        shells.append(max_electrons)
    else:
        shells.append(electron)
    electron -= max_electrons
    n += 1
print(shells)


