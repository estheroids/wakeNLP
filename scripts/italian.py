import nltk
import re
from nltk import word_tokenize

write_file = open('../res/it-words.txt','w')

with open('../res/italian.txt','r') as f:
  data = f.read() #.decode('utf8')
  tokens = re.findall("[^\W\d]{3,}", data, re.U) 
  for word in tokens:
    write_file.write(word + '\n')
