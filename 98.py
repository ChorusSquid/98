import discord
from discord.ext import commands
from bs4 import BeautifulSoup as bs
##from lxml import html
from urllib.request import urlopen, urlretrieve
##import urllib
##import wikia
from random import *
import os

cards = ['Aaron', "Aaron's Secret", 'Acceleration', 'Allergic Temmie', 'Alphys', 'Angel of Death', 'Annoying Dog', 'Another Chance', 'Asgore', 'Asriel', 'Asriel Dreemurr', 'Assault', 'Astigmatism', 'Big Bob', 'Big Bomb', 'Big Mouth', 'Blue Laser', 'Blue Snail', 'Bob', 'Bomb', 'Brain Freeze', 'Brain Shift', 'Bratty', 'Break', 'Bridge Seed', 'Bunbun', 'Burgerpants', 'Cactus', 'Candy Dish', 'Casual Undyne', 'Catty', 'Chara', 'Charles', 'Chilldrake', 'Clam Boy', 'Clam Girl', 'Cloning', 'Coffee Man', 'Coffin', 'Cold Winter', 'Contamination', 'Crazy Bun', 'Dancer Mettaton', 'Defrosting', 'Diamond Boy 1', 'Diamond Boy 2', 'Dimensional Box', 'Disco Ball', 'Dog Food', 'Dog House', 'Dogamy', 'Dogaressa', 'Doggo', 'Dummy', 'Echo Fish', 'Echo Flower', 'Elder Puzzler', 'Endogeny', 'Everyman', 'Explosion', 'Expulsion', 'Faun', 'Feast', 'Ferry', 'Final Charge', 'Final Froggit', 'Fire Trap', 'Fishing Rod', 'Flowey', 'Force of Nature', 'Fortune', 'Fridge', 'Frisk', 'Froggit', 'Froggit Trio', 'Fuku Fire', 'Garbage', 'Gaster', 'Gaster Follower 1', 'Gaster Follower 2', 'Gaster Follower 3', 'Gerson', 'Gift Bear', 'Glad Dummy', 'Glyde', 'Golden Flowers', 'Goner Kid', 'Greater Dog', 'Grillby', 'Gyftrot', 'Headshot', 'Heal', 'Heal Delivery', 'Heats Flamesman', 'Hyper Goner', 'Ice', 'Ice Cap', 'Ice Wolf', 'Igloo', 'Inflation', 'Innkeeper', 'Investment', 'Janitor', 'Jerry', 'Knife', 'Knight Knight', 'Lamp', 'Last Dream', 'Lemon Bread', 'Lesser Dog', 'Librarian', 'Longevity', 'Loox', 'Loren', 'MTT Fountain', 'Mace', 'Mad Dummy', 'Madjick', 'Manticore', 'Memorial Statue', 'Memory Head', 'Mettaton', 'Mettaton Ex', 'Mettaton NEO', 'Microwave', 'Migosp', 'Migospel', 'Moldbygg', 'Moldessa', 'Moldsmal', 'Monster Kid', 'Muffet', "Muffet's Pet", 'Multi Shot', 'Nacarat Jester', 'Napstablook', 'Nice Cream Guy', 'Omega Flowey', 'Oni', 'Onion San', 'Orange Laser', 'Papyrus', 'Papyrus Statue', 'Parsnik', 'Penetration', 'Pie', 'Poison', 'Politics Bear', 'Pollutant Gas', 'Protection', 'Punishment', 'Pyrope', 'Reaper Bird', 'Receptionist 1', 'Receptionist 2', 'Receptionist 3', 'Red Bird', 'Red Snail', 'Redacted', 'Resurrection', 'River Person', 'Rock', 'Royal Guard 1', 'Royal Guard 2', 'Sad Customer', 'Sad Dragon', 'Same Fate', 'Sans', 'Scarf Mouse', 'Shambling Mass', 'Sharing', 'Shootout', 'Shopping', 'Shyren', 'Skateboard Girl', 'Slowing', 'Small Bird', 'Snail Trainer', 'Snow Poff', 'Snow Storm', 'Snowdrake', "Snowdrake's Mom", 'Snowman', 'So Sorry', 'Soothing', 'Spider', 'Spider Web', 'Strafe', 'Strength', 'Temmie', 'Temmie Statue', 'Termination', 'Test of Will', 'The Heroine', 'Timer', 'Tiny Froggit', 'Toriel', 'Trader Temmie', 'Trash Tornado', 'Tree', 'Tsunderplane', 'Ugly Fish', 'Undyne', "Undyne's Spears", 'Vegetoid', 'Vulkin', "Vulkin's Cloud", 'Water Cooler', 'Whimsalot', 'Whimsun', 'Will to Fight', 'Worsening', 'Woshua', 'Yellow Snail']
gen = {"Bun": "Bunbun", "Dog Residue": "Annoying Dog", "Doodlebog": "So Sorry", "Gaster Blaster": "Gaster", "Gift": "Gift Bear", "Left Tentacle": "Onion San", "Load": "Omega Flowey", "Lost Soul 1": "Angel of Death", "Lost Soul 2": "Angel of Death", "Lost Soul 3": "Angel of Death", "Lost Soul 4": "Angel of Death", "Lost Soul 5": "Angel of Death", "Lost Soul 6": "Angel of Death", "Mettabot": "Dancer Mettaton", "Pebble": "Rock", "Right Tentacle": "Onion San", "Temmie 2": "Temmie", "Thundersnail": "Snail Trainer"}

