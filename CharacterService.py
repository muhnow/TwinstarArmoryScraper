import Config
import ExcelService
import requests
from lxml import html


def makeRequest(characterName):
	print("Processing " + characterName + "...")

	url = Config.armoryLinkWithoutName + characterName

	response = requests.get(url)

	if(response.status_code == 200):
		pageTree = html.fromstring(response.content)
		parseCharacterData(characterName, pageTree)
	else:
		print('error parsing ' + characterName)

def parseCharacterData(characterName, pageTree):
	itemNames = pageTree.xpath('//item[@name]/@name')
	itemIlvls = pageTree.xpath('//item[@level]/@level')
	enchants = pageTree.xpath('//item[@permanentenchant]/@permanentenchant')
	slots = pageTree.xpath('//item[@slot]/@slot')

	characterInfo = [itemNames, itemIlvls, enchants, slots]

	print("Retrieved data for " + characterName	+ "! Uploading to sheet...")

	ExcelService.uploadToGoogle(characterInfo, characterName)

def processPlayers():
	ExcelService.deleteData()

	for player in Config.players:
		makeRequest(player)
