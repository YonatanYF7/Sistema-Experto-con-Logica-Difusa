# interfaz_de_usuario.py
def mostrar_bienvenida():
    print("'Bienvenido a la aplicación de recomendación de propina'")
    print("Por favor ingrese la calidad del servicio y de la comida para recibir una recomendación de propina.\n")

def obtener_entrada_usuario():
    while True:
        try:
            calidad_servicio = float(input("Ingrese la calidad del servicio (0-10): "))
            if 0 <= calidad_servicio <= 10:
                break
            else:
                print("Error: La calidad del servicio debe estar entre 0 y 10.")
        except ValueError:
            print("Error: Ingrese un número válido para la calidad del servicio.")

    while True:
        try:
            calidad_comida = float(input("Ingrese la calidad de la comida (0-10): "))
            if 0 <= calidad_comida <= 10:
                break
            else:
                print("Error: La calidad de la comida debe estar entre 0 y 10.")
        except ValueError:
            print("Error: Ingrese un número válido para la calidad de la comida.")
    
    while True:
        try:
            total_factura = float(input("Ingrese el total de la factura: "))
            if total_factura > 0:
                break
            else:
                print("Error: El total de la factura debe ser mayor a 0.")
        except ValueError:
            print("Error: Ingrese un número válido para el total de la factura.")

    return calidad_servicio, calidad_comida, total_factura

def mostrar_recomendacion(propina_recomendada, total_factura):
    porcentaje_propina = propina_recomendada
    propina = (porcentaje_propina / 100) * total_factura
    print(f"\nLa propina recomendada es: {porcentaje_propina:.2f}%")
    print(f"Esto equivale a: {propina:.2f} de un total de {total_factura:.2f}")