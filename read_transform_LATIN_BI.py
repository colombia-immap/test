import csv

with open('../../power bi data/FB_AU_Latinamerica.csv', 'r') as csvfile_1:
    new_rows=[]
    data = csv.reader(csvfile_1, delimiter=',', quotechar='|')
    count = 0
    for a in data:
        new_a = a
        if a[0] == 'pais':
            new_a.extend(['mau_audience_dec31_21', 'dau_audience_dec31_21', 'indicador_presion_dec31_21'])
            new_rows.append(new_a)
        if a[0] == '#country+name':
            new_a.extend(['inneed+migrants+monthly','inneed+migrants+daily', 'indicator'])
            new_rows.append(new_a)
        population = a[1]
        if a[0] == '':
            m = 0
            d = 0

            index = round((int(m)*100000)/int(population))

            to_append = [m,d,index]
            new_a.extend(to_append)
            new_rows.append(new_a)

            count = count + 1
            print(a[0],m,d, count)
        else:        
            with open('../dataLAT_expats/dataframe_collected_finished_latin_dec31.csv', 'r') as csvfile_2:
                collected = csv.reader(csvfile_2, delimiter=',', quotechar='|')

                for b in collected:
                    if b[11] != 'geo_locations':
                        chunk = b[26]
                        tojson = chunk.split("'")
                        if a[0] != 'pais' and a[0] != '#country+name':
                            if a[2] == tojson[3]:
                                d = b[42]
                                ml = b[44]
                                mu = b[45]
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

with open('../../power bi data/FB_AU_Latinamerica.csv', 'w',newline='') as f:
    #Overwrite the old file with the modified rows
    writer = csv.writer(f)
    writer.writerows(new_rows)
f.close()