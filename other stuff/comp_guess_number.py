import random

number = random.randint (1,100)
comp = random.randint(1,100)

print (number)
print (comp)

while comp != number:
    if comp > number:
        print ("lesser")
        comp = comp // 2
        print (comp)
    elif comp < number:
        print ("bigger")
        c = (100-comp)//2
        comp = comp + c
        print (comp)
    
