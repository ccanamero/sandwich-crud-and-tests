
from unittest.mock import MagicMock 
from get_all_sandwiches import function_get_all_sandwiches

# test
def test_get_all_sandwiches():
    connection_db = MagicMock()

    connection_db.function_get_all_sandwiches(connection_db)
    connection_db.function_get_all_sandwiches.assert_called_once()

    function_get_all_sandwiches(connection_db) # Para que se vea reflejado en la BD