#Diccionarios estructuras de datos 
#def validarNotaAltaAndBaja()
def promedioNotas(notas):
    
    sumatoria = 0
    sumatoria += notas['Nota1']
    sumatoria += notas['Nota2']
    sumatoria += notas['Nota3']
    sumatoria += notas['Nota4']
    
    #Entregar la nota mas alta y mas baja max y min 
    notaMasAlta = max(notas['Nota1'], notas['Nota2'], notas['Nota3'], notas['Nota4'])
    notaMasBaja = min(notas['Nota1'], notas['Nota2'], notas['Nota3'], notas['Nota4'])

    #preguntamos cual de las notas es la mas alta y baja
    if notaMasAlta == notas['Nota1']:
        notaAlta ='Nota1'
    elif notaMasAlta == notas['Nota2']:
        notaAlta = 'Nota2'
    elif notaMasAlta == notas['Nota3']:
        notaAlta = 'Nota3'
    else:
        notaAlta = 'Nota4'
    
    if notaMasBaja == notas['Nota1']:
        notaBaja ='Nota1'
    elif notaMasBaja == notas['Nota2']:
        notaBaja = 'Nota2'
    elif notaMasBaja == notas['Nota3']:
        notaBaja = 'Nota3'
    else:
        notaBaja = 'Nota4'
    
    promedio = round(sumatoria / 4,2)
    
    resultado = { 'Estudiante': notas['Estudiante'], 'Codigo': notas['Codigo'], 'Promedio': promedio, 'Nota Alta': notaAlta, 'Nota baja': notaBaja,  } 
    
    return resultado

dicNotas = {}

#llenando el diccionario ingresando los valores por teclado
dicNotas['Nota1'] = float(input("Digite la nota 1: "))
dicNotas['Nota2'] = float(input("Digite la nota 2: "))
dicNotas['Nota3'] = float(input("Digite la nota 3: "))
dicNotas['Nota4'] = float(input("Digite la nota 4: "))
#Modificar el programa para que pida un codigo y la funcion devuelva el nombre el codigo y el promedio de notas.
dicNotas['Estudiante'] = str(input("Digite el nombre del estudiante: "))
dicNotas['Codigo'] = input("Digite el codigo del estudiante: ")

print("El promedio de las notas es:", promedioNotas(dicNotas))