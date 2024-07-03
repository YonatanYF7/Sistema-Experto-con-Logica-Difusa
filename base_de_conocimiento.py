# base_de_conocimiento.py
import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl

def obtener_variables_difusas():
    # Definir los rangos de las variables de entrada
    calidad = ctrl.Antecedent(np.arange(0, 11, 1), 'calidad')
    servicio = ctrl.Antecedent(np.arange(0, 11, 1), 'servicio')
    propina = ctrl.Consequent(np.arange(0, 27, 1), 'propina')

    # Definir las funciones de pertenencia para calidad
    calidad['baja'] = fuzz.trimf(calidad.universe, [0, 0, 5])
    calidad['media'] = fuzz.trimf(calidad.universe, [0, 5, 10])
    calidad['alta'] = fuzz.trimf(calidad.universe, [5, 10, 10])

    # Definir las funciones de pertenencia para servicio
    servicio['malo'] = fuzz.trimf(servicio.universe, [0, 0, 5])
    servicio['regular'] = fuzz.trimf(servicio.universe, [0, 5, 10])
    servicio['bueno'] = fuzz.trimf(servicio.universe, [5, 10, 10])

    # Definir las funciones de pertenencia para propina
    propina['baja'] = fuzz.trimf(propina.universe, [0, 0, 10])  # Rango mínimo a 10%
    propina['media'] = fuzz.trimf(propina.universe, [10, 15, 20])  # Rango medio 15-20%
    propina['alta'] = fuzz.trimf(propina.universe, [20, 25, 25])  # Rango máximo a 25%

    return calidad, servicio, propina
