
from fastapi import FastAPI
from insert_sandwich import function_insert_sandwich

app = FastAPI()

@app.post("/sandwiches/")
def post_sandwich():
    nombre = 'lourdes'
    tipo_pan = 'trigo'
    ingredientes = 'pollo, bacon, lechuga, tomate, queso'
    function_insert_sandwich(nombre, tipo_pan, ingredientes)
    return {"resultado": "OK"}

# 
# INSTALLATION
#
# sudo apt install pipenv
# pipenv install fastapi uvicorn
