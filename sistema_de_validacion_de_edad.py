print("#----------------------------------#")
print("#--| sistema de validacion edad |--#")
print("#----------------------------------#")
try:
    edad = int(input("ingrese su edad: "))
    if edad < 0:
        print("la edad no puede ser negativa.")
    elif edad < 18:
        print("eres menor de edad.")
    else:
        print("eres mayor de edad.")
except ValueError:
    print("error: debes ingresar un numero valido.")