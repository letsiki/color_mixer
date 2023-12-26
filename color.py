import mixbox


class Color:

    def __init__(self, r, g, b):
        self.R = r
        self.G = g
        self.B = b
    def __add__(self, other):
        mixed_color = mixbox.lerp((self.R, self.G, self.B), (other.R, other.G, other.B), t=0.5)
        return Color(mixed_color[0], mixed_color[1], mixed_color[2])

    def __str__(self):
        return '#{:02x}{:02x}{:02x}'.format(self.R, self.G, self.B)

