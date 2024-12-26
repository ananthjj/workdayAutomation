# Workday Automation

A Flask-based web automation tool with a Chrome extension, designed to automate entry of "Skills" on Workday applications. This project automates searching, selecting, and handling dropdown skill options dynamically based on predefined skills, leveraging both Flask for backend processing and Selenium for browser automation.

---

### Features

- Dropdown Automation: Automatically searches for predefined skills and selects matching options.
- Dynamic Matching: Matches skills with dropdown options using `data-automation-label` attributes.
- Chrome Extension: Includes a Chrome extension to trigger automation directly from the browser.
- Error Handling: Robust logging and error handling for seamless operation.
- Custom Server: Flask server handles automation requests.

---

### Directory Structure

workdayAutomation/
├── chrome-extension/         # Chrome extension files
│   ├── background.js         # Handles extension behavior
│   └── manifest.json         # Chrome extension configuration
├── venv/                     # Virtual environment for dependencies
├── automate_skills.py        # Main Python script for Selenium automation
├── automation_server.py      # Flask server for handling automation requests
└── README.md                 # Project documentation

---

### Prerequisites

Ensure you have the following installed before running the project:

- Python 3.7 or higher
- Google Chrome
- ChromeDriver (matching your Chrome version)
- Flask (`pip install flask`)
- Selenium (`pip install selenium`)

---

### Getting Started

#### Clone the Repository

git clone https://github.com/ananthjj/workdayAutomation.git
cd workdayAutomation

#### Set Up the Virtual Environment

1. Create a virtual environment:
   python3 -m venv venv

2. Activate the virtual environment:
   - Linux/Mac:
     source venv/bin/activate
   - Windows:
     venv\Scripts\activate

3. Install dependencies:
   pip install flask selenium

---

### Chrome Extension Setup

1. Open Chrome and navigate to `chrome://extensions/`.
2. Enable Developer Mode (top-right corner).
3. Click Load unpacked and select the `chrome-extension/` folder.
4. The extension is now loaded and ready to use.

---

### Running the Automation

#### 1. Start Chrome in Debug Mode
Run Chrome with the remote debugging port enabled:

- Linux/Mac:
  google-chrome --remote-debugging-port=9222 --user-data-dir=/tmp/chrome-debug

- Windows:
  "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\chrome-debug"

#### 2. Start the Flask Server
Run the Flask application to enable automation:

python automation_server.py

#### 3. Trigger Automation
Access the automation server in your browser or trigger it via the Chrome extension.

- Server URL:
  http://127.0.0.1:5000/run-automation

---

### File Details

#### automate_skills.py
- Contains the Selenium logic to:
  - Search for predefined skills.
  - Match skills with dropdown options.
  - Click the appropriate option dynamically.

#### automation_server.py
- A Flask server that:
  - Listens for automation requests.
  - Executes the automate_skills.py logic.

#### chrome-extension/
- background.js:
  - Handles Chrome extension interactions.
  - Sends requests to the Flask server for automation.
- manifest.json:
  - Configures the Chrome extension.

---

### Example Code Snippet

# Locate the search box
search_box = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@data-automation-id="searchBox"]')))
search_box.clear()
search_box.send_keys(skill)

# Find all dropdown options
dropdown_options = driver.find_elements(By.XPATH, '//div[@data-automation-id="promptOption"]')

# Match and click the skill
for option in dropdown_options:
    label = option.get_attribute('data-automation-label')
    if label == skill:
        driver.execute_script("arguments[0].scrollIntoView(true);", option)
        option.click()
        break

---

### Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
   git checkout -b feature/your-feature-name

3. Commit your changes:
   git commit -m "Add your message"

4. Push to the branch:
   git push origin feature/your-feature-name

5. Open a pull request.

---

### License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

### Issues

If you encounter any issues, please open an issue in this repository.
