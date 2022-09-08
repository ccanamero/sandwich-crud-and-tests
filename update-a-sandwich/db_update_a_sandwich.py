
import mysql.connector

def update_a_sandwich_from_table(nombre:str, tipo_pan:str):
    
    connection = mysql.connector.connect(host='localhost',
                                        database='Sandwiches',
                                        user='aUser',
                                        password='password')

    try:

        cursor = connection.cursor()
        mySql_update_query = "UPDATE Sandwiches SET tipo_pan = %s WHERE nombre = %s"

        record = (tipo_pan, nombre)
        cursor.execute(mySql_update_query, record)
        connection.commit()
        print(cursor.rowcount, "record(s) affected") 
        print("Record inserted successfully into Sandwiches table")


    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")