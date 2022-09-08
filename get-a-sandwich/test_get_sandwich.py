
from unittest.mock import MagicMock 
from get_sandwich import function_get_a_sandwich

# test
def test_get_sandwich():
    connection_db = MagicMock()
    nombre = 'soso'

    connection_db.function_get_a_sandwich(connection_db, nombre)
    connection_db.function_get_a_sandwich.assert_called_once()

    function_get_a_sandwich(connection_db, nombre) # Para que se vea reflejado en la BD