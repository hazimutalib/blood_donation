import requests
import pandas as pd

# GitHub raw content URL for the CSV file
github_raw_url = "https://raw.githubusercontent.com/MoH-Malaysia/data-darah-public/main/donations_state.csv"

# Make a GET request to the raw content URL
response = requests.get(github_raw_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Save the content to a local file
    local_file_path = "donations_state.csv"
    df = pd.read_csv('https://raw.githubusercontent.com/MoH-Malaysia/data-darah-public/main/donations_state.csv')
    print(df.head())
    with open(local_file_path, 'wb') as file:
        file.write(response.content)

    print(f"File downloaded successfully. Saved to: {local_file_path}")
else:
    print(f"Failed to fetch file. Status code: {response.status_code}")
