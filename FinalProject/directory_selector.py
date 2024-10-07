import curses
import paramiko

def list_directories(ssh_client):
    """List directories in the user's home directory using the SSH client."""
    stdin, stdout, stderr = ssh_client.exec_command('ls -d */')
    directories = stdout.read().decode().splitlines()
    return [d.rstrip('/') for d in directories]

def directory_selection_ui(stdscr, ssh_client, username):
    directories = list_directories(ssh_client)

    if not directories:
        stdscr.addstr(3, 0, "No directories found. Press any key to exit.")
        stdscr.refresh()
        stdscr.getch()
        return None

    curses.curs_set(0)
    stdscr.clear()
    stdscr.addstr(0, 0, f"Welcome, {username}! Select a directory to upload files:", curses.A_BOLD)

    current_selection = 0
    while True:
        for idx, directory in enumerate(directories):
            if idx == current_selection:
                stdscr.addstr(idx + 2, 0, f"{directory}", curses.A_REVERSE)
            else:
                stdscr.addstr(idx + 2, 0, f"{directory}")

        stdscr.refresh()
        key = stdscr.getch()
        if key == ord('q'):
            return None
        elif key == curses.KEY_UP and current_selection > 0:
            current_selection -= 1
        elif key == curses.KEY_DOWN and current_selection < len(directories) - 1:
            current_selection += 1
        elif key == ord('\n'):
            selected_directory = directories[current_selection]
            return selected_directory
    return None
