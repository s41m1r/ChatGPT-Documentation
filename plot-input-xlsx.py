import pandas as pd
import matplotlib.pyplot as plt

def create_box_plot(excel_file, sheet_name, category_column, value_column):
    # Read the Excel file with the specified sheet name
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    
    # Create a box plot
    plt.figure(figsize=(12, 6))
    df.boxplot(column=value_column, by=category_column, rot=90)
    
    # Customize the plot
    plt.xlabel(category_column)
    plt.ylabel(value_column)
    plt.title(f'Box Plot of {value_column} by {category_column}')
    
    # Show the plot
    plt.tight_layout()
    plt.show()


# Example usage:
# Replace 'your_data.xlsx' with the path to your Excel file
create_box_plot('Data/output/readability_metrics3Original.xlsx', 'Summary', 'Type of test', 'Average')
create_box_plot('Data/output/readability_metrics3Devs.xlsx', 'Summary', 'Type of test', 'Average')
create_box_plot('Data/output/readability_metrics3Devs.xlsx', 'Summary','Type of test', 'Median')
create_box_plot('Data/output/readability_metrics3Devs.xlsx', 'Summary','Type of test', 'StdDev')
