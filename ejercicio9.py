#intente
try:
    temp_far = float(input("Digite la temperatura en grados farenheit: "))
    temp_celcius = (temp_far - 32) * (5/9)
    print("La temperatura", temp_celcius)
except:
    print("Digite un numero")