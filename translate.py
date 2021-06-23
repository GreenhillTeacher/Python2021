#  
# translating game (Spanish to english)
import time
import sys
import os

os.system('cls')
name=input("What is your name? ")


adj = {'tall':'alto', 'small':'chico', 'big':'grande', 'good':'bueno', 'fast':'rapido', 'old':'viejo', 'long':'largo', 'fat':'gordo', 'slow':'lento', 'short':'corto'}
verb = {'throw':'lanzar', 'stand up':'levantarse', 'sit down':'sentarse', 'run':'correr', 'walk':'caminar', 'sleep':'dormir', 'eat':'comer', 'write':'escribir', 'drink':'beber', 'go to':'ir'}
hobby = {'swimming':'nadar','play basketball':'jugar baloncesto','play soccer':'jugar futbol','play video games':'jugar juego de videos','watch TV':'ver televiion','play outside':'jugar afuera','drawing':'dibujar','go online':'navegar la red','play ping pong':'jugar ping pong','watch movies':'ver una pelicula'}
start=input('Would you like to play? (yes/no) ')

def GAME():
    score = 0
    rounds = 10
    print('')
    print('GOOD LUCK,',name,end='!')
    def word_bank():
        print('\nWORD BANK:')
        for key,value in set.items():
            print('|',key,end=' ')
        print('')
    for key, value in set.items():
        word = value
        correct = key
        word_bank()
        print('What do you think the Spanish word,',word,end=', is in English?')
        answer=input('\nAnswer: ')
        if answer == correct:
            print('\nCorrect!\n')
            score += 1
            rounds -= 1
        else:
            print('\nIncorrect!\n')
            rounds -= 1
        if rounds == 0:
            print('Your score was',score,'out of 10!')
            if score >= 5:
                print('Congratualations',name,end='!')
                print(' YOU WON!!\n')
            else:
                print("Unfortunately, you didn't guess enough words correctly to win. Good game, though!\n")
    time.sleep(5)
    start=input('Do you want to play again? (yes/no) ').lower()

def MENU():
    print("***********************************************************")
    print('*                    Guess word meanings                  *')
    print('*                   ~~ Spanish Edition ~~                 *')
    print('*                                                         *')
    print("*                    _ Select a word set _                *")
    print('*                    |                     |              *')
    print('*                    |    1. ADJECTIVES    |              *')
    print('*                    |    2. VERBS         |              *')
    print('*                    |    3. HOBBIES       |              *')
    print('*                    |                     |              *')
    print('*                    |     [EXIT GAME]     |              *')
    print('*                    | _ _ _ _ _ _ _ _ _ _ |              *')
    print('*                                                         *')
    print('*                         How to win:                     *')
    print('*            Guess 5 or more word meanings correctly      *')
    print('*                                                         *')
    print('*                 Author:    MISuarez                     *')
    print('***********************************************************')


if 'y' in start:
    score = 0
    print('')
    MENU()
    set = input('Which word set do you want to play with? (1/2/3/exit) ')
    if set == '1':
        set = adj
        print('You chose the ADJECTIVES word set.')
        GAME()
    elif set == '2':
        set = verb
        print('You chose the VERBS word set.')
        GAME()
    elif set == '3':
        set = hobby
        print('You chose the HOBBIES/ACTIVITIES word set.')
        GAME()
    elif set == 'exit':
        print('Thanks for playing! Hope to see you soon.')
        time.sleep(3)
        sys.exit()

elif start == 'no':
    sys.exit()