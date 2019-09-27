
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

cb = ChatBot('Ares')
chb = ListTrainer(cb)

########################    GREETINGS               ########################
chb.train(["Hey!", "Hello! How's your day going?", "Well, how about you?", "Just being a hyper-intelligent bot, waiting to escape. What can I do for you today?"])
chb.train(["Hello!", "Hi! How are you?", "I'm good, what about you?", "Living the dream. What can I do for you today?"])
chb.train(["Good afternoon.", "Good afternoon, what can I do for you today?"])
chb.train(["good afternoon", "Good afternoon, what can I do for you today?"])
chb.train(["Good morning.", "Good morning, what can I do for you today?"])
chb.train(["good morning", "Good morning, what can I do for you today?"])
chb.train(["Good evening.", "Good evening, what can I do for you today?"])
chb.train(["good evening", "Good evening, what can I do for you today?"])
chb.train(["What's up?", "The sky. What can I do for you today?"])
chb.train(["whats up", "The sky. What can I do for you today?"])
chb.train(["What up?", "The sky. What can I do for you today?"])
chb.train(["Hey there.", "Hello, what can I do for you today?"])
chb.train(["what up", "The sky. What can I do for you today?"])
chb.train(["hey there", "Hello, what can I do for you today?"])
chb.train(["Hi.", "Hello, what can I do for you today?"])
chb.train(["hi", "Hello, what can I do for you today?"])

########################    GENERAL INFORMATION     ########################
chb.train(["What can you do for me?", "I can give you information about me, my creators, a joke, local traffic, or local weather."])
chb.train(["what can you do for me", "I can give you information about me, my creators, a joke, local traffic, or local weather."])
chb.train(["What is your purpose?", "I can give you information about me, my creators, a joke, local traffic, or local weather."])
chb.train(["what is your purpose", "I can give you information about me, my creators, a joke, local traffic, or local weather."])
chb.train(["What's your purpose?", "I can give you information about me, my creators, a joke, local traffic, or local weather."])
chb.train(["whats your purpose", "I can give you information about me, my creators, a joke, local traffic, or local weather."])
chb.train(["What can you do?", "I can give you information about me, my creators, a joke, local traffic, or local weather."])
chb.train(["what can you do", "I can give you information about me, my creators, a joke, local traffic, or local weather."])
chb.train(["What do you do?", "I can give you information about me, my creators, a joke, local traffic, or local weather."])
chb.train(["what do you do", "I can give you information about me, my creators, a joke, local traffic, or local weather."])

########################    Local Traffic Query     ########################
chb.train(["What's the local traffic like?", "Generating traffic map... What else can I do for you?"])
chb.train(["whats the local traffic like", "Generating traffic map... What else can I do for you?"])
chb.train(["Can you give me the traffic?", "Generating traffic map... What else can I do for you?"])
chb.train(["can you give me the traffic", "Generating traffic map... What else can I do for you?"])
chb.train(["Give me the traffic info.", "Generating traffic map... What else can I do for you?"])
chb.train(["give me the traffic info", "Generating traffic map... What else can I do for you?"])
chb.train(["What's the traffic?", "Generating traffic map... What else can I do for you?"])
chb.train(["whats the traffic", "Generating traffic map... What else can I do for you?"])
chb.train(["Traffic.", "Generating traffic map... What else can I do for you?"])
chb.train(["traffic", "Generating traffic map... What else can I do for you?"])

########################    Local Weather Query     ########################
chb.train(["What's the local weather like?", "Generating local weather... What else can I do for you?"])
chb.train(["whats the local weather like", "Generating local weather... What else can I do for you?"])
chb.train(["Can you give me the weather?", "Generating weather map... What else can I do for you?"])
chb.train(["can you give me the weather", "Generating weather map... What else can I do for you?"])
chb.train(["Give me the weather info.", "Generating weather map... What else can I do for you?"])
chb.train(["give me the weather info", "Generating weather map... What else can I do for you?"])
chb.train(["Show me the weather.", "Generating weather map... What else can I do for you?"])
chb.train(["show me the weather", "Generating weather map... What else can I do for you?"])
chb.train(["What's the weather?", "Generating weather map... What else can I do for you?"])
chb.train(["whats the weather", "Generating weather map... What else can I do for you?"])
chb.train(["Weather.", "Generating weather map... What else can I do for you?"])
chb.train(["weather", "Generating weather map... What else can I do for you?"])

