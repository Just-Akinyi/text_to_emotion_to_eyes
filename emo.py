import pandas as pd
from LeXmo import LeXmo
from nltk import word_tokenize
from nltk.stem.snowball import SnowballStemmer
import requests
import nltk
nltk.download('punkt')

podcast_file = "emo.txt"

with open(podcast_file, encoding="utf-8") as pod_file:
    file_data = pod_file.read()
emo = LeXmo.LeXmo(file_data)
# print(emo)
for key in emo.items():
    if type(key) == int:
        emo[key] = key*100
    print(emo)
print(emo)
# emo.pop('text',None)//rounds off
# print(emo)
