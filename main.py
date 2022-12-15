import random


class Hero:
    """Класс описания героя игры."""
    SKILL = "hit"
    BASE_HP = 1000
    BASE_ATTACK = 50
    ULTA = "mega hit"
    RANGE_ATTACK = (20, 100)

    def __init__(self,
                 name: str,):
        self.name = name

    def info(self):
        return(f'Меня зовут {self.name}, \n'              
              f'Я умею {self.SKILL}')

    def attack(self) -> int:
        return self.BASE_ATTACK + random.randint(*self.RANGE_ATTACK)

    def ulta(self) -> int:
        return self.BASE_ATTACK * random.randint(2, 10)




class Mage(Hero):
    """Тут крутое описание с точкой в конце."""
    SKILL = "Fire ball"
    BASE_HP = 1500
    BASE_ATTACK = 100
    ULTA = "Mega frire ball"
    RANGE_ATTACK = (20, 100)


Zeus = Mage('Zeus')

class Warior(Hero):
    '''воин лол.'''
    SKILL = "sword hit"
    BASE_HP = 3000
    BASE_ATTACK = 59
    ULTA = "udaryi nogami"
    RANGE_ATTACK = (20, 100)


Uyiot = Warior('Doryler')

class Healer(Hero):
    SKILL = "plesk kislotoy"
    BASE_HP = 900
    BASE_ATTACK = 34
    ULTA = "massoviy hill"
    RANGE_ATTACK = (2, 100)


def choose_character():
    c = {
        'mage': Mage,
        'Warior': Warior,
        'Healer': Healer
    }
    character = input('Здраствуй путник. выберете класс:\n'
              'маг - большой урон. маленькое хп. нг если хорошо владеть им то он может стать неплохим оружием\n'
              'для выбора напиши mage\n'
              'воин здоровы но слабый\n'
              'для выбора напиши Warior\n'
              'целитель исцеляет союзников но и имеет урон хоть и слабый\n'
              'для выбора напишите Healer\n')

    return c[character](input('ведите никнейм:'))


def training(character):
    print(f'Короче я спас тебя, и в благородство играть не буду. Ты лишился имени я дал тебе другое - {character.name}\n'
          f' я тебе дал способности {Character.SKILL}\n'
          f' начнем тренировку, а дальше ты сам!\n ')

    action = None
    while action != 'skip':
        e = {
            'e': character.attack(),
            'q': character.ulta()
        }

        action = input('напишите\n"e" для атаки\n'
                   '"q" для ульты\n')
        if action in e:
            print(e[action])


if __name__ == '__main__':
    Character = choose_character()
    training(Character)
