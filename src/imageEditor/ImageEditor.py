from src.imageEditor.Pixel import Pixel
from PIL import Image


class ImageEditor:
    def __init__(self):
        self._original_image = None
        self._has_image = False
        self.copy_size = (0, 0)
        self.copy_image = []
        self._name = None

    def has_image(self) -> bool:
        return self._has_image

    def load_image(self, image_name: str):
        self._original_image = Image.open(image_name)
        if self._original_image.mode == "RGB":
            self._has_image = True
            self._copy_original_image()
            self._name = image_name
        else:
            self._has_image = False
            raise NameError()

    def save_image(self, name: str=None):
        if not self._has_image:
            return
        n = Image.new("RGB", self.copy_size)
        for i in range(self.copy_size[1]):
            for j in range(self.copy_size[0]):
                n.putpixel((j, i), self.copy_image[i][j].get_data())
        if name is None:
            n.save(self._name)
        else:
            n.save(name)

    def _copy_original_image(self):
        self.copy_size = self._original_image.size
        self.copy_image = []
        for i in range(self.copy_size[1]):
            self.copy_image.append([])
            for j in range(self.copy_size[0]):
                self.copy_image[i].append(Pixel(*self._original_image.getpixel((j, i))))

    def rotate(self, deg: int):
        if not self._has_image:
            return
        if deg == 90:
            self.copy_size = (self.copy_size[1], self.copy_size[0])
            img = self.copy_image
            self.copy_image = [[Pixel() for _ in range(self.copy_size[0])] for _ in range(self.copy_size[1])]
            for i in range(self.copy_size[1]):
                for j in range(self.copy_size[0]):
                    self.copy_image[i][j] = img[j][i]

        elif deg == -90:
            self.copy_size = (self.copy_size[1], self.copy_size[0])
            img = self.copy_image
            self.copy_image = [[Pixel() for _ in range(self.copy_size[0])] for _ in range(self.copy_size[1])]
            for i in range(self.copy_size[1]):
                for j in range(self.copy_size[0]):
                    self.copy_image[i][j] = img[j][self.copy_size[1] - i - 1]

        else:
            raise NotImplemented("Rotate only 90 or -90 deg")

    def increase(self, pixels: int=0) -> None:
        if not self._has_image:
            return
        for i in range(self.copy_size[1]):
            for j in range(self.copy_size[0]):
                self.copy_image[i][j].increase(pixels)

    def decrease(self, pixels: int=0) -> None:
        if not self._has_image:
            return
        for i in range(self.copy_size[1]):
            for j in range(self.copy_size[0]):
                self.copy_image[i][j].decrease(pixels)

    def inverse(self) -> None:
        if not self._has_image:
            return
        for i in range(self.copy_size[1]):
            for j in range(self.copy_size[0]):
                self.copy_image[i][j].inverse()

    def horizontal_mirroring(self):
        if not self._has_image:
            return
        for i in range(self.copy_size[1] // 2 - 1):
            for j in range(self.copy_size[0]):
                tmp = self.copy_image[i][j]
                self.copy_image[i][j] = self.copy_image[self.copy_size[1] - 1 - i][j]
                self.copy_image[self.copy_size[1] - 1 - i][j] = tmp

    def vertical_mirroring(self):
        if not self._has_image:
            return
        for i in range(self.copy_size[1]):
            for j in range(self.copy_size[0] // 2 - 1):
                tmp = self.copy_image[i][j]
                self.copy_image[i][j] = self.copy_image[i][self.copy_size[0] - 1 - j]
                self.copy_image[i][self.copy_size[0] - 1 - j] = tmp

    def gray_scale(self):
        if not self._has_image:
            return
        for i in range(self.copy_size[1]):
            for j in range(self.copy_size[0]):
                self.copy_image[i][j].gray_scale()

    def original_image(self):
        if not self._has_image:
            return
        self._copy_original_image()

    def convolution(self):
        """
        mask - >    0 1 2
                    3 4 5
                    6 7 8
        :return:
        """
        if not self._has_image:
            return
        mask = (-1, -1, -1, -1, 9, -1, -1, -1, -1)
        img = [[Pixel() for _ in range(self.copy_size[0])] for _ in range(self.copy_size[1])]
        for i in range(self.copy_size[1]):
            img[i][0] = self.copy_image[i][0]
            img[i][self.copy_size[0] - 1] = self.copy_image[i][self.copy_size[0] - 1]
        for j in range(self.copy_size[0]):
            img[0][j] = self.copy_image[0][j]
            img[self.copy_size[1] - 1][j] = self.copy_image[self.copy_size[1] - 1][j]
        for i in range(1, self.copy_size[1] - 1):
            for j in range(1, self.copy_size[0] - 1):
                img[i][j] = self._calculate_convolution(mask, (self.copy_image[i - 1][j - 1],
                                                               self.copy_image[i - 1][j],
                                                               self.copy_image[i - 1][j + 1],
                                                               self.copy_image[i][j - 1],
                                                               self.copy_image[i][j],
                                                               self.copy_image[i][j + 1],
                                                               self.copy_image[i + 1][j - 1],
                                                               self.copy_image[i + 1][j],
                                                               self.copy_image[i + 1][j + 1]))
        self.copy_image = img

    @staticmethod
    def _calculate_convolution(mask, pixels) -> Pixel:
        count = 1
        tmp = [0, 0, 0]
        for i in range(9):
            # count += mask[i]
            tmp[0] += mask[i] * pixels[i].red
            tmp[1] += mask[i] * pixels[i].green
            tmp[2] += mask[i] * pixels[i].blue
        return Pixel(int(tmp[0] // count), int(tmp[1] // count), int(tmp[2] // count))

    def blur(self):
        """
        mask - >    0 1 2
                    3 4 5
                    6 7 8
        :return:
        """
        if not self._has_image:
            return
        mask = (1, 1, 1, 1, 1, 1, 1, 1, 1)
        img = [[Pixel() for _ in range(self.copy_size[0])] for _ in range(self.copy_size[1])]
        for i in range(self.copy_size[1]):
            img[i][0] = self.copy_image[i][0]
            img[i][self.copy_size[0] - 1] = self.copy_image[i][self.copy_size[0] - 1]
        for j in range(self.copy_size[0]):
            img[0][j] = self.copy_image[0][j]
            img[self.copy_size[1] - 1][j] = self.copy_image[self.copy_size[1] - 1][j]
        for i in range(1, self.copy_size[1] - 1):
            for j in range(1, self.copy_size[0] - 1):
                img[i][j] = self._calculate_blur(mask, (self.copy_image[i - 1][j - 1],
                                                        self.copy_image[i - 1][j],
                                                        self.copy_image[i - 1][j + 1],
                                                        self.copy_image[i][j - 1],
                                                        self.copy_image[i][j],
                                                        self.copy_image[i][j + 1],
                                                        self.copy_image[i + 1][j - 1],
                                                        self.copy_image[i + 1][j],
                                                        self.copy_image[i + 1][j + 1]))
        self.copy_image = img

    @staticmethod
    def _calculate_blur(mask, pixels) -> Pixel:
        count = 0
        tmp = [0, 0, 0]
        for i in range(9):
            count += mask[i]
            tmp[0] += mask[i] * pixels[i].red
            tmp[1] += mask[i] * pixels[i].green
            tmp[2] += mask[i] * pixels[i].blue
        return Pixel(int(tmp[0] // count), int(tmp[1] // count), int(tmp[2] // count))

    def close_image(self):
        self._original_image = None
        self._has_image = False
