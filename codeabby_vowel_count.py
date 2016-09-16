num_strings = int(input())
answer = []
vowel_count = 0
for j in range(num_strings):
    
    sentence = input()
    counts = {i:0 for i in 'aeiouy'}
    for char in sentence:
        if char in counts:
            vowel_count += 1
    answer.append(vowel_count)
    vowel_count = 0

print (' '.join(list(map(str, answer))))
