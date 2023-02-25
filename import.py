from math import pi
class circle:
    def __init__(self, radius):
        self.radius = radius
    def circm_area(self):
        circm_area = self.radius * 2 * pi
        return circm_area
c1 = circle(5)
c2 = circle(10)
print(c1.circm_area)