import math

#Entrada de datos
voltaje = float(input("Ingrese el voltaje del motor (V) : "))
corriente = float(input("Ingrese la corriente del motor (A) : "))
velocidad_rpm = float(input("Ingrese la velocidad del motor (RPM) : "))

#calculo de la potencia y par del motor
potencia = voltaje * corriente
par = (potencia * 1000) / (2 * math.pi * velocidad_rpm / 60)

#Salida de resultados  
print("\n" + "=" * 40)
print("\n Resultados del motor")
print("\n" + "=" * 40)
print(f"\nLa potencia del motor es: {potencia:.2f} W")
print(f"El par del motor es: {par:.2f} Nm")
print("\n" + "=" * 40)