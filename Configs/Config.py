# Key -> Item Slot Number according to WoW
# Value -> Column index in the google sheet
slotColumnDict = {
	#Helmet
	0:4,
	#Neck
	1:5,
	#Shoulder
	2:6,
	#Chest
	4:7,
	#Bracers
	8:8,
	#Legs
	6:9,
	#Boots
	7:10,
	#Belt
	5:11,
	#Gloves
	9:12,
	#Ring 1
	10:13,
	#Ring 2
	11:14,
	#Trinket 1
	12:15,
	#Trinket 2
	13:16,
	#Cape
	14:17,
	#Main hand
	15:18,
	#Off hand
	16:19,
	#Thrown / Relic
	17:20
}

# Players list that is used for HTTP Requests towards the Twinstar Armory URL
# Adding / removing players from this list is how you modify who appears on the spreadsheet output 
players = ['Avery', 'Bagelsdk', 'Xenophics', 'Jizzlin', 'Eyeconic', 'Freedom', 'Aarellia', 'Manao', 'Momentine', 'Ambition']

# Base armory URL
armoryLinkWithoutName = "http://armory.twinstar.cz/character-sheet.xml?r=Apollo2&cn="

# Slot numbers determined by blizzard that we are chosing to ignore 
# 3 is shirt, 18 is tabard, we don't care about those
slotsToIgnore = [3, 18]
