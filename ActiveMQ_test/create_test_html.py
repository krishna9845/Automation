import json
import os
import os.path
import time

import numpy as np
import pandas as pd
from jinja2 import Environment, FileSystemLoader
from selenium import webdriver as seleniumWebDriver

df = pd.read_excel('clients7C.xlsx', sheet_name='Sheet1')

env = Environment(loader=FileSystemLoader('./'))
template = env.get_template('stomp-scl-usr_test_TV_durable.html')
# Load the template
template_browser = env.get_template('test_mq.html')

for client_id in df['Client ID']:
    # Iterate over each client ID in the DataFrame

    # Render the template with the current client ID
    output = template.render(client_id=client_id)

    # Do something with the rendered output
    # For example, you can save it to a new file
    filename = os.path.abspath(f'./html_files/output_{client_id}.html')
    print(filename)
    with open(filename, 'w') as file:
        file.write(output)


output = template_browser.render(client_list=json.dumps(df['Client ID'].to_list()))
with open("./html_filesss/test_mq_balta.html", 'w') as file:
    file.write(output)

filename = os.path.abspath(f'./html_filesss/test_mq_balta.html')

chrome_options = seleniumWebDriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--privileged")
chrome_options.add_argument("--headless")
# chrome_options.add_experimental_option('prefs', {'download.default_directory': download_path})
# desired_capabilities = chrome_options.to_capabilities()
# driver = seleniumWebDriver.Chrome(
#         executable_path=os.getcwd() + f"web_drivers/darwin/chromedriver",
#         desired_capabilities=desired_capabilities,
#         chrome_options=chrome_options
# )
# driver.implicitly_wait(time_to_wait=10)
# driver.maximize_window()
# # chrome_options = Options()
# # chrome_options.add_argument("--headless")  # Enable headless mode
# # Set path to the chromedriver executable (update with your own path)
#
# # Create a new instance of the Chrome driver with the headless options
#
# # Create a new instance of the Selenium WebDriver
# # driver = webdriver.Chrome(drivers, options=chrome_options)
# # Load the generated HTML file
#
# driver.get(f'file://{filename}')

