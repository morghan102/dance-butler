# Dance Butler

Dance Butler is a small Python script that takes men's dance card entries from images and puts them into a spreadsheet so that we can sort the columns and reverse engineer corresponding _women's_ dance cards automatically.

## A note on formatting

Make sure the images you scan follow a convention that Dance Butler can understand. If the text in your images isn't formatted correctly, then Dance Butler won't know where to break text into columns in the spreadsheet.

[we need to create and illustrate the format here]

## How to use

1. Take pictures of the dance card entries. They need to be as clear and legible as possible. Avoid handwritten entries.
2. Load all of the images into a folder on your computer where Dance Butler lives.
3. Using the command line, run Dance Butler on the image folder.

That's it. A spreadsheet will be created in the folder with images. Open the spreadsheet, double check the entries (there may be a few wrong entries to fix), and make dance cards.

## How it works

Dance Butler uses Tesseract OCR (Optical Character Recognition) through a Python library/wrapper called Pytesser (https://pypi.org/project/PyTesser/). It turns text in images into actual text blocks in the computer.

Next, Dance Butler breaks the text into comma-delimited rows using pattern matching with Regex (https://docs.python.org/3/howto/regex.html).

Last, Dance butler outputs those sections into rows and columns in a spreadsheet using another library just for spreadsheets (https://docs.python.org/3/library/csv.html).