
from db_insert_sandwich import insert_varibles_into_table

# Contains the function to inserts sandwiches

# def function_insert_sandwich(connection_db, nombre: str, tipo_pan: str, ingredientes: str):
#    print("Dentro de la función de insertar sandwich: %s, %s, %s.", nombre, tipo_pan, ingredientes)
#    insert_varibles_into_table(nombre, tipo_pan, ingredientes)

def function_insert_sandwich(nombre: str, tipo_pan: str, ingredientes: str):
    print("Dentro de la función de insertar sandwich: %s, %s, %s.", nombre, tipo_pan, ingredientes)
    insert_varibles_into_table(nombre, tipo_pan, ingredientes)