#Escriba un funcion que devuelva un numero de acuerdo al dia de la semana
#Lunes = 1, martes = 2, miercoles = 3, jueves = 4 ,viernes = 5, sabado = 6 y domingo = 7
def semana(dia):
    if dia == 1:
        print("El valor ingresado", dia , " es Lunes.")
    elif dia == 2:
        print("El valor ingresado", dia , " es Martes.")
    elif dia == 3:
        print("El valor ingresado", dia , " es Miercoles.")
    elif dia == 4:
        print("El valor ingresado", dia , " es Jueves.")
    elif dia == 5:
        print("El valor ingresado", dia , " es Viernes.")
    elif dia == 6:
        print("El valor ingresado", dia , " es Sabado.")
    elif dia == 7:
        print("El valor ingresado", dia , " es Domingo.")
    elif dia == 0:
        print("No exite el dia")
    else:
        print("El valor ingresado no hace parte a un dia de la semana. Por favor digite un valor del 1 al 7.")
        
def mostrarDiasSemana():
    mostrarDia = semana(dia)
    valor = mostrarDia
    return valor

dia = int(input("Ingrese un dia  de la semana en valor numerico: "))
imprimirFuncion = mostrarDiasSemana()
#print(imprimirFuncion)
#print("El dia de la semana es: ", int(imprimirFuncion))