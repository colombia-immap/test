import csv
import json
with open('FB_AU_Peruvian_Cities.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	geo_locations = []
	name = "Venezuelan Expats in Peruvian Cities"
	count = 0
	for row in spamreader:
		if row[1] != 'MUNICIPIO' and row[3] != "" and row[1] != '#adm2+name':
			geo_locations.append({"name":"cities", "values": [{"key":row[3]}],"location_types": ["home"]})
			pass
	genders = [0]
	ages_ranges = [{"min":13, "max":65}]
	behavior = [{"or": [6026404871583],"name": "Expats(Venezuela)"}]
	query = {"name" : name, "geo_locations":geo_locations, "genders": genders, "ages_ranges":ages_ranges, "behavior":behavior}
	filename = "peruvian_cities_expats.json"
	query_json = json.dumps(query)

	with open(filename, 'w') as file:
		file.write(query_json)