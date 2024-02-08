def game(number):
    return max(list(map(int, str(number)))) - min(list(map(int, str(number))))
