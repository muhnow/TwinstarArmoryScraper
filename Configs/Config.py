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
players = ['Avery', 'Bagelsdk', 'Muhnow', 'Jizzlin', 'Eyeconic', 'Freedom', 'Aarellia', 'Manao', 'Momentine', 'Ambition']

# Slot numbers determined by blizzard that we are chosing to ignore when gathering character gear slots
# 3 is shirt, 18 is tabard, we don't care about those
slotsToIgnore = [3, 18]

# Slot numbers determined by blizzard we are looking for when doing enchant validation
slotsWithoutEnchants = [1, 5, 10, 11, 12, 13, 17]

# Slot numbers determined by blizzard for ring 1 and ring 2. We'll check these to see if an enchanter is 
# enchanting their rings or not
ringSlots = [10, 11]

# At the top of the sheet there is a table header row, and the indexing of excel rows starts at 0.
# So you get +2 as an offset to find a row in the actual data set.
headerRowOffset = 2

# You set this value equal to the number of columns you're displaying in the top row. 
totalColumns = 21