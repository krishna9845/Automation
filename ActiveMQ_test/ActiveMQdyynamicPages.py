import pandas as pd
from jinja2 import Environment, FileSystemLoader

# Load the Excel file into a pandas DataFrame
df = pd.read_excel('clients.xlsx', sheet_name='Sheet1')

# Create the Jinja2 environment
env = Environment(loader=FileSystemLoader('./'))

# Load the template
template = env.get_template('template.html')

# Iterate over each client ID in the DataFrame
for client_id in df['Client ID']:
    # Render the template with the current client ID
    output = template.render(client_id=client_id)

    # Do something with the rendered output
    # For example, you can save it to a new file
    filename = f'output_{client_id}.html'
    with open(filename, 'w') as file:
        file.write(output)
