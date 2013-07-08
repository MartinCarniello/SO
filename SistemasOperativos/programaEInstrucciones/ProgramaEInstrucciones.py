'''
Created on 27/04/2013

@author: Carne
'''

class Programa:
    def __init__(self, ins, mem):
        self.instrucciones = ins
        self.memoria = mem

    def add(self, instruccion):
        self.instrucciones.append(instruccion)

    def run(self):
        for i in self.instrucciones:
            i.ejecutar(self.memoria)

class Memoria:
    def __init__(self):
        self.memo = {'0000': 4098, '0001': 4139, '0002': 4139, '0003': 4139}

    def get(self, dirValor):
        return self.memo[dirValor]

    def put(self, dirRes, valor):
        self.memo.
        
class Instruccion:
    def __init__(self, d1, d2, r):
        self.dir1 = d1
        self.dir2 = d2
        self.resultado = r

    def ejecutar(self, memoria):
        valor1 = self.memoria.get(self.dir1)
        valor2 = self.memoria.get(self.dir2)

        memoria.put(self.resultado, operar(valor1, valor2))
        
class Suma(Instruccion):
    def operar(self, valor1, valor2):
        
        return valor1 + valor2

class Resta(Instruccion):
    def operar(self, valor1, valor2):
        
        return valor1 - valor2

class Multiplicacion(Instruccion):
    def operar(self, valor1, valor2):
        
        return valor1 * valor2

class Division(Instruccion):
    def operar(self, valor1, valor2):
        
        return valor1 / valor2