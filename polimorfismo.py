class Coche():
    def enMovimiento(self):
        print("Me desplazo en 4 ruedas")
        
class Moto():
    def enMovimiento(self):
        print("Me desplazo en 2 ruedas")
class Camion():
    def enMovimiento(self):
        print("Me desplazo en 6 ruedas")


#       Polimorfismo
def desplazamientoVehiculo(vehiculo):
    vehiculo.enMovimiento()

miVehiculo = Moto()

desplazamientoVehiculo(miVehiculo)
