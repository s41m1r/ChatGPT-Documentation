import pandas as pd
import matplotlib.pyplot as plt

# Define the data from Table 1 (Original)
data_original = {
    'Project Name': ['Amazon', 'Amazon', 'Amazon', 'Amazon', 'Amazon', 'Amazon', 'Amazon', 'Euronym', 'Euronym', 'Euronym', 'Euronym', 'Euronym', 'Euronym', 'Euronym', 'Facebook', 'Facebook', 'Facebook', 'Facebook', 'Facebook', 'Facebook', 'Facebook'],
    'Type of test': ['Coleman-Liau Index', 'Dale-Chall Readability Score', 'Difficult Words', 'Flesch Reading Ease', 'Flesch-Kincaid Grade', 'Gunning Fog', 'Linsear Write Formula', 'Coleman-Liau Index', 'Dale-Chall Readability Score', 'Difficult Words', 'Flesch Reading Ease', 'Flesch-Kincaid Grade', 'Gunning Fog', 'Linsear Write Formula', 'Coleman-Liau Index', 'Dale-Chall Readability Score', 'Difficult Words', 'Flesch Reading Ease', 'Flesch-Kincaid Grade', 'Gunning Fog', 'Linsear Write Formula'],
    'Baseline': [10.66, 8.45, 71, 57.16, 8.8, 8.7, 6, 20.05, 10.06, 142, 35.34, 11, 9.16, 6.3, 12.41, 7.45, 168, 53.51, 10.2, 9.61, 11.6]
}

# Define the data from Table 2 (Developers)
data_developers = {
    'Project Name': ['Amazon', 'Amazon', 'Amazon', 'Amazon', 'Amazon', 'Amazon', 'Amazon', 'Euronym', 'Euronym', 'Euronym', 'Euronym', 'Euronym', 'Euronym', 'Euronym', 'Facebook', 'Facebook', 'Facebook', 'Facebook', 'Facebook', 'Facebook', 'Facebook'],
    'Type of test': ['Coleman-Liau Index', 'Dale-Chall Readability Score', 'Difficult Words', 'Flesch Reading Ease', 'Flesch-Kincaid Grade', 'Gunning Fog', 'Linsear Write Formula', 'Coleman-Liau Index', 'Dale-Chall Readability Score', 'Difficult Words', 'Flesch Reading Ease', 'Flesch-Kincaid Grade', 'Gunning Fog', 'Linsear Write Formula', 'Coleman-Liau Index', 'Dale-Chall Readability Score', 'Difficult Words', 'Flesch Reading Ease', 'Flesch-Kincaid Grade', 'Gunning Fog', 'Linsear Write Formula'],
    'Average': [14.57083333, 10.2375, 110.25, 37.435, 11.725, 11.6, 8.168882275, 23.82333333, 12.49666667, 130.8333333, 13.74916667, 13.73333333, 11.385, 9.432440476, 17.275, 10.99833333, 109.75, 36.52833333, 10.50833333, 9.2175, 5.507112795]
}

# Define the data from Table 3 (Managers)
data_managers = {
    'Project Name': ['Amazon', 'Amazon', 'Amazon', 'Amazon', 'Amazon', 'Amazon', 'Amazon', 'Euronym', 'Euronym', 'Euronym', 'Euronym', 'Euronym', 'Euronym', 'Euronym', 'Facebook', 'Facebook', 'Facebook', 'Facebook', 'Facebook', 'Facebook', 'Facebook'],
    'Type of test': ['Coleman-Liau Index', 'Dale-Chall Readability Score', 'Difficult Words', 'Flesch Reading Ease', 'Flesch-Kincaid Grade', 'Gunning Fog', 'Linsear Write Formula', 'Coleman-Liau Index', 'Dale-Chall Readability Score', 'Difficult Words', 'Flesch Reading Ease', 'Flesch-Kincaid Grade', 'Gunning Fog', 'Linsear Write Formula', 'Coleman-Liau Index', 'Dale-Chall Readability Score', 'Difficult Words', 'Flesch Reading Ease', 'Flesch-Kincaid Grade', 'Gunning Fog', 'Linsear Write Formula'],
    'Average': [9.900833333, 8.49, 68.5, 59.50833333, 8.933333333, 9.945833333, 8.246527778, 13.915, 9.973333333, 98, 42.46916667, 11.325, 12.29, 10.54087302, 11.2125, 9.121666667, 89.5, 56.73583333, 9.141666667, 10.44, 8.837400794]
}

# Create dataframes
df_original = pd.DataFrame(data_original)
df_developers = pd.DataFrame(data_developers)
df_managers = pd.DataFrame(data_managers)

# Combine the data from all three tables into one dataframe
merged_df = pd.concat([df_original, df_developers[['Type of test', 'Average']], df_managers[['Type of test', 'Average']]], axis=1)

# Create a box plot for the merged data
plt.figure(figsize=(12, 6))
merged_df.boxplot(column=['Baseline', 'Average', 'Average'], by='Type of test', rot=90)

# Customize the plot
plt.xlabel('Type of Test')
plt.ylabel('Value')
plt.title('Box Plot Comparison of Original, Developers (Average), and Managers (Average)')

# Show the plot
plt.tight_layout()
plt.show()
