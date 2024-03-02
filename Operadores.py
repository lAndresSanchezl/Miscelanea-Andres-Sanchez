import math

def area_triangulo(base, altura):
    return (base * altura) / 2

def suma_numeros(a, b):
    return a + b

def cuadrado_numero(numero):
    return numero ** 2

def euros_a_dolares(euros, tasa_cambio):
    return euros * tasa_cambio

def area_perimetro_cuadrado(lado):
    area = lado ** 2
    perimetro = 4 * lado
    return area, perimetro

def area_volumen_cilindro(radio, altura):
    area_base = math.pi * radio ** 2
    volumen = area_base * altura
    return area_base, volumen

def longitud_area_circunferencia(radio):
    longitud = 2 * math.pi * radio
    area_circulo_inscrito = math.pi * radio ** 2
    return longitud, area_circulo_inscrito

def promedio_tres_numeros(num1, num2, num3):
    return (num1 + num2 + num3) / 3

def main():
    while True:
        print("\nMenu:")
        print("1. Calcular el área de un triángulo")
        print("2. Sumar dos números")
        print("3. Elevar un número al cuadrado")
        print("4. Convertir euros a dólares")
        print("5. Calcular área y perímetro de un cuadrado")
        print("6. Calcular área y volumen de un cilindro")
        print("7. Calcular longitud y área de una circunferencia")
        print("8. Calcular el promedio de tres números")
        print("99. Salir")

        opcion = input("Ingrese el número de la opción que desea: ")

        if opcion == '1':
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            print("El área del triángulo es:", area_triangulo(base, altura))
        elif opcion == '2':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print("La suma de los dos números es:", suma_numeros(num1, num2))
        elif opcion == '3':
            num = float(input("Ingrese un número: "))
            print("El número elevado al cuadrado es:", cuadrado_numero(num))
        elif opcion == '4':
            euros = float(input("Ingrese la cantidad de euros: "))
            tasa_cambio = float(input("Ingrese la tasa de cambio de euros a dólares: "))
            print("La cantidad en dólares es:", euros_a_dolares(euros, tasa_cambio))
        elif opcion == '5':
            lado = float(input("Ingrese el lado del cuadrado: "))
            area, perimetro = area_perimetro_cuadrado(lado)
            print("El área del cuadrado es:", area)
            print("El perímetro del cuadrado es:", perimetro)
        elif opcion == '6':
            radio = float(input("Ingrese el radio del cilindro: "))
            altura = float(input("Ingrese la altura del cilindro: "))
            area_base, volumen = area_volumen_cilindro(radio, altura)
            print("El área de la base del cilindro es:", area_base)
            print("El volumen del cilindro es:", volumen)
        elif opcion == '7':
            radio = float(input("Ingrese el radio de la circunferencia: "))
            longitud, area_circulo_inscrito = longitud_area_circunferencia(radio)
            print("La longitud de la circunferencia es:", longitud)
            print("El área del círculo inscrito es:", area_circulo_inscrito)
        elif opcion == '8':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            num3 = float(input("Ingrese el tercer número: "))
            print("El promedio de los tres números es:", promedio_tres_numeros(num1, num2, num3))
        elif opcion == '99':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()