from PIL import Image

def Is_sad():
    sad_eyes_img = Image.open('data/sad_eyes.png')
    return (sad_eyes_img.show())

def Is_happy():
    happy_eyes_img = Image.open('data/happy_eyes.png')
    return (happy_eyes_img.show())

def Is_angry():
    angry_eyes_img = Image.show('data/angry_eyes.png')
    return (angry_eyes_img)

def Is_fear():
    fear_eyes_img = Image.show('data/fear_eyes.png')
    return (fear_eyes_img)

def Is_surprised():
    surprise_eyes_img = Image.show('data/surprise_eyes.png')
    return (surprise_eyes_img)

def Is_neutral():
    neutral_eyes_img = Image.open('data/neutral_eyes.png')
    return (neutral_eyes_img.show())
