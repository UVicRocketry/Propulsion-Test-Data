
###############################################################################
# Converts json dumped data from the PDP to CSV format.
# Also creates a "seconds" column from the "timestamp" entry for easier
# plotting.
#
# To use, run this script with the file name of the json data passed as an
# argument. For example:
# $ python json_to_csv.py my_json.txt
# A file of the same name with the extension .csv will be created.
###############################################################################


import sys
import json
import pandas as pd
from datetime import datetime

# Read the file name from command-line arguments
try:
    file_name = sys.argv[1]
except IndexError:
    print('Unknown file. Pass file name in call to program')
    sys.exit()

# List of dictionaries corresponding to each line of JSON data
ds = []

# Read the JSON data from the file
try:
    with open(file_name, 'r') as file:
        print('Reading. This may take a while...')
        lines = file.readlines()

        for line in lines:
            json_data = line.strip()  # Clean up any extra whitespace/newlines
            data_dict = json.loads(json_data)
            ds.append(data_dict)

except Exception as e:
    print(f'Error: {e}')
    sys.exit()

df = pd.DataFrame(ds)

# Convert 'timestamp' field to datetime objects and calculate the 'seconds' column
df['timestamp'] = pd.to_datetime(df['timestamp'])
first_timestamp = df['timestamp'].iloc[0]
df['seconds'] = (df['timestamp'] - first_timestamp).dt.total_seconds()

# Convert to csv
output_file_name = file_name[:-3] + 'csv'
with open(output_file_name, 'w') as out_file:
    print('Converting to csv...')
    df.to_csv(out_file, index=False)

print("Done.")
