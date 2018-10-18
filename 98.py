import discord
from discord.ext import commands
from bs4 import BeautifulSoup as bs
##from lxml import html
from urllib.request import urlopen, urlretrieve
##import urllib
##import wikia
from random import *
import os

prices = ['Break', 'Force of Nature', 'Fridge', 'Golden Hit', 'Protection', 'Shopping', 'Tiny Froggit',
          'Acceleration', 'Assault', 'Blue Snail', 'Dummy', 'Heal', 'Inflation', 'Investment', 'Penetration', 'Poison', 'Red Snail', 'Sacrifice', 'Spider', 'Snowman', 'Will to Fight', 'Yellow Snail',
          'Froggit', 'Moldsmal', 'Migosp', 'Loox', 'Annoying Dog', 'Bridge Seed', 'Charles', 'Defrosting', 'G Follower 1', 'Ice Replica', 'Lamp', 'Monster Kid', 'Pie', 'Ragel', 'Siphoning', 'Strength', 'Temmie',
          'Allergic Temmie', 'Big Bob', 'Bomb', 'Burger Bush', 'Cactus', 'Candy Dish', 'Cloning', 'Crazy Bun', 'Diamond Boy 1', 'Diamond Boy 2', 'Doggo', 'Echo Flower', 'Ferry', 'Fishing Rod', 'Flowey', 'Fox Head', 'Goner Kid', 'Ice Cap', 'Janitor', 'Knife', 'Mace', 'Memorial Statue', 'Microwave', 'Moldbygg', 'Napstablook', 'Punishment', 'Punk Hamster', 'Rage', 'Receptionist 3', 'Resurrection', 'Scarf Mouse', 'Script Bomb', 'Shootout', 'Shyren', 'Slowing', 'Soothing', 'Spider Web', 'Temmie Statue', 'Timer', 'Trash Tornado', 'Vegetoid', 'Water Cooler', 'Whimsun', 'Worsening',
          'Blue Laser', 'Bone Painting', 'Chilldrake', 'Coffin', 'Disco Ball', 'Editor 1', 'Editor 2', 'Fast Sanction', 'Faun', 'Feast', 'Fire Trap', 'Froggit Trio', 'Fuku Fire', 'Glad Dummy', 'Golden Flowers', 'Heats Flamesman', 'Ice', 'Last Dream', 'Librarian', 'Longevity', 'Memory Head', 'Mettaton', 'Migospel', 'Moldessa', 'Octofriend', 'Orange Laser', 'Parsnik', 'Politics Bear', 'Pollutant Gas', 'Receptionist 2', 'Redacted', 'Small Bird', 'Snow Poff', 'Snowdin Sign', 'Snowdrake', 'Strafe', 'Termination', 'Tree', 'Vulkin', "Vulkin's Cloud",
          'Aaron', "Aaron's Secret", 'Alphys', 'Another Chance', 'Asriel', 'Bench', 'Big Mouth', 'Bob', 'Brain Shift', 'Bunbun', 'Clam Boy', 'Cold Winter', 'Dimensional Box', 'Dog Food', 'Dog House', 'Dogamy', 'Dogaressa', 'Echo Fish', 'Expulsion', 'Garbage', 'Gaster', 'Gift Bear', 'Grillby', 'Hot Dog Vulkin', 'Igloo', 'Jerry', 'Loren', 'MTT Fountain', 'Madjick', "Muffet's Pet", 'Multi Shot', 'Nacarat Jester', 'Pyrope', 'Red Bird', 'Skateboard Girl', 'So Sorry', 'Trader Temmie', "Undyne's Spears",
          'Brain Freeze', 'Burgerpants', 'Business Dude', 'Dad Slime', 'Explosion', 'Eye', 'Fortune', 'G Follower 2', 'Ice Wolf', 'Innkeeper', 'Lemon Bread', 'Lesser Dog', 'Mad Dummy', 'Nice Cream Guy', 'Papyrus Statue', 'Reaper Bird', 'Receptionist 1', 'Rock', 'Sad Customer', 'Sad Dragon', 'Sans', 'Shambling Mass', 'Snail Trainer', 'TV', 'Ugly Fish', 'Woshua',
          'Astigmatism', 'Big Bomb', 'Bratty', 'Catty', 'Clam Girl', 'Dancer Mettaton', 'Dress Lion', 'Everyman', 'Final Charge', 'Final Froggit', 'Greater Dog', 'HeadShot', 'Hot Dog Harpy', 'Manticore', 'Oni', 'Same Fate', 'Snow Storm', "Snowdrake's Mom", 'Test of Will', 'Throne', 'Whimsalot',
          'Coffee Man', 'Contamination', 'Elder Puzzler', 'Endogeny', 'G Follower 3', 'Gerson', 'Gyftrot', 'River Person', 'Tsunderplane',
          'Knight Knight', 'Mettaton NEO', 'Royal Guard 1', 'Royal Guard 2',
          'Cool Papyrus', 'Glyde', 'Mettaton Ex', 'Muffet',
          'Onion San', 'Toriel',
          'Casual Undyne', 'Papyrus', 'Robot 98',
          'Asgore', 'Frisk', 'Undyne',
          'Omega Flowey', 
          'The Heroine',
          'Asriel Dreemurr',
          'Angel of Death',
          'Hyper Goner',
          'Chara']

