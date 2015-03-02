with open("2.txt") as f:
	for line in f:
		arr = line.split("\t")
		date = arr[0]
		zip = arr[2]
		text = arr[4]
