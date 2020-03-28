import Config
from ExcelService import ExcelService
from CharacterInfo import CharacterInfo
import requests
from lxml import html

class CharacterService:
    def __init__(self):
        self.ExcelService = ExcelService()
        self.CharacterInfoList = []

    def getCharacterInfo(self, characterName):
        print("Processing " + characterName + "...")

        url = Config.armoryLinkWithoutName + characterName

        response = requests.get(url)

        if(response.status_code == 200):
            pageTree = html.fromstring(response.content)
            self.parseCharacterData(characterName, pageTree)
        else:
            print('Error parsing ' + characterName + '.')

    def parseCharacterData(self, characterName, pageTree):
        itemNames = pageTree.xpath('//item[@name]/@name')
        itemIlvls = pageTree.xpath('//item[@level]/@level')
        enchants = pageTree.xpath('//item[@permanentenchant]/@permanentenchant')
        slots = pageTree.xpath('//item[@slot]/@slot')

        characterInfo = CharacterInfo(characterName, itemNames, itemIlvls, enchants, slots)

        self.CharacterInfoList.append(characterInfo)

        print("Retrieved data for " + characterName	+ "!")

    def processPlayers(self):
        for player in Config.players:
            self.getCharacterInfo(player)
        
        print("-----------------------------------")


