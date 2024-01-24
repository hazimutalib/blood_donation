# import pyarrow.parquet as pq

# # Specify the path to your Parquet file
# # parquet_file_path = 'C:/Users/Analyst07/Desktop/blood_donation/blood_donation_retention_2024 (1).parquet'
# parquet_file_path = 'https://dub.sh/ds-data-granular'
# # Use pyarrow to read the Parquet file
# table = pq.read_table(parquet_file_path)

# # Convert the table to a Pandas DataFrame
# df = table.to_pandas()

# # Now 'df' contains your data from the Parquet file
# print(df.head())
# print(max(df.visit_date))
# print(len(df))


import pyarrow.parquet as pq
import pandas as pd
from io import BytesIO
import requests

# Replace 'your_parquet_file_url' with the actual URL of your Parquet file
parquet_file_url = 'https://dub.sh/ds-data-granular'

# Download the Parquet file from the URL
response = requests.get(parquet_file_url)
parquet_data = BytesIO(response.content)

# Read the Parquet file into a Pandas DataFrame
df = pq.read_pandas(parquet_data).to_pandas()

# Now you can work with the DataFrame (df)
print(df)
