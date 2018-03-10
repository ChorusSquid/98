import discord
from discord.ext import commands
from bs4 import BeautifulSoup as bs
##from lxml import html
from urllib.request import urlopen, urlretrieve
##import urllib
##import wikia
from random import *
import os

cards = ['Aaron', 'Allergic Temmie', 'Alphys', 'Angel of Death', 'Annoying Dog', 'Asgore', 'Asriel', 'Asriel Dreemurr', 'Astigmatism', 'Big Bob', 'Big Bomb', 'Big Mouth', 'Blue Laser', 'Blue Snail', 'Bob', 'Bomb', 'Bratty', 'Bridge Seed', 'Bunbun', 'Burgerpants', 'Cactus', 'Candy Dish', 'Casual Undyne', 'Catty', 'Chara', 'Charles', 'Chilldrake', 'Clam Boy', 'Clam Girl', 'Coffee Man', 'Coffin', 'Crazy Bun', 'Dancer Mettaton', 'Diamond Boy 1', 'Diamond Boy 2', 'Dimensional Box', 'Disco Ball', 'Dog Food', 'Dog House', 'Dogamy', 'Dogaressa', 'Doggo', 'Dummy', 'Echo Fish', 'Echo Flower', 'Elder Puzzler', 'Endogeny', 'Everyman', 'Faun', 'Ferry', 'Final Froggit', 'Fire Trap', 'Fishing Rod', 'Flowey', 'Frisk', 'Froggit', 'Fuku Fire', 'Garbage', 'Gaster', 'Gaster Follower 1', 'Gaster Follower 2', 'Gaster Follower 3', 'Gerson', 'Gift Bear', 'Glad Dummy', 'Glyde', 'Golden Flowers', 'Goner Kid', 'Greater Dog', 'Grillby', 'Gyftrot', 'Heats Flamesman', 'Ice', 'Ice Cap', 'Ice Wolf', 'Igloo', 'Innkeeper', 'Janitor', 'Jerry', 'Knight Knight', 'Lamp', 'Lemon Bread', 'Lesser Dog', 'Librarian', 'Loox', 'Loren', 'MTT Fountain', 'Mace', 'Mad Dummy', 'Madjick', 'Manticore', 'Memorial Statue', 'Memory Head', 'Mettaton', 'Mettaton Ex', 'Mettaton NEO', 'Microwave', 'Migosp', 'Migospel', 'Moldbygg', 'Moldessa', 'Moldsmal', 'Monster Kid', 'Muffet', "Muffet's Pet", 'Nacarat Jester', 'Napstablook', 'Nice Cream Guy', 'Omega Flowey', 'Oni', 'Onion San', 'Orange Laser', 'Papyrus', 'Papyrus Statue', 'Parsnik', 'Politics Bear', 'Pyrope', 'Reaper Bird', 'Receptionist 1', 'Receptionist 2', 'Receptionist 3', 'Red Bird', 'Red Snail', 'Redacted', 'River Person', 'Rock', 'Royal Guard 1', 'Royal Guard 2', 'Sad Customer', 'Sad Dragon', 'Sans', 'Scarf Mouse', 'Shambling Mass', 'Shyren', 'Skateboard Girl', 'Small Bird', 'Snail Trainer', 'Snow Poff', 'Snowdrake', "Snowdrake's Mom", 'Snowman', 'So Sorry', 'Spider', 'Temmie', 'Temmie Statue', 'The Heroine', 'Timer', 'Tiny Froggit', 'Toriel', 'Trader Temmie', 'Trash Tornado', 'Tree', 'Tsunderplane', 'Ugly Fish', 'Undyne', 'Vegetoid', 'Vulkin', "Vulkin's Cloud", 'Water Cooler', 'Whimsalot', 'Whimsun', 'Woshua', 'Yellow Snail']
gen = {"Bun": "Bunbun", "Dog Residue": "Annoying Dog", "Doodlebog": "So Sorry", "Gaster Blaster": "Gaster", "Gift": "Gift Bear", "Left Tentacle": "Onion San", "Load": "Omega Flowey", "Lost Soul 1": "Angel of Death", "Lost Soul 2": "Angel of Death", "Lost Soul 3": "Angel of Death", "Lost Soul 4": "Angel of Death", "Lost Soul 5": "Angel of Death", "Lost Soul 6": "Angel of Death", "Mettabot": "Dancer Mettaton", "Pebble": "Rock", "Right Tentacle": "Onion San", "Temmie 2": "Temmie", "Thundersnail": "Snail Trainer"}
spells = ["Aaron's Secret", 'Acceleration', 'Another Chance', 'Assault', 'Brain Freeze', 'Brain Shift', 'Break', 'Cloning', 'Cold Winter', 'Contamination', 'Defrosting', 'Explosion', 'Expulsion', 'Feast', 'Final Charge', 'Force of Nature', 'Fortune', 'Fridge', 'Froggit Trio', 'Headshot', 'Heal', 'Heal Delivery', 'Hyper Goner', 'Inflation', 'Investment', 'Knife', 'Last Dream', 'Longevity', 'Multi Shot', 'Penetration', 'Pie', 'Poison', 'Pollutant Gas', 'Protection', 'Punishment', 'Resurrection', 'Same Fate', 'Sharing', 'Shootout', 'Shopping', 'Slowing', 'Snow Storm', 'Soothing', 'Spider Web', 'Strafe', 'Strength', 'Termination', 'Test of Will', "Undyne's Spears", 'Will to Fight', 'Worsening']

