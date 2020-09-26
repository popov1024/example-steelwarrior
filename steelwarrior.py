def expectedValue(numbers):
    # count of tanks pairs
    n = penetrations(numbers) * 2

    l = len(numbers)

    if (n == 0):
        return 0

    # expected values for normal
    return factorial(l) / factorial(l - n) / 2

def penetrations(numbers):
    c = len(numbers)
    n = 0
    for j in range(0, c - 1):
        for i in range(0, c - 1 - j):
            if numbers[i] > numbers[i + 1]:
                t = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = t
                n += 1
    return n

def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

n = int(input())
setups = list()
for i in range(0, n):
    s = str(input()).split(' ')
    setups.append(s)

for i in range(0, n):
    e = expectedValue(setups[i])
    print("{:.6f}".format(e))