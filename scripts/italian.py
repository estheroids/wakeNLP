import nltk
from nltk import word_tokenize

write_file = open('../res/it-words.txt','wb')

with open('../res/italian.txt','r') as f:
    data = f.read().decode('utf8')
    tokens = word_tokenize(data)
    tokens = [w.lower() for w in nltk.Text(tokens)]
    unique = sorted(list(set(tokens)))
    for word in unique:
      write_file.write(word.encode('utf8') + "\n")

    

    
