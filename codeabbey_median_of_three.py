num = int(input())
median = []

for item in range(num):
    a, b, c  = map(int, input().split())
    if (a < b and a > c) or (a > b and a < c):
        median.append(a)
    elif (b < a and b > c) or (b > a and b < c):
        median.append(b)
    elif (c < a and c > b) or (c > a and c < b):
        median.append(c)

print (' '.join(list(map(str, median))))
