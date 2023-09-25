# Import the pandas library and read and merge data from provided URLs using the common 'Mouse ID' column.
import pandas as pd
merged_df = pd.read_csv('https://raw.githubusercontent.com/GBov81/Module-5/main/Pymaceuticals/data/Mouse_metadata.csv')\
    .merge(pd.read_csv('https://raw.githubusercontent.com/GBov81/Module-5/main/Pymaceuticals/data/Study_results.csv'), on='Mouse ID')

# Display the number of unique mice IDs in the merged DataFrame.
print("Number of unique mice IDs in merged DataFrame:", merged_df['Mouse ID'].nunique())

# Check for mouse IDs with duplicate time points.
duplicate_mouse_ids = merged_df[merged_df.duplicated(subset=['Mouse ID', 'Timepoint'])]['Mouse ID']

# Display the data associated with mouse IDs having duplicate time points.
print("Mouse IDs with duplicate time points:")
print(merged_df[merged_df['Mouse ID'].isin(duplicate_mouse_ids)])

# Create a new DataFrame with data removed for mouse IDs having duplicate time points.
cleaned_df = merged_df[~merged_df['Mouse ID'].isin(duplicate_mouse_ids)]

# Display the updated number of unique mice IDs in the cleaned DataFrame.
print("Number of unique mice IDs in the cleaned DataFrame:", cleaned_df['Mouse ID'].nunique())


