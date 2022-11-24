import nltk
import os

paths = nltk.data.path
print(paths)
print('another')
existing = next(p for p in nltk.data.path if os.path.exists(p))
print(existing)