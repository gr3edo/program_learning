import random

heads = 0
tails = 0
count = 0

while count != 100:
    toss = random.randint(1,2)
    if toss == 1:
        heads += 1
    else:
        tails += 1
    count +=1
print ("Count: ",count)
print ("Heads: ",heads)
print ("Tails: ",tails)
