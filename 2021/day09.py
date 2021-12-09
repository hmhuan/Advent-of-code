mat = []
basins = []
n = 0
while True:
    try:
        s = input()
        temp = []
        basins.append([])
        for el in s:
            temp.append(int(el))
            basins[-1].append(0)
        mat.append(temp)
        n += 1
    except EOFError:
        break
    pass

result = 0
for i in range(n):
    for j in range(n):
        l, r, u, d = 9, 9, 9, 9
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

# part 2
def flow_down(i, j):
    if mat[i][j] == 9:
        return
    if i > 0:
        if mat[i][j] > mat[i - 1][j]:
            return flow_down(i - 1, j)
    if i < m - 1:
        if mat[i][j] > mat[i + 1][j]:
            return flow_down(i + 1, j)
    if j > 0:
        if mat[i][j] > mat[i][j - 1]:
            return flow_down(i, j - 1)
    if j < n - 1:
        if mat[i][j] > mat[i][j + 1]:
            return flow_down(i, j + 1)
    basins[i][j] += 1


for i in range(m):
    for j in range(n):
        flow_down(i, j)

flat_list = []
for basin_row in basins:
    flat_list.extend(basin_row)
flat_list.sort()
print(flat_list[-1] * flat_list[-2] * flat_list[-3] )
