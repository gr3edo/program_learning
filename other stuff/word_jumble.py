import random
WORDS =("python", "anagramm", "easy", "difficult", "answer")
word = random.choice(WORDS)
correct = word
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print ("Welcome to the Anagramms game!")
print ("Here is anagramm:", jumble)
guess = input ("Yout try: ")
while guess != correct and guess != "":
    print ("You are wrong!")
    guess = input ("Yout try: ")

if guess == correct:
    print("YES!! CONGRATZ!!")

input ("Press Enter to exit")
