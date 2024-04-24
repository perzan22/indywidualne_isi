from random import random


def gra(x: int):
    guessed = int(input('Proszę zgadnąć liczbę od 1 do 100: '))

    while guessed != x:
        if guessed < x:
            print('Za mała liczba!')
        else:
            print('Za duża liczba!')
        guessed = int(input('Proszę zgadnąć jeszcze raz: '))
    
    print('Brawo zgadłeś liczbę!')
    


if __name__ == '__main__':

    x = int(random() * 100)
    gra(x)
