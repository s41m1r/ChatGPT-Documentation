import os
from textstat import textstat

def read_text_files_in_subfolders(folder_path):
    file_contents = []

    # Check if the folder path exists
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        return file_contents

    # Walk through the folder and its subfolders
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            # Check if the file is a text file
            if file_name.endswith(".tex") and os.path.isfile(file_path):
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                    file_contents.append((file_path, content))

    return file_contents

# Example usage:
folder_path = "/Users/saimirbala/Downloads/Software documentation + ChatGPT/Data/GPT4_Devs"
file_contents = read_text_files_in_subfolders(folder_path)

# Print the list of tuples
for file_path, content in file_contents:
    print(f"File Path: {file_path}\nflesch_reading_ease:\n{textstat.flesch_reading_ease(content)}\n")
