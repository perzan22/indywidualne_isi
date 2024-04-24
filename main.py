import funkcje as u

if __name__ == '__main__':

    x = int(input('Proszę podać liczbę x: '))
    y = int(input('Proszę podać liczbę y: '))
    print(f'x - y = {u.odejmowanie(x,y)}')
    print(f'x / y = {u.dzielenie(x,y)}')
    print(f'x * y = {u.mnozenie(x,y)}')
    print(f'x % y = {u.modulo(x,y)}')

