import numpy as np


def obtener_calificaciones():
    calificaciones = []
    while len(calificaciones) < 5:
        try:
            calificacion = float(input(f"Ingrese la calificación {len(calificaciones) + 1} (0-10): "))
            if 0 <= calificacion <= 10:
                calificaciones.append(calificacion)
            else:
                print("Error: La calificación debe estar entre 0 y 10.")
        except ValueError:
            print("Error: Debe ingresar un número válido.")
    return calificaciones


def calcular_estadisticas(calificaciones):
    promedio = np.mean(calificaciones)
    mediana = np.median(calificaciones)
    desviacion_estandar = np.std(calificaciones)
    calificacion_maxima = np.max(calificaciones)
    calificacion_minima = np.min(calificaciones)

    return promedio, mediana, desviacion_estandar, calificacion_maxima, calificacion_minima


def determinar_estado(promedio):
    if promedio >= 9:
        return "Excelente"
    elif promedio >= 7:
        return "Bueno"
    elif promedio >= 5:
        return "Aprobado"
    else:
        return "Reprobado"


def generar_recomendacion(estado, desviacion_estandar):
    if estado == "Excelente":
        return "¡Sigue así! Mantén tu esfuerzo y busca nuevas metas."
    elif estado == "Bueno":
        return "Buen trabajo. Intenta mantener la consistencia."
    elif estado == "Aprobado":
        return "Es hora de reforzar tus estudios para mejorar."
    else:
        if desviacion_estandar > 2:
            return "Considera buscar ayuda adicional o tutoría."
        else:
            return "Dedica más tiempo a estudiar y organiza mejor tu tiempo."


def mostrar_resumen(calificaciones):
    promedio, mediana, desviacion_estandar, calificacion_maxima, calificacion_minima = calcular_estadisticas(
        calificaciones)
    estado = determinar_estado(promedio)
    recomendacion = generar_recomendacion(estado, desviacion_estandar)

    print("\nResumen del análisis:")
    print(f"Calificaciones: {calificaciones}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Desviación Estándar: {desviacion_estandar:.2f}")
    print(f"Calificación más alta: {calificacion_maxima:.2f}")
    print(f"Calificación más baja: {calificacion_minima:.2f}")
    print(f"Estado del estudiante: {estado}")
    print(f"Recomendación: {recomendacion}")


def main():
    calificaciones = obtener_calificaciones()
    mostrar_resumen(calificaciones)


if __name__ == "__main__":
    main()
