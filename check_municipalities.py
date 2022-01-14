import csv

with open('../FB_AU_Colombian_Cities_v3.csv', 'rb') as csvfile_1:
	new_rows=[]
	data = csv.reader(csvfile_1, delimiter=',', quotechar='|')
	count = 0
	for a in data:
		new_a = a		
		with open('../salud.csv', 'rb') as csvfile_2:
			collected = csv.reader(csvfile_2, delimiter=',', quotechar='|')
			for b in collected:
				if a[0] != 'DEPARTAMENTO' and b[0] != 'Departamento':
					if a[2] == b[5]:
						new_rows.append(a[0:3]);
csvfile_1.close()

with open('../salud.csv', 'wb') as f:
    #Overwrite the old file with the modified rows
    writer = csv.writer(f)
    writer.writerows(new_rows)

