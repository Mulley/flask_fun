from enum import Enum


class Expansions(Enum):
    """Accepted Expansions."""

    core = "Core"
    dc = "Dark City"
    gotg = "Guardians of the Galaxy"


class MarvelClasses(Enum):
    """The marvel classes."""

    covert = "Covert"
    instinct = "Instinct"
    ranged = "Ranged"
    strength = "Strength"
    tech = "Tech"


class MarvelGroups(Enum):
    """The Marvel groups."""

    # Core
    avengers = "Avengers"
    shield = "S.H.I.E.L.D."
    solo = "None"
    spider_friends = "Spider Friends"
    xmen = "X-MEN"
    # Dark City
    mk = "Marvel Knights"
    xforce = "X-Force"
    # Gotg
    gotg = "Guardians of the Galaxy"


PLAYER_AMOUNT = [1, 2, 3, 4, 5]

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
    Expansions.core.name: [
        {"Name": "Dr. Doom", "Leads": "Doombot Legion"},
        {"Name": "Loki", "Leads": "Enemies of Asgard"},
        {"Name": "Magneto", "Leads": "Brotherhood"},
        {"Name": "Red Skull", "Leads": "HYDRA"}
    ],
    Expansions.dc.name: [
        {"Name": "Apocalypse", "Leads": "Four Horsemen"},
        {"Name": "Kingpin", "Leads": "Streets of New York"},
        {"Name": "Mephisto", "Leads": "Underworld"},
        {"Name": "Mr. Sinister", "Leads": "Marauders"},
        {"Name": "Stryfe", "Leads": "MLF"}
    ],
    Expansions.gotg.name: [
        {"Name": "Supreme Intelligence of the Kree",
         "Leads": "Kree Starforce"},
        {"Name": "Thanos", "Leads": "Infinity Gems"}
    ]
}

SCHEMES = {
    Expansions.core.name: [
        "The Legacy Virus",
        "Midtown Bank Robbery",
        "Negative Zone Prison Breakout",
        "Portals to the Dark Dimension",
        "Replace Earth's Leaders With Killbots",
        "Secret Invasion of the Skrull Shapeshifters",
        "Super Hero Civil War",
        "Unleash the Power of the Cosmic Cube"],
    Expansions.dc.name: [
        "Capture Baby Hope",
        "Detonate the Helicarrier",
        "Massive Earthquake Generator",
        "Organized Crime Wave",
        "Save Humanity",
        "Steal the Weaponized Plutonium",
        "Transform Citizens into Demons",
        "X-Cutioner's Song"],
    Expansions.gotg.name: [
        "Unite the Shards",
        "Forge the Infinity Gauntlet",
        "Intergalactic Kree Nega-Bomb",
        "The Kree-Skrull War"]
}

