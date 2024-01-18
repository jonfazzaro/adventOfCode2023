from curses.ascii import isdigit


def calibrate(input):
    if not len(input):
        return 0

    return sum(map(value, input.splitlines()))


def value(line):
    nums = digits(words_to_digits(line))
    return int(str(nums[0]) + str(nums[-1]))


def digits(line):
    return list(filter(len, map(digit, line)))


def digit(c):
    if isdigit(c):
        return c
    return ""


def words_to_digits(line):
    numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0}

    for w, d in numbers.items():
        line = line.replace(w, f"{w}{d}{w}")

    return line
