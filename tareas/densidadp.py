import math 
listadatos=[[1964375,126577691],[30608,5853677],[8452,476415]]   #federal, estatal, minipical, km^2, personas
def densidad_poblacional():
	print("""Escribe si lo quieres la densidad poblacional \n
		 1) Federal
		 2) Estatal (Guanajuato)
		 3) Municilal (Irapuato)		""")
	value = int(input("Seleccione una opcion en numero real: "))
	if value == 1:
	   print(str(listadatos[0][0] / listadatos[0][1]) + " hab/km^2")
	elif value == 2:
 	   print(str(listadatos[1][0] / listadatos[1][1])+ " hab/km^2")
	elif value == 3:
	   print(str(listadatos[3][0] / listadatos[2][1])+ " hab/km^2")
	else:
	   print("Error")


	#switch(value) = {
	#	case "1": print(1),#return listadatos[0][0] / listadatos[0][1]
	#	case "2": print(2),#return listadatos[1][0] / listadatos[1][1]
	#	case "3": print(3),#return listadatos[2][0] / listadatos[2][1]	
	 #             }

	return 0

densidad_poblacional()





#print(listadatos[0][1])
#print(densidad_poblacional(1,2))
#print(densidad_poblacional(1,2.4))
#print(densidad_poblacional(1,5))
#print(densidad_poblacional(1.3,2.6))


# Fuente Wikipedia 
# pagina del INEGI
