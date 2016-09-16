s = input()
i,c = input().split()
i = int(i)
s = s[:i] + c + s[i+1:]
print (s)
