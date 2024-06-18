"Conversión de Temperatura: Escribe un programa que convierta una temperatura dada en grados Celsius a grados Fahrenheit."

celsius = float(input( "Ingrese la temperatura en Celsius: " ))

def celsius_a_fahrenheit (celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temperatura = celsius_a_fahrenheit(celsius)
print('La temperatura dada en celsius es es de: ', temperatura ,'F')