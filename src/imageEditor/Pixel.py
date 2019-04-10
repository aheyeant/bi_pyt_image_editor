

class Pixel:

    def __init__(self, red: int=0, green: int=0, blue: int=0):
        self.red = red
        self.green = green
        self.blue = blue

        if red > 255:
            self.red = 255
        if green > 255:
            self.green = 255
        if blue > 255:
            self.blue = 255

        if red < 0:
            self.red = 0
        if green < 0:
            self.green = 0
        if blue < 0:
            self.blue = 0

    def increase(self, pixels: int=0):
        if (self.red + pixels) > 255:
            self.red = 255
        else:
            self.red += pixels

        if (self.green + pixels) > 255:
            self.green = 255
        else:
            self.green += pixels

        if (self.blue + pixels) > 255:
            self.blue = 255
        else:
            self.blue += pixels

    def decrease(self, pixels: int=0):
        if (self.red - pixels) < 0:
            self.red = 0
        else:
            self.red -= pixels

        if (self.green - pixels) < 0:
            self.green = 0
        else:
            self.green -= pixels

        if (self.blue - pixels) < 0:
            self.blue = 0
        else:
            self.blue -= pixels

    def inverse(self):
        self.red = ~self.red & 0xff
        self.green = ~self.green & 0xff
        self.blue = ~self.blue & 0xff

    def gray_scale(self):
        tmp = (self.red + self.green + self.blue) // 3
        self.red = self.green = self.blue = tmp

    def get_data(self):
        return self.red, self.green, self.blue
