def potega(x: int) -> int:
    return x*x*x

if __name__ == '__main__':
    number = int(input('Podaj liczbę: '))
    print(f'Liczba podniesiona do potęgi trzeciej wynosi: {potega(number)}')