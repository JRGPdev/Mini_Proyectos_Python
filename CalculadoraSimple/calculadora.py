def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

operacion = float(input("Ingrese la operación a realizar: \n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n"))

#pedir al usuario que ingrese los valores
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

#realizar la operación
if operacion == 1:
    print(f"El resultado de la suma es: {suma(num1, num2)}")
elif operacion == 2:
    print(f"El resultado de la resta es: {resta(num1, num2)}")
elif operacion == 3:
    print(f"El resultado de la multiplicación es: {multiplicacion(num1, num2)}")
elif operacion == 4:
    print(f"El resultado de la división es: {division(num1, num2)}")
else:
    print("Operación no válida")