spells = ['Break', 'Force of Nature', 'Fridge', 'Golden Hit', 'Protection', 'Shopping',
          'Acceleration', 'Assault', 'Heal', 'Inflation', 'Investment', 'Penetration', 'Poison', 'Sacrifice', 'Will to Fight',
          'Defrosting', 'Ice Replica', 'Siphoning', 'Strength',
          'Cloning', 'Knife', 'Pie', 'Punishment', 'Rage', 'Resurrection', 'Shootout', 'Slowing', 'Soothing', 'Spider Web', 'Worsening',
          'Fast Sanction', 'Feast', 'Froggit Trio', 'Last Dream', 'Octofriend', 'Pollutant Gas', 'Strafe', 'Termination',
          "Aaron's Secret", 'Another Chance',  'Brain Shift', 'Cold Winter', 'Expulsion', 'Fortune', 'Longevity', 'Multi Shot', "Undyne's Spears",
          'Brain Freeze', 'Explosion',
          'Final Charge', 'HeadShot', 'Same Fate', 'Snow Storm', 'Test of Will',
          'Contamination',
          'Hyper Goner']
monsters = [m for m in prices if m not in spells]
gen = {"Bun": "Bunbun", "Dog Residue": "Annoying Dog", "Doodlebog": "So Sorry", "Gaster Blaster": "Gaster", "Gift": "Gift Bear", "Kid Slime": "Dad Slime", "Left Tentacle": "Onion San", "Load": "Omega Flowey", "Lost Souls": "Angel of Death", "Lost Soul 1": "Angel of Death", "Lost Soul 2": "Angel of Death", "Lost Soul 3": "Angel of Death", "Lost Soul 4": "Angel of Death", "Lost Soul 5": "Angel of Death", "Lost Soul 6": "Angel of Death", "Lost Souls": "Angel of Death", "Mettabot": "Dancer Mettaton", "Pebble": "Rock", "Right Tentacle": "Onion San", "Temmie 2": "Temmie", "Tentacles": "Onion San", "Thundersnail": "Snail Trainer"}

