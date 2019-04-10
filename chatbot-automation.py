# chatbot automation

import nltk
import warnings

warnings.filterwarnings("ignore")

import random
import string  

chatbot_automation_file = open('chatbot-automation.txt', 'r', errors='ignore')
chatbot_automation_file_raw = chatbot_automation_file.read()
chatbot_automation_file_raw = chatbot_automation_file_raw.lower()
sent_tokens = nltk.sent_tokenize(chatbot_automation_file_raw)  # converts to list of sentences
word_tokens = nltk.word_tokenize(chatbot_automation_file_raw)  # converts to list of words

sent_tokens[:2]

word_tokens[:4]

wordNetLemmer = nltk.stem.WordNetLemmatizer()


def lemmatizerToken(tokens):
    return [wordNetLemmer.lemmatize(token) for token in tokens]


remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


def lemmatizerNormalize(text):
    return lemmatizerToken(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


USER_REQUESTS = ("hello", "hi", "hey",)
USER_RESPONSES = ["hi", "hey", "hello"]


# Checking for greetings
def userRequest(sentence):
    for word in sentence.split():
        if word.lower() in USER_REQUESTS:
            return random.choice(USER_RESPONSES)


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Generating response
def response(user_response):
    bot_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=lemmatizerNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if (req_tfidf == 0):
        bot_response = bot_response + "I am sorry! I don't get you"
        return bot_response
    else:
        bot_response = bot_response + sent_tokens[idx]
        return bot_response


flag = True
print("Chatbot: My name is Chatbot. I will answer your queries about deployment builds . If you want to exit, type tata!")

while (flag == True):
    user_response = input()
    user_response = user_response.lower()
    if (user_response != 'tata'):
        if (user_response == 'thanks' or user_response == 'thank you'):
            flag = False
            print("Chatbot: You are welcome..")
        else:
            if (userRequest(user_response) != None):
                print("Chatbot: " + greeting(user_response))
            else:
                print("Chatbot: ", end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag = False
        print("Chatbot: Bye! take care..")
