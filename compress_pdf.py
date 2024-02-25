from PyPDF2 import PdfReader, PdfWriter

def compress_pdf(input_file_path, output_file_path):
    pdf_reader = PdfReader(input_file_path)
    pdf_writer = PdfWriter()

    for page in pdf_reader.pages:
        pdf_writer.add_page(page)

    with open(output_file_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

    print(f'Compressed PDF saved as {output_file_path}')

input_pdf = '/Users/sivas/Desktop/Personal/Boat/Nonsuch Bot/merged_output4.pdf'
output_pdf = '/Users/sivas/Desktop/Personal/Boat/Nonsuch Bot/merged_output4_compress.pdf'
compress_pdf(input_pdf, output_pdf)
