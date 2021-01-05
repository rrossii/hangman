# hangman

import random
HANGMAN_PICS = ['''
 +---+
     |
     |
     |
    ===''', '''
 +---+
 0   |
     |
     |
    ===''', '''
 +---+
 0   |
 |   |
     |
    ===''', '''
 +---+
  0  |
 /|  |
     |
    ===''', '''
 +---+
  0  |
 /|\ |
     |
    ===''', '''
 +---+
  0  |
 /|\ |
 /   |
    ===''', '''
 +---+
  0  |
 /|\ |
 / \ |
    ===''']

words = '''аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея
        индюк кит кобра коза козел койот корова кошка кролик крыса курица лама ласка лебедь лев лиса лосось лось лягушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь олень орел осел панда паук питон
        попугай пума семга скунс собака сова тигр тритон тюлень утка форель хорек черепаха ястреб ящерица'''.split()
correctLetters = []
wrongLetters = []
def secretWord(words):
    secretIndex = random.randint(0, len(words)-1)
    print('Я загадала слово. Попробуй отгадать его по частям! Секретное слово состоит из', len(words[secretIndex]),
          'букв. Назови букву.')

    return words[secretIndex]

def display():
    print(HANGMAN_PICS[len(wrongLetters)])

    blanks = '_'*len(rightWord)
    for i in range(len(rightWord)):
        if rightWord[i] in correctLetters:
            blanks = blanks[:i] +  rightWord[i] + blanks[i+1:]
    if arg in correctLetters:
        print('Ты уже угадал(-а) эту букву.')
        guessLetter()
    if arg in wrongLetters:
        print('Эта буква не подходит.')
        guessLetter()
    print(blanks)


def guessLetter():



    letter = str(input())

    if letter in rightWord:
        correctLetters.append(letter)
        display()
        print('Ты угадал букву!')
    else:
        wrongLetters.append(letter)
        display()
        print('К сожалению, такой буквы нет.')

def checkLetters(arg):
    if arg in correctLetters:
        print('Ты уже угадал(-а) эту букву.')
        guessLetter()
    if arg in wrongLetters:
        print('Эта буква не подходит.')
        guessLetter()




playAgain = 'да'
rightWord = secretWord(words)
while playAgain == 'да':

    guessLetter()
    checkLetters(' ')





