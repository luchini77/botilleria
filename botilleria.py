class Botilleria:

    cerveza = ""
    vino = ""
    agua = ""

    def __init__(self,marca,litros,precio):
        self.marca = marca
        self.litros = litros
        self.precio = precio

    def __str__(self):
        return "{} {} de {} litro, tiene un precio de {} pesos.".format(self.cerveza,self.marca,self.litros,self.precio)



class Cerveza(Botilleria):

    cerveza = "Cerveza"



class Vino(Botilleria):

    vino = "Vino"



class Aguas(Botilleria):

    agua = "Agua"

