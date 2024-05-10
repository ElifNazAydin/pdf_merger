"""
A Python script to merge multiple PDF files into a single PDF.

The script prompts the user for a folder path containing PDF files, merges them
using PyPDF2, and saves the merged PDF as 'Merged_PDFs_Output.pdf' in the same folder.

Requirements:
- PyPDF2: Install via 'pip install PyPDF2'
"""

import os
from PyPDF2 import PdfReader, PdfWriter

def getPath():
    folder_path = input('Enter the folder path containing the PDF files: ').strip()
    if not os.path.isdir(folder_path):
        raise ValueError('Invalid folder path. Please provide a valid path.')
    return folder_path

def collectFiles(folder_path):
    pdf_files = []
    for root, dirs, filenames in os.walk(folder_path):
        for filename in filenames:
            if filename.lower().endswith('.pdf'):
                pdf_files.append(os.path.join(root, filename))
    return pdf_files

def mergeFiles(pdf_files):
    pdf_writer = PdfWriter()
    for filename in pdf_files:
        try:
            with open(filename, 'rb') as pdf_file_obj:
                pdf_reader = PdfReader(pdf_file_obj)
                for page in pdf_reader.pages:
                    pdf_writer.add_page(page)
        except:
            print(f'Error reading {filename}')
    return pdf_writer

def saveOutput(pdf_writer, folder_path):
    # The output file path in the same folder
    output_file_path = os.path.join(folder_path, 'Merged_PDFs_Output.pdf')
    with open(output_file_path, 'wb') as pdf_output:
        pdf_writer.write(pdf_output)
    return output_file_path

def main():
    folder_path = getPath()
    pdf_files = collectFiles(folder_path)
    print('PDF files found:', pdf_files)
    pdf_writer = mergeFiles(pdf_files)
    output_file_path = saveOutput(pdf_writer, folder_path)
    print(f'Merged file created successfully at: {output_file_path}')

if __name__ == '__main__':
    main()