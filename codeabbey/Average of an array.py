import math

answers = []
cases = int(input())

def rounding(x):
    num = math.modf(x)
    if num[0] < 0.5:
        return math.floor(x)
    else:
        return math.ceil(x)
    return num

for i in range(cases):
    array = [int(x) for x in input().split()]
    array.pop()
    total_average = (sum(x for x in array)) / len(array)
    total_average = rounding(total_average)
    answers.append(total_average)

print(' '.join(list(map(str, answers))))
