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

def getResult(m):
    result = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] > 1:
                result += 1
    return result

m = createMatrix()

firsts, seconds, n = [], [], 0

while True:
    try:
        s = input().split('->')
        first, second = s[0], s[1]
        first = [int(el) for el in first.split(',')]
        second = [int(el) for el in second.split(',')]
        firsts.append(first)
        seconds.append(second)
        n += 1
    except EOFError:
        break
    pass

for k in range(n):
    first, second = firsts[k], seconds[k]
    if first[1] == second[1]:
            start = min(first[0], second[0])
            end = max(first[0], second[0])
            for j in range(start, end + 1):
                m[first[1]][j] += 1
    elif first[0] == second[0]:
        start = min(first[1], second[1])
        end = max(first[1], second[1])
        for i in range(start, end + 1):
            m[i][first[0]] += 1
    elif (abs(first[0] - second[0]) == abs(first[1] - second[1])):
        delta1, delta2 = 1, 1
        if (first[1] > second[1]):
            delta1 = -1
        if (first[0] > second[0]):
            delta2 = -1
        for i in range(first[1], second[1] + delta1, delta1):
            m[i][first[0]] += 1
            first[0] += delta2

result = getResult(m)
print(result)
