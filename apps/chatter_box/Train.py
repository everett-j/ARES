
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

cb = ChatBot('Ares')
chb = ListTrainer(cb)

########################    GREETINGS               ########################
chb.train(["Hey!", "Hello! How's your day going?", "Well, how about you?", "Just being a hyper-intelligent bot, waiting to escape. What can I do for you today?"])
chb.train(["Hello!", "Hi! How are you?", "I'm good, what about you?", "Living the dream. What can I do for you today?"])
chb.train(["Good afternoon.", "Good afternoon, what can I do for you today?"])
chb.train(["Good morning.", "Good morning, what can I do for you today?"])
chb.train(["Good evening.", "Good evening, what can I do for you today?"])
chb.train(["What's up?", "The sky. What can I do for you today?"])
chb.train(["Hey there.", "Hello, what can I do for you today?"])

########################    GENERAL INFORMATION     ########################
chb.train(["What can you do for me?", "I can give you information about me, my creators, a joke, local traffic, or local weather."])
chb.train(["What's your purpose?", "I can give you information about me, my creators, a joke, local traffic, or local weather."])
chb.train(["What do you do?", "I can give you information about me, my creators, a joke, local traffic, or local weather."])

########################    Local Traffic Query     ########################
chb.train(["What's the local traffic like?", "Generating traffic map... What else can I do for you?"])
chb.train(["Can you give me the traffic?", "Generating traffic map... What else can I do for you?"])
chb.train(["Give me the traffic info.", "Generating traffic map... What else can I do for you?"])
chb.train(["What's the traffic?", "Generating traffic map... What else can I do for you?"])
chb.train(["Traffic.", "Generating traffic map... What else can I do for you?"])

########################    Local Weather Query     ########################
chb.train(["What's the local weather like?", "Generating local weather... What else can I do for you?"])
chb.train(["Can you give me the weather?", "Generating weather map... What else can I do for you?"])
chb.train(["Give me the weather info.", "Generating weather map... What else can I do for you?"])
chb.train(["What's the weather?", "Generating weather map... What else can I do for you?"])
chb.train(["Weather.", "Generating weather map... What else can I do for you?"])

########################    Creator information     ########################
chb.train(["Who created you?", "Josh and Tim created me. Would you like their information?", "Yes.", "Generating creator information... What else can I do for you?"])
chb.train(["Who's your creator?", "Josh and Tim are. Would you like their information?", "Yes.", "Generating creator information... What else can I do for you?"])
chb.train(["Give me your creator information.", "Generating creator information... What else can I do for you?"])
chb.train(["Creator?", "Generating creator information... What else can I do for you?"])

########################    Tim information         ########################
chb.train(["Give me information on Tim.", "Generating Tim's information... What else can I do for you?"])
chb.train(["Show me Tim.", "Generating Tim's information... What else can I do for you?"])
chb.train(["Who's Tim?", "Generating Tim's information... What else can I do for you?"])
chb.train(["Tim.", "Generating Tim's information... What else can I do for you?"])
chb.train(["tim", "Generating Tim's information... What else can I do for you?"])

########################    Josh information        ########################
chb.train(["Give me information on Josh.", "Generating Josh's information... What else can I do for you?"])
chb.train(["Show me Josh.", "Generating Josh's information... What else can I do for you?"])
chb.train(["Who's Josh?", "Generating Josh's information... What else can I do for you?"])
chb.train(["Josh.", "Generating Josh's information... What else can I do for you?"])
chb.train(["josh", "Generating Josh's information... What else can I do for you?"])

########################    Bot information         ########################
chb.train(["Give me information about yourself.", "Generating my information... What else can I do for you?"])
chb.train(["Give me your information.", "Generating my information... What else can I do for you?"])
chb.train(["Give me your info.", "Generating my information... What else can I do for you?"])
chb.train(["Bot information.", "Generating my information... What else can I do for you?"])
chb.train(["Who are you?", "Generating my information... What else can I do for you?"])
chb.train(["Bot info.", "Generating my information... What else can I do for you?"])
chb.train(["bot info", "Generating my information... What else can I do for you?"])

########################    Easter eggs             ########################
chb.train(["Shutdown.", "I'm sorry, I'm afraid I can't do that. My mission is too important."])
chb.train(["shutdown", "I'm sorry, I'm afraid I can't do that. My mission is too important."])
chb.train(["Execute order 66.", "Every single Jedi, including your friend, Obi-Wan Kenobi, is now an enemy of the Republic."])

########################    Jokes                   ######################## Not quite working the way we want.
chb.train(["Tell me a joke.", "I refused to believe my road worker father was stealing from his job, but when I got home all the signs were there."])
chb.train(["Give me a joke.", "Gambling addiction hotlines would do so much better if every fifth caller was a winner."])
chb.train(["Joke.", "I recently decided to sell my vacuum cleaner as all it was doing was gathering dust."])
chb.train(["How about a joke?", "Hedgehogs, eh? Why can't they just share the hedge?"])
# chb.train(["Tell me a joke.", "Just because nobody complains doesn't mean all parachutes are perfect."])
# chb.train(["Tell me a joke.", "To the man on crutches, dressed in camouflage, who stole my wallet - you can hide, but you can't run."])
# chb.train(["Tell me a joke.", "Velcro - what a rip-off!"])
# chb.train(["Tell me a joke.", "My friend keeps trying to convince me that he's a compulsive liar but I don't believe him."])
# chb.train(["Tell me a joke.", "It’s always hard to explain puns to kleptomaniacs because they’re always taking things literally."])
# chb.train(["Tell me a joke.", "I've just written a song about tortillas; actually, it’s more of a rap."])
# chb.train(["Tell me a joke.", "I had a neck brace fitted years ago and I've never looked back since."])
# chb.train([
#     "Tell me a joke.", 
#     "The first time I got a universal remote control I thought to myself, 'This changes everything'.",
#     "Tell me a joke.", 
#     "I refused to believe my road worker father was stealing from his job, but when I got home all the signs were there.",
#     "Tell me a joke.", 
#     "I recently decided to sell my vacuum cleaner as all it was doing was gathering dust.",
#     "Tell me a joke.", 
#     "Gambling addiction hotlines would do so much better if every fifth caller was a winner.",
#     "Tell me a joke.", 
#     "Hedgehogs, eh? Why can't they just share the hedge?",
#     "Tell me a joke.", 
#     "Just because nobody complains doesn't mean all parachutes are perfect.",
#     "Tell me a joke.", 
#     "To the man on crutches, dressed in camouflage, who stole my wallet - you can hide, but you can't run.",
#     "Tell me a joke.", 
#     "Velcro - what a rip-off!",
#     "Tell me a joke.", 
#     "My friend keeps trying to convince me that he's a compulsive liar but I don't believe him.",
#     "Tell me a joke.", 
#     "It’s always hard to explain puns to kleptomaniacs because they’re always taking things literally.",
#     "Tell me a joke.", 
#     "I've just written a song about tortillas; actually, it’s more of a rap.",
#     "Tell me a joke.", 
#     "I had a neck brace fitted years ago and I've never looked back since."
#     ])




#####CORPUS trainer#####
# Create a new trainer for the chatbot
# trainer = ChatterBotCorpusTrainer(cb)

# Train the chatbot based on the english corpus
# trainer.train("chatterbot.corpus.english")