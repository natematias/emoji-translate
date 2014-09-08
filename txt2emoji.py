import codecs
import sys
import json
import nltk
from nltk.stem.porter import *
import random


emoji = json.loads(codecs.open("emoji-data/emoji.json").read())
stemmer = PorterStemmer()
emojihash = {}
for emo in emoji:
  emojihash[emo[u'name']] = emo

for line in codecs.open(sys.argv[1]):
  tokens = nltk.word_tokenize(line)
  stems = []
  emojicount = 0
  for token in tokens:
    stem = stemmer.stem(token)
    stems.append(stem)
    k = emojihash.keys()
    random.shuffle(k)
    for emo in k:
      if emo.lower().find(stem)>=0:
        try:
          sys.stdout.write(unichr(int(emojihash[emo][u'unified'], 16)).encode('utf-8') + " ")
          #print " " + stem + " : "  + emo.lower()
          emojicount += 1
          break
        except:
          continue
  if(emojicount>0):
    sys.stdout.write("\n")
  #print line
