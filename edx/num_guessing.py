low = 0
high = 100
ans = (low + high) // 2
print ('Please think of a number between 0 and 100!')
while True:
    user = input('Is your secret number ' + str(ans) + '?\n'
                + 'Enter "h" to indicate the guess is too high. '
                + 'Enter "l" to indicate the guess is too low. '
                + 'Enter "c" to indicate I guessed correctly. ')
    if user == 'h':
        high = ans
    elif user == 'l':
        low = ans
    elif user == 'c':
        print ('Game over. Your secret number was: ' + str(ans))
        break
    else:
        print ('Sorry, I did not understand your input.')
    ans = (low + high) // 2
