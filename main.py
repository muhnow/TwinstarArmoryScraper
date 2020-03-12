from lxml import html
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Apollo Character Data").sheet1

# Key -> Item Slot Number according to WoW
# Value -> Column index in the google sheet
slotColumnDict = {
	#Helmet
	0:1,
	#Neck
	1:2,
	#Shoulder
	2:3,
	#Chest
	4:4,
	#Bracers
	8:5,
	#Legs
	6:6,
	#Boots
	7:7,
	#Belt
	5:8,
	#Gloves
	9:9,
	#Ring 1
	10:10,
	#Ring 2
	11:11,
	#Trinket 1
	12:12,
	#Trinket 2
	13:13,
	#Cape
	14:14,
	#Main hand
	15:15,
	#Off hand
	16:16,
	#Thrown / Relic
	17:17
}

#sheet.update_cell(2, 1, "This is from my local python script!")

players = ['Avery', 'Bagelsdk', 'Xenophics', 'Jizzlin', 'Eyeconic', 'Freedom', 'Aarellia', 'Preyeet', 'Manao', 'Momentine', 'Ambition'];
armoryLinkWithoutName = "http://armory.twinstar.cz/character-sheet.xml?r=Apollo2&cn="
slotsToIgnore = [3, 18]

def makeRequest(characterName):
	print("Processing " + characterName + "...")

	url = armoryLinkWithoutName + characterName;

	response = requests.get(url);

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

	uploadToGoogle(characterInfo, characterName)


def uploadToGoogle(characterInfo, characterName):
	tableHeaderRowOffset = 2
	sheetColOffset = 2
	totalSlots = 18

	charRow = [''] * totalSlots
	charRow[0] = characterName
	charIndex = players.index(characterName)
	charRowIndex = charIndex + tableHeaderRowOffset
	items = characterInfo[0]
	slots = characterInfo[3]

	for index,item in enumerate(items):
		itemSlot = int(slots[index])

		if(itemSlot not in slotsToIgnore):
			sheetCol = slotColumnDict[itemSlot]
			
			charRow[sheetCol] = item


	print(charRow)
	sheet.insert_row(charRow, charRowIndex)


	print("Finished uploading data for " + characterName + "!")
	print("---------------------------------------------------")



def deleteData():
	for i in range(0, 10):
		sheet.delete_row(2)


def processPlayers():
	deleteData()

	for player in players:
		makeRequest(player)


processPlayers();




