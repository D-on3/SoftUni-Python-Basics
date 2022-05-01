var = input()
score = 0

for i in var:
    if i == 'a':
        score += 1
    elif i == 'e':
        score += 2
    elif i == 'i':
        score += 3
    elif i == 'o':
        score += 4
    elif i == 'u':
        score += 5
print(score)