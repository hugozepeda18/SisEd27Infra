import psycopg2
import pandas as pd 
import os 

connection = psycopg2.connect (
			database="...",
            host="...",
            user="...",
            password="...",
            port="..."
		)

cursor = connection.cursor()

""" file_path = './Matrícula - 3º VESPERTINO_mod.xls'
df = pd.read_excel(file_path)
print(df)
df.fillna('', inplace=True)
 """

sql = """
CREATE TABLE usuario
(
	id SERIAL PRIMARY KEY,
    personal_id INT,
    email VARCHAR(100),
    password VARCHAR(150),
    role VARCHAR(50),
    CONSTRAINT fk_personal_user FOREIGN KEY (personal_id) REFERENCES personal(id)
)
    """
cursor.execute(sql)
print('Table created')


""" for index, row in df.iterrows():
    sql = "INSERT INTO alumno (matricula, nombre, apellido_paterno, apellido_materno, curp, grado, grupo, sexo, edad, correo, turno, incidencias, incidencias_graves, incidencias_muy_graves) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)"
    cursor.execute(sql, tuple(row))
    print(index) """

connection.commit()
connection.close()
print('DONE')