classes = {"DT": ["`'Determination: Start the game with 1 extra life. When you would die, gain 15 HP instead.'`", 'Another Chance', 'Hyper Goner', 'Knife', 'Last Dream', 'Resurrection', 'Same Fate', 'Will to Fight'],
           "PATIENCE": ["`'Patience: At the start of your turn, deal 1 damage to all paralyzed enemy monsters. If there is none, paralyze a random enemy monster.'`", 'Brain Freeze', 'Cold Winter', 'Defrosting', 'Fridge', 'Protection', 'Sharing', 'Slowing', 'Snow Storm'],
           "BRAVERY": ["`'Bravery: At the start of your turn, draw cards until you got 4 cards into your hand.'`", "Aaron's Secret", 'Acceleration', 'Assault', 'Final Charge', 'Froggit Trio', 'Penetration', 'Strength'],
           "INTEGRITY": ["`'Integrity: At the end of your turn, gain 1 gold for every 5 gold spent during the turn (max 2).'`", 'Break', 'Cloning', 'Expulsion', 'Fortune', 'Inflation', 'Investment', 'Shopping'],
           "PV": ["`'Perseverance: Whenever an enemy monster is damaged, give it KR. At the start of your opponent's turn, monsters under KR take 1 damage.'`", 'Brain Shift', 'Contamination', 'Poison', 'Pollutant Gas', 'Spider Web', 'Termination', 'Worsening'],
           "KINDNESS": ["`'Kindness: At the end of your turn, restore 2 hp to you and 1 hp to all your monsters.'`", 'Feast', 'Force of Nature', 'Heal', 'Heal Delivery', 'Longevity', 'Pie', 'Soothing', 'Test of Will'],
           "JUSTICE": ["`'Justice: At the end of your turn, deal 1 damage to a random enemy monster.\nIf you have less HP than your opponent, deal 1 bonus damage to him.'`", 'Explosion', 'Headshot', 'Multi Shot', 'Punishment', 'Shootout', 'Strafe', "Undyne's Spears"]}

nine = commands.Bot(command_prefix = "98!", description = "* I Am 98, A Bot Dedicated to the Card Game Known As 'Undercards'.")
cli = discord.Client

def get_images(url, card, rat = None):
    rarities = ["COMMON", "RARE", "EPIC", "LEGENDARY", "DETERMINATION", "UNKOWN"]
    links = []
    try:
        soup = bs(urlopen(url).read(), "html.parser")
##        soup = html.parse(urlopen(url))
    except:
        return "`* Card Not Found.`"
    images = [img for img in soup.findAll('img')]
##    images = [img for img in soup.find_class('img')]
    image_links = [each.get('src') for each in images]
##    image_links = [each.text_content('src') for each in images]
    for each in image_links:
        if "vignette.wikia.nocookie.net/undercards/images/" in each:
            links.append(each)
    for pack in links:
        for r in rarities:
            if r in pack:
                links.remove(pack)
    if rat:
        for pack in links:
            if rat.replace(" ", "_").title()[:-1] not in pack:
                links.remove(pack)
            elif rat.title().split()[0] not in pack:
                links.remove(pack)
    return links[0].replace("/scale-to-width-down/305", "")

@nine.event
async def on_ready():
    await nine.change_presence(game=discord.Game(name='Undercards ❤', url='https://undercards.net/', type=1))
    
