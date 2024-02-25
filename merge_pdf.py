import os
from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(folder_path, output_filename):
    pdf_writer = PdfWriter()

    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith('.pdf') and filename != os.path.basename(output_filename):
            file_path = os.path.join(folder_path, filename)
            try:
                pdf_reader = PdfReader(file_path)
                num_pages = len(pdf_reader.pages)
                print(f"Adding {num_pages} pages from {filename}")

                for page in pdf_reader.pages:
                    pdf_writer.add_page(page)

            except Exception as e:
                print(f"Error processing file {filename}: {e}")

    with open(output_filename, 'wb') as out:
        pdf_writer.write(out)
        print(f'Merged PDF saved as {output_filename}')

folder_path = '/Users/sivas/Desktop/Personal/Boat/Nonsuch Bot/pdfs'
output_filename = '/Users/sivas/Desktop/Personal/Boat/Nonsuch Bot/merged_output4.pdf'

merge_pdfs(folder_path, output_filename)
