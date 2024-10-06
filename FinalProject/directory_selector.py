import curses
import os

def list_directories(stdscr, base_path):
    if not os.path.exists(base_path):
        stdscr.addstr(0, 0, f"Directory does not exist: {base_path}")
        stdscr.refresh()
        stdscr.getch()  # Wait for a key press to acknowledge
        return []  # Return an empty list if the directory doesn't exist

    directories = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
    return directories

def directory_selection_ui(stdscr, username):
    # Use os.path.expanduser to get the user's home directory
    base_path = os.path.expanduser(f"~/")  # This will point to the logged-in user's home directory
    stdscr.addstr(0, 0, f"Base path: {base_path}")
    stdscr.refresh()
    stdscr.getch()

    directories = list_directories(stdscr, base_path)

    stdscr.clear()
    stdscr.addstr(0, 0, f"Welcome, {username}! Select a directory to upload files:")
    for idx, directory in enumerate(directories):
        stdscr.addstr(idx + 2, 0, f"{idx + 1}. {directory}")

    stdscr.addstr(len(directories) + 2, 0, "Press the number corresponding to the directory and ENTER.")
    stdscr.refresh()

    key = stdscr.getch()
    selected_index = key - ord('1')  # Convert to zero-based index
    if 0 <= selected_index < len(directories):
        selected_directory = directories[selected_index]
        stdscr.clear()
        stdscr.addstr(0, 0, f"You selected: {selected_directory}")
        stdscr.addstr(2, 0, "Now you can drag and drop files to upload them.")
        stdscr.refresh()
        stdscr.getch()
    else:
        stdscr.addstr(4, 0, "Invalid selection. Press any key to return.")
        stdscr.refresh()
        stdscr.getch()
                    