cases = int(input())
answer = []

for item in range(cases):
    weight, height = input().split()
    weight = int(weight)
    height = float(height)
    
    bmi = weight / (height**2)
    if bmi < 18.5:
        answer.append("under")
    elif bmi < 25.0 and bmi > 18.5:
        answer.append("normal")
    elif bmi < 30.0 and  bmi > 25.0:
        answer.append("over")
    elif bmi > 30.0:
        answer.append("obese")
print (' '.join(list(map(str, answer))))
