import random

n = 1
m = 100
user = random.randint(n,m)
computer = m // 2

while computer != user:
    if computer > user:
        print ("lesser")
        m = computer
        computer = computer - ((m-n)//2)
    elif computer < user:
        print ("bigger")
        n = computer
        computer = ((m-n)//2)+computer
print ("right one")
print ("User:", user)
print ("Computer:", computer)

