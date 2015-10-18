import nltk
import re
from nltk import word_tokenize

write_file = open('../res/fr-words.txt','w')

with open('../res/french.txt','r') as f:
  data = f.read() #.decode('utf8')
  tokens = re.findall("^\S+", data, re.M) 
  for word in tokens:
    write_file.write(word + '\n')
