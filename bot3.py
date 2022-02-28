import discord

# Initialisation
client = discord.Client()

@client.event
async def on_ready():
    print("Le Bot est Prêt")
    for serveur in client.guilds:
        print("    Serveur :",serveur.name)

class msg_:
    def __init__(self,message):
        self.all = message.content
        self.prefix = self.all[0]
        self.content = self.all[1:]
        self.msg = message
        self.salon = message.channel
        self.author = message.author

@client.event
async def on_message(message):
    try:
        msg = msg_(message)
        if msg.prefix == "$":
            if msg.content.split(" ")[0] == "dilemme":
                m=await msg.salon.send("> Question du dilemme :")
                def check(m):
                    return m.author == msg.author
                response = await client.wait_for('message',check=check)
                question = response.content
                await response.delete()
                await m.delete()
                m = await msg.salon.send("> Nombre de réponse :")
                nb = await client.wait_for('message',check=check)
                await m.delete()
                ls=[] #Liste réponse possible
                for i in range(int(nb.content)):
                    m2 = await msg.salon.send(f"> Réponse {i+1} :")
                    response = await client.wait_for('message',check=check)
                    ls.append(response.content)
                    await response.delete()
                    await m2.delete()
                await nb.delete()
                m = await msg.salon.send("> Participants (séparés par un espace) :")
                response = await client.wait_for('message',check=check)
                prp = response.content.split(" ")
                await response.delete()
                await m.delete()
                print(question, ls, prp)
                embed=discord.Embed(title=f"{question}", description=f"Tu viens d'être appelé par {msg.author} pour participer à un dilemme ANONYME", color=discord.Color.blue())
                #embed.set_author(name="Dilemme BOT",url="",icon_url="")
                t=1
                for i in ls:
                    embed.add_field(name=f"Réponse {t}",value=f"{i}",inline=True)
                    t+=1
                embed.set_footer(text="Answer by the number (timeout = 30s)")
                print(embed)
                #await msg.salon.send(embed=embed)
                rep_dic={}
                for p in prp:
                    id_ = str(p)[3:-1]
                    try:
                        user = await client.fetch_user(id_)
                        await user.send(embed=embed)
                        def check2(m):
                            print(str(m.channel).split(" ")[-1], str(user))
                            print("auteur",m.author, user)
                            return str(m.channel).split(" ")[-1] == str(user) and str(m.author) == str(user)
                        choix = await client.wait_for('message',check=check2,timeout=30)
                        if choix == None:
                            key_ = "ABS"
                        else:
                            key_ = choix.content
                        try : 
                            va = rep_dic[key_]
                        except:
                            va = 0
                        va += 1
                        rep_dic[key_] = va
                        print(f"REP : {rep_dic}")
                    except : pass
                embed=discord.Embed(title=f"Résultat de {question}", description=f"Ceci est un dilemme ANONYME proposé par {msg.author} ", color=discord.Color.green())
                for key in rep_dic:
                    if True:
                        try:
                            l=ls[int(key)-1]
                            embed.add_field(name=f"{l}",value=f"NB : {rep_dic[key]}",inline=True)
                        except:
                            embed.add_field(name=f"{key}",value=f"NB : {rep_dic[key]}",inline=True)
                embed.set_footer(text="Merci pour votre participation :-)") 
                await msg.salon.send(embed=embed)
                
            elif msg.content.split(" ")[0] == "get_channel_id":
                await msg.salon.send(f"{msg.salon}")
            elif msg.content.split(" ")[0] == "get_user_id":
                await msg.salon.send(f"{msg.author}") 
    except: pass  





# Connection
token_file = open("token.txt","r")
token = str(token_file.read())
token_file.close()
client.run(token)

