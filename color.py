import mixbox


class Color:

    def __init__(self, rgb):
        self.R = rgb[0]
        self.G = rgb[1]
        self.B = rgb[2]

    def __add__(self, other):
        return Color(mixbox.lerp((self.R, self.G, self.B), (other.R, other.G, other.B), t=0.5))


