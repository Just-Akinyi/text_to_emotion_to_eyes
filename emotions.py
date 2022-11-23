import text2emotion as te
import re
import nltk

podcast_file = "data.txt"
nltk.download('averaged_perceptron_tagger')

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

# so far we have two lists 1 for sentences another for their emotions
pure_emotions = []
for states in emotional_list:
    for emotional_value in states.value():
        # check if the emotion has bonus and keep its name
        if round(emotional_value) > 0:  # what if they tie
            pure_emotions.append(states.key())
            print(pure_emotions)

# lets show emotions on face now ['sad', 'happy', 'angry']
#the library supports 5 emotions
for mood in pure_emotions:
    if mood == "Happy":
        pass
        # put the eye
        # put brows
    elif mood == "Angry":
        pass
        # put the eye
        # put brows
    elif mood == "Surprise":
        pass
        # put the eye
        # put brows
    elif mood == "Sad":
        pass
        # put the eye
        # put brows
    elif mood == "Fear":
        pass
        # put the eye
        # put brows
    else:
        print('completed')
        # normal eye
        # normal brows
