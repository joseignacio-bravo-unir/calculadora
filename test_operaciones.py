"""
test_operaciones.py

Descripción:
    Este módulo contiene la clase de pruebas unitarias para validar las funciones definidas
    en el módulo 'operaciones.py'. Utiliza la librería estándar `unittest` para garantizar 
    que las operaciones matemáticas básicas (suma, resta, multiplicación, división) funcionan 
    correctamente bajo diferentes escenarios, incluidos casos límite.

Clase:
    - TestOperaciones(unittest.TestCase): Define pruebas unitarias para cada operación 
        matemática, comprobando casos normales, casos límite y manejo de errores.

Características:
    - Pruebas para operaciones básicas (suma, resta, multiplicación, división).
    - Validación de resultados esperados en casos con números positivos, negativos y cero.
    - Comprobación del manejo correcto de excepciones, como la división por cero.

Requisitos:
    - Python 3.x
    - El módulo 'operaciones.py' debe estar en el mismo directorio o disponible en el PATH.

Ejemplo de Uso:
    Ejecuta las pruebas con el siguiente comando:
    $ python -m unittest test_operaciones.py

Autores: 
    Cristina Cacho Martín
    Patricia Casas Vázquez
    Irene Dacosta Guisado
    José Ignacio Bravo Vicente

Histórico de Versiones:
    - 2024-01-13: Fork de versión inicial con pruebas básicas.
    - 2024-01-14: Revisión de formato, añadido feedback en tests.
"""

import unittest  # Importa el módulo unittest para realizar pruebas unitarias
from operaciones import sumar, restar, multiplicar, dividir  # Importa las funciones a probar


class TestOperaciones(unittest.TestCase):
    """
    Clase de pruebas unitarias para validar las funciones matemáticas básicas 
    definidas en el módulo 'operaciones.py'.

    Métodos:
        - setUp(): Configura los datos iniciales y define los casos de prueba.
        - Métodos específicos de prueba (test_*): Validan cada operación matemática.
    """
    

    def setUp(self):
        """
        Método que se ejecuta antes de cada prueba para configurar los datos iniciales.

        Configura un diccionario llamado 'operaciones' que contiene:
            - La función asociada a cada operación.
            - Casos de prueba normales con sus argumentos y resultados esperados.
            - Casos de error (si aplican), incluyendo las excepciones esperadas.
        """            
        self.operaciones = {
            # Pruebas para la función sumar
            "sumar": {
                "func": sumar,  # Asocia la función sumar
                "tests": [  
                    {"args": (10, 4), "expected": 14},  
                    {"args": (-5, 7), "expected": 2},  
                    {"args": (-9, -3), "expected": -12},  
                ],
            },

            # Pruebas para la función restar
            "restar": {  
                "func": restar,  # Asocia la función restar
                "tests": [  
                    {"args": (7, 4), "expected": 3},  
                    {"args": (-12, 4), "expected": -16},  
                    {"args": (-5, -5), "expected": 0},  
                ],
            },

            # Pruebas para la función multiplicar
            "multiplicar": {  
                "func": multiplicar,  # Asocia la función multiplicar
                "tests": [  
                    {"args": (7, 2), "expected": 14},  
                    {"args": (-3, 3), "expected": -9},  
                    {"args": (-5, -4), "expected": 20},  
                ],
            },

            # Pruebas para la función dividir
            "dividir": {  
                "func": dividir,  # Asocia la función dividir
                "tests": [  
                    {"args": (12, 3), "expected": 4},  # Caso 1: división exacta
                    {"args": (15, 5), "expected": 3},  # Caso 2: división exacta
                ],

                # Casos que generan errores (como división por cero)
                "errors": [  
                    {"args": (8, 0), "exception": ValueError},  # Caso: división por cero
                ],
            },
        }


    # Define un método de prueba para todas las operaciones
    def test_operaciones(self):
        """
        Método de prueba genérico para validar todas las operaciones definidas en el diccionario 'self.operaciones'.

        Realiza dos tipos de validaciones:
        1. Pruebas normales: Comprueba que las funciones devuelven los resultados esperados para los casos proporcionados.
        2. Pruebas de excepciones: Verifica que las funciones manejan correctamente los errores esperados, como la división por cero.

        Utiliza subtests para ejecutar cada caso de prueba de manera independiente, evitando que un error afecte a otros casos.
        """
        # Recorre cada operación (suma, resta, etc.) definida en el diccionario de pruebas
        for op_name, op_data in self.operaciones.items():
            # Obtiene la función asociada a la operación actual (sumar, restar, etc.)
            func = op_data["func"]  

            # Feedback inicial para la operación
            print(f"\n--- Probando operación: {op_name} ---")

            # Pruebas con resultados esperados:
            for test in op_data.get("tests", []):  # Itera sobre los casos de prueba normales
                with self.subTest(op=op_name, args=test["args"]):  # Subtest para este caso específico
                    print(f"  -> Probando {op_name} con argumentos {test['args']}, esperando {test['expected']}...")
                    # Comprueba que la función da el resultado esperado para los argumentos proporcionados
                    self.assertEqual(func(*test["args"]), test["expected"])

            # Pruebas que esperan excepciones:
            for error_test in op_data.get("errors", []):  # Itera sobre los casos que generan errores
                with self.subTest(op=op_name, args=error_test["args"]):  # Subtest para este caso específico
                    print(f"  -> Probando {op_name} con argumentos {error_test['args']}, esperando excepción {error_test['exception'].__name__}...")
                    # Comprueba que la función lanza la excepción esperada cuando se usan estos argumentos
                    with self.assertRaises(error_test["exception"]):
                        func(*error_test["args"])  


if __name__ == '__main__':
    unittest.main()  
