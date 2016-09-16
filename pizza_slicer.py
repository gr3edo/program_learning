word = "пицца"
print("Введите начальный и конечный индексы для того среза 'пиццы'. который хотите получить.")
print("Для выхода нажмите Enter. не вводя начальную позицию ")
start = None
while start != "":
    start = (input("\nНачальная позиция: "))
    if start:
        start = int(start)
        finish = int(input("Koнeчнaя позиция: "))
        print("Cpeз word[", start, ":", finish, "]выглядит как", end=" ")
        print(word[start:finish])
input("\n\nHaжмитe Enter. чтобы выйти.") 