rarities = {"common": ['Aaron', 'Assault', 'Astigmatism', 'Blue Laser', 'Blue Snail', 'Bomb', 'Break', 'Bridge Seed', 'Bunbun', 'Cactus', 'Candy Dish', 'Charles', 'Crazy Bun', 'Dog Food', 'Dummy', 'Echo Flower', 'Endogeny', 'Everyman', 'Faun', 'Ferry', 'Final Froggit', 'Fishing Rod', 'Force of Nature', 'Fortune', 'Fridge', 'Froggit', 'Froggit Trio', 'Fuku Fire', 'Gaster Follower 1', 'Gaster Follower 2', 'Gaster Follower 3', 'Gift Bear', 'Golden Flowers', 'Heal', 'Heats Flamesman', 'Ice', 'Ice Cap', 'Igloo', 'Investment', 'Janitor', 'Jerry', 'Knife', 'Knight Knight', 'Lamp', 'Lemon Bread', 'Loox', 'Loren', 'Mace', 'Madjick', 'Memory Head', 'Microwave', 'Migosp', 'Migospel', 'Moldbygg', 'Moldessa', 'Moldsmal', 'MTT Fountain', 'Oni', 'Orange Laser', 'Parsnik', 'Pie', 'Poison', 'Politics Bear', 'Protection', 'Punishment', 'Pyrope', 'Reaper Bird', 'Receptionist 1', 'Red Snail', 'Resurrection', 'Rock', 'Royal Guard 1', 'Royal Guard 2', 'Sad Customer', 'Sad Dragon', 'Scarf Mouse', 'Shambling Mass', 'Sharing', 'Shootout', 'Shyren', 'Slowing', 'Small Bird', 'Snowdrake', "Snowdrake's Mom", 'Snowman', 'Spider', 'Spider Web', 'Strafe', 'Strength', 'Tiny Froggit', 'Tree', 'Tsunderplane', 'Ugly Fish', 'Vegetoid', 'Vulkin', 'Water Cooler', 'Whimsalot', 'Whimsun', 'Will to Fight', 'Worsening', 'Woshua', 'Yellow Snail'],
            "rare": ["Aaron's Secret", 'Allergic Temmie', 'Annoying Dog', 'Another Chance', 'Big Bob', 'Big Mouth', 'Burgerpants', 'Chilldrake', 'Clam Boy', 'Clam Girl', 'Coffee Man', 'Coffin', 'Cold Winter', 'Defrosting', 'Diamond Boy 1', 'Diamond Boy 2', 'Dimensional Box', 'Disco Ball', 'Dog House', 'Dogamy', 'Dogaressa', 'Doggo', 'Echo Fish', 'Elder Puzzler', 'Explosion', 'Expulsion', 'Feast', 'Fire Trap', 'Garbage', 'Glad Dummy', 'Glyde', 'Greater Dog', 'Gyftrot', 'Ice Wolf', 'Lesser Dog', 'Librarian', 'Mad Dummy', 'Manticore', 'Memorial Statue', 'Monster Kid', "Muffet's Pet", 'Nacarat Jester', 'Nice Cream Guy', 'Papyrus Statue', 'Penetration', 'Pollutant Gas', 'Receptionist 2', 'Red Bird', 'Redacted', 'Same Fate', 'Shopping', 'Skateboard Girl', 'Snow Poff', 'So Sorry', 'Soothing', 'Temmie', 'Temmie Statue', 'Termination', 'Timer', 'Trash Tornado', "Undyne's Spears", "Vulkin's Cloud"],
            "epic": ['Acceleration', 'Alphys', 'Asriel', 'Big Bomb', 'Bob', 'Brain Freeze', 'Brain Shift', 'Bratty', 'Catty', 'Cloning', 'Contamination', 'Dancer Mettaton', 'Final Charge', 'Flowey', 'Gaster', 'Goner Kid', 'Grillby', 'Headshot', 'Heal Delivery', 'Hyper Goner', 'Inflation', 'Innkeeper', 'Last Dream', 'Longevity', 'Mettaton', 'Multi Shot', 'Napstablook',  'Onion San', 'Receptionist 3', 'River Person', 'Snail Trainer', 'Snow Storm', 'Test of Will', 'Trader Temmie'],
            "legendary": ['Asgore', 'Asriel Dreemurr', 'Casual Undyne', 'Gerson', 'Mettaton Ex', 'Mettaton NEO', 'Muffet', 'Papyrus', 'Sans', 'Toriel', 'Undyne'],
            "determination": ['Angel of Death', 'Chara', 'Frisk', 'Omega Flowey', 'The Heroine']}

