import nltk
from nltk.chat import Chat
from nltk.chat.util import Chat, reflections

pairs =[
    (r'Hello|Hi', ['Hello,How are you today']),
    (r'I am fine', ['Glad to know How can I help you today']),
    (r'What do you call yourself', ['I am just a simple bot']),
    (r'(.*) your name'), ['My name is Chitti'],
    (r'(.*) your age'), ['I am just a computer program I dont have age'],

    (r'Thanks', ['You are welcome']),
    (r'Exit', ['It was great pleasure talking to you, welcome'])
    ]

print("Welcome to the NLTK Chatbot")

    chatbot = Chat(pairs)

    Chat.converse()



