import discord

# Initialisation
client = discord.Client()

@client.event
async def on_ready():
    print("Le bot est prêt")

@client.event
async def on_message(message):
    contenu = message.content.lower()
    if contenu == "ping":
        salon=message.channel
        await salon.send("pong")
    if contenu == "jules méchant modo":
        salon=message.channel
        for i in range(100):
            await salon.send(f"Méchant Modo")

@client.event
async def on_message_delete(message):
    contenu = message.content.lower()
    author = message.author
    salon = message.channel
    await salon.send(f"L'utilisateur **{author}** a supprimé un message :\n```{contenu}```")#\n*A-t-il des choses à se reprocher ?*")


@client.event
async def on_typing(channel, user, when):
    print(f"Au Tient, {user} est entrain d'écrire")
    #await channel.send(f"Au Tient, {user} est entrain d'écrire")

@client.event
async def on_message_edit(before, after):
    await before.channel.send(f"L'utilisateur **{before.author}** a modifié un message :\n```{before.content}```")# ```{after.content}```")



"""
Différence entre on_reaction_add et on_raw_reaction_add :
La première se base sur le cache des messages (tous ceux envoyé depuis le start du bot)
Alors que la deuxième (raw) prend en compte tout les message
Les objets retournés ne sont pas les mêmes
Pour les analyser, surtout le raw, faire un print(payload) est conseillé
"""
@client.event
async def on_reaction_add(reaction, user):
    print(f"L'utilisateur {user} a ajouter la réaction {reaction}")
@client.event
async def on_raw_reaction_add(payload):
    print(payload)
    user_id = payload.user_id
    username = await client.fetch_user(user_id)
    #Salon
    salon_id = payload.channel_id
    salon = await client.fetch_channel(salon_id)
    #Reaction
    reaction = payload.emoji.name
    #Message
    message_id = payload.message_id
    contenu = await client.fetch_message(message_id)
    
    #Result
    await salon.send(f"L'utilisateur **{username}** a ajouté une réaction *{reaction}* au message :\n```{contenu}```")




# Connection
token_file = open("token.txt","r")
token = str(token_file.read())
token_file.close()
client.run(token)