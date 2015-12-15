stop = 'y'

import random
nummer = random.randint(1,9)

while stop == 'y':
    guessed_nummer = int(input("Noem een nummer tussen 1 en 9 "))
    if nummer == guessed_nummer:
        print ("good job! That was right!" )
    elif nummer > guessed_nummer:
        print ("Sorry, that number was lower then the answer")
    elif nummer < guessed_nummer:
        print ("Sorry, that number was higher then the answer")

    stop = input('Want to play again? Type y, if not type n ')

