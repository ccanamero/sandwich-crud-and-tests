
import mysql.connector

def delete_a_sandwich_from_table(nombre:str):
    
    connection = mysql.connector.connect(host='localhost',
                                        database='Sandwiches',
                                        user='aUser',
                                        password='password')

    try:

        cursor = connection.cursor()
        mySql_select_Query = """DELETE FROM Sandwiches WHERE nombre = %s"""
        cursor.execute(mySql_select_Query, (nombre,))
        connection.commit()
        print("Record inserted successfully into Sandwiches table")

    except mysql.connector.Error as e:
        print("Error deleting data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")