
#try excep
#Hacer un prorgrama que pida por teclado y haga la division de ambos 
#z = xy
try:
    x = float(input("Ingrese el primer valor: "))
    y = float(input("Ingrese el segundo valor: "))
    
    try:    
        z = x / y
        print("Valor de z: ", z)
    except:
        print("La division entre cero no esta difinida. ")
        
except:
    print("Solo se puede digitar numeros")