import csv

with open('../FB_AU_Colombian_regions.csv', 'r') as csvfile_1:
    new_rows=[]
    data = csv.reader(csvfile_1, delimiter=',', quotechar='|')
    count = 0
    for a in data:
        new_a = a
        if a[0] == 'DEPARTAMENTO':
            new_a.extend(['mau_audience_jul15', 'dau_audience_jul15', 'indicador_presion_jul15'])
            new_rows.append(new_a)
        if a[0] == '#adm1+name':
            new_a.extend(['inneed+migrants+monthly','inneed+migrants+daily', 'indicator+rate'])
            new_rows.append(new_a)
    pass
    print(new_rows)