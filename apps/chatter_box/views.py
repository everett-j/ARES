# Create your views here.
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

    
def index(request):
    return render(request, 'chatter_box/index.html')


def chatter(request):
    chatbot = ChatBot('Ares', trainer='chatterbot.trainers.ListTrainer')
    response = chatbot.get_response("Bot info.")
    print(response)
    return render(request, 'chatter_box/index.html')