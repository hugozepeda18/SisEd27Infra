import pandas as pd
import mysql.connector
# Load the Excel file into a DataFrame
file_path = './Matrícula - 1º VESPERTINO.xls'
df = pd.read_excel(file_path)
print(df)
df.fillna('', inplace=True)
connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='...',
    database='escuela',
    auth_plugin='mysql_native_password',
)

cursor = connection.cursor()

# Insert data from the DataFrame into the MySQL table
for index, row in df.iterrows():
    sql = "INSERT INTO personal (matricula, nombre, apellido_paterno, apellido_materno, curp, grado, grupo, sexo, edad, correo, turno, incidencias, incidencias_graves, incidencias_muy_graves) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    print(index)

# Commit the transaction
connection.commit()

# Close the connection
cursor.close()
connection.close()
print('DONE')