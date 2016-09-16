string = input()
str_to_search_for = input()

count = 0
for x in range(len(string) - len(str_to_search_for) + 1):
    if string[x:x+len(str_to_search_for)] == str_to_search_for:
        count += 1
print (count)
