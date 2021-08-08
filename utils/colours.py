from discord import Color
color_list = [Color.green(), Color.blue(), Color.red(), Color.gold(), Color.dark_blue(), Color.dark_gold(
), Color.dark_green(), Color.dark_red(), Color.dark_teal(), Color.dark_grey(), Color.dark_orange(), Color.dark_magenta()]


def give_random_color():
    import random
    random.seed()
    l = random.choice(color_list)
    return l
