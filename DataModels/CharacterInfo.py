import math

class CharacterInfo:
    def __init__(self, name, itemNames, itemIlvls, enchants, slots, activeSpec, professions):
        self.Name = name
        self.ItemNames = itemNames
        self.ItemLevels = itemIlvls
        self.ItemEnchants = enchants
        self.ItemSlots = slots
        self.ActiveSpec = activeSpec
        self.Profession1 = professions[0] if len(professions) > 0 else None
        self.Profession2 = professions[1] if len(professions) > 1 else None
        self.ValidationMessages = []
    
    def getAverageItemLevel(self):
        return math.floor(sum(self.ItemLevels) / len(self.ItemLevels))
    
