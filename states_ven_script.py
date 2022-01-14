import csv
import json
with open('../FB_AU_Ven_states.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	geo_locations = []
	name = "Users in venezuelan states"
	count = 0
	codes = []
	for row in spamreader:
		if row[0] != 'admin1' and row[0] != '#adm1+name':
			if row[2] not in codes:
				codes.append(row[2])
				geo_locations.append({"name":"regions", "values": [{"key":row[2]}],"location_types": ["home", "recent"], "pySocialWatcherReference": row[0]})
				pass
	genders = [0]
	ages_ranges = [{"min":13, "max":65}]
	query = {"name" : name, "geo_locations":geo_locations, "genders": genders, "ages_ranges":ages_ranges}
	filename = "venezuelan_regions_users.json"
	query_json = json.dumps(query)

	with open(filename, 'w') as file:
		file.write(query_json)