def sum_of_squares(number):
    string = str(number)
    digits = [int(char) ** 2 for char in string]
    return sum(digits)


def happy(number):
    box = []
    n = number
    while n != 1 and n not in box:
        box.append(n)
        n = sum_of_squares(n)
    return n == 1

    return False


assert sum_of_squares(130) == 10
assert all([happy(n) for n in (1, 10, 100, 130, 97)])
assert not all(happy(n) for n in (2, 3, 4, 5, 6, 8, 9))
