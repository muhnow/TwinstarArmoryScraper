import requests
from lxml import etree

class HttpService:
    characterSheetUrl = "http://armory.twinstar.cz/character-sheet.xml?r=Apollo2&cn="

    def __init__(self):
        return
    
    def getCharacterSheet(self, characterName):
        url = self.characterSheetUrl + characterName

        response = requests.get(url)

        if (response.status_code != 200):
            return None
        
        pageTree = etree.XML(response.content)

        return pageTree

