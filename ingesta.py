import mysql.connector
import csv
import boto3

# Conexión a la base de datos MySQL
connection = mysql.connector.connect(
    host='3.230.28.178',
    port=8002,
    user='root',
    password='utec',
    database='mysql'
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM rockies")
rows = cursor.fetchall()

# Guardar los registros en un archivo CSV
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([i[0] for i in cursor.description])  # Escribir encabezados de columnas
    writer.writerows(rows)

cursor.close()
connection.close()

# Subir el archivo CSV a S3
s3 = boto3.client('s3')
ficheroUpload = 'data.csv'
nombreBucket = 'jpaca'
s3.upload_file(ficheroUpload, nombreBucket, ficheroUpload)
print("Ingesta completada")

