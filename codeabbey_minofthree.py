num = int(input())
mins = []

for item in range(num):
    a, b, c  = map(int, input().split())
    min1 = min(a, b)
    mins.append(min(min1,c))

print (' '.join(list(map(str, mins))))
