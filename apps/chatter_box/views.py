# Create your views here.
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from django.http import JsonResponse
from json_response import JsonResponse



    
def index(request):
    return render(request, 'chatter_box/index.html')


def chatter(request):
    chatbot = ChatBot('Ares', trainer='chatterbot.trainers.ListTrainer')
    response = chatbot.get_response("Bot info.")
    print(response)
    response = chatbot.get_response("text")
    print(response)

    
    return render(request, 'chatter_box/index.html')


def send_text( request, text):
    chatbot = ChatBot('Ares', trainer='chatterbot.trainers.ListTrainer')
    # response = chatbot.get_response("Bot info.")
    # print(response)
    response = chatbot.get_response(text = text)
    print(response)
    return redirect("/")
