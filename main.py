numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
position = 0


def odd_position():
    for i in numbers:
        if numbers[i] % 2:
            print(i, "is not in odd position in the list")
            print()
        else:
            if numbers[i] / 2:
                print(i, "is in odd position in the list")
                print()
    return odd_position()


print(odd_position())