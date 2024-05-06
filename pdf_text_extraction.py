import os
import subprocess
import os
import fitz
from bs4 import BeautifulSoup
import asyncio
from pyppeteer import launch
import subprocess
import html2text
import tkinter as tk
from tkinter import filedialog
import tkinter as tk
from tkinter import filedialog





def convert_pdf_to_html(pdf_file):
    """
    Converts a PDF file to HTML using the pdf2htmlEX command-line tool.

    Args:
        pdf_file (str): The path to the PDF file to be converted.

    Raises:
        subprocess.CalledProcessError: If the pdf2htmlEX command fails to execute.

    """
    command = ['pdf2htmlEX', pdf_file,'pdf_to_html.html']
    subprocess.run(command, check=True)

def remove_images_from_html(html_file):
    """
    Removes all <img> tags from an HTML file.

    Args:
        html_file (str): The path to the HTML file.

    Returns:
        None

    Raises:
        FileNotFoundError: If the HTML file does not exist.

    """
    with open(html_file, 'r') as f:
        content = f.read()
    soup = BeautifulSoup(content, 'html.parser')
    for img in soup.find_all('img'):
        img.decompose()
    with open('pdf_to_html.html', 'w') as f:
        f.write(str(soup))
    return 'pdf_to_html.html'    

def pdf_to_plaintext(pdf_path):
    """
    Convert a PDF file to plain text.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        None
    """
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()    
    with open("pdf_to_text.txt", 'w', encoding='utf-8') as f:
        f.write(text)

def html_to_pdf(html_file):
    """
    Converts an HTML file to a PDF file.

    Args:
        html_file (str): The path to the HTML file.

    Returns:
        None
    """
    with open(html_file, 'r') as f:
        content = f.read()
    async def generate_pdf_from_html(html_content, pdf_path):
        browser = await launch()
        page = await browser.newPage()
        await page.setContent(html_content)
        await page.pdf({'path': pdf_path, 'format': 'A4'})
    asyncio.get_event_loop().run_until_complete(generate_pdf_from_html(content, 'html_to_pdf.pdf'))

def html_to_text(html_file):
    """
    Convert HTML content to plain text.

    Args:
        html_file (str): The path to the HTML file.

    Returns:
        str: The plain text content extracted from the HTML file.
    """

    with open(html_file, 'r') as f:
        content = f.read()
    current_directory = os.path.dirname(html_file)
    text_filepath = os.path.join(current_directory, "html_to_text.txt")
    text=html2text.html2text(content)
    print(text)
    print(text_filepath)
    with open(text_filepath, 'w', encoding='utf-8') as f:    
        f.write(text)    
def get_file_path():
    layout = [[sg.Text("Select PDF File")], [sg.In(), sg.FileBrowse(file_types=(("PDF Files", "*.pdf"),))]]

    window = sg.Window('File Browser', layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        if event == 'Browse':
            file_path = values[0]
            break

    window.close()
    return file_path
def main():
    root = tk.Tk()
    root.withdraw()
    pdf_file_path = filedialog.askopenfilename(title="Select PDF File", filetypes=[("PDF Files", "*.pdf")])
    pdf_to_plaintext(pdf_file_path)
    convert_pdf_to_html(pdf_file_path)
    html_file_path = 'pdf_to_html.html'
    html_file_path = remove_images_from_html(html_file_path)
    html_to_pdf(html_file_path)
    html_to_text(html_file_path)

if __name__ == "__main__":
    main()
main()  
 