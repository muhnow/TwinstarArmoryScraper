# Key -> Item Slot Number according to WoW
# Value -> Column index in the google sheet
slotColumnDict = {
	#Helmet
	0:1,
	#Neck
	1:2,
	#Shoulder
	2:3,
	#Chest
	4:4,
	#Bracers
	8:5,
	#Legs
	6:6,
	#Boots
	7:7,
	#Belt
	5:8,
	#Gloves
	9:9,
	#Ring 1
	10:10,
	#Ring 2
	11:11,
	#Trinket 1
	12:12,
	#Trinket 2
	13:13,
	#Cape
	14:14,
	#Main hand
	15:15,
	#Off hand
	16:16,
	#Thrown / Relic
	17:17
}

# Players list that is used for HTTP Requests towards the Twinstar Armory URL
# Adding / removing players from this list is how you modify who appears on the spreadsheet output 
players = ['Avery', 'Bagelsdk', 'Xenophics', 'Jizzlin', 'Eyeconic', 'Freedom', 'Aarellia', 'Preyeet', 'Manao', 'Momentine', 'Ambition']

# Base armory URL
armoryLinkWithoutName = "http://armory.twinstar.cz/character-sheet.xml?r=Apollo2&cn="

# Slot numbers determined by blizzard that we are chosing to ignore 
# 3 is shirt, 18 is tabard, we don't care about those
slotsToIgnore = [3, 18]
