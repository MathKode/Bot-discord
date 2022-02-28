import discord

# Initialisation
client = discord.Client()

@client.event
async def on_ready():
    print("Le Bot est Prêt")

@client.event
async def on_message(message):
    contenu = message.content.lower()
    author = message.author
    if contenu[0] == "$":
        if contenu[1:] == "notes" or contenu[1:] == "note":
            print("NOTE",author)
            #Step 1 : Login
            await author.send("Bonjour, pour accèder à tes notes, merci de te log\n > %USERNAME MP")
    if contenu[0] == "%":
        print("DM reçu de",author)
        contenu = message.content.split(" ")
        username = contenu[0][1:]
        del contenu[0]
        mp = " ".join(contenu)
        print(username,mp)
        
        





# Connection
token_file = open("token.txt","r")
token = str(token_file.read())
token_file.close()
client.run(token)