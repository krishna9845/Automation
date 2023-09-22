# Load the Excel file into a pandas DataFrame
import multiprocessing
import os.path
import time

import numpy as np
import pandas as pd
from jinja2 import Environment, FileSystemLoader
from selenium import webdriver as seleniumWebDriver

# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# Create the Jinja2 environment
env = Environment(loader=FileSystemLoader('./'))

# Load the template
template = env.get_template('template.html')


def process_row(df):
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
        # Set Chrome options for running the browser in headless mode

        # driver = WebDriver(browser='chrome')
        chrome_options = seleniumWebDriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--privileged")
        chrome_options.add_argument("--headless")
        # chrome_options.add_experimental_option('prefs', {'download.default_directory': download_path})
        desired_capabilities = chrome_options.to_capabilities()
        driver = seleniumWebDriver.Chrome(
            executable_path=os.getcwd() + f"web_drivers/darwin/chromedriver",
            desired_capabilities=desired_capabilities,
            chrome_options=chrome_options
        )
        driver.implicitly_wait(time_to_wait=10)
        driver.maximize_window()
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")  # Enable headless mode

        # Set path to the chromedriver executable (update with your own path)

        # Create a new instance of the Chrome driver with the headless options

        # Create a new instance of the Selenium WebDriver
        # driver = webdriver.Chrome(drivers, options=chrome_options)
        # Load the generated HTML file

        driver.get(f'file://{filename}')
        time.sleep(1200)
        driver.quit()
        # driver.implicitly_wait(300)
        # driver.quit()
        return df


if __name__ == '__main__':
    # Define a function to apply in parallelßß

    # # Set the number of parallel processes
    num_processes = 100
    print("num_processes", num_processes)
    # Create a sample DataFrame
    df = pd.read_excel('clients_1.xlsx', sheet_name='Sheet1')
    # process_row(df)
    # Split the DataFrame into chunks for parallel processing
    chunks = np.array_split(df, df.shape[0])
    print("Number of client ID's", len(chunks))
    # # Create a multiprocessing Pool
    pool = multiprocessing.Pool(processes=num_processes)
    # # Apply the process_row function to each chunk in parallel
    processed_chunks = pool.map(process_row, chunks)
    # # Concatenate the processed chunks back into a single DataFrame
    processed_df = pd.concat(processed_chunks)
    # # Close the multiprocessing Pool
    pool.close()
    pool.join()
    # # Print the processed DataFrame
    print(processed_df)
