import pickle
listaNombres = ["Gon","Tito","Xiomara","Maia"]
archivo_binario = open("archivo1","wb") #Escribira en binario
pickle.dump(listaNombres,archivo_binario)
archivo_binario.close()
del archivo_binario
