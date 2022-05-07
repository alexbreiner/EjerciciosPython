# 5 nombres de items en un diccionario por teclado
#tipo de sangre
#0-
#edad 29
#def reporte
def informacionPersonal():

    tipoSangre = detallePersona['TipoSangre']
    edad = detallePersona['Edad']
    nombre = detallePersona['Nombre']
    
    infoPersonal = {'Sangre': tipoSangre['TipoSangre'], 'Edad': edad['Edad'], 'Nombre': nombre['Nombre']}
    
    for list_info in infoPersonal:
            #infoPersonal = {'Sangre': tipoSangre['TipoSangre'], 'Edad': edad['Edad'], 'Nombre': nombre['Nombre']}
            #list_info = infoPersonal
            #print("Data"+ list_info) 
        return list_info

detallePersona = {}

detallePersona['TipoSangre'] = input("Digite su tipo de sangre: ")
detallePersona['Edad'] = int(input("Digite su edad: "))
detallePersona['Nombre'] = input("Ingrese su nombre: ")

print("La informacion de la persona es: ", informacionPersonal(detallePersona))