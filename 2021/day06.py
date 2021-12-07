s = input()
numbers = [int(el) for el in s.split(',')]

# part 1
# for i in range(80):
#     n = len(numbers)
#     for j in range(n):
#         numbers[j] -= 1
#         if numbers[j] < 0:
#             numbers[j] = 6
#             numbers.append(8)
#             pass
#         pass
# print(len(numbers))

# part 2
a = [0] * 9 #  0 1 2 3 4 5 6 7 8
for number in numbers:
    a[number] += 1
    pass
for i in range(256):
    b = [0] * 9
    for i, e in enumerate(a):
        if i == 0:
            b[6] += a[0]
            b[8] += a[0]
        else:
            b[i - 1] += a[i]
    for i in range(len(a)):
        a[i] = b[i]
print(sum(a))
