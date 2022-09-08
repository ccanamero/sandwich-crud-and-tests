
from unittest.mock import MagicMock 
from delete_sandwich import function_delete_a_sandwich

# test
def test_delete_sandwich():
    connection_db = MagicMock()
    nombre = 'soso'

    connection_db.function_delete_a_sandwich(connection_db, nombre)
    connection_db.function_delete_a_sandwich.assert_called_once()

    function_delete_a_sandwich(connection_db, nombre) # Para que se vea reflejado en la BD