classes = {"DT": ["`'Determination: Start the game with 1 extra life. When you would die, gain 15 HP instead.'`", 'Another Chance', 'Hyper Goner', 'Knife', 'Last Dream', 'Resurrection', 'Same Fate', 'Will to Fight'],
           "PATIENCE": ["`'Patience: At the start of your turn, deal 1 damage to all paralyzed enemy monsters. If there is none, paralyze a random enemy monster.'`", 'Brain Freeze', 'Cold Winter', 'Defrosting', 'Fridge', 'Protection', 'Sharing', 'Slowing', 'Snow Storm'],
           "BRAVERY": ["`'Bravery: At the start of your turn, draw cards until you got 4 cards into your hand.'`", "Aaron's Secret", 'Acceleration', 'Assault', 'Final Charge', 'Froggit Trio', 'Penetration', 'Strength'],
           "INTEGRITY": ["`'Integrity: At the end of your turn, gain 1 gold for every 5 gold spent during the turn (max 2).'`", 'Break', 'Cloning', 'Expulsion', 'Fortune', 'Inflation', 'Investment', 'Shopping'],
           "PV": ["`'Perseverance: Whenever an enemy monster is damaged, give it KR. At the start of your opponent's turn, monsters under KR take 1 damage.'`", 'Brain Shift', 'Contamination', 'Poison', 'Pollutant Gas', 'Spider Web', 'Termination', 'Worsening'],
           "KINDNESS": ["`'Kindness: At the end of your turn, restore 2 hp to you and 1 hp to all your monsters.'`", 'Feast', 'Force of Nature', 'Heal', 'Heal Delivery', 'Longevity', 'Pie', 'Soothing', 'Test of Will'],
           "JUSTICE": ["`'Justice: At the end of your turn, deal 1 damage to a random enemy monster.\nIf you have less HP than your opponent, deal 1 bonus damage to him.'`", 'Explosion', 'Headshot', 'Multi Shot', 'Punishment', 'Shootout', 'Strafe', "Undyne's Spears"]}

arts = {"Normal": {"Copycat": "Shuffle your starting hand into your deck. Add a copy of your opponent's hand into your hand.",
                   "Draw": "Draw one more card every 5 turns.",
                   "Experience": "Increase XP reward by 25%.",
                   "Froggits": "Summon 2 ally Tiny Froggits when your first turn begins.",
                   "Health": "Start the game with 35/35 HP.",
                   "Hourglass": "Your Future effects are triggered one turn earlier.",
                   "Poke": "Deal 5 damage to your opponent at the start of the game.",
                   "Power": "Give +1/+1 to 4 random monsters in your deck when the game begins.",
                   "Preservation": "You can't draw when your hand is full.",
                   "Prosperity": "Whenever you play a monster, heal yourself by 20% of its cost.",
                   "Reinforcement": "Add 5 random monsters with +2/+2 at the end of your deck when the game begins.",
                   "Solidity": "Give +1 HP to your Taunt monsters when the game begins.",
                   "Spy": "Reveal your opponent's hand at the first and every 5 turns.",
                   "Veteran": "Your monsters gain +1 ATK whenever they attack and kill a monster.",
                   "Vitality": "Whenever an ally monster or spell heals a damaged monster to max HP, give +1 HP to the target.",
                   "Will": "Your monsters with Can't attack can attack."},
        "Legendary": {"Arcane Scepter": "Whenever you cast a spell, cast a random spell on a random target.",
                      "Criticals": "Your monsters have a 20% chance to deal 100% bonus damage while attacking.",
                      "Mines": "Add a Little Mine, Mine and a Big Mine in the opponent's deck at the start of the game (deal damage to the player when drawn).",
                      "Science": "Your Gaster Blasters deal 1 bonus damage. Add 5 Gaster Blasters to your deck at the start of the game."},
        "Gerson": {"Cloudy Glasses": "Start of turn: Give +1 HP to a random ally monster.",
                   "Crab Apple": "Start of turn: Give +1 ATK to a random ally monster.",
                   "Sea Tea": "Start of turn: Restore 3 HP to a random damaged ally monster.",
                   "Torn Notebook": "Start of turn: Deal 1 damage to a random enemy monster."}}

