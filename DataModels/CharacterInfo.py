import math

class CharacterInfo:
    def __init__(self, name, items, activeSpec, professions):
        self.Name = name
        self.Items = items
        self.ActiveSpec = activeSpec
        self.Profession1 = professions[0] if len(professions) > 0 else None
        self.Profession2 = professions[1] if len(professions) > 1 else None
        self.ValidationMessages = []
    
    def getAverageItemLevel(self):
        itemIlvls = [item.Ilvl for item in self.Items]

        return math.floor(sum(itemIlvls) / len(itemIlvls))
    
