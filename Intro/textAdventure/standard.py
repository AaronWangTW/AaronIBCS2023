def userInput(prompt: str) -> int:
    try:
        return int(input(prompt))
    except (ValueError, TypeError):
        return -1


def start():
    print(
        """
        Well, it's the start of yet another day. You wake up in the morning wondering what to do. 
        You have math class at 10am, and now it's 8am. You only finished half of your homework.
        However, you also just finished your midterm yesterday and feel exhausted. 
        What do you do?

            1. Write homework
            2. Play guitar
            3. Play Apex Legends
        """
    )
    choice = -1
    while choice < 1 or choice > 3:
        choice = userInput("Make a choice: ")
        if choice == 1:
            homework()
        elif choice == 2:
            guitar()
        elif choice == 3:
            apex()
        else:
            print("Please choose 1, 2, or 3")


def homework():
    print(
        """
        You rushed and finished the math homework. You feel happy that you achieved something, 
        but you become more exhausted mentally. Later when you have class, you performed badly 
        because of this. At least the teacher is satisfy to see the homework finished. 

        end.
        """
    )


def guitar():
    print(
        """
        You took out your beloved guitar and practiced several pieces. When you are half way through 
        a song, mom knock on the door and complained that she couldn't sleep. Now you finally realized it's
        20 min from the class.

        What do you do now?
            1. Wash face and brush teeth, get ready for class
            2. Rush breakfast
            3. Regret why you didn't do those first
        """
    )
    choice = -1
    while choice < 1 or choice > 3:
        choice = userInput("What do you do now?")
        if choice == 1:
            wash()
        if choice == 2:
            breakfast()
        if choice == 3:
            regret()


def apex():
    print(
        """
        You turn on your laptop and start the game. The first two games didn't go well, but on the third one
        you got carried. You feel happy and rejuvenated with the game. With the currently good attitude and 
        1 hour left, you:
            
            1. Rush the homework now (but with happy mental state)
            2. Chill out for the rest of the time
        """
    )
    choice = -1
    while choice < 1 or choice > 2:
        choice = userInput("Make a choice: ")
        if choice == 1:
            hwButHappy()
        if choice == 2:
            chill()


def wash():
    print(
        """
        You quickly finished the hygiene tasks. You used rest of the time to rest. You performed normally
        in class, nothing special happened. However, you are exceptionally hungry after the class and eat too
        much during lunch. You become even more CHUNGUS. 

        end.
        """
    )


def breakfast():
    print(
        """
        Because you wear mask during class, nothing really happened. The breakfast's energy supported you
        through the tiresome class. Just another Saturday. 

        end.
        """
    )


def regret():
    print(
        """
        You spent rest of the time doubting your life choices and got nothing done.
        Life is hard man.

        end.
        """
    )


def hwButHappy():
    print(
        """
        Although you didn't finish all of your homework, at least you did them happily.
        You also did well in class cuz you are energized. 
        Not a bad Saturday innit'?

        end.
        """
    )


def chill():
    print(
        """
        You chill out, that's it. 
        You feel satisfied, but a little bit hollow cuz you didn't do anything.
        hmmmmmm......

        anyways it's just Saturday.
        end.
        """
    )


if __name__ == '__main__':
    start()
