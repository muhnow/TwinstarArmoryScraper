import gspread
import Configs.Config as Config
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
			self.queueRowsToUpload(info)
		
		self.batchUpload()

	def queueRowsToUpload(self, characterInfo: CharacterInfo):
		charRow = [''] * Config.totalColumns

		charRow[0] = characterInfo.Name
		charRow[1] = characterInfo.getAverageItemLevel()
		charRow[2] = characterInfo.ActiveSpec
		charRow[3] = len(characterInfo.ValidationMessages)

		for item in characterInfo.Items:
			sheetCol = Config.slotColumnDict[item.Slot]
			charRow[sheetCol] = item.getItemDisplayString()

		rowToUpload = {
			'range': self.getCharacterRangeToUpdate(characterInfo.Name),
			'values': [charRow]
		}

		self.rowsToUpload.append(rowToUpload)

	def getCharacterRangeToUpdate(self, characterName):
		characterRowIndex = Config.players.index(characterName) + Config.headerRowOffset

		return "A" + str(characterRowIndex) + ":U" + str(characterRowIndex)

	def batchUpload(self):
		print("Uploading data...")
		sheet.batch_update(self.rowsToUpload)
		print("Data upload complete!")

	def deleteData(self):
		outerBound = 2 + len(Config.players)
		cellRange = 'A2:U' + str(outerBound)

		cellsToDelete = sheet.range(cellRange)

		for cell in cellsToDelete:
			cell.value = ''
		
		sheet.update_cells(cellsToDelete)
