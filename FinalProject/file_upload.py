import curses
import os
import paramiko

def upload_file(ssh_client, file_path, destination_directory):
    """Upload a file via SSH."""
    if not os.path.exists(file_path):
        return False

    try:
        sftp = ssh_client.open_sftp()
        destination_path = f"{destination_directory}/{os.path.basename(file_path)}"
        sftp.put(file_path, destination_path)
        sftp.close()
        return True
    except Exception as e:
        print(f"File upload failed: {e}")
        return False

def get_file_path(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Enter the file path to upload:", curses.A_BOLD)
    stdscr.refresh()

    curses.echo()
    file_path = stdscr.getstr(1, 0).decode('utf-8')
    curses.noecho()

    return file_path.strip()

def file_upload_ui(stdscr, ssh_client, destination_directory):
    while True:
        file_path = get_file_path(stdscr)

        if not file_path:
            break

        success = upload_file(ssh_client, file_path, destination_directory)

        stdscr.clear()
        if success:
            stdscr.addstr(0, 0, f"File uploaded successfully to {destination_directory}", curses.A_BOLD)
        else:
            stdscr.addstr(0, 0, "File upload failed. Please try again.", curses.A_BOLD)

        stdscr.addstr(2, 0, "Press any key to continue or 'q' to quit")
        stdscr.refresh()

        if stdscr.getch() == ord('q'):
            break
