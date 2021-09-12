field = [[" "] * 3 for i in range(3)]


def show():
    print()
    print(f"   | 0 | 1 | 2 |")
    print("----------------")
    for i, row in enumerate(field):
        row_str = f" {i} | {' | '.join(row)} | "
        print(row_str)
        print("----------------")


def ask():
    while True:
        cords = input("     Ваш ход: ").split()

        if len(cords) != 2:
            print("Введите 2 координаты")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите числа")
            continue

        x, y = int(x), int(y)
        if x < 0 or x > 2 or y < 0 or y > 2:
            print("Координаты вне поля")
            continue
        if field[x][y] == " ":
            return x, y
        else:
            print("Клетка занята")


def check():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл КРЕСТИК")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл НОЛИК")
            return True
    return False


def great():
    print("Приветствуем в игре Крестики - Нолики")
    print("Формат ввода: X Y")
    print("Х - номер строки, Y - номер столбца")


great()

num = 0
while True:
    num += 1
    show()
    if num % 2 == 1:
        print("Ходит КРЕСТИК")
    else:
        print("Ходит НОЛИК")
    a, b = ask()
    if num % 2 == 1:
        field[a][b] = "X"
    else:
        field[a][b] = "0"
    if check():
        break
    if num == 9:
        print("Игра окончена. Ничья")
        break
