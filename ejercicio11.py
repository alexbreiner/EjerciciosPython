# realizar una funcion que compare las dos ultimas letras de dos frutas ingresadas por teclado 
# y diga si son iguales o diferentes y hacer control de errores
def compararFrutas(fruta1, fruta2):
    try:
        
        longitudFruta1 = len(fruta1)
        #print("Longitud letra1: " + longitudFruta1)
        longitudFruta2 = len(fruta2)
        #print("Longitud letra2: "+ longitudFruta2)
        
        ultimaLetra1 = fruta1[longitudFruta1 - 1]
        ultimaLetra2 = fruta2[longitudFruta2 - 1]
        
        if ultimaLetra1 ==  ultimaLetra2:
            print("La ultima letra 1 " + str(ultimaLetra1) + " ultima letra 2 " + str(ultimaLetra2) + " son iguales")
        elif ultimaLetra1 !=  ultimaLetra2:
            print("La ultima letra1 " + ultimaLetra1 + " ultima letra 2 " + ultimaLetra2 + " son diferentes")

    except:
        print("No se puede ingresar valores numericos.")
        
    ##return mensaje    

fruta1 = input("Ingrese una fruta: ")
fruta2 = input("Ingrese otra fruta: ")       
compararFrutas(fruta1, fruta2)
