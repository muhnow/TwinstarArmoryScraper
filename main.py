from Services.CharacterInfoService import CharacterInfoService
from Services.ExcelService import ExcelService
from Services.ValidationService import ValidationService


def main():
    characterInfoService = CharacterInfoService()
    excelService = ExcelService()
    validationService = ValidationService()

    excelService.deleteData()

    characterInfoService.processPlayers()

    validationService.validatePlayers(characterInfoService.CharacterInfoList)

    excelService.uploadData(characterInfoService.CharacterInfoList)

main()
