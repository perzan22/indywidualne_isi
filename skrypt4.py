def czyPalindrom(input: str):

    sent = input
    letters = []

    for letter in sent:
        letters.append(letter)
    
    pal_letters = letters[::-1]

    if (pal_letters == letters):
        print(f'Podana fraza jest palindromem.')
    else:
        print(f'Podana fraza nie jest palindromem.')




if __name__ == '__main__':

    fraza = input('Proszę wpisać frazę do sprawdzenia: ')
    czyPalindrom(fraza)
    