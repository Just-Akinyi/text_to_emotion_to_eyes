from nrclex import NRCLex
text = ['love', 'hate']
for i in range (len(text)):
    emotion = NRCLex(text[i])
    print("\n\n", text[i], emotion.top_emotions)