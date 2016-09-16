import random

print( "\tДобро пожаловать в игру 'Отгадай число'!")
print("\nЯ загадал натуральное число из диапазона от 1 до 100.")
print("Постарайтесь отгадать его за минимальное число попыток.\n")
# начальные значения
the_number = random.randint(1, 5)
tries = 15

while tries != 0:
    print ("left", tries, "tries")
    guess = int(input("Baшe предположение: "))
    if guess > the_number:
        print ("lesser")
        tries -= 1
    elif guess < the_number:
        print ("bigger")
        tries -= 1
    elif guess == the_number:
        print ("winner")
        break
    else:
        print ("looser")     

        

