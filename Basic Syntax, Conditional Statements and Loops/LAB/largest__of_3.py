num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

curr_num = 0

if num_1 > num_2 and num_1 > num_3:
    curr_num = num_1
elif num_2 > num_1 and num_2 > num_3:
    curr_num = num_2
else:
    curr_num = num_3

print(curr_num)