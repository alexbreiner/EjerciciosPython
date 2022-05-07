# desicion en cascada
num = int(input("Por favor, digite un numero entero: "))

if num < 0:
    num = num * (-1)
    
if num >= 1 and num <= 9:
    print("El numero tiene 1 digito")
else:
    if num >= 10 and num <= 99:
        print("El numero tiene 2 digitos")
    else:
        if num >= 100 and num <= 999:
            print("El numero tiene 3 digitos")
        else:
            if num >= 1000 and num <= 9999:
                print("El numero tiene 4 digitos")
            else:
                print("El numero tiene mas de 4 digitos")   