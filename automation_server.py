from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

app = Flask(__name__)

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

@app.route('/run-automation', methods=['GET'])
def run_automation():
    try:
        # Connect to existing Chrome session
        options = webdriver.ChromeOptions()
        options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        driver = webdriver.Chrome(options=options)

        # Wait for the page to load
        wait = WebDriverWait(driver, 10)

        for skill in skills:
            print(f"Processing skill: {skill}")

            # Locate the search box
            search_box = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@data-automation-id="searchBox"]')))
            
            # Clear the box and type the skill
            search_box.clear()
            search_box.send_keys(skill)
            # Simulate pressing "Enter"
            search_box.send_keys(Keys.RETURN)
            time.sleep(3)  # Allow time for dropdown to process

            # Find all dropdown options
            dropdown_options = driver.find_elements(By.XPATH, '//div[@data-automation-id="promptOption"]')

            # Iterate through dropdown options to find the matching skill
            for option in dropdown_options:
                label = option.get_attribute('data-automation-label')
                if label == skill:
                    # Scroll to the option to ensure visibility
                    driver.execute_script("arguments[0].scrollIntoView(true);", option)
                    time.sleep(1)  # Allow time for the scroll action

                    # Click the matching option
                    option.click()
                    print(f"Selected: {skill}")

                    # Click the 'X' to clear the search box
                    clear_button = wait.until(EC.element_to_be_clickable(
                        (By.XPATH, '//*[@data-automation-id="clearSearchButton"]')
                    ))
                    clear_button.click()
                    print(f"Cleared search box for skill: {skill}")
                    break
            else:
                print(f"Skill '{skill}' not found in dropdown options.")

        return jsonify({"status": "Automation completed successfully!"})
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({"status": f"Error: {e}"})
    finally:
        driver.quit()

if __name__ == '__main__':
    app.run(port=5000)
