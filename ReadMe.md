# Advent Of Code
This is my advent of code journey

### How to find the first odd element of number:
```
oddNum = num // (num & -num)
```
Example: 100 // (100 & -100) = 25 -> 100 / 2 = 50 / 2 = 25 (stop)
