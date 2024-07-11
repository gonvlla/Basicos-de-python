for i in [1,2,3,4,5,6,7,8,9,10]:
    print("Hola:D") #Repite hola 10 veces
for i in ["Argentina","Francia","Croacia","Marruecos"]:
    print(i) #Repite los valores del rango
    
for i in ["Gongui","Vlla",20]:
    print(i,end = "   ")

band = False
cont = 0

for i in ("gonvillalba22@gmail.com"):
    if(i == "@" or i == "."):
        cont = cont+1 #Determina si esta correcto el email
    
if(cont>0):
    print("E-mail correcto")
else:
    print("E-mail incorrecto")
    
    
for i in range(5):
    print("Adios mundo cruel")
