
from db_get_a_sandwich import get_a_sandwich_from_table

# Contains the function to get a sandwich

def function_get_a_sandwich(connection_db, nombre: str):
    print("Dentro de la función de insertar sandwich: %s.", nombre)
    get_a_sandwich_from_table(nombre)