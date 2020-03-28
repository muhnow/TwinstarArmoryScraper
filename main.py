from CharacterService import CharacterService
from ExcelService import ExcelService


def main():
    characterService = CharacterService()
    excelService = ExcelService()

    excelService.deleteData()

    characterService.processPlayers()

    excelService.uploadData(characterService.CharacterInfoList)


main()

