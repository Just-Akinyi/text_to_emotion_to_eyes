from zutils import Is_angry,Is_fear,Is_happy,Is_neutral,Is_sad,Is_surprised
import text2emotion as te
import re
import nltk

podcast_file = "data.txt"
nltk.download('averaged_perceptron_tagger')

def break_down(podcast_file):
    '''
    Opens podacast file braks it down to short sentences
    Args:
        podcast_file - file with a whole conversation
    Returns:
        sentence_list - a list of short sentences
    '''
    with open(podcast_file, encoding="utf-8") as pod_file:
        file_data = pod_file.read()

    sentences_list = re.split("(?<!\d)[,.](?!\d)", file_data)
    return sentences_list

def read_sentence_emotions(sentences_list):
    '''
    Picks sentence list, gets emothions from each
    Args:
        sentence_list - list of short sentences
    Returns:
        emotional_list - List of dicts
    '''
    emotional_list = []
    for sentence in sentences_list:
        emotion = te.get_emotion(sentence)
        emotional_list.append(emotion)
    return emotional_list
    
def accurate_emotions(emotional_list):
    '''
    Picks list of dicts, from each dict gets highest value
    appends it's the key to a new list
    Args:
        emotional_list - List of dicts
    Returns:
        pure_emotions - list of emotions
    '''
    pure_emotions = []
    for states in emotional_list:
        for emotional_value in states.value():
        # check if the emotion has bonus and keep its name
            if round(emotional_value) > 0:
                pure_emotions.append(states.key())
    return pure_emotions

def show_on_face(pure_emotions):
    '''
    Picks list of emotions, displays eyes matching them
    Args:
        pure_emotions - list of emotions
    Returns:
        eyes matching emotions
    '''
    for mood in pure_emotions:
        if mood == 'Sad':
            Is_sad()
        if mood == 'Happy':
            Is_happy()
        if mood == 'Angry':
            Is_angry()
        if mood == 'Fear':
            Is_fear()
        if mood == 'Surprise':
            Is_surprised()
        else:
            Is_neutral()
