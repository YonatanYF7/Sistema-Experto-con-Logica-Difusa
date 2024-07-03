# main.py
from interfaz_de_usuario import obtener_entrada_usuario, mostrar_recomendacion, mostrar_bienvenida
from base_de_conocimiento import obtener_variables_difusas
from motor_de_inferencia import definir_reglas, inferir_recomendaciones, graficar_funciones_membresia

def main():
    #Paso 1: Muestra la bienvenida
    mostrar_bienvenida()

    #Paso 2: Obtener entrada del usuario
    # Obtener la calidad del servicio, calidad de la comida y el total de la factura del usuario
    calidad_servicio, calidad_comida, total_factura = obtener_entrada_usuario()
    
    # Paso 3: Definir variables difusas
    calidad, servicio, propina = obtener_variables_difusas()
    
    # Paso 4: Definir las reglas difusas
    reglas = definir_reglas((calidad, servicio, propina))
    
    # Paso 5: Inferir la propina recomendada
    propina_recomendada, sistema = inferir_recomendaciones(calidad_servicio, calidad_comida, (calidad, servicio, propina), reglas)
    
    # Paso 6: Graficar funciones de membresía
    graficar_funciones_membresia(calidad_servicio, calidad_comida, sistema)
    
    # Paso 7: Mostrar recomendación al usuario
    mostrar_recomendacion(propina_recomendada, total_factura)

if __name__ == "__main__":
    main()