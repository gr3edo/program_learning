import random
WORDS =("python", "anagramm", "easy", "difficult", "answer")
word = random.choice(WORDS)
correct = word
jumble = ""
points = 2
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print ("Welcome to the Anagramms game!")
print ("Type 'help' to help")
print ("Here is anagramm:", jumble)

guess = input ("Yout try: ")

while guess != correct and guess != "":
    if guess == "help":
        points -= 1
        print (correct[:3])
        guess = input ("Yout try: ")
    else:
        print ("Wrong!")
        guess = input ("Yout try: ")

if guess == correct:
    print("YES!! CONGRATZ!!")

input ("Press Enter to exit")
