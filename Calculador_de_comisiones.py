class Vendedor:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"


class Calculador(Vendedor):
    def __init__(self, nombre, apellido, porcentaje_comision=13):
        super().__init__(nombre, apellido)
        self.porcentaje_comision = porcentaje_comision
        self.ventas = 0
        self.comision = 0

    def registrar_ventas(self, monto):
        if monto >= 0:
            self.ventas = monto
            self.calcular_comision()
            return True
        return False

    def calcular_comision(self):
        self.comision = round(self.ventas * self.porcentaje_comision / 100, 2)

    def mostrar_comision(self):
        return f"Hola {self.nombre_completo()}, tus comisiones de este mes son: ${self.comision}"



nombre = input("Bienvenido\nPor favor, digite su nombre: ")
apellido = input("Digite su apellido: ")
ventas = float(input("Digite sus ventas totales de este mes en $: "))

vendedor = Calculador(nombre, apellido)
if vendedor.registrar_ventas(ventas):
    print(vendedor.mostrar_comision())
else:
    print("Las ventas no pueden ser negativas.")