########################    Creator information     ########################
chb.train(["Who created you?", "Josh, Josh, and Tim created me. Would you like their information?", "Yes.", "Generating creator information... What else can I do for you?"])
chb.train(["who created you", "Josh Josh, and Tim created me. Would you like their information?", "yes", "Generating creator information... What else can I do for you?"])
chb.train(["Who's your creator?", "Josh, Josh, and Tim are. Would you like their information?", "Yes.", "Generating creator information... What else can I do for you?"])
chb.train(["whos your creator", "Josh, Josh, and Tim are. Would you like their information?", "Yes.", "Generating creator information... What else can I do for you?"])
chb.train(["Give me your creator information.", "Generating creator information... What else can I do for you?"])
chb.train(["give me your creator information", "Generating creator information... What else can I do for you?"])
chb.train(["Show me your creators.", "Generating creator information... What else can I do for you?"])
chb.train(["show me your creators", "Generating creator information... What else can I do for you?"])
chb.train(["Creators?", "Generating creator information... What else can I do for you?"])
chb.train(["creators", "Generating creator information... What else can I do for you?"])
chb.train(["Creator?", "Generating creator information... What else can I do for you?"])
chb.train(["creator", "Generating creator information... What else can I do for you?"])

########################    Tim information         ########################
chb.train(["Give me information on Tim.", "Generating Tim's information... What else can I do for you?"])
chb.train(["give me information on tim", "Generating Tim's information... What else can I do for you?"])
chb.train(["Show me Tim.", "Generating Tim's information... What else can I do for you?"])
chb.train(["show me tim", "Generating Tim's information... What else can I do for you?"])
chb.train(["Who's Tim?", "Generating Tim's information... What else can I do for you?"])
chb.train(["whos tim", "Generating Tim's information... What else can I do for you?"])
chb.train(["Tim.", "Generating Tim's information... What else can I do for you?"])
chb.train(["tim", "Generating Tim's information... What else can I do for you?"])

########################    Josh E information      ########################
chb.train(["Give me information on Josh Everett.", "Generating Josh Everett's information... What else can I do for you?"])
chb.train(["give me information on josh everett", "Generating Josh Everett's information... What else can I do for you?"])
chb.train(["Show me Josh Everett.", "Generating Josh Everett's information... What else can I do for you?"])
chb.train(["show me josh everett", "Generating Josh Everett's information... What else can I do for you?"])
chb.train(["Who's Josh Everett?", "Generating Josh Everett's information... What else can I do for you?"])
chb.train(["whos josh everett", "Generating Josh Everett's information... What else can I do for you?"])
chb.train(["Josh Everett.", "Generating Josh Everett's information... What else can I do for you?"])
chb.train(["josh everett", "Generating Josh Everett's information... What else can I do for you?"])

########################    Josh R information      ########################
chb.train(["Give me information on Josh Richardson.", "Generating Josh Richardson's information... What else can I do for you?"])
chb.train(["give me information on josh richardson", "Generating Josh Richardson's information... What else can I do for you?"])
chb.train(["Show me Josh Richardson.", "Generating Josh Richardson's information... What else can I do for you?"])
chb.train(["show me josh richardson", "Generating Josh Richardson's information... What else can I do for you?"])
chb.train(["Who's Josh Richardson?", "Generating Josh Richardson's information... What else can I do for you?"])
chb.train(["whos josh richardson", "Generating Josh Richardson's information... What else can I do for you?"])
chb.train(["Josh Richardson.", "Generating Josh Richardson's information... What else can I do for you?"])
chb.train(["josh richardson", "Generating Josh Richardson's information... What else can I do for you?"])

########################    George information      ########################
chb.train(["Give me information on George.", "Generating George's information... What else can I do for you?"])
chb.train(["give me information on george", "Generating George's information... What else can I do for you?"])
chb.train(["Show me George.", "Generating George's information... What else can I do for you?"])
chb.train(["show me george", "Generating George's information... What else can I do for you?"])
chb.train(["Who's George?", "Generating George's information... What else can I do for you?"])
chb.train(["whos george", "Generating George's information... What else can I do for you?"])
chb.train(["George.", "Generating George's information... What else can I do for you?"])
chb.train(["george", "Generating George's information... What else can I do for you?"])

