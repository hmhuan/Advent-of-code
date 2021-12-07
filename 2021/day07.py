s = input()
numbers = [int(el) for el in s.split(',')]
numbers.sort()
print(len(numbers))
def calcFuel(numbers):
    left, right = 0, 0
    mid = len(numbers) // 2
    for number in numbers:
        left += abs(number - numbers[mid - 1])
        right += abs(number - numbers[mid])
    return min(left, right)

print(calcFuel(numbers))
