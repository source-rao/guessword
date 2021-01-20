import random

wordlist = open('words.txt','r')

# Generate word
allwords = list()
for word in wordlist:
    allwords.append(word)
random.seed()
wordkey = random.randint(0,len(allwords))
word = allwords[wordkey].rstrip()

# Generate list of letters
letters = list()
for letter in word:
    letters.append(letter)

# Generate result list of underscores for blanks
result = list()
for letter in letters:
    result.append('_')

incorrect = 0
guesstest = 0
win = 0
print('The word has ' + str(len(letters)) + ' letters in it.')

while incorrect < 5:
    print('You have ' + str(5 - incorrect) +' incorrect guesses remaining.')
    guess = input('Enter a letter to guess: ').lower()
    count = 0
    for letter in letters:
        if guess == letter:
            result[count] = letters[count]
            guesstest += 1
            count += 1
        else:
            count += 1
    if guesstest == 0:
        incorrect += 1
    else:
        if result.count('_') == 0:
            win = 1
            break
        else:
            guesstest = 0
    print(' '.join(result))

if incorrect > 4 and win != 1:
    print('Sorry, the word was ' + word + '!')
else:
    print('Congratulations! You guessed ' + word + '!')