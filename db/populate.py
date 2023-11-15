import pandas as pd
import mysql.connector
import os 

# Load the Excel file into a DataFrame
file_path = './Matrícula - 1º.xls'
file_path_array = ['./Matrícula - 1º VESPERTINO.xls', './Matrícula - 2º MATUTINO_mod.xls',
                   './Matrícula - 2º  VESPERTINO_mod.xls', './Matrícula - 3º MATUTINO_mod.xls', 
                   './Matrícula - 3º VESPERTINO_mod.xls',]

# Connect to the MySQL database
connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='...',
    database='escuela',
    auth_plugin='mysql_native_password',
)
cursor = connection.cursor()

for files in file_path_array:
    if os.path.isfile(files): 
        df = pd.read_excel(files)
        print(df)
        df.fillna('', inplace=True)
        print(df) 
        # Insert data from the DataFrame into the MySQL table
        for index, row in df.iterrows():
            sql = "INSERT INTO alumno (matricula, nombre, apellido_paterno, apellido_materno, curp, grado, grupo, sexo, edad, correo, turno, incidencias, incidencias_graves, incidencias_muy_graves) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, tuple(row))
            print(index)
        # Commit the transaction
        connection.commit()

        # Close the connection
        cursor.close()
        connection.close()
        print('DONE')
    else: 
        print('File not found' + files)


