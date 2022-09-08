
import mysql.connector

def get_all_sandwiches_from_table():

    connection = mysql.connector.connect(host='localhost',
                                         database='Sandwiches',
                                         user='aUser',
                                         password='password')

    try:
        sql_select_Query = "SELECT * FROM Sandwiches"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)

        print("\n")
        for row in records:
            print("Nombre = ", row[0])
            print("Tipo de pan = ", row[1])
            print("Ingredientes  = ", row[2], "\n")

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")