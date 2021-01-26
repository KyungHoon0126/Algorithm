n = int(input())
coin_types = [1, 3]

if n in coin_types:
    result = -1
elif (n % 5) % 2 == 0:
    result = n // 5 + (n % 5) // 2
else:
    result = ((n // 5) - 1) + ((n % 5 + 5) // 2)

print(result)
