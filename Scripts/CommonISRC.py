import pandas as pd
# Your TSV data file
filename = r"C:\Users\prana\OneDrive\Desktop\unclaimed.csv"

# CSV that contains one column listing column names
columns_file = r"C:\Users\prana\Downloads\star2.csv"

# Read the single-column CSV and convert it into a list
use_columns = pd.read_csv(columns_file, header=None).iloc[:, 0].dropna().tolist()

# Your ISRC to search for
search_isrc = use_columns

# Define which column to search in
search_column = "ISRC"

chunksize = 200000
found_rows = []
for chunk in pd.read_csv(filename, sep=',', chunksize=chunksize):
    matches = chunk[chunk[search_column].isin(search_isrc)]
    if not matches.empty:
        found_rows.append(matches)

# Combine all found rows
if found_rows:
    result_df = pd.concat(found_rows, ignore_index=True)

print(result_df)
df = pd.DataFrame(result_df)
csv_filename = r"C:\Users\prana\Downloads\last.csv"
df.to_csv(csv_filename, index=False, encoding="utf-8")