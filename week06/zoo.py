from abc import ABCMeta


class Animal(metaclass=ABCMeta):
    def __init__(self, kind, shape, character):
        self.kind = kind
        self.shape = shape
        self.character = character

    # 是否凶猛动物
    @property
    def is_ferocious(self):
        return self.shape in ['中', '大'] and self.kind == '食肉' and self.character == '凶猛'


class Cat(Animal):
    voice = '喵'

    def __init__(self, name, kind, shape, character):
        super().__init__(kind, shape, character)
        self.name = name

    @property
    def is_pet(self):
        if self.is_ferocious:
            return False
        else:
            return True


class Dog(Animal):
    voice = '汪'

    def __init__(self, name, kind, shape, character):
        super().__init__(kind, shape, character)
        self.name = name

    @property
    def is_pet(self):
        if self.is_ferocious:
            return False
        else:
            return True


class Zoo(object):
    def __init__(self, name):
        self.name = name

    def add_animal(self, animal):
        """
        添加动物
        :param animal:
        :return:
        """
        item = type(animal).__name__
        if item not in self.__dict__:
            self.__dict__[item] = animal
        else:
            print(f'{item}已经存在')


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
    print('有') if have_cat else print('无')
