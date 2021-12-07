n = 1000

def createMatrix():
    m = []
    for i in range(n):
        m.append([])
        for j in range(n):
            m[-1].append(0)
            pass
        pass
    return m

m = createMatrix()

while True:
    try:
        s = input().split('->')
        first, second = s[0], s[1]
        first = [int(el) for el in first.split(',')]
        second = [int(el) for el in second.split(',')]
        if first[1] == second[1]:
            start = min(first[0], second[0])
            end = max(first[0], second[0])
            for j in range(start, end + 1):
                m[first[1]][j] += 1
        if first[0] == second[0]:
            start = min(first[1], second[1])
            end = max(first[1], second[1])
            for i in range(start, end + 1):
                m[i][first[0]] += 1
    except EOFError:
        break
result = 0
for i in range(n):
    for j in range(n):
        if m[i][j] > 1:
            result += 1
print(result)
