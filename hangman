import random


words = ['python', 'java', 'kotlin', 'javascript']
made_word = random.choice(words)
guessed_symbols = (len(made_word)) * '-'
lives = 8
win = False
print(*'HANGMAN'.strip())
input_symbols = set()
decision = "play"
while decision != "exit":
    decision = input('Type "play" to play the game, "exit" to quit:')
    if decision == "play":
        while lives > 0:
            print('\n' + guessed_symbols)
            letter = input('Input a letter: ')
            if len(letter) != 1:
                print("You should input a single letter")
            elif not (letter.isalpha() and letter.islower()):
                print('Please enter a lowercase English letter')
            elif letter in input_symbols:
                print("You've already guessed this letter")
            elif letter in made_word:
                enumerated_word = [i for i in enumerate(made_word)]
                founded_indexes = [i[0] for i in enumerated_word if i[1] == letter and letter in made_word]
                for i in founded_indexes:
                    list_hidden_word = list(guessed_symbols)
                    list_hidden_word[i] = letter
                    guessed_symbols = ''.join(list_hidden_word)
            else:
                print("That letter doesn't appear in the word")
                lives -= 1
            if letter not in input_symbols:
                input_symbols.add(letter)
            if '-' not in guessed_symbols:
                print(f'You guessed the word {guessed_symbols}!\nYou survived!')
                win = True
                break

        if win is not True and lives <= 0:
            print('You lost!')
