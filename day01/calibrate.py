from curses.ascii import isdigit


def calibrate(input):
    if not len(input):
        return 0

    return sum(map(value, input.split("\n")))


def value(line):
    nums = digits(line)
    return int(str(nums[0]) + str(nums[-1]))


def digits(line):
    return list(filter(len, map(digit, line)))


def digit(c):
    if isdigit(c):
        return c
    return ""
