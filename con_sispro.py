import pyodbc

print(pyodbc.drivers())

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=tcp:cubos.sispro.gov.co;'
                      'Database=SGD_COVID19;'
                      'Trusted_Connection=yes;'
                      'PWD=Minsalud2020*')

cursor = conn.cursor()
#cursor.execute('SELECT * FROM table_name')
cursor.execute('SELECT @@SERVERNAME')

print(cursor)
for i in cursor:
    print(i)