n=int(input())

phonebook = dict(input().split() for _ in range(n))

for j in range(n):
    name = input().strip()
    if name in phonebook:
        print(name + "=" + phonebook[name])
    else:
        print("Not found")
