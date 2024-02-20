import re
import time
from tkinter import Tk, filedialog
import pyautogui as PAG
import PyPDF2

PAG.PAUSE = .5

def select_pdf_file():
  root = Tk()
  root.withdraw()
  pdf_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
  root.destroy()
  return pdf_path

def extract_ids(pdf_path, pattern = r"[A-Z]{3}[0-9]{3}"):
   try:
        with open(pdf_path, 'rb') as pdf_file_obj:
            pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
            ids = []
            num_pages = len(pdf_reader.pages)  # Count pages using PyPDF2's built-in feature
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                matches = re.findall(pattern, text)
                ids.extend(matches)
            return ids, num_pages
   except (FileNotFoundError, IOError) as e:
        print(f"Error: {e}")
        return [], 0  # Return empty list and 0 pages in case of errors

def process_pdf(pdf_path, your_other_function):
  """
  Processes the PDF to count pages, extract IDs, and compare them.

  Args:
    pdf_path: The path to the PDF file.
    your_other_function: A function to be called if the number of extracted IDs
                         matches the number of pages.

  Returns:
    None. Prints messages based on the processing results.
  """
  extracted_ids, num_pages = extract_ids(pdf_path)
  for id_num in extracted_ids:
     PAG.click(1648,236)
     PAG.typewrite(id_num)
     PAG.click(1647,313)
     PAG.typewrite("admission letter")
     PAG.press('enter')
     PAG.click(1660,514)
     PAG.typewrite("202420") # want to make this more dynamic, change per term/year
     PAG.press('enter')
     PAG.click(1830,826)
     while not PAG.pixelMatchesColor(95,187,[44,149,221]):
        if PAG.pixelMatchesColor(1165,294,[44,149,221]):
            PAG.click(1165,294)
        time.sleep(0.5)
     PAG.click(95,187)

  # Compare number of IDs to number of pages
  if len(extracted_ids) == num_pages:
    print("Number of extracted IDs matches number of pages:", len(extracted_ids))
    your_other_function(extracted_ids)  # Call your function here
  else:
    print("Number of extracted IDs does not match number of pages:", len(extracted_ids))
    print("Stopping program.")

# Replace with your actual PDF path and function
pdf_path = "path/to/your/pdf.pdf"

def my_other_function(ids):
  # Do something with the extracted IDs
  print("Extracted IDs:", ids)

process_pdf(select_pdf_file(), my_other_function)

