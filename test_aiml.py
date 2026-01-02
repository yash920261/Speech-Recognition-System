import aiml

kernel = aiml.Kernel()
kernel.learn("chatbot.aiml")

while True:
    text = input("YOU: ").upper()
    print("BOT:", kernel.respond(text))

        