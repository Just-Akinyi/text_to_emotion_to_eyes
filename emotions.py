import text2emotion as te
import re
from zutils import Is_angry, Is_fear,Is_happy, Is_neutral,Is_sad,Is_surprised
import nltk
# nltk.data.path
podcast_file = "data.txt"
nltk.download('omw-1.4')
with open(podcast_file, encoding="utf-8") as pod_file:
    file_data = pod_file.read()

print(file_data)
sentences_list = re.split("(?<!\d)[,.](?!\d)", file_data)
# an array of sentences
# [ 'i am happy', 'i am sad']
print(sentences_list)

# read emotions of the sentences
emotional_list = []  # this is a list of dictionaries
for sentence in sentences_list:
    # output is emotional dicts for each sentence
    emotion = te.get_emotion(sentence)
    emotional_list.append(emotion)
print(emotional_list)
print('-------------------------------------------------')
# so far we have two lists 1 for sentences another for their emotions
pure_emotions = []
for i in range(len(pure_emotions)):
    for key, val in emotional_list[i].items():
        if val > 1:
            pure_emotions.append(key)
        else:
            key[i] = "neutral"
            pure_emotions.append(key)
        print(pure_emotions)
    # print (pure_emotions)
# for states in emotional_list:
#     for emotional_value in states.values():
#         # check if the emotion has bonus and keep its name
#         if round(emotional_value) > 0:  # what if they tie
#             pure_emotions.append(states.keys())
# print(pure_emotions)
 
# lets show emotions on face now ['sad', 'happy', 'angry']
#the library supports 5 emotions
for mood in pure_emotions:
    print('emotion1')
    if mood == "Happy":
        print('happy')
        Is_happy()
print('the end')