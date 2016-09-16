my_list = []
number_of_command = int(input().strip())
for _ in range(number_of_command):
    user_input = input().split()
    command = user_input[0]
    if command == 'append':
        my_list.append(int(user_input[-1]))
    elif command == 'insert':
        my_list.insert(int(user_input[1]), int(user_input[-1]))
    elif command == 'remove':
        my_list.remove(int(user_input[-1]))
    elif command == 'pop':
        my_list.pop()
    elif command == 'index':
        my_list.index(int(user_input[-1]))
    elif command == 'count':
        my_list.count(int(user_input[-1]))
    elif command == 'sort':
        my_list.sort()
    elif command == 'reverse':
        my_list.reverse()
    elif command == 'print':
        print(my_list)
    else:
        pass
