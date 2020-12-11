import os
import random
from discord.ext import commands
import discord
import praw
from discord.ext.commands import has_permissions, MissingPermissions

TOKEN = "Nzg1OTk5NjM1ODA2MDI3ODI2.X9ABNA.7K-EXQMLxtUbd4-rFYeiDXRSM3k"
client = discord.Client()
client = commands.Bot(command_prefix='!')

reddit = praw.Reddit(client_id='7ZDoKq6xs6QauA',
                     client_secret='BRFObxRpKgznXKU_HXQvfcLQxw05Xg',
                     user_agent='Patoto008 CuyoBot')


@client.event
async def on_ready():
    print(f'{client.user.name} está activo!')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Holaaaa {member.name}, estoy probando el bot del server, solo ignora este mensaje!'
    )
#COMANDOS DEL BOT
@client.command(help = "Tira el dado!")
async def dado(ctx):
    rollnums = [
        '1','2','3','4','5','6'
    ]

    numero = random.choice(rollnums)
    await ctx.send(
    f'Rodaste el dado y te salió {numero}'
    )

@client.command(help = "Todos los insultos de Dross")
async def hijueputa(ctx):
    insulta = '**Agarra aire** Una cagada asquerosa, repelente, abyecta, vomitiva, mugrosa, maldita, diarreosa, estercolera, inmunda, malnacida, pudenda, apestosa, maloliente, cabrona, maricona, huevona, pendeja, tarada, cancerígena, jodida, culeada, gilipollesca, pelotuda, encamada, malnacida, retardada, atrasada, inútil, móngola, incestuosa, burda, estúpida, insulsa, putrefacta, traicionera, indigna, chupapollas, soplahuevos, esnifacojones, gueleculo, coprofágica, masca-morrones, infecta, cerda, nauseabunda, cochambrosa, cochina, verdulera, infame, ruin, rastrera, degradada, descerebrada, zopenca, zafia, puta, engreída, esquizofrénica, granulenta, infeliz, profana, calamitosa, deficiente, cretina, lela, ramera, fulana, calientaguevos, ridícula, petarda, pasmarote, fistro, desidiosa, puta, reputa, soputa, recontraputa, hija de puta, hija de un millón de putas, escupepitos, caradepedo, necrofílica, alientoamojón, lambe-bukaka, revuelcaleche, coñoesumadre y de su abuela, conchuda, culoroto, nalgas reventadas, tragasable, succionaditos, esfinterpartido, ojetedesilachado, sorbemocos, capulla, pelmaza, zoquete, masturbadora crónica, espuria, chupa-tampones, regluda, coprófaga, gerontofílica, turra, ojete, atorrante, tierrúa, pajúa, amamaguevos, onanista caradeconcha y MALA PELICULA .'
    await ctx.send(insulta)

@client.command(help = "momo en video")
async def memevid(ctx):
    videos= 'https://www.youtube.com/watch?v=q6EoRBvdVPQ&list=PLXKAG8g1Ls_Ax-SU7rCgyiGWjylB5NHL-&index=1','https://www.youtube.com/watch?v=reApbwcpdmE&list=PLyyC7zbCEJRbjVQoHyu09GGpD1kpAiiHs&index=2','https://www.youtube.com/watch?v=yi8WrSCDfTY&list=PLyyC7zbCEJRbjVQoHyu09GGpD1kpAiiHs&index=3','https://www.youtube.com/watch?v=d6ybQkBF_SI&list=PLyyC7zbCEJRbjVQoHyu09GGpD1kpAiiHs&index=17','https://www.youtube.com/watch?v=pQIu_sIhjMo&list=PLyyC7zbCEJRbjVQoHyu09GGpD1kpAiiHs&index=20','https://www.youtube.com/watch?v=o4QTL7Gosww&list=PLyyC7zbCEJRbjVQoHyu09GGpD1kpAiiHs&index=29','https://www.youtube.com/watch?v=j0lN0w5HVT8','https://www.youtube.com/watch?v=ocaGMulwpEM','https://www.youtube.com/watch?v=lbu3fF0GDkE','https://www.youtube.com/watch?v=hlnpkrJs6wM&list=PLF8RIHxComXNFL-t_fvN8z1fzH__C-cCx&index=1','https://www.youtube.com/watch?v=rUbh9ion6W8','https://www.youtube.com/watch?v=wRjs4zo6EO8&list=PLF8RIHxComXNFL-t_fvN8z1fzH__C-cCx&index=69'

    vm = random.choice(videos)
    await ctx.send(
    f'Jaja wachate este momo :v {vm}'
    )



