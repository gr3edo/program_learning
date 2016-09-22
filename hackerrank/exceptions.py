#if string could be a number - print, else - throw exception
s = input().strip()
try:
    print(int(s))
except ValueError:
    print("Bad String")