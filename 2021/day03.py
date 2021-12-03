# part 1
arr = []
while True:
    try:
        s = input()
        arr.append(s)
    except EOFError:
        break
gamma, epsilon = 0, 0
m = len(arr[0])
for i in range(m):
    count_zero = 0
    for el in arr:
        if el[i] == '0':
            count_zero += 1
        else:
            count_zero -= 1
    gamma <<= 1
    epsilon <<= 1
    if count_zero < 0:
        gamma += 1
    else:
        epsilon += 1
print(gamma * epsilon)
