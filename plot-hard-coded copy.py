import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# Sample data ...
data_original = """Project Name	Type of test	Average
Amazon	Coleman-Liau Index	10,66
Amazon	Dale-Chall Readability Score	8,45
Amazon	Difficult Words	71
Amazon	Flesch Reading Ease	57,16
Amazon	Flesch-Kincaid Grade	8,8
Amazon	Gunning Fog	8,7
Amazon	Linsear Write Formula	6
Euronym	Coleman-Liau Index	20,05
Euronym	Dale-Chall Readability Score	10,06
Euronym	Difficult Words	142
Euronym	Flesch Reading Ease	35,34
Euronym	Flesch-Kincaid Grade	11
Euronym	Gunning Fog	9,16
Euronym	Linsear Write Formula	6,3
Facebook	Coleman-Liau Index	12,41
Facebook	Dale-Chall Readability Score	7,45
Facebook	Difficult Words	168
Facebook	Flesch Reading Ease	53,51
Facebook	Flesch-Kincaid Grade	10,2
Facebook	Gunning Fog	9,61
Facebook	Linsear Write Formula	11,6"""

data_developers = """Project Name	Type of test	Average
Amazon	Coleman-Liau Index	14.57083333
Amazon	Dale-Chall Readability Score	10.2375
Amazon	Difficult Words	110.25
Amazon	Flesch Reading Ease	37.435
Amazon	Flesch-Kincaid Grade	11.725
Amazon	Gunning Fog	11.6
Amazon	Linsear Write Formula	8.168882275
Euronym	Coleman-Liau Index	23.82333333
Euronym	Dale-Chall Readability Score	12.49666667
Euronym	Difficult Words	130.8333333
Euronym	Flesch Reading Ease	13.74916667
Euronym	Flesch-Kincaid Grade	13.73333333
Euronym	Gunning Fog	11.385
Euronym	Linsear Write Formula	9.432440476
Facebook	Coleman-Liau Index	17.275
Facebook	Dale-Chall Readability Score	10.99833333
Facebook	Difficult Words	109.75
Facebook	Flesch Reading Ease	36.52833333
Facebook	Flesch-Kincaid Grade	10.50833333
Facebook	Gunning Fog	9.2175
Facebook	Linsear Write Formula	5.507112795"""

data_managers = """Project Name	Type of test	Average
Amazon	Coleman-Liau Index	9.900833333
Amazon	Dale-Chall Readability Score	8.49
Amazon	Difficult Words	68.5
Amazon	Flesch Reading Ease	59.50833333
Amazon	Flesch-Kincaid Grade	8.933333333
Amazon	Gunning Fog	9.945833333
Amazon	Linsear Write Formula	8.246527778
Euronym	Coleman-Liau Index	13.915
Euronym	Dale-Chall Readability Score	9.973333333
Euronym	Difficult Words	98
Euronym	Flesch Reading Ease	42.46916667
Euronym	Flesch-Kincaid Grade	11.325
Euronym	Gunning Fog	12.29
Euronym	Linsear Write Formula	10.54087302
Facebook	Coleman-Liau Index	11.2125
Facebook	Dale-Chall Readability Score	9.121666667
Facebook	Difficult Words	89.5
Facebook	Flesch Reading Ease	56.73583333
Facebook	Flesch-Kincaid Grade	9.141666667
Facebook	Gunning Fog	10.44
Facebook	Linsear Write Formula	8.837400794"""

# Read data into dataframes
df_original = pd.read_csv(StringIO(data_original), delimiter='\t')
df_developers = pd.read_csv(StringIO(data_developers), delimiter='\t')
df_managers = pd.read_csv(StringIO(data_managers), delimiter='\t')

# Merge the dataframes on 'Project Name' and 'Type of test'
combined_df = pd.merge(df_original, df_developers, on=['Project Name', 'Type of test'], suffixes=('_Original', '_Developers'))
combined_df = pd.merge(combined_df, df_managers, on=['Project Name', 'Type of test'], suffixes=('', '_Managers'))

# Create a grouped or stacked column chart
fig, ax = plt.subplots(figsize=(12, 6))

# Number of bars
n = len(combined_df)
index = range(n)

# Width of a bar
bar_width = 0.2

# Create bars for Original, Developers, and Managers
plt.bar(index, combined_df['Average'], bar_width, label='Original')
plt.bar([i + bar_width for i in index], combined_df['Average_Developers'], bar_width, label='Developers')
plt.bar([i + 2 * bar_width for i in index], combined_df['Average_Original'], bar_width, label='Managers')

# X-axis labels
plt.xticks([i + bar_width for i in index], combined_df['Project Name'] + ' - ' + combined_df['Type of test'], rotation=90)

# Set labels and title
plt.xlabel('Project Name - Type of Test')
plt.ylabel('Average')
plt.title('Comparison of Original, Developers, and Managers')

# Show legend
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
