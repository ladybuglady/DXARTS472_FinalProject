import pandas as pd
import random
import re
from textblob import TextBlob
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
s=set(stopwords.words('english'))
s.update(['sex', 'fuck', 'fucked', 'bitch', 'horny', 'sexual'])
trivial = ['feel', 'i\'m', 'i', 'each', 'every', 'feeling', 'within', 'under', 'over']

# datasets from Kaggle
text_1 = pd.read_csv("../Emotion_final.csv") # start after "ing" or "ed"
emots_1 = text_1['Emotion'].unique() # ['sadness' 'anger' 'love' 'surprise' 'fear' 'happy']

text_2 = pd.read_csv("../tweet_emotions.csv") # remove @
emots_2 = text_2['sentiment'].unique() # ['empty' 'sadness' 'enthusiasm' 'neutral' 'worry' 'surprise' 'love' 'fun' 'hate' 'happiness' 'boredom' 'relief' 'anger']

text_2.loc[text_2['sentiment']=='empty'] = 'neutral'
text_2.loc[text_2['sentiment']=='enthusiasm'] = 'happy'
text_2.loc[text_2['sentiment']=='fun'] = 'happy'
text_2.loc[text_2['sentiment']=='hate'] = 'anger'
text_2.loc[text_2['sentiment']=='happiness'] = 'happy'
text_2.loc[text_2['sentiment']=='relief'] = 'neutral'

text_1 = text_1.rename(columns = {'Emotion':'sentiment', 'Text': 'content'})
text_2 = text_2.drop('tweet_id', axis=1)

text = pd.concat([text_1, text_2])

def series_to_string(series):
    message = ""
    for indx, values in series.items():
        for i in values:
            message += i + ' '
    return message
    


def filter_words(statement):
    words = re.split(' ', statement)
    return list(filter(lambda x: (x.lower() not in s) and ('@' not in x) and ('www' not in x) and not (x.isnumeric()), words))

def filter_content(statement):
    words = statement.split()
    return list(filter(lambda x: ('@' not in x) and ('www' not in x) and ('http' not in x), words))


def random_selector():
    random_text = text.sample().apply(lambda x: filter_content(x['content']), axis=1)
    return series_to_string(random_text)

def theme_selector():
    statement =  text.sample()['content'].item()
    while type(statement) is not str or len(statement.split()) == 1:
         statement = text.sample()['content'].item()
    
    # possible theme words
   
    words = filter_words(statement)
    print("Theme:")
    theme = random.choice(words).lower()
    while theme in trivial or len(text[text['content'].str.contains(theme)])==0: # might be 0 after filtering tho..
        theme = random.choice(words).lower()
    print(theme)

    theme_texts = text[text['content'].str.contains(theme)]
    theme_texts = theme_texts.apply(lambda x: filter_content(x['content']), axis=1)
    if len((theme_texts)) > 20:
        theme_texts = theme_texts.sample(n=20)
    return series_to_string(theme_texts), theme

def emotion_selector(emotion=None):
    if emotion is None:
        emo =  text.sample()['sentiment'].item()
    else:
        emo = emotion
    while type(statement) is not str:
         statement =  text.sample()['sentiment'].item()
    print(emo)
    emo_texts = text[text['sentiment'] == emo]
    if len(emo_texts()) > 50:
        emo_texts = emo_texts.sample(n=50)['content']
    return emo_texts

## theme and emotion..

def theme_emotion_selector(emotion):
    # first pick the theme

    statement =  text.sample()['content'].item()
    while type(statement) is not str or len(statement.split()) == 1:
         statement = text.sample()['content'].item()
    
    # possible theme words
   
    words = filter_words(statement)
    print("Theme:")
    theme = random.choice(words).lower()
    while theme in trivial or len(text[text['content'].str.contains(theme)])==0: # might be 0 after filtering tho..
        theme = random.choice(words).lower()
    print(theme)
   
    theme_texts = text[text['content'].str.contains(theme)]
    # choose emotions
    emotive_theme_texts = theme_texts[theme_texts['sentiment'] == emotion]

    # cleanup
    emotive_theme_texts = emotive_theme_texts.apply(lambda x: filter_content(x['content']), axis=1)
    if len((emotive_theme_texts)) > 3:
        emotive_theme_texts = emotive_theme_texts.sample(n=3)
    return series_to_string(emotive_theme_texts), theme



def pressure_selector(pressure):
    if pressure >= 100:
        return emotion_selector("happy")
    else:
        return emotion_selector("anger")


theme_emotion_selector("love")