class Shape:
    def _init_(self, colour, square=10):
        self.colour = colour
        self.square = square
    def get_colour(self):
        return self.colour
    def set_colour(self, new_colour):
        self.colour = new_colour
a = Shape('Red')
print(a.get_colour())
    def get_square(self):
        return self.square
    def set_square(self, new_square):
        self.square = new_square
a = Square('5')
print(a.get_square())