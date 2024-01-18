import pyarrow.parquet as pq

# Specify the path to your Parquet file
parquet_file_path = 'C:/Users/Analyst07/Desktop/govtech/blood_donation_retention_2024.parquet'

# Use pyarrow to read the Parquet file
table = pq.read_table(parquet_file_path)

# Convert the table to a Pandas DataFrame
df = table.to_pandas()

# Now 'df' contains your data from the Parquet file
print(df.head())

print(len(df))