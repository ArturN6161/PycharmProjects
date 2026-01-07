def n_dice():
    try:
        while True:
            try:
                number_of_dice = int(input('Enter the number of dice: '))
                if number_of_dice not in range(1, 100 + 1):
                    print("The number must be between 1 and 100")
                else:
                    return number_of_dice
            except ValueError:
                print("Please enter the number, not string!")
    except KeyboardInterrupt:
        print('The function was interrupted by the user')
        exit()


def build_a_ladder(number_of_dice):
    remains = number_of_dice
    ladder_levels = []
    step = 1
    while remains > step:
        ladder_levels.append(step)
        remains, step = remains - step, step + 1
    if remains > 0:
        ladder_levels[-1] += remains 
    print(ladder_levels)
    return ladder_levels


def draw_ladder(ladder_levels):
    print("~" * 36)
    for level in ladder:
        print("[_]" * level)


n = n_dice()
ladder = build_a_ladder(n)
draw_ladder(ladder)