class ItemInfo:
    def __init__(self, itemName, itemIlvl, itemSlot, itemEnchant):
        self.Name = itemName
        self.Slot = itemSlot
        self.Enchant = itemEnchant
        self.Ilvl = itemIlvl
    
    def getItemDisplayString(self):
        return self.Name + " (" + str(self.Ilvl) + ")"