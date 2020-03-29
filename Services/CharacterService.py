from Configs.Config import *
from DataModels.CharacterInfo import CharacterInfo
import requests
import click
from lxml import html

class CharacterService:
    def __init__(self):
        self.CharacterInfoList = []

    def getCharacterInfo(self, characterName):
        url = armoryLinkWithoutName + characterName

        response = requests.get(url)

        if(response.status_code == 200):
            pageTree = html.fromstring(response.content)
            self.parseCharacterData(characterName, pageTree)
        else:
            return

    def parseCharacterData(self, characterName, pageTree):
        itemNames = pageTree.xpath('//item[@name]/@name')
        itemIlvls = pageTree.xpath('//item[@level]/@level')
        enchants = pageTree.xpath('//item[@permanentenchant]/@permanentenchant')
        slots = pageTree.xpath('//item[@slot]/@slot')

        characterInfo = CharacterInfo(characterName, itemNames, itemIlvls, enchants, slots)

        self.CharacterInfoList.append(characterInfo)

    def processPlayers(self):
        with click.progressbar(players, label="Retrieving character data...", item_show_func=self.progressItemLabel) as bar:
            for player in bar:
                self.getCharacterInfo(player)
        
        print("-----------------------------------")


    def progressItemLabel(self, b):
        return b