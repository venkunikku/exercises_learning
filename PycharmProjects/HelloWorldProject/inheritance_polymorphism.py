#Inheritance and polymorphism example

class Animal:
    """ Example of poly."""

    """More comments about this class."""
    def quack(self):
        return self.strings['quack']
    def bark(self): return self.strings['bark']
    def talk(self): return self.strings['talk']
    def mcv_pattern(self): return self._doaction('talk')

    def _doaction(self,action):
        if action in self.strings:
            return self.strings[action]
        else:
            return "Does not have this in the dictionary {0} from class {1}".format(action,self.get_class_name())

    def get_class_name(self):
        return self.__class__.__name__.lower()

class Duck(Animal):
    strings = dict(quack = 'Duck Quacking', bark = 'duck cannot bark', talk = 'Duck cannot talk too')
class Dog(Animal):
    strings = dict(quack = 'Dog no Quacking', bark = 'Dog barks', talk = 'Dog cannot talk too')
class Huma(Animal):
    strings = dict(quack = 'Human no Quacking', bark = 'Human cannot bark', talkk = 'Human can talk too')

if __name__ == '__main__':
    duck = Duck()
    print(duck.quack())
    human = Huma()
    print(human.bark())
    dog=Dog()
    print(dog.bark())
    print(dog.quack())

    print('trying mvc patter****')
    print(human.mcv_pattern())