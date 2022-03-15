import mysql.connector
import pymysql.cursors

def createConnectionDB() -> any:
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="",
        port=3306,
        cursorclass=pymysql.cursors.DictCursor,
    )
    return connection


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


def insertBLOB(id, nombre, usuario, enlace, foto, biodataFile):
    print("Inserting BLOB into python_employee table")
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='',
                                             user='root',
                                             password='')

        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO datos
                          (id, nombre, usuario, enlace, foto, biodataFile) VALUES (%s,%s,%s,%s,%s,%s)"""

        empPicture = convertToBinaryData(foto)
        file = convertToBinaryData(biodataFile)

        # Convert data into tuple format
        insert_blob_tuple = (id, nombre, usuario, enlace, foto, biodataFile)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into python_employee table", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

insertBLOB(1, "Rodrigo","Rivera", "https://www.youtube.com/","C:/Users/images/foto.jpg", "C:/Users/static/images/foto_biodata.txt")


def selectData():
    connection = createConnectionDB()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM bd.datos;"
            cursor.execute(sql)
            result = cursor.fetchall()
    return result
        
        
        