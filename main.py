
import os
from typing import List
from PyPDF2 import PdfMerger  # type: ignore

COMBINED_PDF_NAME = "Combined Lectures.pdf"
FOLDER_PATH = "/Users/dannymolloy/Library/Mobile Documents/com~apple~CloudDocs/University/SENG2130/Lectures"

def combine_pdfs(combined_pdf_name: str, directory_path: str) -> None:
    """
    Combine all PDF files in the given directory into a single PDF file.
    Excludes the combined PDF file if it already exists.
    
    Args:
        combined_pdf_name: The name of the combined PDF file
        directory_path: The directory containing PDF files to combine
    """
    # If directory_path doesn't end with a slash, add it
    if not directory_path.endswith('/') and not directory_path.endswith('\\'):
        directory_path = directory_path + '/'
    
    # Full path for the combined PDF
    combined_pdf_path = os.path.join(directory_path, combined_pdf_name)
    
    # Get all PDF files in the directory
    pdf_files: List[str] = [
        os.path.join(directory_path, filename) 
        for filename in os.listdir(directory_path) 
        if filename.lower().endswith('.pdf')
    ]
    
    # Exclude the combined PDF if it already exists
    if os.path.exists(combined_pdf_path):
        pdf_files = [pdf for pdf in pdf_files if pdf != combined_pdf_path]
    
    # Check if there are PDF files to combine
    if not pdf_files:
        print(f"No PDF files found in {directory_path} to combine.")
        return
    
    # Sort the PDF files to ensure consistent ordering
    pdf_files.sort()
    
    # Create a PdfMerger object
    merger: PdfMerger = PdfMerger()  # type: ignore
    
    # Add each PDF to the merger
    for pdf in pdf_files:
        print(f"Adding {os.path.basename(pdf)}")
        merger.append(pdf)  # type: ignore
    
    # Write the combined PDF to a file
    print(f"Creating combined PDF: {combined_pdf_name}")
    merger.write(combined_pdf_path)  # type: ignore
    merger.close()  # type: ignore
    
    print(f"Successfully combined {len(pdf_files)} PDF files into {combined_pdf_name}")

if __name__ == "__main__":
    combine_pdfs(COMBINED_PDF_NAME, FOLDER_PATH)
