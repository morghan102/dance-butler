import pytesseract as tess
import re
tess.pytesseract.tesseract_cmd = r'C:\Users\aaron\AppData\Local\Tesseract-OCR\tesseract.exe'
from PIL import Image
import glob
image_list = []
for filename in glob.glob('./*.jpg'):
    im=image.open(filemane)
    image_list.append(in)

img = Image.open('gentlemens_dancesheet.png')
text = tess.image_to_string(img)

# get the initial name string, this will be a matchobject
name = re.search('Gentleman: ([^\d|\n]+)', text).group()


# get just the match string from the match object
#name = name.group()

# clean up the text we don't need, we only want name
name = re.sub('Gentleman: ', '', name)

# get rid of gentleman's name in text
text = re.sub('Gentleman: ([^\d]+)', '', text)

# Split women's names into separate list items
text = re.sub('(\d)\s?-\s?(\d)\s?',r'\1-\2,', text)
text = re.sub('\n','', text)
text = re.sub('(.)(\d-\d)',r'\1\n\2', text)

# text = re.sub('\d-d','$1', text)


#print(text)

textList = text.split('\n')

#print(textList)

i = 0 
for x in textList:
    textList[i] = name + ',' + x
    i = i + 1

print(textList)

#text = re.sub('\n', '', text)

# print(name)
# print(text)

# find the gentlemans name and put in a variable, remove from text (Done)

# make sure every lady's name is on it's own line (Done)
    # Find \s, Replace ()
    # Find \n, Replace ()
    # Find (?=\d-\d) Replace \n
    # Find (\d-d), Replace $1.

# split the text on new lines into a list 

# loop through the list adding the gentleman's name to each line (Done)

# join the list back into a text block

# replace (regex) all spaces (but not newlines) with commas
text = '\n'.join(textList)

file = open('fl.csv','w')
# for line in text:
#     file.writelines([line])

file.writelines(text)

file.close()
#SaveFile = open('text.txt','w').write(text)#.close()


