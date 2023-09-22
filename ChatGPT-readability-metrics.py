import os
import pandas as pd
from textstat import flesch_reading_ease, flesch_kincaid_grade, gunning_fog, coleman_liau_index, linsear_write_formula, dale_chall_readability_score, difficult_words
from statistics import median, stdev
import seaborn as sns
import matplotlib.pyplot as plt


def calculate_readability_metrics(text):
    metrics = {
        "Flesch Reading Ease": flesch_reading_ease(text),
        "Flesch-Kincaid Grade": flesch_kincaid_grade(text),
        "Gunning Fog": gunning_fog(text),
        "Coleman-Liau Index": coleman_liau_index(text),
        "Linsear Write Formula": linsear_write_formula(text),
        "Dale-Chall Readability Score": dale_chall_readability_score(text),
        "Difficult Words": difficult_words(text)
    }
    return metrics

def process_folder(folder_path):
    results = []
    
    # Check if the folder path exists
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        return results

    # Walk through the folder and its subfolders
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith(".tex"):
                file_path = os.path.join(root, file_name)
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                    versions = file_name.split("_")
                    if len(versions) == 3:
                        version_number = pd.to_numeric(versions[1],errors="coerce")
                    else:
                        version_number = "N/A"
                    
                    # Extract the Project name from the second last part of the File path
                    project_name = file_path.split("/")[-2]

                    metrics = calculate_readability_metrics(content)
                    metrics["File Path"] = file_path
                    metrics["Version Number"] = version_number
                    metrics["Project Name"] = project_name  # Add Project Name to the metrics
                    results.append(metrics)

    return results

def process(folder_path, audience):
    results = process_folder(folder_path)

    # Create a DataFrame from the results
    df = pd.DataFrame(results)

    # Melt the DataFrame to have metrics as columns
    df_melted = pd.melt(df, id_vars=["File Path", "Project Name", "Version Number"], var_name="Type of test", value_name="output")\
        .sort_values(by=['Project Name','Version Number'])
    

    # Calculate average, median, and standard deviation for each metric, grouped by Project Name
    summary = df_melted.groupby(["Type of test","Project Name"]).agg(
        Average=("output", "mean"),
        Median=("output", median),
        StdDev=("output", stdev)
    ).reset_index()

    # Create a DataFrame with metric explanations
    metric_explanations = {
        "Flesch Reading Ease": "Measures the readability of text (higher values indicate easier readability).",
        "Flesch-Kincaid Grade": "Measures the U.S. grade level needed to understand the text.",
        "Gunning Fog": "Estimates the years of formal education needed to understand the text.",
        "Coleman-Liau Index": "Evaluates the understandability of text based on characters.",
        "Linsear Write Formula": "Estimates readability based on sentence length and easy words.",
        "Dale-Chall Readability Score": "Assesses the understandability of text for a U.S. 4th-grade student.",
        "Difficult Words": "Counts the number of difficult words in the text."
    }
    
    metric_explanations_df = pd.DataFrame(metric_explanations.items(), columns=["Type of test", "Metric Explanation"])
    # Directory path where you want to save the file
    output_directory = "Data/output"

    # Create the directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Write the results and metric explanations to an Excel file with separate tabs
    with pd.ExcelWriter(os.path.join(output_directory, f"readability_metrics3{audience}.xlsx"), engine="xlsxwriter") as writer:
        df_melted.to_excel(writer, sheet_name="Results", index=False)
        summary.to_excel(writer, sheet_name="Summary", index=False)
        metric_explanations_df.to_excel(writer, sheet_name="Metric Explanations", index=False)

    # Create a box plot for the summary statistics, grouped by Test and Project Name
    plt.figure(figsize=(12, 8))
    sns.boxplot(data=df_melted, x="Type of test", y="output", hue="Project Name")
    plt.xticks(rotation=90)
    plt.yscale('log')  # Set y-axis to logarithmic scale
    plt.title("Box Plot of Readability Metrics by Test and Project")
    plt.tight_layout()
    
    # Export the plot as a PDF (vector graphics)
    plt.savefig("Data/output/readability_metrics_box_plot"+audience+".pdf", format="pdf")

def main():

    folder_path = "Data/GPT4_Devs"
    process(folder_path,"Devs")

    folder_path = "Data/GPT4_Manager"
    process(folder_path,"Manager")

    folder_path = "Data/Original descriptions"
    process(folder_path,"Original")
    
if __name__ == "__main__":
    main()
