import gspread
import Config
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Apollo Character Data").sheet1

def uploadToGoogle(characterInfo, characterName):
	tableHeaderRowOffset = 2
	sheetColOffset = 2
	totalSlots = 18

	charRow = [''] * totalSlots
	charRow[0] = characterName
	charIndex = Config.players.index(characterName)
	charRowIndex = charIndex + tableHeaderRowOffset
	items = characterInfo[0]
	slots = characterInfo[3]

	for index,item in enumerate(items):
		itemSlot = int(slots[index])

		if(itemSlot not in Config.slotsToIgnore):
			sheetCol = Config.slotColumnDict[itemSlot]
			
			charRow[sheetCol] = item

	sheet.insert_row(charRow, charRowIndex)


	print("Finished uploading data for " + characterName + "!")
	print("---------------------------------------------------")



def deleteData():
	for i in range(0, 10):
		sheet.delete_row(2)