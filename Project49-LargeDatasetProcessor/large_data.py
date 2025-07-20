import pandas as pd

csv_file = "large_dataset.csv"

chunk_size = 10000

total_rows = 0
total_errors = 0

for chunk in pd.read_csv(csv_file, chunksize=chunk_size):
    error_rows = chunk[chunk['status'] == 'error']
    total_errors += len(error_rows)
    total_rows += len(chunk)

print(f"Total rows processed: {total_rows}")
print(f"Total error entries: {total_errors}")