HEROES = {
    Expansions.core.name: [
        {"Name": "Captain America",
         "Group": MarvelGroups.avengers.value,
         "Classes": [MarvelClasses.covert.value,
                     MarvelClasses.instinct.value,
                     MarvelClasses.strength.value,
                     MarvelClasses.tech.value]},
        {"Name": "Spider-Man",
         "Group": MarvelGroups.spider_friends.value,
         "Classes": [MarvelClasses.covert.value,
                     MarvelClasses.instinct.value,
                     MarvelClasses.strength.value,
                     MarvelClasses.tech.value]},
        {"Name": "Iron Man",
         "Group": MarvelGroups.avengers.value,
         "Classes": [MarvelClasses.ranged.value,
                     MarvelClasses.tech.value]},
        {"Name": "Thor",
         "Group": MarvelGroups.avengers.value,
         "Classes": [MarvelClasses.ranged.value,
                     MarvelClasses.strength.value]},
        {"Name": "Rogue",
         "Group": MarvelGroups.xmen.value,
         "Classes": [MarvelClasses.covert.value,
                     MarvelClasses.strength.value]},
        {"Name": "Wolverine",
         "Group": MarvelGroups.xmen.value,
         "Classes": [MarvelClasses.instinct.value]},
        {"Name": "Cyclops",
         "Group": MarvelGroups.xmen.value,
         "Classes": [MarvelClasses.ranged.value,
                     MarvelClasses.strength.value]},
        {"Name": "Storm",
         "Group": MarvelGroups.xmen.value,
         "Classes": [MarvelClasses.covert.value,
                     MarvelClasses.ranged.value]},
        {"Name": "Nick Fury",
         "Group": MarvelGroups.shield.value,
         "Classes": [MarvelClasses.covert.value,
                     MarvelClasses.strength.value,
                     MarvelClasses.tech.value]},
        {"Name": "Hawkeye",
         "Group": MarvelGroups.avengers.value,
         "Classes": [MarvelClasses.instinct.value,
                     MarvelClasses.tech.value]},
        {"Name": "Black Widow",
         "Group": MarvelGroups.avengers.value,
         "Classes": [MarvelClasses.covert.value,
                     MarvelClasses.tech.value]},
        {"Name": "Emma Frost",
         "Group": MarvelGroups.xmen.value,
         "Classes": [MarvelClasses.covert.value,
                     MarvelClasses.instinct.value,
                     MarvelClasses.ranged.value,
                     MarvelClasses.strength.value]},
        {"Name": "Hulk",
         "Group": MarvelGroups.avengers.value,
         "Classes": [MarvelClasses.instinct.value,
                     MarvelClasses.strength.value]},
        {"Name": "Gambit",
         "Group": MarvelGroups.xmen.value,
         "Classes": [MarvelClasses.covert.value,
                     MarvelClasses.instinct.value,
                     MarvelClasses.ranged.value]},
        {"Name": "Deadpool",
         "Group": MarvelGroups.solo.value,
         "Classes": [MarvelClasses.covert.value,
                     MarvelClasses.instinct.value,
                     MarvelClasses.tech.value]}],
    Expansions.dc.name: [
        {"Name": "Punisher",
         "Group": MarvelGroups.mk.value,
         "Classes": [MarvelClasses.strength.value,
                     MarvelClasses.tech.value]},
        {"Name": "Daredevil",
         "Group": MarvelGroups.mk.value,
         "Classes": [MarvelClasses.covert.value,
                     MarvelClasses.instinct.value,
                     MarvelClasses.strength.value]},
        {"Name": "Elektra",
         "Group": MarvelGroups.mk.value,
         "Classes": [MarvelClasses.covert.value,
                     MarvelClasses.instinct.value]},
        {"Name": "Nightcrawler",
         "Group": MarvelGroups.xmen.value,
         "Classes": [MarvelClasses.covert.value,
                     MarvelClasses.instinct.value]},
        {"Name": "Colossus",
         "Group": MarvelGroups.xforce.value,
         "Classes": [MarvelClasses.covert.value,
                     MarvelClasses.strength.value]},
        {"Name": "Ghost Rider",
         "Group": MarvelGroups.mk.value,
         "Classes": [MarvelClasses.ranged.value,
                     MarvelClasses.strength.value,
                     MarvelClasses.tech.value]},
        {"Name": "Jean Grey",
         "Group": MarvelGroups.xmen.value,
         "Classes": [MarvelClasses.covert.value,
                     MarvelClasses.ranged.value]},
        {"Name": "Angel",
         "Group": MarvelGroups.xmen.value,
         "Classes": [MarvelClasses.covert.value,
                     MarvelClasses.instinct.value,
                     MarvelClasses.strength.value]},
        {"Name": "Forge",
         "Group": MarvelGroups.xforce.value,
         "Classes": [MarvelClasses.tech.value]},
        {"Name": "Domino",
         "Group": MarvelGroups.xforce.value,
         "Classes": [MarvelClasses.covert.value,
                     MarvelClasses.instinct.value,
                     MarvelClasses.tech.value]},
        {"Name": "Iron Fist",
         "Group": MarvelGroups.mk.value,
         "Classes": [MarvelClasses.instinct.value,
                     MarvelClasses.strength.value]},
        {"Name": "Bishop",
         "Group": MarvelGroups.xmen.value,
         "Classes": [MarvelClasses.covert.value,
                     MarvelClasses.ranged.value,
                     MarvelClasses.tech.value]},
        {"Name": "Cable",
         "Group": MarvelGroups.xforce.value,
         "Classes": [MarvelClasses.covert.value,
                     MarvelClasses.ranged.value,
                     MarvelClasses.tech.value]},
        {"Name": "Blade",
         "Group": MarvelGroups.mk.value,
         "Classes": [MarvelClasses.covert.value,
                     MarvelClasses.instinct.value,
                     MarvelClasses.strength.value,
                     MarvelClasses.tech.value]},
        {"Name": "Iceman",
         "Group": MarvelGroups.xmen.value,
         "Classes": [MarvelClasses.ranged.value,
                     MarvelClasses.strength.value]},
        {"Name": "Professor X",
         "Group": MarvelGroups.xmen.value,
         "Classes": [MarvelClasses.covert.value,
                     MarvelClasses.instinct.value,
                     MarvelClasses.ranged.value]},
        {"Name": "Wolverine X-Force",
         "Group": MarvelGroups.xforce.value,
         "Classes": [MarvelClasses.covert.value,
                     MarvelClasses.instinct.value,
                     MarvelClasses.strength.value]}],
    Expansions.gotg.name: [
        {"Name": "Drax the Destroyer",
         "Group": MarvelGroups.gotg.value,
         "Classes": [MarvelClasses.instinct.value,
                     MarvelClasses.strength.value]},
        {"Name": "Gamora",
         "Group": MarvelGroups.gotg.value,
         "Classes": [MarvelClasses.covert.value,
                     MarvelClasses.instinct.value]},
        {"Name": "Groot",
         "Group": MarvelGroups.gotg.value,
         "Classes": [MarvelClasses.covert.value,
                     MarvelClasses.strength.value]},
        {"Name": "Rocket Raccoon",
         "Group": MarvelGroups.gotg.value,
         "Classes": [MarvelClasses.instinct.value,
                     MarvelClasses.ranged.value,
                     MarvelClasses.tech.value]},
        {"Name": "Star-Lord",
         "Group": MarvelGroups.gotg.value,
         "Classes": [MarvelClasses.covert.value,
                     MarvelClasses.ranged.value,
                     MarvelClasses.tech.value]}]
}
