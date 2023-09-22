import os
import glob
import pandas as pd
import nltk
from nltk.parse import CoreNLPParser
from nltk.tree import Tree
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.parse.corenlp import CoreNLPDependencyParser

# Function to calculate average sentence length in words
def average_sentence_length(text):
    sentences = sent_tokenize(text)
    word_count = sum(len(word_tokenize(sentence)) for sentence in sentences)
    sentence_count = len(sentences)
    return word_count / sentence_count if sentence_count > 0 else 0

# Function to calculate average sentence complexity
def average_sentence_complexity(text):
    # Initialize the CoreNLP Parser
    parser = CoreNLPParser(url="http://localhost:9000")
    
    # Tokenize and parse the text
    tokens = list(parser.tokenize(text))
    parse_tree = list(parser.parse(tokens))[0]
    
    # Calculate sentence complexity
    num_complex_sentences = 0
    num_simple_sentences = 0
    
    for subtree in parse_tree.subtrees(filter=lambda x: x.label() == 'SBAR'):
        num_complex_sentences += 1
    
    for subtree in parse_tree.subtrees(filter=lambda x: x.label() == 'S'):
        num_simple_sentences += 1

    if num_simple_sentences == 0:
        return 0
    
    return num_complex_sentences / num_simple_sentences


# Function to count paragraphs, code snippets, lists, and tables
def count_elements(text):
    paragraphs = text.count('\n\n')
    code_snippets = text.count('```')/2
    
    # Combine bullet point lists (starting with "- ") and numbered lists (starting with "1. ")
    bullet_and_numbered_lists = text.count('- ') + text.count('1. ')
    
    tables = text.count('Table')
    
    return paragraphs, code_snippets, bullet_and_numbered_lists, tables


# Directory containing .tex files
directory = 'Data'

# Create a list to store data per file
data = []

# Iterate through .tex files in subfolders
for file_path in glob.glob(os.path.join(directory, '**/*.tex'), recursive=True):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Calculate metrics
    avg_sentence_length = average_sentence_length(text)
    #avg_sentence_complexity = average_sentence_complexity(text)
    total_words = len(word_tokenize(text))
    paragraphs, code_snippets, bullet_lists, tables = count_elements(text)
    
    # Determine jargon (adjust as needed)
    #jargon = "Business English" if "business_term" in text.lower() else "Common English"
    
    # Append data for this file to the list
    data.append([file_path, avg_sentence_length, \
                 #avg_sentence_complexity, \
                 total_words, paragraphs, code_snippets, bullet_lists, tables])

# Create a DataFrame
df = pd.DataFrame(data, columns=["File Path", "Avg Sentence Length", \
                                 #"Avg Sentence Complexity", \
                                 "Total Words", "Paragraphs", "Code Snippets", "Bullet Lists", "Tables"])

# Export to Excel
df.to_excel("output/DescriptivesNLTK.xlsx", index=False)
