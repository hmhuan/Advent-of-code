mat = []
check = []
n = 0
while True:
    try:
        s = input()
        temp = []
        for el in s:
            temp.append(int(el))
        mat.append(temp)
        n += 1
    except EOFError:
        break
    pass

result = 0
for i in range(n):
    for j in range(n):
        l, r, u, d = 10, 10, 10, 10
        if (i > 0):
            u = mat[i - 1][j]
        if (i < n - 1):
            d = mat[i + 1][j]
        if (j > 0):
            l = mat[i][j - 1]
        if (j < n - 1):
            r = mat[i][j + 1]
        if (l > mat[i][j] and r > mat[i][j] and u > mat[i][j] and d > mat[i][j]):
            result += (mat[i][j] + 1)
            pass
        pass
    pass

print(result)
