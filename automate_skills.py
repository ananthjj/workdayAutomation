import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# List of skills
skills = [
    "Software Development", "UX Design", "Cloud Deployment", "Data Analysis and Visualization",
    "Quality Assurance Testing", "Database Administration", "Product Management", "Agile Practices",
    "Requirements Gathering", "Wireframing", "Process Improvement", "Technical Writing",
    "Attention to Detail", "Cross-Functional Collaboration", "Communication and Leadership",
    "Research and Development", "Customer and Market Insights", "Futurology", "Python", "R", "SQL",
    "C", "C++", "Java", "JavaScript", "Prolog", "Racket", "HTML", "CSS", "ARM", "Linux", "MATLAB",
    "Flask", "React", "AWS", "Google Cloud", "Android SDK", "OpenAI", "Mistral", "Gemini", "Phi",
    "Llama", "Ollama", "Hugging Face", "Airtable", "Zilliz", "Firebase", "Snowflake", "Figma",
    "Draw Things", "IMOD", "PEET", "RELION3", "Adobe Cloud"
]

def automate_skills():
    # Set up ChromeDriver
    driver = webdriver.Chrome()

    # Navigate to the webpage (replace with the actual URL)
    driver.get("https://example-workday-url.com")  # Replace with the actual Workday page URL
    time.sleep(5)  # Wait for the page to load

    for skill in skills:
        # Locate the search box
        search_box = driver.find_element(By.XPATH, '//input[@id="search-box-id"]')  # Update XPath
        search_box.clear()
        search_box.send_keys(skill)
        time.sleep(1)  # Wait for the dropdown to populate

        # Select the skill from the dropdown
        dropdown_option = driver.find_element(By.XPATH, f'//div[contains(text(), "{skill}")]')  # Update XPath
        dropdown_option.click()

        # Wait for the selection to be processed
        time.sleep(2)

    # Close the browser
    driver.quit()

print("Press CTRL+ALT+A to start the automation")
keyboard.add_hotkey('ctrl+alt+a', automate_skills)

# Keep the script running
keyboard.wait('esc')  # Press ESC to exit the program
