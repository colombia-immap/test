import csv

with open('FB_AU_Colombian_Cities_gender.csv', 'rb') as csvfile_1:
	new_rows=[]
	data = csv.reader(csvfile_1, delimiter=',', quotechar='|')
	count = 0
	for a in data:
		new_a = a
		if a[0] == 'DEPARTAMENTO':
			new_a.extend(['mau_hombres_jun15', 'dau_hombres_jun15', 'mau_mujeres_jun15', 'dau_mujeres_jun15']) 
			new_rows.append(new_a)
		if a[0] == '#adm1+name':
			new_a.extend(['inneed+label', 'inneed+label', 'inneed+label', 'inneed+label']) 
			new_rows.append(new_a)
 		population = a[6]
		if a[3] == '':
			h = 0
			m = 0
			to_append = [h,0,m,0]
			new_a.extend(to_append)
			new_rows.append(new_a)

			# count = count + 1
			# print a[0],a[1],h,m, count
		else:		
			with open('dataCOL_gender_age_expats/dataframe_collected_finished_cities_gender_expats_jan31.csv', 'rb') as csvfile_2:
				collected = csv.reader(csvfile_2, delimiter=',', quotechar='|')
				h = m = 'a'
				for b in collected:
					if b[10] != 'geo_locations':
						chunk = b[12]
						tojson = chunk.split("'")
						if a[0] != 'DEPARTAMENTO' and a[0] != '#adm1+name':
							if a[3] == tojson[5]:
								dau = b[42]
								if b[5] == '1.0':
									h = b[43]
									hd = b[42]									
									if dau == '0':
										h = 0
																		
								if b[5] == '2.0':
									m = b[43]
									md = b[42]
									if dau == '0':
										m = 0

								if h != 'a' and m != 'a':
									to_append = [h,hd,m,md]
									new_a.extend(to_append)
									new_rows.append(new_a)

								#count = count + 1
								#print a[0],a[1], count
								pass
csvfile_1.close()

with open('FB_AU_Colombian_Cities_gender.csv', 'wb') as f:
    #Overwrite the old file with the modified rows
    writer = csv.writer(f)
    writer.writerows(new_rows)

