import curses
from login import login_ui
from directory_selector import directory_selection_ui

def main(stdscr):
    curses.curs_set(0)  # Hide the cursor at the start
    # Start with the login UI
    username = login_ui(stdscr)

    if username:
        # Proceed to directory selection after successful login
        directory_selection_ui(stdscr, username)

if __name__ == "__main__":
    curses.wrapper(main)
