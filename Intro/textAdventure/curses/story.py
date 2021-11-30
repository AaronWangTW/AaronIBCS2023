import context as c


def start(ctx):
    menu = c.create_menu(
        """
        Well, it's the start of yet another day. You wake up in the morning wondering what to do. 
        You have math class at 10am, and now it's 8am. You only finished half of your homework.
        However, you also just finished your midterm yesterday and feel exhausted. 
        
        What do you do?""",
        [
            c.create_menu_item(1, "1. Write homework", homework),
            c.create_menu_item(2, "2. Play guitar", guitar),
            c.create_menu_item(3, "3. Play Apex Legends", apex)
        ])
    return c.draw_menu(ctx, menu)


def homework(ctx):
    menu = c.create_menu(
        """
        You rushed and finished the math homework. You feel happy that you achieved something, 
        but you become more exhausted mentally. Later when you have class, you performed badly 
        because of this. At least the teacher is satisfy to see the homework finished. 

        end.""",
        [
        ])
    return c.draw_menu(ctx, menu)


def guitar(ctx):
    menu = c.create_menu(
        """
        You took out your beloved guitar and practiced several pieces. When you are half way through 
        a song, mom knock on the door and complained that she couldn't sleep. Now you finally realized it's
        20 min from the class.
        
        What do you do now?""",
        [
            c.create_menu_item(
                1, "1. Wash face and brush teeth, get ready for class", wash),
            c.create_menu_item(2, "2. Rush breakfast", breakfast),
            c.create_menu_item(
                3, "3. Regret why you didn't do those first", regret)
        ])
    return c.draw_menu(ctx, menu)


def apex(ctx):
    menu = c.create_menu(
        """
        You turn on your laptop and start the game. The first two games didn't go well, but on the third one
        you got carried. You feel happy and rejuvenated with the game. With the currently good attitude and 
        1 hour left, you:""",
        [
            c.create_menu_item(
                1, "1. Rush the homework now (but with happy mental state)", hwButHappy),
            c.create_menu_item(
                2, "2. Chill out for the rest of the time", chill)
        ])
    return c.draw_menu(ctx, menu)


def wash(ctx):
    menu = c.create_menu(
        """
        You quickly finished the hygiene tasks. You used rest of the time to rest. You performed normally
        in class, nothing special happened. However, you are exceptionally hungry after the class and eat too
        much during lunch. You become even more CHUNGUS. 

        end.""",
        [])
    return c.draw_menu(ctx, menu)


def breakfast(ctx):
    menu = c.create_menu(
        """
        Because you wear mask during class, nothing really happened. The breakfast's energy supported you
        through the tiresome class. Just another Saturday. 

        end.""",
        [])
    return c.draw_menu(ctx, menu)


def regret(ctx):
    menu = c.create_menu(
        """
        You spent rest of the time doubting your life choices and got nothing done.
        Life is hard man.

        end.""",
        [])
    return c.draw_menu(ctx, menu)


def hwButHappy(ctx):
    menu = c.create_menu(
        """
        Although you didn't finish all of your homework, at least you did them happily.
        You also did well in class cuz you are energized. 
        Not a bad Saturday innit'?

        end.""",
        [])
    return c.draw_menu(ctx, menu)


def chill(ctx):
    menu = c.create_menu(
        """
        You chill out, that's it. 
        You feel satisfied, but a little bit hollow cuz you didn't do anything.
        hmmmmmm......

        anyways it's just Saturday.
        end.""",
        [])
    return c.draw_menu(ctx, menu)


def main():
    ctx = c.init()
    cb = start(ctx)
    while cb != None:
        cb = cb(ctx)


if __name__ == "__main__":
    main()
