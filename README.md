# Website Status Checker - Flask App

This is a simple Flask web application that allows you to select a website from a list and run several network diagnostic commands on it. The app shows the output of commands like `ping`, `nslookup`, `traceroute` (or `tracert` on Windows), and `curl` HTTP headers, and it also extracts and displays the HTTP status code from the site.

<img width="433" height="161" alt="image" src="https://github.com/user-attachments/assets/8c4db55f-4dc5-4762-9450-968d71a5e66a" />


---

## Features

- Select a website from a predefined list.
- Run network commands: `ping`, `nslookup`, `traceroute`/`tracert`, and `curl`.
- Display the output of each command in the browser.
- Show HTTP status code returned by the website or display if unreachable.

---

## Prerequisites

- Python 3.x installed
- Flask installed (`pip install flask`)
- `curl` command line tool installed and available in your system PATH

---

## Installation and Usage

1. Clone or download this repository.

2. Make sure you have Flask installed. If not, install it using:

   ```bash
   pip install flask

3. Ensure curl is installed on your system:

- On Linux/macOS, curl usually comes pre-installed.

- On Windows 10 or later, curl is included by default.

4. Run the Flask app:

   ```bash
   python app.py

5. Open your browser and go to:

- http://127.0.0.1:5000/

6. Select a website from the dropdown and click Check.

7. View the status message and the output of the diagnostic commands.
