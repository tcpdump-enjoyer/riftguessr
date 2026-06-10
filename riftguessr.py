import argparse
import random

from PIL import Image


def zoom(image: Image, x: int, y: int) -> None:
    base_width, base_height = image.size
    
    zoom_width = base_width // x
    zoom_height = base_height // y

    zoom_x = random.randint(0, x)
    zoom_y = random.randint(0, y)

    left   = zoom_x * zoom_width
    upper  = zoom_y * zoom_height
    right  = left  + zoom_width
    lower  = upper + zoom_height

    if zoom_x == x - 1:
        right = base_width
    if zoom_y == y - 1:
        lower = base_height

    tile = image.crop((left, upper, right, lower))
    tile.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("level", type=int, help="3-5: beginner, 6-10: intermediate, 11-15: expert")
    args = parser.parse_args()

    if not getattr(args, "level") in range(3, 16):
        print("Please choose a level between 3-16")

    x = getattr(args, "level")
    y = getattr(args, "level")

    zoom(Image.open("rift.jpg"), x, y)