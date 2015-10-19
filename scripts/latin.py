import nltk
import re
from nltk import word_tokenize

write_file = open('../res/la-words.txt','w')

with open('../res/latin.txt','r') as f:
  data = f.read() 
  tokens = re.findall("^\S*\s:", data, re.M) 
  for word in tokens:
    write_file.write(word[0:-2] + '\n')
