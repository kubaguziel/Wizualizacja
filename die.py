from random import randint

class Die():
    """Klasa przedstawiająca pojedyńczą kość do gry"""

    def __init__(self,num_sides=6) -> None:
        """Założenie że kość ma postać sześcianu"""
        self.num_sides = num_sides

    def roll(self):
        """Zwrot wartości z zakresu 1 do liczby ścianek"""
        return randint(1,self.num_sides)
    