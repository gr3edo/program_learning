num = int(input())
i = 0
sums = []

for time in range(num):
    a, b = map(int, input().split())
    sums.append(round(a / b))

print (' '.join(list(map(str, sums))))
