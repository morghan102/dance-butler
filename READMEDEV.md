These notes are specifically for development, and are meant to be read by a python developer, or developer in training.

## Project Outline

The goal is to be able to run `dance.py` on a folder of images (such as that included in the root directory) and:

1. Read the text in them using OCR.
2. Reformat the text.
3. Output the results as a spreadsheet in CSV format.

The images in `/images` are your sample data to develop with.

### Sample Output

```
Ravi Thieme,1-5,Leah Lakey
Ravi Thieme,1-6,Emilee Jongeward
Ravi Thieme,2-1,Heather Young
Ravi Thieme,2-2, Lichelle Crevison
Skyler Young,1-5,Jasmine Molinaro
Skyler Young,1-6,Cora Jongeward
Skyler Young,2-1,Shoshannah Thieme
Skyler Young,2-2,Emilee Jongeward
Zach Stambaugh,2-6,Shoshannah Thieme
Zach Stambaugh,3-1,Andrea Stambaugh
Zach Stambaugh,3-2,Leah Lakey
Zach Stambaugh,3-3,Kate Rodriguez
Joseph Gray,| - | Alisha McNeil
Joseph Gray,1-2,Andrea Stambaugh
Joseph Gray,1-3,Kayla Schoonhoven
Joseph Gray,1-4,Shoshannah Thieme
```

### Notes

- The specifics of architecture I leave to you. Please study the sample data and the required output, and then determine the best path from point A to point B. If you get stuck, however, please don't hesitate to reach out for discussion. Learning when to ask for help is a science in and of itself.

- OCR is not perfect and so there will be some errors in the output (see the first entry for "Joseph Gray" in the data above: 1s are substituted for pipes). You job is to reduce the number and severity of these errors as much as possible.

- Related to the point above, beware of sample bias, or over optimizing for one sample data set. In the real world, your application will potentially need to work as optimally as possible with varying qualities of data. Finding out the requirements in that direction is always advisable.

- **Tip:** In order to optimize your outputs, you will almost certainly need to dabble in thresholding and/or other techniques for adjusting the images so they will be accurately "read" by PyTesser. This is actually the biggest potential rabbit hole in the script, as image preprocessing is a massive topic. Here are a couple starting points:
- - https://docs.opencv.org/master/d7/d4d/tutorial_py_thresholding.html
- - https://nanonets.com/blog/ocr-with-tesseract/ (skip to the section "OCR with Pytesseract and OpenCV")

## Recommended Modules

Modules used may be at the developer's discretion, however, I recommend using the following:

1. PyTesser OCR (https://pypi.org/project/PyTesser/)
2. OpenCV image tools (https://pypi.org/project/opencv-python/)
3. re, for regex (https://docs.python.org/3/library/re.html)
4. glob, for basic local file manipulation (https://docs.python.org/3/library/glob.html)

A spreadsheet or CSV module is optional, but not actually necessary. CSVs are, by definition, simply comma-delimited lists. Basic pattern matching and reformatting is adequate to create the required output. In general, it's best to keep things as simple as possible :)

