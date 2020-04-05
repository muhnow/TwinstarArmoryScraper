class ValidationService:
    # Move these messages to a validation messages constant file at some point 
    MissingProfession = "Missing professions : " 
    GatheringProfession = "Gathering professions : "

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
        