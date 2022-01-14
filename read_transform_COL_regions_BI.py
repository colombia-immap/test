import csv

with open('../../power bi data/FB_AU_Colombian_regions.csv', 'r') as csvfile_1:
    new_rows=[]
    data = csv.reader(csvfile_1, delimiter=',', quotechar='|')
    count = 0
    for a in data:
        new_a = a
        if a[0] == 'DEPARTAMENTO':
            new_a.extend(['mau_audience_dec31_21', 'dau_audience_dec31_21', 'indicador_presion_dec31_21'])
            new_rows.append(new_a)
        if a[0] == '#adm1+name':
            new_a.extend(['inneed+migrants+monthly','inneed+migrants+daily', 'indicator+rate'])
            new_rows.append(new_a)
        population = a[3]#Colombia regions
        if a[2] == '':
            m = 0
            d = 0

            index = round((int(m)*100000)/int(population))

            to_append = [m,d,index]
            new_a.extend(to_append)
            new_rows.append(new_a)

            count = count + 1
            print(a[0],m,d, count)
        else:
            with open('../dataCOL_expats/dataframe_collected_finished_regions_dec31.csv', 'r') as csvfile_2:
                collected = csv.reader(csvfile_2, delimiter=',', quotechar='|')

                for b in collected:
                    if b[11] != 'geo_locations':
                        chunk = b[26]
                        tojson = chunk.split("'")
                        if a[0] != 'DEPARTAMENTO' and a[0] != '#adm1+name':
                            if a[2] == tojson[5]:
                                d = b[44]
                                ml = b[46]
                                mu = b[47]                                
                                if d == '0':
                                    m = 0
                                else:
                                    m=round((int(mu)+int(ml))/2)
                               
                                index = round((int(m)*100000)/int(population))

                                to_append = [m,d,index]
                                new_a.extend(to_append)
                                new_rows.append(new_a)

                                count = count + 1
                                print(a[0],m,d, count)
                                pass
csvfile_1.close()

with open('../../power bi data/FB_AU_Colombian_regions.csv', 'w', newline='') as f:
    #Overwrite the old file with the modified rows
    writer = csv.writer(f)
    writer.writerows(new_rows)
f.close()
