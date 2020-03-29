import gspread
import Config
from oauth2client.service_account import ServiceAccountCredentials
from DataModels.CharacterInfo import CharacterInfo

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Apollo Character Data").sheet1

class ExcelService():
	def __init__(self):
		self.rowsToUpload = []

	def uploadData(self, charInfoList):
		print("Queueing data...")

		for info in charInfoList:
			self.queueData(info)
		
		self.batchUpload()

	def queueData(self, characterInfo: CharacterInfo):
		tableHeaderRowOffset = 2
		totalSlots = 18

		charRow = [''] * totalSlots
		charIndex = Config.players.index(characterInfo.Name)
		charRowIndex = charIndex + tableHeaderRowOffset
		rangeToUpdate = "A" + str(charRowIndex) + ":R" + str(charRowIndex)

		items = characterInfo.ItemNames
		slots = characterInfo.ItemSlots

		charRow[0] = characterInfo.Name

		for index,item in enumerate(items):
			itemSlot = int(slots[index])

			if(itemSlot not in Config.slotsToIgnore):
				sheetCol = Config.slotColumnDict[itemSlot]
				
				charRow[sheetCol] = item

		rowToUpload = {
			'range': rangeToUpdate,
			'values': [charRow]
		}

		self.rowsToUpload.append(rowToUpload)

	def batchUpload(self):
		print("Uploading data...")
		sheet.batch_update(self.rowsToUpload)
		print("Data upload complete!")

	def deleteData(self):
		outerBound = 2 + len(Config.players)
		cellRange = 'A2:R' + str(outerBound)

		cellsToDelete = sheet.range(cellRange)

		for cell in cellsToDelete:
			cell.value = ''
		
		sheet.update_cells(cellsToDelete)
