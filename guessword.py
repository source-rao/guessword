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

# Variables
incorrect = 0
guesstest = 0
incorrectguesses = list()

print('The word has ' + str(len(letters)) + ' letters in it.')

while incorrect < 5:
    print('You have ' + str(5 - incorrect) +' incorrect guesses remaining.')
    guess = input('Enter a letter to guess: ').lower()
    count = 0
    for letter in letters: # Check each letter against guessed character
        if guess == letter:
            result[count] = letters[count] # Replace '_' with correctly guessed character
            guesstest += 1 # Counter verifying if a guess was correct
            count += 1 # Move position in result array
        else:
            count += 1
    if guesstest == 0: # If incorrect guess
        incorrect += 1 # Increment incorrect guess count
        incorrectguesses.append(guess) # Add incorrect guess to guessed list
    elif result.count('_') == 0: # Elif no blanks remaining
        print('Congratulations! You guessed ' + word + '!')
        break
    else:
        guesstest = 0 # Reset correct guess verifier
    print(' '.join(result)) # Print result
    if incorrect > 0:
        guessedstr = ' '.join(incorrectguesses) # Stringify list of incorrect guesses
        print('Incorrect guesses: ' + guessedstr)

if incorrect > 4:
    print('Sorry, the word was ' + word + '!')