from enum import Enum


class Expansions(Enum):
    """Accepted Expansions."""

    core = 1
    dc = 2
    gotg = 3


class MarvelClasses(Enum):
    """The marvel classes."""

    covert = 1
    instinct = 2
    ranged = 3
    strength = 4
    tech = 5


class MarvelGroups(Enum):
    """The Marvel groups."""

    # Core
    avengers = 11
    shield = 12
    solo = 13
    spider_friends = 14
    xmen = 15
    # Dark City
    mk = 21
    xforce = 22
    # Gotg
    gotg = 31


PLAYER_AMOUNT = ["1", "2", "3", "4", "5"]

DIFFICULTIES = ["Normal", "Heroic", "Champion", "Legendary"]

MASTERMIND_DIFFICULTIES = [
    "Distracted",
    "Normal",
    "Maniacal",
    "Enraged",
    "Tyrant",
    "Nightmare",
    "All-Powerful"]

MASTERMINDS = {
    Expansions.core: ["Dr. Doom", "Loki", "Magneto", "Red Skull"],
    Expansions.dc: ["Apocalypse", "Kingpin", "Mephisto",
                    "Mr. Sinister", "Stryfe"],
    Expansions.gotg: ["Supreme Intelligence of the Kree", "Thanos"]
}

SCHEMES = {
    Expansions.core: [
        "The Legacy Virus",
        "Midtown Bank Robbery",
        "Negative Zone Prison Breakout",
        "Portals to the Dark Dimension",
        "Replace Earth's Leaders With Killbots",
        "Secret Invasion of the Skrull Shapeshifters",
        "Super Hero Civil War",
        "Unleash the Power of the Cosmic Cube"],
    Expansions.dc: [
        "Capture Baby Hope",
        "Detonate the Helicarrier",
        "Massive Earthquake Generator",
        "Organized Crime Wave",
        "Save Humanity",
        "Steal the Weaponized Plutonium",
        "Transform Citizens into Demons",
        "X-Cutioner's Song"],
    Expansions.gotg: [
        "Unite the Shards",
        "Forge the Infinity Gauntlet",
        "Intergalactic Kree Nega-Bomb",
        "The Kree-Skrull War"]
}

HEROES = {
    Expansions.core: [
        {"Name": "Captain America",
         "Group": MarvelGroups.avengers,
         "Classes": [MarvelClasses.covert,
                     MarvelClasses.instinct,
                     MarvelClasses.strength,
                     MarvelClasses.tech]},
        {"Name": "Spider-Man",
         "Group": MarvelGroups.spider_friends,
         "Classes": [MarvelClasses.covert,
                     MarvelClasses.instinct,
                     MarvelClasses.strength,
                     MarvelClasses.tech]},
        {"Name": "Iron Man",
         "Group": MarvelGroups.avengers,
         "Classes": [MarvelClasses.ranged,
                     MarvelClasses.tech]},
        {"Name": "Thor",
         "Group": MarvelGroups.avengers,
         "Classes": [MarvelClasses.ranged,
                     MarvelClasses.strength]},
        {"Name": "Rogue",
         "Group": MarvelGroups.xmen,
         "Classes": [MarvelClasses.covert,
                     MarvelClasses.strength]},
        {"Name": "Wolverine",
         "Group": MarvelGroups.xmen,
         "Classes": [MarvelClasses.instinct]},
        {"Name": "Cyclops",
         "Group": MarvelGroups.xmen,
         "Classes": [MarvelClasses.ranged,
                     MarvelClasses.strength]},
        {"Name": "Storm",
         "Group": MarvelGroups.xmen,
         "Classes": [MarvelClasses.covert,
                     MarvelClasses.ranged]},
        {"Name": "Nick Fury",
         "Group": MarvelGroups.shield,
         "Classes": [MarvelClasses.covert,
                     MarvelClasses.strength,
                     MarvelClasses.tech]},
        {"Name": "Hawkeye",
         "Group": MarvelGroups.avengers,
         "Classes": [MarvelClasses.instinct,
                     MarvelClasses.tech]},
        {"Name": "Black Widow",
         "Group": MarvelGroups.avengers,
         "Classes": [MarvelClasses.covert,
                     MarvelClasses.tech]},
        {"Name": "Emma Frost",
         "Group": MarvelGroups.xmen,
         "Classes": [MarvelClasses.covert,
                     MarvelClasses.instinct,
                     MarvelClasses.ranged,
                     MarvelClasses.strength]},
        {"Name": "Hulk",
         "Group": MarvelGroups.avengers,
         "Classes": [MarvelClasses.instinct,
                     MarvelClasses.strength]},
        {"Name": "Gambit",
         "Group": MarvelGroups.xmen,
         "Classes": [MarvelClasses.covert,
                     MarvelClasses.instinct,
                     MarvelClasses.ranged]},
        {"Name": "Deadpool",
         "Group": MarvelGroups.solo,
         "Classes": [MarvelClasses.covert,
                     MarvelClasses.instinct,
                     MarvelClasses.tech]}]
}
