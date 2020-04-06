import click
import requests
import Configs.Config as Config
from DataModels.CharacterInfo import CharacterInfo
from DataModels.ItemInfo import ItemInfo
from Services.HttpService import HttpService
from lxml import etree

class CharacterInfoService:
    def __init__(self):
        self.HttpService = HttpService()
        self.CharacterInfoList = []

    def processPlayers(self):
        with click.progressbar(Config.players, label="Retrieving character data...", item_show_func=self.progressItemLabel) as bar:
            for player in bar:
                self.getCharacterInfo(player)
        
        print("-----------------------------------")

    def getCharacterInfo(self, characterName):
        characterPageTree = self.HttpService.getCharacterSheet(characterName) 
        
        self.parseCharacterSheet(characterName, characterPageTree)

    def parseCharacterSheet(self, characterName, pageTree):
        characterTabGroup = pageTree.find("characterInfo").find("characterTab")

        items = self.getItems(characterTabGroup)
        activeSpec = self.getActiveSpec(characterTabGroup)
        professions = self.getProfessions(characterTabGroup)

        characterInfo = CharacterInfo(characterName, items, activeSpec, professions)

        self.CharacterInfoList.append(characterInfo)

    def getActiveSpec(self, characterTabGroup):
        talentSpecTags = characterTabGroup.find("talentSpecs").getchildren()

        activeSpec = [child.get("prim") for child in talentSpecTags if child.get("active") == '1' ][0]

        return activeSpec
    
    def getProfessions(self, characterTabGroup):
        professionTags = characterTabGroup.find("professions").getchildren()

        professions = [child.get("name") for child in professionTags]

        return professions

    def getItems(self, characterTabGroup):
        items = []
        itemTags = characterTabGroup.find("items").getchildren()

        for itemTag in itemTags:
            name = itemTag.get("name")
            ilvl = int(itemTag.get("level"))
            enchant = itemTag.get("permanentenchant")
            slot = int(itemTag.get("slot"))

            if (slot not in Config.slotsToIgnore):
                itemInfo = ItemInfo(name, ilvl, slot, enchant)
                
                items.append(itemInfo)

        return items

    def progressItemLabel(self, b):
        return b
