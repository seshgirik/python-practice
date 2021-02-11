

class Pizza:

    def __init__(self, size, ingredients):

        self.size = size
        self.ingredients = ingredients

    @staticmethod
    def area(size):
        print(f'area for {size} is {size*size}')
        return size*size

    @classmethod
    def italian(cls, size):

        return cls(size, ingredients=['capsicum', 'onions', 'cheese'])

    @classmethod
    def california(cls, value):
        ingredients = value.split('-')
        size = 99
        return cls(size, ingredients)


paneer_pizza = Pizza(10, ['paneer', 'cheese'])
italian_pizza = Pizza.italian(100)
california_pizza = Pizza.california("cheese-paneer-capsicum-mushroom")
print(f'california pizza ingredients {california_pizza.ingredients} , size is {california_pizza.size}')
print(paneer_pizza.size)
print(paneer_pizza.area(paneer_pizza.size))
print(f' italian pizza size: {italian_pizza.size} , area: {italian_pizza.area(italian_pizza.size)}, \n ingredients {italian_pizza.ingredients}')



