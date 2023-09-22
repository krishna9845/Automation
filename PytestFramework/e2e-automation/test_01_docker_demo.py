from selenium import webdriver

# Configure Selenium to connect to the VNC server in the Docker container
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument('--headless')
options.add_argument('--remote-debugging-port=9222')
options.add_argument('--disable-extensions')

driver = webdriver.Remote(
    command_executor='http://localhost:4444',
    desired_capabilities=options.to_capabilities(),
)

# Use Selenium to interact with the browser
driver.get('https://www.example.com')
print(driver.title)

# Close the browser
driver.quit()