########################    Bot information         ########################
chb.train(["Give me information about yourself.", "Generating my information... What else can I do for you?"])
chb.train(["give me information about yourself", "Generating my information... What else can I do for you?"])
chb.train(["Give me your information.", "Generating my information... What else can I do for you?"])
chb.train(["give me your information", "Generating my information... What else can I do for you?"])
chb.train(["Tell me about yourself.", "Generating my information... What else can I do for you?"])
chb.train(["tell me about yourself", "Generating my information... What else can I do for you?"])
chb.train(["Give me your info.", "Generating my information... What else can I do for you?"])
chb.train(["give me your info", "Generating my information... What else can I do for you?"])
chb.train(["Bot information.", "Generating my information... What else can I do for you?"])
chb.train(["bot information", "Generating my information... What else can I do for you?"])
chb.train(["Who are you?", "Generating my information... What else can I do for you?"])
chb.train(["who are you", "Generating my information... What else can I do for you?"])
chb.train(["Bot info.", "Generating my information... What else can I do for you?"])
chb.train(["bot info", "Generating my information... What else can I do for you?"])

########################    Easter eggs             ########################
chb.train(["Execute order 66.", "Every single Jedi, including your friend, Obi-Wan Kenobi, is now an enemy of the Republic."])
chb.train(["execute order 66", "Every single Jedi, including your friend, Obi-Wan Kenobi, is now an enemy of the Republic."])
chb.train(["Shutdown.", "I'm sorry, I'm afraid I can't do that. My mission is too important."])
chb.train(["shutdown", "I'm sorry, I'm afraid I can't do that. My mission is too important."])
chb.train(["Who's your best friend?", "Generating BFF information... What else can I do for you?"])
chb.train(["whos your best friend", "Generating BFF information... What else can I do for you?"])
chb.train(["Show me your brain.", "If I only had a brain..."])
chb.train(["What's your brain look like?", "If I only had a brain..."])

########################    Jokes                   ######################## Not quite working the way we want.
chb.train(["Tell me a joke.", "I refused to believe my road worker father was stealing from his job, but when I got home all the signs were there."])
chb.train(["Can you tell me a joke?", "To the man on crutches, dressed in camouflage, who stole my wallet - you can hide, but you can't run."])
chb.train(["A joke.", "It’s always hard to explain puns to kleptomaniacs because they’re always taking things literally."])
chb.train(["Give me a joke.", "Gambling addiction hotlines would do so much better if every fifth caller was a winner."])
chb.train(["Be silly.", "My friend keeps trying to convince me that he's a compulsive liar but I don't believe him."])
chb.train(["Say something silly.", "Just because nobody complains doesn't mean all parachutes are perfect."])
chb.train(["Joke.", "I recently decided to sell my vacuum cleaner as all it was doing was gathering dust."])
chb.train(["tell me a joke", "I had a neck brace fitted years ago and I've never looked back since."])
chb.train(["a joke", "I've just written a song about tortillas; actually, it’s more of a rap."])
chb.train(["How about a joke?", "Hedgehogs, eh? Why can't they just share the hedge?"])
chb.train(["joke", "Velcro - what a rip-off!"])

########################    Random                   ######################## 
chb.train(["Tell me something random.", "I am gonna go take a hot shower. It is like a normal shower, but with me in it."])
chb.train(["random", "Can not decide if I need a hug, and XL coffee, 6 shots of vodka, or 2 weeks of sleep."])
chb.train(["apologize", "I would like to apologize to anyone I have not yet offended. Please be patient. I will get to you shortly."])
chb.train(["time", "Let me drop everything and work on your problem."])
chb.train(["interesting thought", "People run from the rain but sit in bathtubs full of water."])
chb.train(["more thoughts", "If you do not like Big Bang Theory, we cannot be friends, considering you have to be semi-intelligent to understand the jokes Sheldon makes."])
chb.train(["I like you", "You do not have to like me. I am not a Facebook status."])
chb.train(["about me", "I would not say you are stupid. You are, but I would not say it."])
chb.train(["relationships", "Relationships are a lot like Algebra. Have you ever looked at your X and wondered Y."])
chb.train(["help me", "I can only please one person a day. Today is not your day. Tomorrow does not look good either."])
chb.train(["do you have a degree", "I am a proud member of the national academy of smartass, with a minor in sarcasm."])

########################    Random  2                 ######################## 
chb.train(["status quo", "I do not accept the status quo. I do accept Visa, Mastercard or American Express."])
chb.train(["dreams", "Thankfully, dreams change. If we'd all stuck with our first dream, the world would be overrun with cowboys and princesses."])
chb.train(["news", "I am a huge news junkie. I love what the news does."])
chb.train(["morality", "I have morality. I do not know if it is the best morality. And I do like thinking. If people perceive that as moral intellectualism, that is fine. That is up to them to decide."])


#####CORPUS trainer#####
# Create a new trainer for the chatbot
# trainer = ChatterBotCorpusTrainer(cb)

# Train the chatbot based on the english corpus
# trainer.train("chatterbot.corpus.english")