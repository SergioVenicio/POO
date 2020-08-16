class TwoDimensionalPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def toString(self):
        return (f"""\
            I'm a 3 dimensional point.
            My x coordinate is: {self.x}
            My y coordinate is: {self.y}""")


class ThreeDimensionalPoint(TwoDimensionalPoint):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def toString(self):
        return (f"""\
            I'm a 3 dimensional point.
            My x coordinate is: {self.x}
            My y coordinate is: {self.y}
            My z coordinate is: {self.z}""")
