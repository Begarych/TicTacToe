field = [[" ", 0, 1, 2],
         [0, "-", "-", "-"],
         [1, "-", "-", "-"],
         [2, "-", "-", "-"]]


def show_field():  # фунуция для вывода поля игры
    for i in field:
        print(*i)


def changes(x, y, ans='x'):  # функция для внесения изменений в матрицу
    while True:  # проверка занятости клетки
        if field[x+1][y+1] == '-':
            field[x+1][y+1] = ans
            break
        else:
            x, y = list(map(int, input('The cell is already occupied\nPlease, select an empty cell:').split(",")))


def win(l):  # функция для определения победы
    for i in range(1, 4):
        if (l[i][1] == l[i][2] == l[i][3]) and l[i][1] != '-':
            return f"Victory for {l[i][1]}"
    for i in range(1, 4):
        if (l[1][i] == l[2][i] == l[3][i]) and l[1][i] != '-':
            return f"Victory for {l[i][1]}"
    if (l[1][1] == l[2][2] == l[3][3]) and l[1][1] != '-':
        return f"Victory for {l[1][1]}"
    if (l[1][3] == l[2][2] == l[3][1]) and l[1][3] != '-':
        return f"Victory for {l[1][3]}"
    if ('-' not in l[1]) and ('-' not in l[2]) and ('-' not in l[3]):
        return "Draw"
    return "\nNext Round\n"


turn = 1
first_sign = input("Who's first x or o:")
second_sign = None
while True:  # метод для определения кто ходит первый
    if first_sign == 'o':
        second_sign = 'x'
        break
    elif first_sign == 'x':
        second_sign = 'o'
        break
    else:
        first_sign = input("\nIncorrect symbol, please enter x or o:")

while True:  # сама программа
    try:  # проверка правильности вводимых данных
        show_field()
        coord = list(map(int, input('Enter the coordinates of your move separated by commas:').split(",")))
        if turn % 2 == 0:
            changes(coord[0], coord[1], second_sign)
        else:
            changes(coord[0], coord[1], first_sign)
        turn += 1
        print(win(field))
        if win(field) != "\nNext Round\n":
            show_field()
            break
    except (IndexError, ValueError) as error:
        print("Enter coordinates correct")