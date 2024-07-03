# motor_de_inferencia.py
import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl

def definir_reglas(variables):
    calidad, servicio, propina = variables

    # Definir las reglas difusas
    regla1 = ctrl.Rule(servicio['malo'] | calidad['baja'], propina['baja'])
    regla2 = ctrl.Rule(servicio['regular'], propina['media'])
    regla3 = ctrl.Rule(servicio['bueno'] | calidad['alta'], propina['alta'])

    return [regla1, regla2, regla3]

def inferir_recomendaciones(calidad_servicio, calidad_comida, variables, reglas):
    calidad, servicio, propina = variables

    # Crear el sistema de control
    sistema_control = ctrl.ControlSystem(reglas)
    sistema = ctrl.ControlSystemSimulation(sistema_control)

    # Asignar valores de entrada
    sistema.input['calidad'] = calidad_comida
    sistema.input['servicio'] = calidad_servicio

    # Calcular la salida
    sistema.compute()

    # Obtener la propina recomendada
    propina_recomendada = sistema.output['propina']
    return propina_recomendada, sistema

def graficar_funciones_membresia(calidad_servicio, calidad_comida, sistema):
    # Generar puntos en el universo de calidad
    x_calidad = np.arange(0, 11, 0.1)

    # Obtener los valores de membresía para cada función basado en la entrada del usuario
    memb_baja = fuzz.trimf(x_calidad, [0, 0, 5])
    memb_media = fuzz.trimf(x_calidad, [0, 5, 10])
    memb_alta = fuzz.trimf(x_calidad, [5, 10, 10])

    # Calcular los grados de membresía específicos para las entradas del usuario (calidad de servicio)
    calidad_servicio_baja = fuzz.interp_membership(x_calidad, memb_baja, calidad_servicio)
    calidad_servicio_media = fuzz.interp_membership(x_calidad, memb_media, calidad_servicio)
    calidad_servicio_alta = fuzz.interp_membership(x_calidad, memb_alta, calidad_servicio)

    # Calcular los grados de membresía específicos para las entradas del usuario (calidad de comida)
    calidad_comida_baja = fuzz.interp_membership(x_calidad, memb_baja, calidad_comida)
    calidad_comida_media = fuzz.interp_membership(x_calidad, memb_media, calidad_comida)
    calidad_comida_alta = fuzz.interp_membership(x_calidad, memb_alta, calidad_comida)

    # Crear subplots
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 6))

    # Graficar las funciones de membresía para calidad del servicio
    ax1.plot(x_calidad, memb_baja, label='Baja')
    ax1.plot(x_calidad, memb_media, label='Media')
    ax1.plot(x_calidad, memb_alta, label='Alta')
    
    ax1.scatter([calidad_servicio], [calidad_servicio_baja], color='red')
    ax1.scatter([calidad_servicio], [calidad_servicio_media], color='red')
    ax1.scatter([calidad_servicio], [calidad_servicio_alta], color='red')
    
    ax1.text(calidad_servicio, calidad_servicio_baja, f'{calidad_servicio_baja:.2f}', horizontalalignment='right')
    ax1.text(calidad_servicio, calidad_servicio_media, f'{calidad_servicio_media:.2f}', horizontalalignment='right')
    ax1.text(calidad_servicio, calidad_servicio_alta, f'{calidad_servicio_alta:.2f}', horizontalalignment='right')
    
    ax1.set_title('Funciones de Membresía para Calidad del Servicio')
    ax1.set_xlabel('Calidad del Servicio')
    ax1.set_ylabel('Grado de Membresía')
    ax1.legend()
    ax1.grid(True)

    # Graficar las funciones de membresía para calidad de la comida
    ax2.plot(x_calidad, memb_baja, label='Baja')
    ax2.plot(x_calidad, memb_media, label='Media')
    ax2.plot(x_calidad, memb_alta, label='Alta')
    
    ax2.scatter([calidad_comida], [calidad_comida_baja], color='red')
    ax2.scatter([calidad_comida], [calidad_comida_media], color='red')
    ax2.scatter([calidad_comida], [calidad_comida_alta], color='red')
    
    ax2.text(calidad_comida, calidad_comida_baja, f'{calidad_comida_baja:.2f}', horizontalalignment='right')
    ax2.text(calidad_comida, calidad_comida_media, f'{calidad_comida_media:.2f}', horizontalalignment='right')
    ax2.text(calidad_comida, calidad_comida_alta, f'{calidad_comida_alta:.2f}', horizontalalignment='right')
    
    ax2.set_title('Funciones de Membresía para Calidad de la Comida')
    ax2.set_xlabel('Calidad de la Comida')
    ax2.set_ylabel('Grado de Membresía')
    ax2.legend()
    ax2.grid(True)

    # Graficar las funciones de membresía para propina
    x_propina = np.arange(0, 26, 0.1)
    propina_baja = fuzz.trimf(x_propina, [0, 0, 13])
    propina_media = fuzz.trimf(x_propina, [0, 13, 25])
    propina_alta = fuzz.trimf(x_propina, [13, 25, 25])

    # Calcular la propina recomendada
    propina_recomendada = sistema.output['propina']
    propina_baja_valor = fuzz.interp_membership(x_propina, propina_baja, propina_recomendada)
    propina_media_valor = fuzz.interp_membership(x_propina, propina_media, propina_recomendada)
    propina_alta_valor = fuzz.interp_membership(x_propina, propina_alta, propina_recomendada)

    ax3.plot(x_propina, propina_baja, label='Baja')
    ax3.plot(x_propina, propina_media, label='Media')
    ax3.plot(x_propina, propina_alta, label='Alta')

    ax3.scatter([propina_recomendada], [propina_baja_valor], color='red')
    ax3.scatter([propina_recomendada], [propina_media_valor], color='red')
    ax3.scatter([propina_recomendada], [propina_alta_valor], color='red')

    ax3.text(propina_recomendada, propina_baja_valor, f'{propina_baja_valor:.2f}', horizontalalignment='right')
    ax3.text(propina_recomendada, propina_media_valor, f'{propina_media_valor:.2f}', horizontalalignment='right')
    ax3.text(propina_recomendada, propina_alta_valor, f'{propina_alta_valor:.2f}', horizontalalignment='right')

    ax3.set_title('Funciones de Membresía para Propina')
    ax3.set_xlabel('Propina')
    ax3.set_ylabel('Grado de Membresía')
    ax3.legend()
    ax3.grid(True)

    # Mostrar los gráficos
    plt.tight_layout()
    plt.show()
