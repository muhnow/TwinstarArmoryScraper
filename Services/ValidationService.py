import Configs.Config as Config

class ValidationService:
    # Move these messages to a validation messages constant file at some point 
    MissingProfession = "Missing professions : " 
    GatheringProfession = "Gathering professions : "
    MissingEnchants = "Missing enchants: " 

    def __init__(self):
        self.ErrorMessages = []
    
    def validatePlayers(self, characterInfoList):
        for char in characterInfoList:
            self.validateCharacter(char)
            

    def validateCharacter(self, characterInfo):
        self.validateProfessions(characterInfo)
        self.validateEnchants(characterInfo)

        characterInfo.ValidationMessages = self.ErrorMessages

        self.ErrorMessages = []

        return 
    
    def validateProfessions(self, characterInfo):
        gatheringProfs = ["Mining", "Skinning", "Herbalism"]
        characterProfs = [characterInfo.Profession1, characterInfo.Profession2]

        # Validate missing professions
        missingProfessionsCount = len([prof for prof in characterProfs if prof == None])

        if (missingProfessionsCount != 0):
            errorMsg = self.MissingProfession + str(missingProfessionsCount)

            self.ErrorMessages.append(errorMsg)

        # Validate gathering professions
        charGatheringProfs = [prof for prof in characterProfs if prof in gatheringProfs]
        
        if (len(charGatheringProfs) != 0):
            errorMsg = self.GatheringProfession

            for prof in charGatheringProfs:
                errorMsg += (prof + " ")
            
            self.ErrorMessages.append(errorMsg)

    def validateEnchants(self, characterInfo):
        characterProfs = [characterInfo.Profession1, characterInfo.Profession2]
        missingEnchantItemSlots = [item.Slot for item in characterInfo.Items if (item.Enchant == "0" and item.Slot not in Config.slotsWithoutEnchants)]

        missingEnchantCount = 0

        # If enchanter, verify rings are enchanted
        if ("Enchanting" in characterProfs):
            missingEnchantCount += len([slot for slot in Config.ringSlots if slot in missingEnchantItemSlots])
        
        # If engineer, ignore glove enchant if we found a missing enchant. Likely a tinker exists on the piece
        # but there isn't a way for me to tell
        if ("Engineering" in characterProfs and 9 in missingEnchantItemSlots):
            missingEnchantItemSlots.remove(9)

        # If tailor, ignore cloak enchant if we found a missing enchant. Likely, an embroidery exists on the piece
        # but there isn't a way for me to tell
        if ("Tailoring" in characterProfs and 14 in missingEnchantItemSlots):
            missingEnchantItemSlots.remove(14)

        missingEnchantCount += len(missingEnchantItemSlots)

        if (missingEnchantCount > 0):
            slotNamesWithMissingEnchants = [Config.slotNameDict[slot] for slot in missingEnchantItemSlots]

            errorMsg = self.MissingEnchants + ', '.join(slotNamesWithMissingEnchants)
            self.ErrorMessages.append(errorMsg)