import pickle
listaNombres = ["Gon","Tito","Xiomara","Maia"]
archivo_binario = open("archivo1","wb")
pickle.dump(listaNombres,archivo_binario)
archivo_binario.close()
del archivo_binario
