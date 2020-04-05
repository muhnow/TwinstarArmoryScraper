import click
import requests
import Configs.Config as Config
from DataModels.CharacterInfo import CharacterInfo
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
        itemNames = pageTree.xpath('//item[@name]/@name')
        itemIlvls = [int(num) for num in pageTree.xpath('//item[@level]/@level') if int(num) > 100]
        enchants = pageTree.xpath('//item[@permanentenchant]/@permanentenchant')
        slots = [int(slot) for slot in pageTree.xpath('//item[@slot]/@slot')]

        activeSpec = self.getActiveSpec(pageTree)
        professions = self.getProfessions(pageTree)

        characterInfo = CharacterInfo(characterName, itemNames, itemIlvls, enchants, slots, activeSpec, professions)

        self.CharacterInfoList.append(characterInfo)

    def getActiveSpec(self, pageTree):
        talentSpecTags = pageTree.find("characterInfo").find("characterTab").find("talentSpecs").getchildren()

        activeSpec = [child.get("prim") for child in talentSpecTags if child.get("active") == '1' ][0]

        return activeSpec
    
    def getProfessions(self, pageTree):
        professionTags = pageTree.find("characterInfo").find("characterTab").find("professions").getchildren()

        professions = [child.get("name") for child in professionTags]

        return professions

    def progressItemLabel(self, b):
        return b
