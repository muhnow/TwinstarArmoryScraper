import gspread
import Config
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Apollo Character Data").sheet1

class ExcelService():


	def __init__(self):
		self.rowsToUpload = []

	def queueData(self, characterInfo, characterName):
		tableHeaderRowOffset = 2
		totalSlots = 18

		charRow = [''] * totalSlots
		charIndex = Config.players.index(characterName)
		charRowIndex = charIndex + tableHeaderRowOffset
		rangeToUpdate = "A" + str(charRowIndex) + ":R" + str(charRowIndex)

		items = characterInfo[0]
		slots = characterInfo[3]

		charRow[0] = characterName

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

		# sheet.insert_row(charRow, charRowIndex)


		print("Finished uploading data for " + characterName + "!")
		print("---------------------------------------------------")


	def batchUpload(self):
		sheet.batch_update(self.rowsToUpload)

	def deleteData(self):
		outerBound = 2 + len(Config.players)
		cellRange = 'A2:R' + str(outerBound)

		cellsToDelete = sheet.range(cellRange)

		for cell in cellsToDelete:
			cell.value = ''

		sheet.update_cells(cellsToDelete)