# PDF Processing Tool
This Python application allows you to process PDF files in various ways. It provides the following functionalities:

Convert a PDF file to plain text.
Convert a PDF file to HTML.
Remove images from an HTML file.
Convert an HTML file back to a PDF.
Convert an HTML file to plain text.
# Dependencies
The application uses the following Python libraries:

- os
- subprocess
- fitz (PyMuPDF)
- BeautifulSoup
- asyncio
- pyppeteer
- html2text
- tkinter
- PySimpleGUI
- gradio
# How to Use

The application provides a simple graphical user interface (GUI) for selecting a PDF file and choosing the desired processing option. The options are:

pdf_to_plaintext: Converts the selected PDF file to plain text.
pdf_to_html_to_text: Converts the selected PDF file to HTML, removes images from the HTML, converts the HTML back to a PDF, and finally converts the HTML to plain text.
To use the application, simply run the Python script, select a PDF file using the file dialog, and choose the desired processing option.

# Functions
The application includes the following main functions:

- convert_pdf_to_html(pdf_file): Converts a PDF file to HTML using the pdf2htmlEX command-line tool.
- remove_images_from_html(html_file): Removes all <img> tags from an HTML file.
- pdf_to_plaintext(pdf_path): Converts a PDF file to plain text using the fitz (PyMuPDF) library.
- html_to_pdf(html_file): Converts an HTML file to a PDF file using the pyppeteer library.
- html_to_text(html_file): Converts an HTML file to plain text using the html2text library.
- get_file_path(): Opens a file dialog for selecting a PDF file.
- process_pdf(pdf_file_path, choice): Processes a PDF file according to the chosen option.
# Note
This application requires the pdf2htmlEX command-line tool to be installed on your system.