@client.command()
async def animeme(ctx):
    subreddit = reddit.subreddit("animemes")
    all_subs = []
    top = subreddit.hot(limit=50)
    for submission in top:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    em = discord.Embed(title=name)
    em.set_image(url=url)
    await ctx.send(embed=em)

@client.command()
async def meme(ctx):
    subreddit = reddit.subreddit("memes")
    all_subs = []
    top = subreddit.hot(limit=50)
    for submission in top:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    em = discord.Embed(title=name)
    em.set_image(url=url)
    await ctx.send(embed=em)

@client.command()
async def pewds(ctx):
    subreddit = reddit.subreddit("pewdiepiesubmissions")
    all_subs = []
    top = subreddit.hot(limit=50)
    for submission in top:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    em = discord.Embed(title=name)
    em.set_image(url=url)
    await ctx.send(embed=em)

@client.command()
async def switchthemes(ctx):
    subreddit = reddit.subreddit("nxthemes")
    all_subs = []
    top = subreddit.hot(limit=50)
    for submission in top:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    em = discord.Embed(title=name)
    em.set_image(url=url)
    await ctx.send(embed=em)

@client.command()
async def maicra(ctx):
    subreddit = reddit.subreddit("minecraft")
    all_subs = []
    top = subreddit.hot(limit=50)
    for submission in top:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    em = discord.Embed(title=name)
    em.set_image(url=url)
    await ctx.send(embed=em)

@client.command()
async def cringe(ctx):
    subreddit = reddit.subreddit("cringetopia")
    all_subs = []
    top = subreddit.hot(limit=50)
    for submission in top:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    em = discord.Embed(title=name)
    em.set_image(url=url)
    await ctx.send(embed=em)

@client.command()
async def hmm(ctx):
    subreddit = reddit.subreddit("minecrafthmmm")
    all_subs = []
    top = subreddit.hot(limit=50)
    for submission in top:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    em = discord.Embed(title=name)
    em.set_image(url=url)
    await ctx.send(embed=em)


@client.command()
async def memechafa(ctx):
    subreddit = reddit.subreddit("MemesLatinoamerica")
    all_subs = []
    top = subreddit.hot(limit=50)
    for submission in top:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    em = discord.Embed(title=name)
    em.set_image(url=url)
    await ctx.send(embed=em)

@client.command()
async def pussy(ctx):
    subreddit = reddit.subreddit("cats")
    all_subs = []
    top = subreddit.hot(limit=50)
    for submission in top:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    em = discord.Embed(title=name)
    em.set_image(url=url)
    await ctx.send(embed=em)

@client.command()
async def limpiaojos(ctx):
    subreddit = reddit.subreddit("aww")
    all_subs = []
    top = subreddit.hot(limit=50)
    for submission in top:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    em = discord.Embed(title=name)
    em.set_image(url=url)
    await ctx.send(embed=em)

@client.command(help = "Te da coordenadas random")
async def coordsrandom(ctx):
    cor01 = '0','0','0','0','0','0','0','1','2','1','2','1','2'
    cor012 = '0','0','1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9'
    cor0123= '0','0','0','1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9'
    cor1234 ='0','0','0','1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9'
    cor21 = '0','0','0','0','1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9'
    cor22 = '0','0','0','1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9'
    cor23 ='0','0','0','1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9'
    cor31 ='0','0','1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9'
    cor32='0','0','0','0','1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9'
    cor33='0','0','0','0','1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9'

    COR1 = random.choice(cor01)
    COR2 = random.choice(cor012)
    COR3 = random.choice(cor0123)
    COR4 = random.choice(cor1234)
    COR5 = random.choice(cor21)
    COR6 = random.choice(cor22)
    COR7 = random.choice(cor23)
    COR8 = random.choice(cor31)
    COR9 = random.choice(cor32)
    COR10 = random.choice(cor33)
    await ctx.send(f'{COR1}{COR2}{COR3}{COR4}, {COR5}{COR6}{COR7}, {COR8}{COR9}{COR10}, esas son tus coordenadas random lol, me vale vrga si queda lejos')

@client.command()
async def status(ctx):
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Intentando minar Diamantes :b'))

@client.command(pass_context = True)
async def intercambio(ctx, *, message):
    user = message.author
    miembro = "names of people i will censor for privacy lol"
    gifted = random.choice(member)

    await ctx.send(f'{user} gifts ||{gifted}||')



@client.command()
async def say(ctx, *, question):
    await ctx.message.delete()
    await ctx.send(f'{question}')












client.run(TOKEN)
