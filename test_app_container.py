from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Setup Chrome WebDriver
driver = webdriver.Chrome()
# Open the containerized app
driver.get("http://localhost:8080")
def log_result(message):
    print(f"[+] {message}")
# --- Test Case 1: Valid Name Input —
name_input = driver.find_element(By.ID, "username")
name_input.clear()
name_input.send_keys("DevOps")
greet_button = driver.find_element(By.TAG_NAME, "button")
greet_button.click()
time.sleep(5)
output = driver.find_element(By.ID, "greeting").text
assert output == "Hello, DevOps!", "❌ Test 1 Failed"
log_result("✅ Test 1 Passed - Valid name input greeted correctly.")
# --- Test Case 2: Empty Input Handling —
name_input.clear()
greet_button.click()
time.sleep(5)
output = driver.find_element(By.ID, "greeting").text
assert output == "Please enter your name.", "❌ Test 2 Failed"
log_result("✅ Test 2 Passed - Empty input handled.")

# --- Save Screenshot —
driver.save_screenshot("selenium_test_output.png")
log_result("📸 Screenshot saved as selenium_test_output.png")
driver.quit()
