import math

class CharacterInfo:
    def __init__(self, name, itemNames, itemIlvls, enchants, slots, activeSpec):
        self.Name = name
        self.ItemNames = itemNames
        self.ItemLevels = itemIlvls
        self.ItemEnchants = enchants
        self.ItemSlots = slots
        self.ActiveSpec = activeSpec
    
    def getAverageItemLevel(self):
        return math.floor(sum(self.ItemLevels) / len(self.ItemLevels))
