sentences = input('Enter a sentences:')

char_count = len(sentences)
word_count = len(sentences.split())
vowels = 'aeiou'
vowel_count = 0

for char in sentences.lower():
    if char in vowels:
        vowel_count += 1


print('Sentences:', sentences)
print('-'*20)
print('Charcaters:', char_count)
print('Words:', word_count)
print('Vowels:', vowel_count)
