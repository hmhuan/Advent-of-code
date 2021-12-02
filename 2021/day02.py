depth = 0
aim = 0
width = 0
F, U, D = 'forward', 'up', 'down'
# Part 1
# while True:
#     try:
#         s = input().split(' ')
#         task, value = s[0], s[1]
#         if (task == F):
#             width += int(value)
#         elif (task == D):
#             depth += int(value) 
#         else:
#             depth -= int(value)
#     except EOFError:
#         break
# print(depth * width)

# Part 2
while True:
    try:
        s = input().split(' ')
        task, value = s[0], s[1]
        if (task == F):
            width += int(value)
            depth += aim * int(value)
        elif (task == D):
            aim += int(value) 
        else:
            aim -= int(value)
    except EOFError:
        break
print(depth * width)
