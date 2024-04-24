class Dog:
    def __init__(self, name: str, age: int, coat_color: str):
        self.name = name
        self.age = age
        self.coat_color = coat_color
    
    def sound(self):
        print(f'{self.name} is barking!')

if __name__ == '__main__':
    
    dog = Dog('Burek', 2, 'black')
    dog2 = Dog('Azor', 1, 'brown')
    dog3 = Dog('Dogo', 3, 'white')

    dog.sound()
    dog2.sound()
    dog3.sound()
