#definition funtion personality 

a = int(input("ingrese el numero 1: "))
b = int(input("ingrese el numero 2: "))


def sumarDosNumeros(x, y):
    z = x + y
    return z

def sumarDosNumeros2(x,y):
    z = x + y
    return z

print("Log se sumaran el valor de las dos funciones")
funtion1 = sumarDosNumeros(a , b)
print("valor de funcion 1 es:", funtion1)
funtion2 = sumarDosNumeros2(a , b)
print("valor de funcion 2 es:", funtion2)

suma = funtion1 + funtion2
multiplicacion = funtion1 * funtion2
adision = funtion1 - funtion2
division = funtion1 / funtion2
potenciacion = funtion1**funtion2

print("El resultado de la suma es: " + str(suma) +" de la multiplicacion: " + str(multiplicacion) + " de la adision es: "+ str(adision) + " de la division es: "+ str(division) + " de la potenciacion es: " + str(potenciacion) + " de las funciones a, b")
