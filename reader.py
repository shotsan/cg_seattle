import PyPDF2

def read_pdf(file_path):
    # Open the PDF file
    with open(file_path, 'rb') as file:
        # Create PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Get total number of pages
        num_pages = len(pdf_reader.pages)
        
        # Extract text from each page
        for page_num in range(num_pages):
            # Get page object
            page = pdf_reader.pages[page_num]
            
            # Extract text
            text = page.extract_text()
            
            # Print page number and content
            print(f"\nPage {page_num + 1}:")
            print("=" * 50)
            print(text)

# Example usage
if __name__ == "__main__":
    pdf_path = "input.pdf"
    read_pdf(pdf_path)

