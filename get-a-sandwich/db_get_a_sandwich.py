
import mysql.connector

def get_a_sandwich_from_table(nombre:str):
    
    connection = mysql.connector.connect(host='localhost',
                                        database='Sandwiches',
                                        user='aUser',
                                        password='password')

    try:

        cursor = connection.cursor()
        mySql_select_Query = """SELECT * FROM Sandwiches WHERE nombre = %s"""
        cursor.execute(mySql_select_Query, (nombre,))
        # get all records
        records = cursor.fetchall()

        for row in records:
            print("Nombre = ", row[0], )
            print("Tipo de pan = ", row[1])
            print("Ingredientes  = ", row[2], "\n")

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")