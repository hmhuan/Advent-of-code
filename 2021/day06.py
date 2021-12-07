s = input()
numbers = [int(el) for el in s.split(',')]

# part 1
for i in range(80):
    n = len(numbers)
    for j in range(n):
        numbers[j] -= 1
        if numbers[j] < 0:
            numbers[j] = 6
            numbers.append(8)
            pass
        pass
print(len(numbers))
