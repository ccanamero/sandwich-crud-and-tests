# sandwich-crud-and-tests
CRUD en Python para el acceso a una base de datos MySQL de sandwiches. Se ha buscado invertir las dependencias y practicar la realización de test en Python con la herramienta de Pytest: unitario, integración y validación. Las peticiones se realizarán con FastAPI.

Para compilar los test de las diferentes operaciones CRUD hay que entrar en la carpeta correspondiente y ejecutar el comando adecuado:
  > python3 -m pytest test_get_sandwich.py -s
  > python3 -m pytest test_insert_sandwich.py -s
  > python3 -m pytest test_get_all_sandwiches.py -s
  > python3 -m pytest test_delete_a_sandwich.py -s
  > python3 -m pytest test_update_a_sandwich.py -s
