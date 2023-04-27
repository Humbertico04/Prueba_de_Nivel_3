# operaciones.py
class Numero:
    def __init__(self, valor):
        self.is_valid = isinstance(valor, (int, float))
        if self.is_valid:
            self.valor = valor
        else:
            self.invalid_value = valor

    def __str__(self):
        return str(self.valor) if self.is_valid else str(self.invalid_value)

    def suma(self, otro):
        if self.is_valid and isinstance(otro, Numero) and otro.is_valid:
            return Numero(self.valor + otro.valor)
        else:
            return f"Error: Tipo de dato no válido"

    def resta(self, otro):
        if self.is_valid and isinstance(otro, Numero) and otro.is_valid:
            return Numero(self.valor - otro.valor)
        else:
            return f"Error: Tipo de dato no válido"

    def producto(self, otro):
        if self.is_valid and isinstance(otro, Numero) and otro.is_valid:
            return Numero(self.valor * otro.valor)
        else:
            return f"Error: Tipo de dato no válido"

    def division(self, otro):
        if self.is_valid and isinstance(otro, Numero) and otro.is_valid:
            if otro.valor != 0:
                return Numero(self.valor / otro.valor)
            else:
                return "Error: No es posible dividir entre cero"
        else:
            return f"Error: Tipo de dato no válido"

#calculos.py
a = Numero(10)
b = Numero(5)
c = Numero(0)
d = Numero("Hola")

suma_ab = d.suma(b)
resta_bd = b.resta(d)
producto_bb = b.producto(b)
division_ac = a.division(c)

print("{} + {} = {}".format(a, b, suma_ab))
print("{} - {} = {}".format(b, d, resta_bd))
print("{} * {} = {}".format(b, b, producto_bb))
print("{} / {} = {}".format(a, c, division_ac))
