
from db_delete_a_sandwich import delete_a_sandwich_from_table

# Contains the function to delete a sandwich

def function_delete_a_sandwich(connection_db, nombre: str):
    delete_a_sandwich_from_table(nombre)