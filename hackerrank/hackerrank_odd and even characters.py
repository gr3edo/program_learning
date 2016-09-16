cases = int(input())

odd = ""
even = ""
index = 0
for j in range(cases):
    s = input()
    for i in s:
        if index%2 == 0:
            even += i
        else:
            odd += i
        index += 1
    print(even + " " + odd)
    index = 0
    odd = ""
    even = ""    
    
    

