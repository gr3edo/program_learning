inventory = ()
# рассмотрим его как условие
if not inventory:
    print ( "Вы безоружны. " )
input("\nHaжмитe Enter. чтобы продолжить.")
# теперь создадим кортеж с несколькими элементами
inventory = ("меч",
            "кольчуга",
            "щит",
            "целебное снадобье")
# выведем этот кортеж на экран
print ("\nСодержимое кортежа : ")
print (inventory)
# выведем все элементы последовательно
print("\nИтaк. в вашем арсенале:")
for item in inventory:
    print (item)
input( "\n\nHaжмитe Enter. чтобы выйти ") 
