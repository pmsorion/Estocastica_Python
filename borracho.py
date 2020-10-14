import random

class Borracho:

    def __init__(self, name):
        self.name = name

class BorrachoTradicional(Borracho):

    def __init__(self, nombre):
        super() .__init__(nombre)

    def camina(self):
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])

    def camina2(self):
        return random.choice([(0, 1), (0, -2), (3, 0), (-4, 0), (0, 0), (5, 6), (-7, -8)])