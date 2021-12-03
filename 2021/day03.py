arr = []
while True:
    try:
        s = input()
        arr.append(s)
    except EOFError:
        break
gamma, epsilon = 0, 0
o2, co2 = 0, 0
prev_o2, prev_co2 = "", ""
m = len(arr[0])
for i in range(m):
    count_zero = 0
    count_zero_o2, count_zero_co2, count_one_co2 = 0, 0, 0
    for el in arr:
        if el[i] == '0':
            count_zero += 1
            if prev_o2 == el[:i]:
                count_zero_o2 += 1
            if prev_co2 == el[:i]:
                count_zero_co2 += 1
        else:
            count_zero -= 1
            if prev_o2 == el[:i]:
                count_zero_o2 -= 1
            if prev_co2 == el[:i]:
                count_one_co2 += 1
    o2 <<= 1
    co2 <<= 1
    gamma <<= 1
    epsilon <<= 1
    if count_zero < 0:
        gamma += 1
    else:
        epsilon += 1
        
    if count_zero_o2 <= 0:
        o2 += 1
        prev_o2 += '1'
    else:
        prev_o2 += '0'
        
    if count_zero_co2 == 0:
        co2 += 1
        prev_co2 += '1'
    else:
        if count_one_co2 == 0 or count_one_co2 >= count_zero_co2:
            prev_co2 += '0'
        else:
            prev_co2 += '1'
            co2 += 1
                
print(gamma * epsilon)
print(o2 * co2)
