n1 = int(input())
combination = 0
for x1 in range(0, n1 + 1):
    for x2 in range(0, n1 + 1):
        for x3 in range(0, n1 + 1):
            if x1 + x2 + x3 == n1:
                combination += 1

print(combination)