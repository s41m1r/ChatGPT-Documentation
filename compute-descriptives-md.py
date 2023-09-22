import os
import pandas as pd
from markdown_it import MarkdownIt
import nltk
from nltk import sent_tokenize, word_tokenize

# Function to count elements and calculate average sentence length in words
def count_elements(text):
    # Initialize counters
    num_paragraphs = 0
    num_headers = 0
    num_highlighted_items = 0
    num_links = 0
    num_code_snippets = text.count('```') / 2
    
    # Count both bullet and numbered lists
    num_lists = text.count('- ') + text.count('1. ')  # Add other list types as needed
    
    num_tables = text.count('Table')

    # Tokenize the text into sentences using NLTK
    sentences = sent_tokenize(text)
    num_sentences = len(sentences)

    # Tokenize the text into words using NLTK
    words = word_tokenize(text)
    text_length_in_words = len(words)

    # Calculate average sentence length in words
    if num_sentences > 0:
        avg_sentence_length = text_length_in_words / num_sentences
    else:
        avg_sentence_length = 0

    # Initialize the MarkdownIt parser
    md = MarkdownIt()

    # Parse the Markdown text
    tokens = md.parse(text)

    # Iterate through tokens to count headers, links, and highlighted items
    for token in tokens:
        if token.type == 'paragraph_open':
            num_paragraphs += 1
        elif token.type == 'heading_open':
            num_headers += 1
        elif token.type == 'strong_open' or token.type == 'em_open':
            num_highlighted_items += 1
        elif token.type == 'link_open':
            num_links += 1

    return (
        num_paragraphs, num_headers, num_highlighted_items, num_links,
        num_code_snippets, num_lists, num_tables, num_sentences,
        text_length_in_words, avg_sentence_length
    )

# Function to process a .md file
def process_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Count elements and calculate average sentence length
    (
        num_paragraphs, num_headers, num_highlighted_items, num_links,
        num_code_snippets, num_bullet_lists, num_tables, num_sentences,
        text_length_in_words, avg_sentence_length
    ) = count_elements(text)

    return {
        'File': file_path,
        'Number of Paragraphs': num_paragraphs,
        'Number of Headers': num_headers,
        'Number of Highlighted Items': num_highlighted_items,
        'Number of Links': num_links,
        'Number of Code Snippets': num_code_snippets,
        'Number of Bullet Point Lists': num_bullet_lists,
        'Number of Tables': num_tables,
        'Number of Sentences': num_sentences,
        'Length of Text (words)': text_length_in_words,
        'Average Sentence Length (words)': avg_sentence_length
    }

# Initialize a list to store the results
results_list = []

# Process .md files in subfolders
for root, _, files in os.walk('Data'):
    for file in files:
        if file.endswith('.tex'):
            file_path = os.path.join(root, file)
            file_results = process_md_file(file_path)
            results_list.append(file_results)

# Create a DataFrame from the results list
results_df = pd.DataFrame(results_list)

# Define the output file path
output_file = 'output/Descriptives.xlsx'

# Export the DataFrame to an Excel file
results_df.to_excel(output_file, index=False)

print(f'Results saved to {output_file}')