costs = {'Break': 0, 'Force of Nature': 0, 'Fridge': 0, 'Protection': 0, 'Shopping': 0, 'Tiny Froggit': 0,
         'Acceleration': 1, 'Assault': 1, 'Blue Snail': 1, 'Dummy': 1, 'Heal': 1, 'Inflation': 1, 'Investment': 1, 'Penetration': 1, 'Poison': 1, 'Red Snail': 1,  'Spider': 1, 'Snowman': 1, 'Will to Fight': 1, 'Yellow Snail': 1,
         'Froggit': 2, 'Moldsmal': 2, 'Migosp': 2, 'Loox': 2, 'Annoying Dog': 2, 'Bridge Seed': 2, 'Charles': 2, 'Defrosting': 2, 'Froggit': 2, 'G Follower 1': 2, 'Lamp': 2, 'Loox': 2, 'Migosp': 2, 'Moldsmal': 2, 'Monster Kid': 2, 'Strength': 2, 'Temmie': 2,
         'Allergic Temmie': 3, 'Big Bob': 3, 'Bomb': 3, 'Cactus': 3, 'Candy Dish': 3, 'Cloning': 3, 'Crazy Bun': 3, 'Diamond Boy 1': 3, 'Diamond Boy 2': 3, 'Doggo': 3, 'Echo Flower': 3, 'Ferry': 3, 'Fishing Rod': 3, 'Flowey': 3, 'Goner Kid': 3, 'Ice Cap': 3, 'Janitor': 3, 'Knife': 3, 'Mace': 3, 'Memorial Statue': 3, 'Microwave': 3, 'Moldbygg': 3, 'Napstablook': 3, 'Pie': 3, 'Punishment': 3, 'Punk Hamster': 3, 'Receptionist 3': 3, 'Resurrection': 3, 'Scarf Mouse': 3, 'Script Bomb': 3, 'Shootout': 3, 'Shyren': 3, 'Slowing': 3, 'Soothing': 3, 'Spider Web': 3, 'Temmie Statue': 3, 'Timer': 3, 'Trash Tornado': 3, 'Vegetoid': 3, 'Water Cooler': 3, 'Whimsun': 3, 'Worsening': 3,
         'Blue Laser': 4, 'Chilldrake': 4, 'Coffin': 4, 'Disco Ball': 4, 'Faun': 4, 'Feast': 4, 'Fire Trap': 4, 'Froggit Trio': 4, 'Fuku Fire': 4, 'Glad Dummy': 4, 'Golden Flowers': 4, 'Heats Flamesman': 4, 'Ice': 4, 'Last Dream': 4, 'Librarian': 4, 'Longevity': 4, 'Memory Head': 4, 'Mettaton': 4, 'Migospel': 4, 'Moldessa': 4, 'Orange Laser': 4, 'Parsnik': 4, 'Politics Bear': 4, 'Pollutant Gas': 4, 'Receptionist 2': 4, 'Redacted': 4, 'Small Bird': 4, 'Snow Poff': 4, 'Snowdin Sign': 4, 'Snowdrake': 4, 'Strafe': 4, 'Termination': 4, 'Tree': 4, 'Vulkin': 4, "Vulkin's Cloud": 4,
         'Aaron': 5, "Aaron's Secret": 5, 'Alphys': 5, 'Another Chance': 5, 'Asriel': 5, 'Big Mouth': 5, 'Bob': 5, 'Brain Shift': 5, 'Bunbun': 5, 'Clam Boy': 5, 'Cold Winter': 5, 'Dimensional Box': 5, 'Dog Food': 5, 'Dog House': 5, 'Dogamy': 5, 'Dogaressa': 5, 'Echo Fish': 5, 'Expulsion': 5, 'Garbage': 5, 'Gaster': 5, 'Gift Bear': 5, 'Grillby': 5, 'Hot Dog Vulkin': 5, 'Igloo': 5, 'Jerry': 5, 'Loren': 5, 'MTT Fountain': 5, 'Madjick': 5, "Muffet's Pet": 5, 'Multi Shot': 5, 'Nacarat Jester': 5, 'Pyrope': 5, 'Red Bird': 5, 'Skateboard Girl': 5, 'So Sorry': 5, 'Trader Temmie': 5, "Undyne's Spears": 5,
         'Brain Freeze': 6, 'Burgerpants': 6, 'Dad Slime': 6, 'Explosion': 6, 'Fortune': 6, 'G Follower 2': 6, 'Ice Wolf': 6, 'Innkeeper': 6, 'Lemon Bread': 6, 'Lesser Dog': 6, 'Mad Dummy': 6, 'Nice Cream Guy': 6, 'Papyrus Statue': 6, 'Reaper Bird': 6, 'Receptionist 1': 6, 'Rock': 6, 'Sad Customer': 6, 'Sad Dragon': 6, 'Sans': 6, 'Shambling Mass': 6, 'Snail Trainer': 6, 'Ugly Fish': 6, 'Woshua': 6,
         'Astigmatism': 7, 'Big Bomb': 7, 'Bratty': 7, 'Catty': 7, 'Clam Girl': 7, 'Everyman': 7, 'Final Charge': 7, 'Final Froggit': 7, 'Greater Dog': 7,'HeadShot': 7, 'Manticore': 7, 'Oni': 7, 'Same Fate': 7, 'Snow Storm': 7, "Snowdrake's Mom": 7, 'Test of Will': 7, 'Whimsalot': 7,
         'Coffee Man': 8, 'Contamination': 8, 'Dancer Mettaton': 8, 'Elder Puzzler': 8, 'Endogeny': 8, 'G Follower 3': 8, 'Gerson': 8, 'Gyftrot': 8, 'River Person': 8, 'Tsunderplane': 8,
         'Knight Knight': 9, 'Mettaton NEO': 9, 'Royal Guard 1': 9, 'Royal Guard 2': 9,
         'Glyde': 10, 'Mettaton Ex': 10, 'Muffet': 10,
         'Onion San': 11, 'Toriel': 11,
         'Casual Undyne': 12, 'Papyrus': 12,
         'Asgore': 14, 'Frisk': 14, 'Undyne': 14,
         'Omega Flowey': 15,
         'The Heroine': 16,
         'Asriel Dreemurr': 18,
         'Angel of Death': 22,
         'Hyper Goner': 35,
         'Chara': 40

rarities = {"common": ['Aaron', 'Assault', 'Astigmatism', 'Bench', 'Blue Laser', 'Blue Snail',  'Bomb', 'Bone Painting', 'Break', 'Bridge Seed', 'Bunbun', 'Cactus', 'Candy Dish', 'Charles', 'Crazy Bun', 'Dad Slime', 'Dog Food', 'Dress Lion', 'Dummy', 'Echo Flower', 'Endogeny', 'Everyman', 'Eye', 'Faun', 'Ferry', 'Final Froggit', 'Fishing Rod', 'Force of Nature', 'Fortune', 'Fox Head', 'Fridge', 'Froggit', 'Froggit Trio', 'Fuku Fire', 'Gaster Follower 1', 'Gaster Follower 2', 'Gaster Follower 3', 'Gift Bear', 'Golden Flowers', 'Heal', 'Heats Flamesman', 'Hot Dog Vulkin', 'Ice', 'Ice Cap', 'Igloo', 'Investment', 'Janitor', 'Jerry', 'Knife', 'Knight Knight', 'Lamp', 'Lemon Bread', 'Loox', 'Loren', 'Mace', 'Madjick', 'Memory Head', 'Microwave', 'Migosp', 'Migospel', 'Moldbygg', 'Moldessa', 'Moldsmal', 'MTT Fountain', 'Oni', 'Orange Laser', 'Parsnik', 'Pie', 'Poison', 'Politics Bear', 'Protection', 'Punishment', 'Pyrope', 'Reaper Bird', 'Receptionist 1', 'Red Snail', 'Resurrection', 'Rock', 'Royal Guard 1', 'Royal Guard 2', 'Sad Customer', 'Sad Dragon', 'Scarf Mouse', 'Script Bomb', 'Shambling Mass', 'Sharing', 'Shootout', 'Shyren', 'Slowing', 'Small Bird', 'Snowdrake', "Snowdrake's Mom", 'Snowman', 'Spider', 'Spider Web', 'Strafe', 'Strength', 'Tiny Froggit', 'Tree', 'Tsunderplane', 'TV', 'Ugly Fish', 'Vegetoid', 'Vulkin', 'Water Cooler', 'Whimsalot', 'Whimsun', 'Will to Fight', 'Worsening', 'Woshua', 'Yellow Snail'],
            "rare": ["Aaron's Secret", 'Allergic Temmie', 'Annoying Dog', 'Another Chance', 'Big Bob', 'Big Mouth', 'Burgerpants', 'Burger Bush', 'Business Dude', 'Chilldrake', 'Clam Boy', 'Clam Girl', 'Coffee Man', 'Coffin', 'Cold Winter', 'Defrosting', 'Diamond Boy 1', 'Diamond Boy 2', 'Dimensional Box', 'Disco Ball', 'Dog House', 'Dogamy', 'Dogaressa', 'Doggo', 'Echo Fish', 'Editor 1 ', 'Editor 2', 'Elder Puzzler', 'Explosion', 'Expulsion', "Fast Sanction", 'Feast', 'Fire Trap', 'Garbage', 'Glad Dummy', 'Glyde', 'Golden Hit', 'Greater Dog', 'Gyftrot', 'Ice Replica', 'Ice Wolf', 'Lesser Dog', 'Librarian', 'Mad Dummy', 'Manticore', 'Memorial Statue', 'Monster Kid', "Muffet's Pet", 'Nacarat Jester', 'Nice Cream Guy', 'Octofriend', 'Papyrus Statue', 'Penetration', 'Pollutant Gas', 'Punk Hamster', 'Rage', 'Receptionist 2', 'Red Bird', 'Redacted', 'Sacrifice', 'Same Fate', 'Shopping', 'Siphoning', 'Skateboard Girl', 'Snow Poff', 'Snowdin Sign', 'So Sorry', 'Soothing', 'Temmie', 'Temmie Statue', 'Termination', 'Timer', 'Trash Tornado', "Undyne's Spears", "Vulkin's Cloud"],
            "epic": ['Acceleration', 'Alphys', 'Asriel', 'Big Bomb', 'Bob', 'Brain Freeze', 'Brain Shift', 'Bratty', 'Catty', 'Cloning', 'Contamination', 'Dancer Mettaton', 'Final Charge', 'Flowey', 'Gaster', 'Goner Kid', 'Grillby', 'Headshot', 'Heal Delivery', 'Hot Dog Harpy', 'Hyper Goner', 'Inflation', 'Innkeeper', 'Last Dream', 'Longevity', 'Mettaton', 'Multi Shot', 'Napstablook',  'Onion San', 'Ragel', 'Receptionist 3', 'River Person', 'Robot 98', 'Snail Trainer', 'Snow Storm', 'Test of Will', 'Throne', 'Trader Temmie'],
            "legendary": ['Asgore', 'Asriel Dreemurr', 'Cool Papyrus', 'Casual Undyne', 'Gerson', 'Mettaton Ex', 'Mettaton NEO', 'Muffet', 'Papyrus', 'Sans', 'Toriel', 'Undyne'],
            "determination": ['Angel of Death', 'Chara', 'Frisk', 'Omega Flowey', 'The Heroine']}

classes = {"DT": ["`'Determination: Start the game with 1 extra life. When you would die, gain 15 HP instead.'`", 'Another Chance', 'Hyper Goner', 'Knife', 'Last Dream', 'Resurrection', 'Same Fate', 'Will to Fight'],
           "PATIENCE": ["`'Patience: At the start of your turn, deal 1 damage to all paralyzed enemy monsters. If there is none, paralyze a random enemy monster.'`", 'Brain Freeze', 'Cold Winter', 'Defrosting', 'Fridge', 'Protection', 'Sharing', 'Slowing', 'Snow Storm'],
           "BRAVERY": ["`'Bravery: At the start of your turn, draw cards until you got 4 cards into your hand.'`", "Aaron's Secret", 'Acceleration', 'Assault', 'Final Charge', 'Froggit Trio', 'Penetration', 'Strength'],
           "INTEGRITY": ["`'Integrity: At the end of your turn, gain 1 gold for every 5 gold spent during the turn (max 2).'`", 'Break', 'Cloning', 'Expulsion', 'Fortune', 'Inflation', 'Investment', 'Shopping'],
           "PV": ["`'Perseverance: Whenever an enemy monster is damaged, give it KR. At the start of your opponent's turn, monsters under KR take 1 damage.'`", 'Brain Shift', 'Contamination', 'Poison', 'Pollutant Gas', 'Spider Web', 'Termination', 'Worsening'],
           "KINDNESS": ["`'Kindness: At the end of your turn, restore 2 hp to you and 1 hp to all your monsters.'`", 'Feast', 'Force of Nature', 'Heal', 'Heal Delivery', 'Longevity', 'Pie', 'Soothing', 'Test of Will'],
           "JUSTICE": ["`'Justice: At the end of your turn, deal 1 damage to a random enemy monster.\nIf you have less HP than your opponent, deal 1 bonus damage to him.'`", 'Explosion', 'Headshot', 'Multi Shot', 'Punishment', 'Shootout', 'Strafe', "Undyne's Spears"]}

arts = {"Normal": {"Copycat": "Shuffle your starting hand into your deck. Add a copy of your opponent's hand into your hand.",
                   "Draw": "Draw one more card every 4 turns (except turn 1).",
                   "Experience": "Increase XP reward by 25%.",
                   "Froggits": "At the start of the game, add a Tiny Froggit to your hand, and add a Froggit and Final Froggit to your deck.",
                   "Health": "Start the game with 35/35 HP.",
                   "Hourglass": "Your Future effects are triggered one turn earlier. Start of game: Add a Goner Kid to your deck.",
                   "Poke": "Deal 5 damage to your opponent at the start of the game.",
                   "Power": "Give +1/+1 to 4 random monsters in your deck when the game begins.",
                   "Preservation": "You won't draw at the start of your turn if your hand is full.",
                   "Prosperity": "Whenever you play a monster, heal yourself by 20% of its cost.",
                   "Reinforcement": "Add 5 random monsters with +2/+2 at the end of your deck when the game begins.",
                   "Solidity": "Give +1 HP to your Taunt monsters when the game begins.",
                   "Spy": "Start of turn 1 and every 5th turn: Reveal the enemy's hand and give their first spell +1 cost.",
                   "Veteran": "Your monsters with => 3 ATK have: \"Murder: Gain +1 ATK.\"",
                   "Vitality": "Whenever an ally monster or spell heals a damaged monster to max HP, give +1 HP to the target",
                   "Will": "Your monsters with Can't attack can attack."},
        "Legendary": {"Arcane Scepter": "Whenever you cast a spell with a base cost equals or greater than 2, cast a random spell on a random target.",
                      "Criticals": "Your monsters have a 20% chance to deal 100% bonus damage while attacking.",
                      "Mines": "Add a Little Mine, Mine and a Big Mine in the opponent's deck at the start of the game (deal damage to the player when drawn).",
                      "Science": "Your Gaster Blasters deal 1 bonus damage. Add 5 Gaster Blasters to your deck at the start of the game."},
        "Gerson": {"Cloudy Glasses": "Start of turn: Give +1 HP to a random ally monster.",
                   "Crab Apple": "Start of turn: Give +1 ATK to a random ally monster.",
                   "Sea Tea": "Start of turn: Restore 3 HP to a random damaged ally monster.",
                   "Torn Notebook": "Start of turn: Deal 1 damage to a random enemy monster."}}

effects = {"Magic": "The monster will trigger its effect when played on the board.",
           "Dust": "The monster will trigger its effect when dying.",
           "Start of turn": "The monster will trigger its effect at the start of your turn.",
           "End of turn": "The monster will trigger its effect at the end of your turn.",
           "Future": 'The monster will trigger its effect in (x) turns (can\'t be cancelled by the effect "Silence").',
           "Dodge": "The monster will negate any instance of damage (x) times per turn.",
           "Armor": "The monster will negate (x) damage.",
           "Taunt": "You are forced to attack this monster.",
           "Charge": "The monster can attack during its first turn.",
           "Haste": "The monster can attack during its first turn but cannot target the opponent.",
           "KR": "This monster will take 1 damage at the start of your turn.",
           "Can't attack": "This monster can't attack.",
           "Locked": "This monster can't be directly targeted by effects.",
           "Transparency": "You can't target this monster. This effect is removed after an attack.",
           "Candy": "The monster will be healed by 3 at the end of your turn.",
           "Paralyze": "Make a monster unable to attack until the next turn.",
           "Paralyzed": "This monster can't attack until the next turn.",
           "Silence": "Remove all buffs and debuffs of a monster and make it unable to use its abilities.",
           "Silenced": "This monster can no longer use its abilities.",
           "Fatigue": "Damage dealt to players everytime they draw a card when their deck is empty. The damage is increased by 1 after each activation.",
           "Turbo": "The card will trigger its effect when drawn.",
           "Another Chance": "Dust: Summon this monster for your opponent with +1/+1.",
           "Invulnerable": "This monster is immune to all damage.",
           "Determination": "This monster can't be silenced."}

nine = commands.Bot(command_prefix = "98!", description = "`* I Am 98, A Bot Dedicated to the Card Game Known As 'Undercards'.`", case_insensitive = True)

def get_images(url, card, rat = None):
    rarities = ["COMMON", "RARE", "EPIC", "LEGENDARY", "DETERMINATION", "UNKOWN"]
    links = []
    try:
        soup = bs(urlopen(url).read(), "html.parser")
    except:
        return "`* Card Not Found.`"
    images = [img for img in soup.findAll('img')]
    image_links = [each.get('src') for each in images]
    for each in image_links:
        if "vignette.wikia.nocookie.net/undercards/images/" in each:
            links.append(each)
    for pack in links:
        for r in rarities:
            if r in pack:
                links.remove(pack)
    posts = []
    if rat:
        for pack in links:
            if pack.find("Skin") == -1:
                if True: # rep(rat) in pack:
                    if rat.title().split()[0] in pack:
                        if rat.title().split()[-1] in pack:
                            posts.append(pack)
    if not posts:
        if "scale-to-width-down/" in links[0]:
            find = links[0].find("scale-to-width-down/")
            links[0] = links[0][0:find] + links[0][find + 23:]
        return links[0]
    else:
        if "scale-to-width-down/" in posts[0]:
            find = posts[0].find("scale-to-width-down/")
            posts[0] = posts[0][0:find] + posts[0][find + 23:]
        return posts[0]

@nine.event
async def on_ready():
    await nine.change_presence(activity=discord.Streaming(name='Undercards ❤', url='https://undercards.net/'))
    
@nine.command(pass_context=True)
async def greet(ctx):
    """Says Hello."""
    greetings = ["How Are You Today?", "I Am 98.", "What Is Up?"]
    await ctx.send("`* Greetings, " + str(ctx.message.author.display_name).title() + ". " + choice(greetings) + "`")

@commands.is_owner()
@nine.command(pass_context=True)
async def post(ctx, *args):
    post = ""
    for l in args:
        post += str(l) + " "
    post = post[:-1]
    await ctx.send(post)

@commands.is_owner()
@nine.command(pass_context=True)
async def say(ctx, *args):
    post = ""
    for l in args:
        post += str(l) + " "
    post = post[:-1]
    await ctx.send("`" + post + "`")

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
            card = choice(monsters)
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

@nine.command(name = "soul", aliases = ["class"], pass_context=True)
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
        Class = "INTEGRITY"
    if Class in classes:
        text = classes[Class][0]
        spell = choice(classes[Class][1:])
    if text and spell:
##        await ctx.send(text + "\n`Here Is A Random " + text.split(":")[0][2:] + " Spell:`")
##        await ctx.invoke(check, spell)
        await ctx.send(text + "\n`Here Are The Spells Of This Class: " + str(classes[Class][1:]).replace("[", "").replace("]", "") + "`")
    else:
        await ctx.send("`* Soul Not Found.`")
    
@nine.command(name = "artifact", aliases = ["art", "artefact"], pass_context=True)
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

@nine.command(name = "generate", aliases = ["gen"], pass_context=True)
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
    if len(ment) > 1:
        if "RANKED" in ment:
            pass
        else:
            await ctx.send("`* I Can Only Handle One Soul At A Time.`")
    elif not args:
        soul = choice(["DT", "PATIENCE", "BRAVERY", "INTEGRITY", "PV", "KINDNESS", "JUSTICE"])
    if "RANKED" in ment:
        Det = True
        ranks = "Ranked "
        ment.remove("RANKED")
    if not soul:
        soul = ment[0].upper()
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
        pool = monsters + classes[soul][1:]
        while len(deck) < 25:
            mon = choice(pool)
            if mon == "Heal Delivery" or mon == "Sharing":
                pass
            elif mon in rarities["common"] or mon in rarities["rare"]:
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
            while facts[0] == facts[1]:
                facts.remove(facts[1])
                facts.append(choice(list(arts["Normal"].keys())))
            facts.sort()
        elif rarity == 2:
            facts.append(choice(list(arts["Legendary"].keys())))
    if deck:
        deck.sort(key = lambda x: prices.index(x))
        post = "Your " + ranks + classes[soul][0].split(":")[0][2:] + " Deck: "
        for d in deck:
            post += rep(d).replace("_", " ") + ", "
        post = post[:-2]
        post += "\nArtifacts: "
        for f in facts:
            post += f + ", "
##        if "Gerson" in deck:
##            post += choice(list(arts["Gerson"].keys()))
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
    await ctx.send("`* There Are " + str(len(rarities[rar])) + " " + rar.title() + " Cards.\nHere Is A Random One:`")
    await ctx.invoke(check, car)

@nine.command(name = "effect", aliases = ["keyword"], pass_context=True)
async def effect(ctx, *args):
    """Gives a description of an effect or keyword."""
    global effects
    eff = ""
    if not args:
        eff = choice(list(effects.keys())) + " "
    else:
        for i in args:
            eff += i + " "
    eff = eff[:-1].capitalize()
    if eff == "Kr":
        eff = "KR"
    elif eff == "Another chance":
        eff = "Another Chance"
    elif eff == "Not targetable":
        eff = "Locked"
    if eff in effects:
        await ctx.send('`"' + eff + ": " + effects[eff] + '"`')
    else:
        await ctx.send("`Effect Not Found.`")

def wild(card):
    global monsters
    global gen
    url = None
    pages = []
    rat = None
    for page in monsters:
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
    text = text.replace(" ", "_").title().replace("To_", "to_").replace("Of", "of").replace("'S", "'s").replace("Mtt", "MTT").replace("Neo", "NEO").replace("Tv", "TV")

    return text

nine.remove_command("help")

@nine.command()
async def help(ctx):
    """Shows My Instruction Manual."""
    emb = discord.Embed(title = "98", description = nine.description, inline = False)
    emb.add_field(name = "98!greet", value = "Says hello.", inline = False)
    emb.add_field(name = "98!check <card>", value = "Checks Undercards Wiki for the requested card.\n('...' for autocomplete, but only with full keywords)", inline = False)
    emb.add_field(name = "98!soul <soul>", value = "Returns information on the specified soul, and the spells of that class. (alias: 98!class)", inline = False)
    emb.add_field(name = "98!artifact <artifact>", value = "Gives a description of the requested artifact. (aliases: 98!art, 98!artefact)", inline = False)
    emb.add_field(name = "98!rarity <rarity>", value = "Returns a random card of the selected rarity.", inline = False)
    emb.add_field(name = "98!effect <effect>", value = "Gives a description of the requested effect of keyword. (alias: 98!keyword)", inline = False)
    emb.add_field(name = "98!generate <soul>", value = "Generates a random deck of the soul you choose, including artifacts. Call `98!generate <soul> ranked` for no DTs. (alias: 98!gen)", inline = False)
    emb.add_field(name = "98!help", value = "Shows commands.", inline = False)
    await ctx.send(embed=emb)
                        
nine.run(os.environ["BOT_TOKEN"])