nine = commands.Bot(command_prefix = "98!", description = "`* I Am 98, A Bot Dedicated to the Card Game Known As 'Undercards'.`", case_insensitive = True)
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
            if rep(rat)[:-1] not in pack:
                links.remove(pack)
            elif rat.title().split()[0] not in pack:
                links.remove(pack)
    return links[0].replace("/scale-to-width-down/305", "").replace("/scale-to-width-down/220", "")

@nine.event
async def on_ready():
    await nine.change_presence(activity=discord.Streaming(name='Undercards ❤', url='https://undercards.net/'))
    
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
        if not card:
            card = choice(cards)
        if rep(card).replace("_", " ")[:-1] in gen:
            rat = card
            card = gen[rep(card).replace("_", " ")[:-1]]
            for bit in gen:
                if rat.title()[:-1] in bit:
                    url = "http://undercards.wikia.com/wiki/" + rep(gen[bit])
        if not url:
            url = "http://undercards.wikia.com/wiki/" + rep(card)
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
    elif not args:
        Class = choice(list(classes.keys()))
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
    
@nine.command(pass_context=True)
async def artifact(ctx, *args):
    """Gives a description of the requested artifact."""
    art = ""
    fax = []
    for a in args:
        art += str(a) + " "
    art = art[:-1].title()
    if not art:
        if randint(1, 2) == 1:
            art = choice(list(arts["Normal"].keys()))
        else:
            art = choice(list(arts["Legendary"].keys()))
    if art.endswith("..."):
        for i in arts["Normal"]:
            if art[:-3] in i:
                fax.append(i)
        for i in arts["Legendary"]:
            if art[:-3] in i:
                fax.append(i)
        for i in arts["Gerson"]:
            if art[:-3] in i:
                fax.append(i)
        if len(fax) > 1:
            await ctx.send("`* Here Are The Artifacts I Found: " + str(fax).replace("[", "").replace("]", "") + "`")
        elif not fax:
            pass
        else:
            art = fax[0]
    if (art not in arts["Normal"] and art not in arts["Legendary"] and art not in arts["Gerson"]) and not fax:
        await ctx.send("`* Artifact Not Found.`")
    else:
        if art in arts["Normal"]:
            await ctx.send("`'" + art + " | Normal | " + arts["Normal"][art] + "'`")
        elif art in arts["Legendary"]:
            await ctx.send("`'" + art + " | Legendary | " + arts["Legendary"][art] + "'`")
        elif art in arts["Gerson"]:
            await ctx.send("`'" + art + " | Gerson | " + arts["Gerson"][art] + "'`")

