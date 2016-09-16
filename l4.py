start = int (input("Otkuda nachat'"))
end = int (input("Gde zakonchit'"))
step = int (input("Shag"))

for i in range (start, end, step):
    print (i, end=' ')