@nine.command(pass_context=True)
async def greet(ctx):
    """Says Hello."""
    greetings = ["How Are You Today?", "I Am 98.", "What Is Up?"]
    await ctx.send("`* Greetings, " + str(ctx.message.author.display_name).title() + ". " + choice(greetings) + "`")

@nine.command(pass_context=True)
async def post(ctx, *args):
    post = ""
    for l in args:
        post += str(l) + " "
    if discord.ext.commands.is_owner():
        await ctx.send("`" + post[:-1] + "`")

##@nine.command(pass_context=True)
##async def erase(ctx, number = 1):
##    if discord.ext.commands.is_owner():
##        number = int(number)
##        async for message in cli.logs_from(channel, limit = number):
##            if str(message.author.id) == '417314377083912192':
##                await cli.delete_message(message)
    
@nine.command(pass_context=True)
async def check(ctx, *args):
    """Checks Undercards Wiki For The Requested Card."""
    url = None
    card = ""
    rat = None
    for l in args:
        card += str(l) + " "
    if not card.endswith("... "):
        if card.title().replace("To", "to").replace("Of", "of").replace("'S", "'s")[:-1] in gen:
            rat = card
            card = gen[card.title().replace("To", "to").replace("Of", "of")[:-1]]
            for bit in gen:
                if rat.title()[:-1] in bit:
                    url = "http://undercards.wikia.com/wiki/" + gen[bit].replace(" ", "_").title().replace("To", "to").replace("Of", "of").replace("'S", "'s")
        if not url:
            url = "http://undercards.wikia.com/wiki/" + card.replace(" ", "_").title().replace("To", "to").replace("Of", "of").replace("'S", "'s")
        await ctx.send(get_images(url, card, rat))
    else:
        await ctx.send(wild(card))

@nine.command(pass_context=True)
async def soul(ctx, *args):
    """Displays data on the specified class."""
    text = None
    spell = None
    if len(args) > 1:
        await ctx.send("`* I Can Only Handle One Soul At A Time.`")
    elif len(args) == 0:
        pass
    else:
        Class = args[0].upper()
    if Class == "DETERMINATION":
        Class = "DT"
    if Class.startswith("PERS"):
        Class = "PV"
    if Class.startswith("INTEG"):
        Class = "Integrity"
    if Class in classes:
        text = classes[Class][0]
        spell = choice(classes[Class][1:])
    if text and spell:
        await ctx.send(text + "\n`Here Is A Random " + text.split(":")[0][2:] + " Spell:`")
        await ctx.invoke(check, spell)
    else:
        await ctx.send("`* Soul Not Found.`")
    
def wild(card):
    global cards
    global gen
    url = None
    pages = []
    rat = None
    for page in cards:
        if card[:-4].title() in page:
            pages.append(page)
    for tor in gen:
        if card[:-4].title() in tor:
            pages.append(tor)        
    if len(pages) > 1: 
        return("`* Here Are The Cards I Found: " + str(pages).replace("[", "").replace("]", "") + "`")
    elif not pages:
        return("`* Card Not Found.`")
    else:
        if pages[0] in gen:
            card = gen[pages[0]]
            rat = pages[0]
        else:
            card = pages[0]
        for bit in gen:
            if card.title()[:-1] in bit:
                url = "http://undercards.wikia.com/wiki/" + gen[bit].replace(" ", "_").title().replace("To", "to").replace("Of", "of").replace("'S", "'s")
        if not url:
            url = "http://undercards.wikia.com/wiki/" + card.replace(" ", "_").title().replace("To", "to").replace("Of", "of").replace("'S", "'s")
        return get_images(url, card, rat)

nine.remove_command("help")

@nine.command()
async def help(ctx):
    """Shows My Instruction Manual."""
    emb = discord.Embed(title = "98", description = nine.description, inline = False)
    emb.add_field(name = "98!greet", value = "Says hello.", inline = False)
    emb.add_field(name = "98!check <card>", value = "Checks Undercards Wiki for the requested card.\n('...' for autocomplete, but only with full keywords)", inline = False)
    emb.add_field(name = "98!soul <soul>", value = "Returns information on the specified soul, and a random spell of that class.", inline = False)
    emb.add_field(name = "98!help", value = "Shows commands.", inline = False)
    await ctx.send(embed=emb)
                        
nine.run(os.environ.get["BOT_TOKEN"])
