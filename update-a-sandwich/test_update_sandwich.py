
from unittest.mock import MagicMock 
from update_sandwich import function_update_a_sandwich

# test
def test_update_sandwich():
    connection_db = MagicMock()
    nombre = 'mixto'
    tipo_pan =  'sin gluten'

    connection_db.function_update_a_sandwich(connection_db, nombre, tipo_pan)
    connection_db.function_update_a_sandwich.assert_called_once()

    function_update_a_sandwich(connection_db, nombre, tipo_pan) # Para que se vea reflejado en la BD