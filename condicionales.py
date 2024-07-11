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
    