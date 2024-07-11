salario_gerente = int(input("Ingrese salario del gerente: "))
print("Salario gerente: $" + str(salario_gerente))
salario_subgerente = int(input("Ingrese salario del subgerente: "))
print("Salario subgerente: $" + str(salario_subgerente))
salario_empleada = int(input("Ingrese salario de empleada: "))
print("Salario empleada: $" + str(salario_empleada))

if(salario_gerente>salario_subgerente>salario_empleada):
    print("Esta correcto")
else:
    print("Incorrecto")
#Determinar becado
print("Sistema de becas")
km = int (input("Kilometros hasta la institucion: "))
print("Km: " + str(km))
cant_hermanos = int(input("Cantidad de hermanos: "))
print("Cant. hermanos: " + str(cant_hermanos))
salario = int(input("Salario familiar mensual: $"))
print("Salario mensual: $" + str(salario))
if(km>40 and cant_hermanos>2 and salario<20000):
    print ("Estas becado")
else:
    print("No estaras becado / no cumple condiciones")
    
