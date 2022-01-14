import csv
import json
with open('municipios.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	geo_locations = []
	name = "Venezuelan Expats in Colombian Regions"
	count = 0
	codes = []
	for row in spamreader:
		if row[1] != 'MUNICIPIO':
			if row[3] not in codes:
				codes.append(row[3])
				geo_locations.append({"name":"regions", "values": [{"key":row[3]}],"location_types": ["home"]})
				pass
	genders = [0]
	ages_ranges = [{"min":13, "max":65}]
	behavior = [{"or": [6026404871583],"name": "Expats(Venezuela)"}]
	query = {"name" : name, "geo_locations":geo_locations, "genders": genders, "ages_ranges":ages_ranges, "behavior":behavior}
	filename = "colombian_regions_expats.json"
	query_json = json.dumps(query)

	with open(filename, 'w') as file:
		file.write(query_json)