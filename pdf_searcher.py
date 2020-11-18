import PyPDF2
import re
import sys
import os

def main(args):
  string = ''.join(args)
  output = PyPDF2.PdfFileWriter()
  pages = 0

  # change these to whatever folders you want
  slides_location = "put_pdfs_here"
  output_location = "search_results"

  for file_name in os.listdir(slides_location):
    if "pdf" not in file_name: continue
    object = PyPDF2.PdfFileReader(slides_location + "/" + file_name)
    num_pages = object.getNumPages()

    for i in range(0, num_pages):
        page_obj = object.getPage(i)
        text = page_obj.extractText()
        result = re.search(string, text, re.IGNORECASE)

        if result:
          output.addPage(page_obj)
          pages += 1

  if pages > 0:
    output_filename = output_location + "/" + '_'.join(args) + ".pdf"
    with open(output_filename, "wb") as outputStream:
      output.write(outputStream)

    print("'" + ' '.join(args) + "'" + " found on " + str(pages) + " pages")
    print("pdf stored in " + output_location + " as " + "'" + '_'.join(args) + ".pdf'")
  else:
    print("'" + ' '.join(args) + "' not found in files")



if __name__ == '__main__':
  main(sys.argv[1:])