@nine.command(pass_context=True)
async def generate(ctx, *args):
    """Generates a random unrestricted deck of the soul you choose, including artifacts."""
    soul = None
    facts = []
    deck = []
    ment = []
    ranks = ""
    limits = {"common": 3, "rare": 3, "epic": 2, "legendary": 1}
    Det = False
    for a in args:
        ment.append(a.upper())
    if len(args) > 1:
        if "RANKED" in ment:
            Det = True
            ranks = "Ranked "
        else:
            await ctx.send("`* I Can Only Handle One Soul At A Time.`")
    elif not args:
        soul = choice(["DT", "PATIENCE", "BRAVERY", "INTEGRITY", "PV", "KINDNESS", "JUSTICE"])
    if not soul:
        soul = args[0].upper()
    if soul == "DETERMINATION":
        soul = "DT"
    if soul.startswith("PERS"):
        soul = "PV"
    if soul.startswith("INT"):
        soul = "INTEGRITY"
    if soul not in classes:
        if soul == "RANKED":
            soul = choice(["DT", "PATIENCE", "BRAVERY", "INTEGRITY", "PV", "KINDNESS", "JUSTICE"])
        else:
            soul = None
            await ctx.send("`* Soul Not Found.`")
    if soul:
        pool = cards + classes[soul][1:]
        while len(deck) < 25:
            mon = choice(pool)
            if mon in rarities["common"] or mon in rarities["rare"]:
                if deck.count(mon) < 3:
                    deck.append(mon)
            elif mon in rarities["epic"]:
                if deck.count(mon) < 2:
                    deck.append(mon)
            elif mon in rarities["legendary"]:
                if deck.count(mon) < 1:
                    deck.append(mon)
            elif mon in rarities["determination"]:
                if not Det:
                    deck.append(mon)
                    Det = True
        rarity = randint(1, 2)
        if rarity == 1:           
            facts.append(choice(list(arts["Normal"].keys())))
            facts.append(choice(list(arts["Normal"].keys())))
            facts.sort()
            if facts[0] == facts[1]:
                facts.remove(facts[1])
        elif rarity == 2:
            facts.append(choice(list(arts["Legendary"].keys())))
    if deck:
        deck.sort()
        post = "Your " + ranks + classes[soul][0].split(":")[0][2:] + " Deck: "
        for d in deck:
            post += rep(d).replace("_", " ") + ", "
        post = post[:-2]
        post += "\nArtifacts: "
        for f in facts:
            post += f + ", "
        if "Gerson" in deck:
            post += choice(list(arts["Gerson"].keys()))
        else:
            post = post[:-2]
        await ctx.send("`" + post + "`")

@nine.command(pass_context=True)
async def rarity(ctx, *args):
    """Returns a random card of the selected rarity."""
    rar = ""
    if len(args) > 1:
        await ctx.send("`* I Can Only Handle One Rarity At A Time.`")
    elif not args:
        rar = choice(["common", "rare", "epic", "legendary", "determination"])
    else:
        rar = args[0].lower()
    if rar == "dt":
        rar = "determination"
    car = choice(rarities[rar])
    await ctx.send("`* There Are " + str(len(rarities[rar])) + " " + rar.title() + " Cards.\nHere is a random one:`")
    await ctx.invoke(check, car)

def wild(card):
    global cards
    global gen
    url = None
    pages = []
    rat = None
    for page in cards:
        if card[:-4].title() in page:
            pages.append(page)
    for arc in spells:
        if card[:-4].title() in arc:
            pages.append(arc)
    for tor in gen:
        if card[:-4].title() in tor:
            pages.append(tor)        
    if len(pages) > 1:
        for p in pages:
            p = rep(p).replace("_", " ")        
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
                url = "http://undercards.wikia.com/wiki/" + rep(gen[bit])
        if not url:
            url = "http://undercards.wikia.com/wiki/" + rep(card)
        return get_images(url, card, rat)
    
def rep(text):
    text = text.replace(" ", "_").title().replace("To ", "to ").replace("Of", "of").replace("'S", "'s").replace("Mtt", "MTT").replace("Neo", "NEO")
    return text

nine.remove_command("help")

@nine.command()
async def help(ctx):
    """Shows My Instruction Manual."""
    emb = discord.Embed(title = "98", description = nine.description, inline = False)
    emb.add_field(name = "98!greet", value = "Says hello.", inline = False)
    emb.add_field(name = "98!check <card>", value = "Checks Undercards Wiki for the requested card.\n('...' for autocomplete, but only with full keywords)", inline = False)
    emb.add_field(name = "98!soul <soul>", value = "Returns information on the specified soul, and a random spell of that class.", inline = False)
    emb.add_field(name = "98!artifact <artifact>", value = "Gives a description of the requested artifact.", inline = False)
    emb.add_field(name = "98!rarity <rarity>", value = "Returns a random card of the selected rarity.", inline = False)
    emb.add_field(name = "98!generate <soul>", value = "Generates a random deck of the soul you choose, including artifacts. Call `98!generate <soul> ranked` for no DTs.", inline = False)
    emb.add_field(name = "98!help", value = "Shows commands.", inline = False)
    await ctx.send(embed=emb)
                        
nine.run(os.environ["BOT_TOKEN"])
