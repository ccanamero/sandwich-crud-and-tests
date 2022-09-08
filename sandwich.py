

# Sandwich : nombre (strg), tipo_pan (string), ingredientes (string)

# Contains the Sandwich definition
class Sandwich: 
    nombre: str
    tipo_pan: str
    ingredientes: str

    def __init__(nombre: str, tipo_pan: str, ingredientes: str):
        self.nombre = nombre
        self.tipo_pan = tipo_pan
        self.ingredientes = ingredientes