import pandas as pd
import matplotlib.pyplot as plt

# Load data from your three tables: Original, Developers, and Management
original_data = pd.read_excel('Data/output/readability_metrics3Original.xlsx')  # Replace with the actual file path
developers_data = pd.read_excel('Data/output/readability_metrics3Devs.xlsx')  # Replace with the actual file path
management_data = pd.read_excel('Data/output/readability_metrics3Manager.xlsx')  # Replace with the actual file path

# Ensure that the three tables have the same structure (columns)
# You can rename columns if needed to match
original_data = original_data.rename(columns={'Project Name': 'Project', 'Type of test': 'Test', 'Average': 'Original'})
developers_data = developers_data.rename(columns={'Project Name': 'Project', 'Type of test': 'Test', 'Average': 'Developers'})
management_data = management_data.rename(columns={'Project Name': 'Project', 'Type of test': 'Test', 'Average': 'Management'})

# Merge the data from the three tables using 'Project' and 'Test' columns as keys
merged_data = pd.merge(original_data, developers_data, on=['Project', 'Test'])
merged_data = pd.merge(merged_data, management_data, on=['Project', 'Test'])

# Create a comparison plot
plt.figure(figsize=(10, 6))

# Customize plot style for a research paper
plt.style.use('seaborn-whitegrid')

# Sort the data for better visualization
merged_data = merged_data.sort_values(by=['Original'])

# Plot the data
plt.plot(merged_data['Project'], merged_data['Original'], marker='o', label='Original', linestyle='-', color='b', linewidth=2)
plt.plot(merged_data['Project'], merged_data['Developers'], marker='s', label='Developers', linestyle='--', color='g', linewidth=2)
plt.plot(merged_data['Project'], merged_data['Management'], marker='^', label='Management', linestyle='-.', color='r', linewidth=2)

# Add labels and title
plt.xlabel('Project')
plt.ylabel('Average Value')
plt.title('Comparison of Developers and Management to Original Data')
plt.xticks(rotation=45)
plt.legend()

# Save the plot as a high-resolution image suitable for a research paper
plt.savefig('comparison_plot.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()
