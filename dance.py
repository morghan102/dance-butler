import pytesseract as tess
# Skyler's path
tess.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'
# Aaron's path
# tess.pytesseract.tesseract_cmd = r'C:\Users\aaron\AppData\Local\Tesseract-OCR\tesseract.exe'

import re
from PIL import Image
import glob
i2 = 1
for filename in glob.glob('./*.jpg'):
    img = Image.open(filename)
    text = tess.image_to_string(img)

    print('round ' + str(i2) + ', filename is: ' + filename)

    i2 = i2 + 1

    # get the initial name string, this will be a matchobject
    name = re.search('Gentleman: ([^\d|\n]+)', text).group()

    # clean up the text we don't need, we only want name
    name = re.sub('Gentleman: ', '', name)

    # get rid of gentleman's name in text
    text = re.sub('Gentleman: ([^\d]+)', '', text)

    # cleanup and format text
    text = re.sub('(\d)\s?-\s?(\d)\s?',r'\1-\2,', text)
    text = re.sub('\n','', text)
    text = re.sub('(.)(\d-\d)',r'\1\n\2', text)

    # split women's names into separate list items
    textList = text.split('\n')

    # add gentleman's name to each line
    i = 0 
    for x in textList:
        textList[i] = name + ',' + x
        i = i + 1

    # replace (regex) all spaces (but not newlines) with commas
    text = '\n'.join(textList)

    # create the CSV
    file = open('dance_list.csv','w')

    file.writelines(text)

    file.close()


