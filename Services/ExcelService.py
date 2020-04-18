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
		nextCharacterRow = 2
		nextErrorMessageRow = 17 

		for info in charInfoList:
			nextCharacterRow = self.queueCharacterInfo(info, nextCharacterRow)
			nextErrorMessageRow = self.queueErrorMessages(info, nextErrorMessageRow)

		self.batchUpload()

	def queueCharacterInfo(self, characterInfo: CharacterInfo, currentRow):
		charRow = [''] * Config.totalColumns

		charRow[0] = characterInfo.Name
		charRow[1] = characterInfo.getAverageItemLevel()
		charRow[2] = characterInfo.ActiveSpec
		charRow[3] = len(characterInfo.ValidationMessages)

		for item in characterInfo.Items:
			sheetCol = Config.slotColumnDict[item.Slot]
			charRow[sheetCol] = item.getItemDisplayString()

		rowToUpload = {
			'range': "A" + str(currentRow) + ":U" + str(currentRow),
			'values': [charRow]
		}

		self.rowsToUpload.append(rowToUpload)

		return currentRow + 1

	def queueErrorMessages(self, characterInfo: CharacterInfo, currentRow):
		msgCount = len(characterInfo.ValidationMessages)
		endRow = (currentRow + (msgCount - 1)) if msgCount > 0 else currentRow
		rangeToUpdate = "A" + str(currentRow) + ":B" + str(endRow)
		values = []

		rowValue = [characterInfo.Name]

		if (msgCount == 0):
			rowValue.append('Clear')

			values.append(rowValue)
			currentRow += 1
		else:
			rowValue.append(characterInfo.ValidationMessages[0])
			values.append(rowValue)

			currentRow += 1

			for message in characterInfo.ValidationMessages[1:]:
				rowValue = []

				rowValue.append(' ')
				rowValue.append(message)

				currentRow += 1

				values.append(rowValue)
			
		rowToUpload = {
			'range': rangeToUpdate,
			'values': values
		}

		self.rowsToUpload.append(rowToUpload)

		return currentRow

	def batchUpload(self):
		print("Uploading data...")
		sheet.batch_update(self.rowsToUpload)
		print("Data upload complete!")

	def deleteData(self):
		self.deleteCharacterData()
		self.deleteErrorData()

	def deleteCharacterData(self):
		outerBound = 2 + len(Config.players)
		cellRange = 'A2:U' + str(outerBound)

		cellsToDelete = sheet.range(cellRange)

		for cell in cellsToDelete:
			cell.value = ''
		
		sheet.update_cells(cellsToDelete)
	
	def deleteErrorData(self):
		startingRow = 17
		endingRow = 100

		cellRange = "A" + str(startingRow) + ":B" + str(endingRow)

		cellsToDelete = sheet.range(cellRange)

		for cell in cellsToDelete:
			cell.value = ''
		
		sheet.update_cells(cellsToDelete)
		