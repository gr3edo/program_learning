# Манипуляции с цитатой
# Демонстрирует строковые методы
#цитата из Томаса Уотсона. который в 1943 г. был директором IBM
quote ="Думаю, на мировом рынке можно будет продать штук пять компьютеров."

print("Исходная цитата ") 
print(quote)
print("\nOнa же в верхнем регистре:")
print(quote.upper())
print("\nB нижнем регистре:")
print(quote.lower())
print("\nKaк заголовок:")
print(quote.title())
print("\nC ма-а-аленькой заменой:")
print(quote.replace("штук пять", "несколько миллионов"))
print("\nA вот опять исходная цитата:")
print(quote)
input("\n\nHaжмитe Enter. чтобы выйти.") 
