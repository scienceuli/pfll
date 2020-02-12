import numpy as np

class Square:
    def __init__(self, width):
        self.width = width

    def get_area(self):
        return self.width**2

    def get_diameter(self):
        return np.sqrt(self.width)