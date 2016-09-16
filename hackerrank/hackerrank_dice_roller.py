cases = int(input())
answer = []

for i in range(cases):
    a = float(input())
    result = (a * 6) + 1
    result = int(result)
    answer.append(result)
print (' '.join(list(map(str, answer))))
