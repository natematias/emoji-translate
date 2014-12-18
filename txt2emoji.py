import codecs
import sys
import json
import nltk
from nltk.stem.porter import *
from nltk.corpus import wordnet
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
    #stems.append(stem)

    l = [x.lemmas for x in [x for x in wordnet.synsets(stem)]]
    synonyms = [x.name for x in [item for sublist in l for item in sublist]]


    k = emojihash.keys()
    random.shuffle(k)
    match = False
    for word in synonyms:
      for emo in k:
        try:
          if emo.lower().find(word)>=0:
            sys.stdout.write(unichr(int(emojihash[emo][u'unified'], 16)).encode('utf-8') + " ")
            #print " " + stem + " : "  + emo.lower()
            emojicount += 1
            match = True
            break
        except:
          continue
      if(match):
        break

  if(emojicount>0):
    sys.stdout.write("\n")
  #print line
