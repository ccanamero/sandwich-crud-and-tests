
# Connection with the Database

import mysql.connector

def insert_varibles_into_table(nombre, tipo_pan, ingredientes):
    
    connection = mysql.connector.connect(host='localhost',
                                        database='Sandwiches',
                                        user='aUser',
                                        password='password')
    try:                                    
        cursor = connection.cursor()
        mySql_insert_query = "INSERT INTO Sandwiches (nombre, tipo_pan, ingredientes) VALUES (%s, %s, %s)"

        record = (nombre, tipo_pan, ingredientes)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("Record inserted successfully into Sandwiches table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# pip install mysql-connector
# pip install mysql-connector-python 