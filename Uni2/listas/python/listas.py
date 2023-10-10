Itic3 = ["Aylin Martinez Santos", "xitlali Gonzalez", "Emmanuel de Jesus Esparza", "Maria Fernanda Pantoja Castillo"," Zuleyma de Jesus Manzano"]
Carreras_Itpa = ["Logistica","ITIC","Gestion Empresarial", "Mecatronica", "Industrial"]
Edades = [18, 20, 19, 20, 20, 19, 19, 18, 19, 19, 19, 19]
 
 #imprimir lista
print(Carreras_Itpa)
print (Itic3)
print(Edades)

#imprimir el tercer campo de cada lista
print(Carreras_Itpa[2])

#Agregar elementos al final de la lista
Itic3.append('xitlali')
print(Itic3)

#Agregar otra lista
Itic3.extend(['Vanessa','Juan'])
print(Itic3)

#Agregar elemento en la posicion 5
Itic3.insert(4,'Jesus')
print(Itic3)

del Edades[0]
print(Edades)

#ver el tamaño de las listas 
print(len(Edades))
print(len(Itic3))
print(len(Carreras_Itpa))

#Eliminar un elemento en especifico
Edades.remove(20)
print(Edades)

#ordenar elementos 
print(Edades)
Edades.sort()
print(Edades)