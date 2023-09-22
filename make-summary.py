import pandas as pd

# Load the data from the existing Excel file
file_path = 'readability_metrics.xlsx'
df = pd.read_excel(file_path)

# Extract project name from the 'File path' column
df['Project'] = df['File Path'].apply(lambda x: x.split('/')[-2])

# Group the data by 'Project', 'Type of Test', and 'Version number' and calculate summary statistics
summary = df.groupby(['Project', 'Type of test']).agg(
    Count=('output', 'count'),
    Mean=('output', 'mean'),
    Median=('output', 'median'),
    StdDev=('output', 'std'),
    Min=('output', 'min'),
    Max=('output', 'max')
).reset_index()

# Save the summary data to a new Excel file
summary_file_path = 'project_summary_over_versions.xlsx'
summary.to_excel(summary_file_path, index=False)

print(f'Summary data saved to {summary_file_path}')
