from PIL import Image
import random


class Fractal:
    """Fractal class."""

    def __init__(self, size, scale, computation):
        """Constructor.

        Arguments:
        size -- the size of the image as a tuple (x, y)
        scale -- the scale of x and y as a list of 2-tuple
                 [(minimum_x, minimum_y), (maximum_x, maximum_y)]
        computation -- the function used for computing pixel values as a function
        """
        self.size = size
        self.scale = scale
        self.computation = computation
        self.img = Image.new("RGB", (size[0], size[1]))

    def compute(self):
        """
        Create the fractal by computing every pixel value.
        """
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                i = self.pixel_value((x, y))
                r = i % 8 * 12
                g = i % 16 * 4
                b = i % 32 * 4
                self.img.putpixel((x, y), (r, g, b))

    def pixel_value(self, pixel):
        """
        Return the number of iterations it took for the pixel to go out of bounds.

        Arguments:
        pixel -- the pixel coordinate (x, y)

        Returns:
        the number of iterations of computation it took to go out of bounds as integer.
        """
        x = (pixel[0] / self.size[0]) * (self.scale[1][0] - self.scale[0][0]) + self.scale[0][0]
        y = (pixel[1] / self.size[1]) * (self.scale[1][1] - self.scale[0][1]) + self.scale[0][1]

        return self.computation((x, y))

    def save_image(self, filename):
        """
        Save the image to hard drive.

        Arguments:
        filename -- the file name to save the file to as a string.
        """
        self.img.save(filename, "PNG")


def mandelbrot_computation(pixel):
    """Return integer -> how many iterations it takes for the pixel to escape the mandelbrot set."""
    z = 0
    iterations = 0
    c = complex(pixel[0], pixel[1])

    for i in range(1024):
        if abs(z) >= 2.0:
            break
        z = z ** 2 + c
        iterations += 1
    return iterations


if __name__ == "__main__":
    mandelbrot = Fractal((1000, 1000), [(-2, -2), (2, 2)], mandelbrot_computation)
    mandelbrot.compute()
    mandelbrot.save_image("mandelbrot.png")
