import text2emotion as te
import re
import nltk
nltk.download('omw-1.4')

podcast_file = "file.txt"

with open(podcast_file, encoding="utf-8") as pod_file:
    file_data = pod_file.read()

sentences_list = re.split("(?<!\d)[,.](?!\d)", file_data)
# an array of sentences
# [ 'i am happy', 'i am sad']
print(sentences_list)

emotional_list = []  # this is a list of dictionaries
for sentence in sentences_list:
    # output is emotional dicts for each sentence
    # emotion = emoji.distinct_emoji_list(sentence)
    emotion = te.get_emotion(sentence)
    emotional_list.append(emotion)
    print(emotional_list)