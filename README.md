# LinkedIn Invitation Automation

This script automates the process of accepting connection invitations on LinkedIn and sending personalized messages to each connection.

## Features

- Logs in to LinkedIn.
- Navigates to the connection requests page.
- Accepts all connection requests.
- Sends a personalized message to each new connection, including a YouTube link.
- The script automatically selects a random YouTube link from a list.

## Requirements

To use this script, you must have:

- Python 3.9 or higher installed.
- Google Chrome installed.
- ChromeDriver installed (compatible with your Chrome version).
- A LinkedIn account.

## Installing Dependencies

1. Clone the repository:
   ```bash
   git clone https://github.com/ReemOmer/LinkedInMessenger.git
   cd LinkedInMessenger
    ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
    ```

3. Create a .env file in the project directory and add your LinkedIn credentials:
   ```bash
    EMAIL=your_email@example.com
    PASSWORD=your_password
    ```

## Running the Script
To run the script, use the following command:
   ```bash
    python accept_invitations.py
```

## Notes
- Make sure to use the correct path for the chromedriver.exe file in the script.
- Always be careful when automating social platforms as it can violate their terms of service. Use this script responsibly.    
