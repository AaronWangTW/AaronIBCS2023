import curses

MENU = "menu"
OPTIONS = "options"
PROMPT = "prompt"
SCREEN = "screen"
POS = "position"
TEXT = "text"
CALLBACK = "callback"
STATUSFORMAT = "|Key: {:>5} Active: {:>3}"


def create_menu_item(pos: int, text: str, callback: callable):
    menu_item = {POS: pos, TEXT: text, CALLBACK: callback}
    return menu_item


def create_menu(prompt: str, options: list) -> dict:
    menu = {
        PROMPT: prompt,
        OPTIONS: options
    }
    return menu


def draw_menu(ctx: dict, menu: dict) -> callable:
    # curses screen to draw to
    s = ctx[SCREEN]
    # menu options we can choose from
    o = menu[OPTIONS]
    # sort options in order
    o.sort(key=lambda x: x[POS])
    # last key to be pressed
    key = 0
    # current index of active option
    active = 0
    h, w = s.getmaxyx()

    while key != 27:
        # 27 is ascii [esc]

        # handle key presses here
        if key == 456 or key == curses.KEY_DOWN:
            active = (active+1) % len(o)
        if key == 450 or key == curses.KEY_UP:
            active = (active-1) % len(o)
        elif key == 10 or key == curses.KEY_ENTER:
            return o[active][CALLBACK]

        s.clear()

        s.addstr(2, 3, menu[PROMPT])

        for idx, opt in enumerate(o):
            if idx == active:
                s.attron(curses.color_pair(2))
                s.addstr(idx+h//2, w//2, opt[TEXT])
                s.attroff(curses.color_pair(2))
            else:
                s.attron(curses.color_pair(1))
                s.addstr(idx+h//2, w//2, opt[TEXT])
                s.attroff(curses.color_pair(1))

        #draw status bar
        statusString = STATUSFORMAT.format(key, active)
        s.attron(curses.color_pair(1))
        s.addstr(h-1, 0, statusString)
        s.addstr(h-1, len(statusString), " " * (w-len(statusString)-1))
        s.attroff(curses.color_pair(1))

        s.move(h-1, 1)
        s.refresh()
        key = s.getch()


def init() -> dict:
    context = {}
    context[SCREEN] = curses.initscr()
    context[SCREEN].clear()
    context[SCREEN].keypad(1)

    # create colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_MAGENTA)

    return context
    # practice things here:
    # h, w = screen.getmaxyx()
    # c = 2
    # screen.attron(curses.color_pair(c))
    # screen.addstr(3,3,"Test")
    # screen.attroff(curses.color_pair(c))

    # screen.move(h-1,1)
    # screen.refresh()
    # key = screen.getch()


if __name__ == "__main__":
    context = init()
    menu = create_menu("Example Prompt", [
        create_menu_item(0, "Option 1", None),
        create_menu_item(1, "Option 2", None),
        create_menu_item(2, "Option 3", None),
        create_menu_item(3, "Option 4", None),
    ])
    draw_menu(context, menu)
