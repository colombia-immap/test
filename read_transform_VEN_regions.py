import csv

with open('../FB_AU_Ven_states.csv', 'r') as csvfile_1:
    new_rows=[]
    data = csv.reader(csvfile_1, delimiter=',', quotechar='|')
    count = 0
    for a in data:
        new_a = a
        if a[0] == 'admin1':
            new_a.extend(['mau_audience_dec31', 'dau_audience_dec31', 'indicador_presion_dec31'])
            new_rows.append(new_a)
        if a[0] == '#adm1+name':
            new_a.extend(['inneed+migrants+monthly','inneed+migrants+daily', 'indicator+rate'])
            new_rows.append(new_a)
        population = a[3] #Venezuelan regions
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
            with open('../dataVEN/dataframe_collected_finished_ven_regions_dec31.csv', 'r') as csvfile_2:
                collected = csv.reader(csvfile_2, delimiter=',', quotechar='|')

                for b in collected:
                    if b[11] != 'geo_locations':
                        chunk = b[25]
                        tojson = chunk.split("'")
                        if a[0] != 'adamin1' and a[0] != '#adm1+name':
                            if a[2] == tojson[5]:
                                d = b[45]
                                ml = b[47]
                                mu = b[48]
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

with open('../FB_AU_Ven_states.csv', 'w',newline='') as f:
    #Overwrite the old file with the modified rows
    writer = csv.writer(f)
    writer.writerows(new_rows)
f.close()