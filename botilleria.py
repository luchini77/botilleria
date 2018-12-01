class Botilleria:


    def __init__(self,marca,litros,precio):
        self.marca = marca
        self.litros = litros
        self.precio = precio

    def __str__(self):
        return "{} de {} litro, tiene un precio de {} pesos.".format(self.marca,self.litros,self.precio)


class Cerveza(Botilleria):

    tipo = ""

    def __str__(self):
        return "{} {} de {} litro, tiene un precio de {} pesos.".format(self.tipo,self.marca,self.litros,self.precio)



class Vino(Botilleria):

    tipo = ""

    def __str__(self):
        return "{} ,{} de {} litro, tiene un precio de {} pesos.".format(self.tipo,self.marca,self.litros,self.precio)



class Aguas(Botilleria):

    tipo = ""

    def __str__(self):
        return "{} {} de {} litro, tiene un precio de {} pesos.".format(self.tipo,self.marca,self.litros,self.precio)

