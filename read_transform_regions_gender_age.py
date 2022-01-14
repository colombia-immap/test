import csv

with open('../FB_AU_Colombian_regions.csv', 'rb') as csvfile_1:
	new_rows=[]
	data = csv.reader(csvfile_1, delimiter=',', quotechar='|')
	count = 0
	for a in data:
		new_a = a[:4]
		if a[0] == 'DEPARTAMENTO':
			new_a.extend(['age_range','mau_hombres_apr29', 'dau_hombres_apr29', 'mau_mujeres_apr29', 'dau_mujeres_apr29']) 
			new_rows.append(new_a)
		if a[0] == '#adm1+name':
			new_a.extend(['#meta+age_range', 'inneed+m+monthly', 'inneed+m+daily', 'inneed+f+monthly', 'inneed+f+daily']) 
			new_rows.append(new_a)

			# count = count + 1
			# print a[0],a[1], count
		else:		
			with open('../dataCOL_gender_age_expats/dataframe_collected_finished_regions_expats_gender_age_apr29.csv', 'rb') as csvfile_2:
				collected = csv.reader(csvfile_2, delimiter=',', quotechar='|')
				h = m = 'a'
				for b in collected:
					if b[10] != 'geo_locations':
						chunk = b[12]
						tojson = chunk.split("'")
						if a[0] != 'DEPARTAMENTO' and a[0] != '#adm1+name':
							if a[2] == tojson[5]:
								chunk_age_min = b[4]
								chunk_age_max = b[3]
								age_min = [int(s) for s in chunk_age_min.split(":")[-1].split('}')[0].split() if s.isdigit()]
								age_max = [int(s) for s in chunk_age_max.split() if s.isdigit()]
								age_range = age_min+age_max
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
									new_a = new_a[:4]
									age_range = "_".join(map(str,age_range))
									to_append = [age_range,h,hd,m,md]
									new_a.extend(to_append)
									new_rows.append(new_a)

								#count = count + 1
								#print a[0],a[1], count
								pass
csvfile_1.close()

with open('../FB_AU_Colombian_regions_gender_age_temp.csv', 'wb') as f:
    #Overwrite the old file with the modified rows
    writer = csv.writer(f)
    writer.writerows(new_rows)
