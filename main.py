from Services.CharacterService import CharacterService
from Services.ExcelService import ExcelService


def main():
    characterService = CharacterService()
    excelService = ExcelService()

    excelService.deleteData()

    characterService.processPlayers()

    excelService.uploadData(characterService.CharacterInfoList)


main()

