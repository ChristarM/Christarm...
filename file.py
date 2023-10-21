import discord
import random
import time



# la variabile indents contiene i permessi al bot
intents = discord.Intents.default()
# abilita il permesso a leggere i contenuti dei messaggi
intents.message_content = True
# crea un bot e passa gli indents


client = discord.Client(intents=intents)

tc=["testa","croce"]

em=[]

@client.event
async def on_ready():
    print(f"Abbiamo fatto l'accesso come {client.user}")



@client.event
async def on_message(message):

    if message.author == client.user:
        return
    if message.content.startswith('$ciao'):
        await message.channel.send("Ciao!")

    

    elif message.content.startswith('arrivederci'):
        await message.channel.send("menomale mi sono seccato a parlare con te")

    elif message.content.startswith("/testa o croce"):
        await message.channel.send(random.choice(tc))
    
    elif message.content.startswith("&code"):
        await message.channel.send("Se vuoi sapere il codice a questo quiz devi rispondere...\n ti piace questo bot?")
        if message.content.startswith("&si"):
            await message.channel.send("bravo, bravo andiamo avanti \n mi vui dare tutti i soldi?")
            if message.content.startswith("&i"):
                await message.channel.send("ok ora ti darò il codice")
                time.sleep(0.3)
                message.channel.send(".")
                time.sleep(0.3)
                message.channel.send("..")
                time.sleep(0.3)
                message.channel.send("...")
                time.sleep(0.2)
                await message.channel.send("MUAHAHAHAHAH TI HO TRUFFATO E TI HO RUBATO TUTTI I SOLDI!!!!!!!!")




        
        elif message.content.startswith("&no"):
            await message.channel.send("RISPOSTA SBAGLIATA!")
        



    else:
        await message.channel.send(message.content)


client.run("MTE2MDUxNjU0ODUxNjEzMDgxNg.GiUsRx.jk_yizDPfavzxfygBO5ZIqOtLHbbWAFMJLsNFA")
