from Services.CharacterInfoService import CharacterInfoService
from Services.ExcelService import ExcelService


def main():
    characterInfoService = CharacterInfoService()
    excelService = ExcelService()

    excelService.deleteData()

    characterInfoService.processPlayers()

    excelService.uploadData(characterInfoService.CharacterInfoList)

main()
