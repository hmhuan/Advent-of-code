s = input()
numbers = [int(el) for el in s.split(',')]

def readGrid(n):
    input()
    arr = []
    while n > 0:
        s = input()
        arr.append([[int(el), False]  for el in s.split()])
        n -= 1
    return arr

def checkBingo(arr):
    n = len(arr)
    for i in range(n):
        bingoR = True
        bingoC = True
        for j in range(n):
            bingoR &= arr[i][j][1]
            bingoC &= arr[j][i][1]
        if (bingoR | bingoC):
            return True
        
    return False

grids = []
while True:
    try:
        grid = readGrid(5)
        grids.append(grid)
    except EOFError:
        break
        
bingo_id = -1
current = 0
win_number = -1
checked = [-1] * len(grids)
for number in numbers:
    for i, grid in enumerate(grids):
        if (checked[i] != -1):
            continue
        for r in grid:
            for c in r:
                if c[0] == number:
                    c[1] = True
        if (checkBingo(grid)):
            checked[i] = current
            current += 1
    if (current == len(grids)):
        win_number = number
        break
    
# find bingo id
for i, check in enumerate(checked):
    if check == len(grids) - 1:
        bingo_id = i

result = 0       
for r in grids[bingo_id]:
    for c in r:
        if c[1] == False:
            result += c[0]

result *= win_number
print(result)
