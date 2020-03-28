import Config
from ExcelService import ExcelService
import requests
from lxml import html

class CharacterService:
    def __init__(self):
    	self.ExcelService = ExcelService();

    def makeRequest(self, characterName):
    	print("Processing " + characterName + "...")

    	url = Config.armoryLinkWithoutName + characterName

    	response = requests.get(url)

    	if(response.status_code == 200):
    		pageTree = html.fromstring(response.content)
    		self.parseCharacterData(characterName, pageTree)
    	else:
    		print('error parsing ' + characterName)

    def parseCharacterData(self, characterName, pageTree):
    	itemNames = pageTree.xpath('//item[@name]/@name')
    	itemIlvls = pageTree.xpath('//item[@level]/@level')
    	enchants = pageTree.xpath('//item[@permanentenchant]/@permanentenchant')
    	slots = pageTree.xpath('//item[@slot]/@slot')

    	characterInfo = [itemNames, itemIlvls, enchants, slots]

    	print("Retrieved data for " + characterName	+ "! Uploading to sheet...")

    	self.ExcelService.queueData(characterInfo, characterName)

    def processPlayers(self):
    	self.ExcelService.deleteData()

    	for player in Config.players:
            self.makeRequest(player)

        self.ExcelService.batchUpload()

