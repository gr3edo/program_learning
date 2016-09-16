num = int(input())
mins = []

for item in range(num):
    a, b = map(int, input().split())
    mins.append(min(a,b))

print (' '.join(list(map(str, mins))))
