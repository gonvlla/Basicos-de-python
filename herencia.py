class Vehiculos():
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False
    
    def arrancar(self):
        self.enMarcha = True
    
    def acelerar(self):
        self.acelera = True
        
    def frenar(self):
        self.frena = True
        
    def estado(self):
        print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nMarcha: ",self.enMarcha,"\nAceleracion: ",self.acelera,"\nFrena: ",self.frena)

class VehiculoElectrico():
    #Si tengo 2 clases heredadas utilizara 1 sola y los valores del constructor de la que este a la
    #izquierda
    def __init__(self):
        self.autonomia = 100
    def cargaVehiculo(self,band):
        if(band):
            self.cargado = True
        else: 
            self.cargando = False

class Moto(Vehiculos):
    whillie = "Base"
    def hacerwillie(self,band):
       if(band == True):
            self.willie = "Voy haciendo willie"
       else:
           self.willie = "No estoy haciendo willie"
    
      # Sobreescritura de metodos
    def estadoMoto(self):
         print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nMarcha: ",self.enMarcha,"\nAceleracion: ",self.acelera,"\nFrena: ",self.frena,"\nWhillie: ",self.willie)
       
class Camion(Vehiculos): #class Camion(Vehiculos,Camion) <-- hereda de vehiculos y de camion
     #   Cuando hay herencia multiple al llamar al cosntructor se toma el de la primera
     #   clase heredada 
    llevaCarga = " "
    
    def llevandoCargas(self,band):
        if(band):
            self.llevaCargas = "Mi camion tiene carga  "
        else:
            self.llevaCargas = "Mi camion no tiene carga "
    
    def estadoCamion(self):
        print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nMarcha: ",self.enMarcha,"\nAceleracion: ",self.acelera,"\nFrena: ",self.frena,"\nCarga: ",self.llevaCargas)

class Bicicleta(Moto):
    pass

print("---------------MI MOTO---------------\n")
miMoto = Moto("Honda","Titan") #Instanciacion del objeto miMoto
miMoto.arrancar = True
miMoto.enMarcha = True
miMoto.frena = False
miMoto.hacerwillie(False)
miMoto.estadoMoto()


miMoto.estado()

print("---------------MI CAMION---------------\n")
miCamion = Camion("Freighliner COE","Western Star 5700EX")
miCamion.arrancar = True
miCamion.enMarcha = True
miCamion.frena = False
miCamion.llevandoCargas(True)
miCamion.estadoCamion()
print("---------------MI BICICLETA---------------\n")
miBici = Bicicleta("Venzo","R45 MTB 2.0")
miBici.acelera = True
miBici.estado()
miBici.arrancar() 

class BicicletaElectrica(VehiculoElectrico,Vehiculos):
    pass