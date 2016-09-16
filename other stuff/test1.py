import random

word = "index"

high = len(word)
low = -len(word)

for i in range (low, high):
    position = random.randrange(low,high)
    print("word[", position, "]\t", word[position])
