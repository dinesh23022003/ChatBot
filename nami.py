from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
chatbot=ChatBot('corona bot')

trainer = ChatterBotCorpusTrainer(chatbot)
  
# Now let us train our bot with multiple corpus
trainer.train( "chatterbot.corpus.english.trivia","chatterbot.corpus.english.ai","chatterbot.corpus.english.psychology",
               "chatterbot.corpus.english.study")
qs = input("Enter the question")
response = chatbot.get_response(qs)
print(response)
trainer.export_for_training('./my_export.json')


