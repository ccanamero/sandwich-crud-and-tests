
from unittest.mock import MagicMock 
from insert_sandwich import function_insert_sandwich

# test
def test_inserts_one_sandwich():
    connection_db = MagicMock()
    nombre = 'soso'
    tipo_pan = 'sin gluten'
    ingredientes = 'lechuga'

    connection_db.function_insert_sandwich(connection_db, nombre, tipo_pan, ingredientes)
    connection_db.function_insert_sandwich.assert_called_once()

    ##function_insert_sandwich(connection_db, nombre, tipo_pan, ingredientes) # Para que se vea reflejado en la BD