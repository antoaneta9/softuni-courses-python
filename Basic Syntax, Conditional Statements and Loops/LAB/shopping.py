budget = int(input())
command = input()
cash = 0

while command != "End":
    cash += int(command)
    if cash > budget:
        print("You went overdraft!")
        break
    command = input()
else:
    print('You bought everything needed.')
