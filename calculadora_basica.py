"""
calculadora.py

** Universidad Internacional de La Rioja **

Curso: Adaptación al Grado de Informática
Asignatura: Procesos en Ingeniería del Software
Práctica: Diseño de pruebas de software - Calculadora con pruebas unitarias

Descripción:
    Aplicación principal para realizar cálculos matemáticos básicos utilizando las funciones
    definidas en el módulo 'operaciones.py'. Proporciona una interfaz de usuario sencilla
    para ejecutar operaciones como suma, resta, multiplicación y división.

Características:
    - Solicita al usuario que introduzca dos números y seleccione una operación.
    - Realiza la operación seleccionada llamando a las funciones de 'operaciones.py'.
    - Maneja errores comunes, como entradas no válidas o división por cero.

Uso:
    Ejecuta este archivo para iniciar la calculadora:
    $ python calculadora.py

Ejemplo:
    Calculadora Básica
    Seleccione una operación:

    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir

    Opción: 1

    Introduzca el primer número: 5
    Introduzca el segundo número: 3

    Resultado: 8

Requisitos:
    - Python 3.x
    - El módulo 'operaciones.py' debe estar en el mismo directorio o disponible en el PATH.

Autores:
    Cristina Cacho Martín
    Patricia Casas Vázquez
    Irene Dacosta Guisado
    José Ignacio Bravo Vicente

Histórico de Versiones:
    - 2024-01-13: Fork de versión inicial con funcionalidad básica.
    - 2024-01-13: Mejoras en la interfaz de usuario y manejo de excepciones.
    - 2024-01-13: Añadida integración con pruebas unitarias automáticas.
    - 2024-01-14: Revisión de formato y separación en módulo operaciones.
    - 2024-01-17: Cambios de formato
"""

from operaciones import sumar, restar, multiplicar, dividir


def mostrar_banner():
    """
    Muestra un banner al inicio de la ejecución con información de la calculadora.
    """
    banner = """
============================================
            CALCULADORA BÁSICA
============================================

Universidad Internacional de La Rioja

Curso: Adaptación al Grado de Informática
Asignatura: Procesos en Ingeniería del Software
Práctica: Diseño de pruebas de software

--------------------------------------------

Autores:
    Cristina Cacho Martín
    Patricia Casas Vázquez
    Irene Dacosta Guisado
    José Ignacio Bravo Vicente

Descripción: 
    Realiza operaciones matemáticas básicas
    como suma, resta, multiplicación y
    división.

============================================
"""
    print(banner)


if __name__ == "__main__":

    mostrar_banner()

    # Repetimos hasta elegir la opción 5
    while True: 
        print(">  Calculadora Básica\n")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir\n")
        
        opcion = input("Elige una operación (1-5): ")

        # salto de linea
        print()
        
        if opcion == "5":
            # Con esta opción salimos del programa calculadora
            print("¡Hasta luego!\n")
            break

        # Según el número seleccionado ejecutamos una opción
        if opcion in ["1", "2", "3", "4"]:
            try:
                a = float(input("Introduce el primer número: "))
                b = float(input("Introduce el segundo número: "))

                # salto de linea
                print()

                if opcion == "1":
                    print(f"La suma de {a} y {b} es: {sumar(a, b)}")
                elif opcion == "2":
                    print(f"La resta de {a} y {b} es: {restar(a, b)}")
                elif opcion == "3":
                    print(f"La multiplicación de {a} y {b} es: {multiplicar(a, b)}")
                elif opcion == "4":
                    print(f"La división de {a} entre {b} es: {dividir(a, b)}")

            except ValueError:
                print("Por favor, introduce valores numéricos válidos.")

            except Exception as e:
                print(f"Error: {e}")
                
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 5.")

        # salto de linea, siguiente
        print()

