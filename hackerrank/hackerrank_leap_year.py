a = int(input())
#even - chetnoe
#odd - nechetnoe
def is_leap(year):
    
    leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    return leap

print (is_leap(a))
