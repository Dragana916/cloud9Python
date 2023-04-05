import re

# read in the file
with open('preproinsulin-seq.txt', 'r') as f:
    text = f.read()

    # remove the "ORIGIN" line
    text = re.sub('ORIGIN', '', text)
    
    # remove all line breaks
    text = re.sub('\n', '', text)
    
    # remove all spaces
    text = re.sub(' ', '', text)
    
    # Remove all numbers from the text using regular expressions
    text = re.sub(r'\d+', '', text)
    
    # remove the "//" line
    text = re.sub('//', '', text)
    
#save changes to the file 
with open('preproinsulin-seq.txt', 'w') as file:
    file.write(text)
    
    
# confirm that the resulting file has exactly 110 characters
if len(text) == 110:
    print("File has 110 characters.")
else:
    print("File does not have 110 characters.")
