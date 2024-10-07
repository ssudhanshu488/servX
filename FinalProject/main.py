import curses
from login import login_ui
from directory_selector import directory_selection_ui
from file_upload import file_upload_ui  # Assuming you have a similar function for uploading files


def main(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

    ssh_client, username = login_ui(stdscr)

    if ssh_client and username:
        selected_directory = directory_selection_ui(stdscr, ssh_client, username)
        if selected_directory:
            file_upload_ui(stdscr, ssh_client, selected_directory)  # Ensure file_upload_ui accepts the SSH client


if __name__ == "__main__":
    curses.wrapper(main)
