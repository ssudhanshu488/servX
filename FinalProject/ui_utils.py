import curses

def loading_bar_animation(stdscr, y, x, width):
    """Display a loading bar animation."""
    stdscr.clear()
    for i in range(width + 1):
        bar = "#" * i + "-" * (width - i)
        try:
            stdscr.addstr(y, x, f"[{bar}]")
        except curses.error:
            pass
        stdscr.refresh()
        curses.napms(50)


def get_input(stdscr, y, x, hidden=False):
    """Get input from the user, optionally hidden (for passwords)."""
    curses.echo() if not hidden else curses.noecho()
    stdscr.move(y, x)
    stdscr.refresh()
    user_input = stdscr.getstr(y, x, 60).decode('utf-8')
    curses.noecho()
    return user_input


def draw_login_page(stdscr, username):
    """Draw the login page."""
    stdscr.clear()
    height, width = stdscr.getmaxyx()



    title = "LOGIN PAGE"
    try:
        stdscr.addstr(2, (width - len(title)) // 2, title, curses.A_BOLD | curses.color_pair(1))
    except curses.error:
        pass

    try:
        stdscr.addstr(6, 4, "Username:")
        stdscr.addstr(8, 4, "Password:")
        stdscr.addstr(6, 15, username)
    except curses.error:
        pass

    stdscr.refresh()

    return 6, 15  # Return the position for input
