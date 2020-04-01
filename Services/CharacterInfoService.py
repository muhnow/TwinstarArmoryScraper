import click
import requests
import Configs.Config as Config
from DataModels.CharacterInfo import CharacterInfo
from lxml import etree


class CharacterInfoService:
    def __init__(self):
        self.CharacterInfoList = []

    def getCharacterInfo(self, characterName):
        url = Config.armoryLinkWithoutName + characterName

        response = requests.get(url)

        if(response.status_code != 200):
            return

        pageTree = etree.XML(response.content)
        
        self.parseCharacterData(characterName, pageTree)

    def parseCharacterData(self, characterName, pageTree):
        itemNames = pageTree.xpath('//item[@name]/@name')
        itemIlvls = [int(num) for num in pageTree.xpath('//item[@level]/@level') if int(num) > 100]
        enchants = pageTree.xpath('//item[@permanentenchant]/@permanentenchant')
        slots = [int(slot) for slot in pageTree.xpath('//item[@slot]/@slot')]

        activeSpec = self.getActiveSpec(pageTree)

        characterInfo = CharacterInfo(characterName, itemNames, itemIlvls, enchants, slots, activeSpec)

        self.CharacterInfoList.append(characterInfo)

    def processPlayers(self):
        with click.progressbar(Config.players, label="Retrieving character data...", item_show_func=self.progressItemLabel) as bar:
            for player in bar:
                self.getCharacterInfo(player)
        
        print("-----------------------------------")

    def getActiveSpec(self, pageTree):
        talentSpecParent = pageTree.find("characterInfo").find("characterTab").find("talentSpecs").getchildren()

        activeSpec = [child.get("prim") for child in talentSpecParent if child.get("active") == '1' ][0]

        return activeSpec

    def progressItemLabel(self, b):
        return b
