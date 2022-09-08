
from db_update_a_sandwich import update_a_sandwich_from_table

# Contains the function to update the sandwich's bread

def function_update_a_sandwich(connection_db, nombre: str, tipo_pan: str):
    update_a_sandwich_from_table(nombre, tipo_pan)