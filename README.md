
# ServX  

**ServX** is a Terminal User Interface (TUI) application designed to simplify file management for students. It allows users to log in with their college server credentials, browse folders on their server homepage, and upload files directly from their local system to the server, freeing up local storage.  

## Features  
- **Secure Login:** Authenticate using college server credentials.  
- **Folder Navigation:** Browse and select folders from the server.  
- **File Upload:** Upload files from your local system to the college server.  
- **Lightweight:** Runs in a terminal with a user-friendly interface.  

---

## Requirements  
- Python 3.7 or higher  
- `paramiko` for SSH connections  
- `curses` for the terminal-based user interface  

---

## Installation  

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/ssudhanshu488/servx.git
   cd servx
   cd FinalProject
   ```  

2. **Install Dependencies**  
   Use the `requirements.txt` file to install all necessary dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  

3. **Run the Application**  
   Start the ServX application using:  
   ```bash
   python servx.py
   ```  

---

## Usage  

1. Launch the application.  
2. Log in using your college server username and password.  
3. Navigate through your server folders using the TUI.  
4. Select a folder and upload files from your local system.  

---

## Compatibility  
- **Linux/macOS:** Built-in `curses` support is used.  
- **Windows:** Requires the `windows-curses` package (installed via `requirements.txt`).  

---

## Future Enhancements  
- Add support for downloading files from the server.  
- Implement a search feature for server folders.  
- Provide file type filters during uploads.  


