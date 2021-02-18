import random


def get_file_ext(filename):
    return filename[filename.index(".") + 1:]


def roll_dice(num):
    return random.randint(1, num)

    yilan_R = random.randint(50, 255)
    yilan_G = random.randint(50, 255)
    yilan_B = random.randint(50, 255)

    yilan_renk = (yilan_R, yilan_G, yilan_B)
    renk = (8, 145, 3)