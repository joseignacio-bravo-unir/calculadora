"""
operaciones.py

Universidad Internacional de La Rioja

Curso: Adaptación al Grado de Informática
Asignatura: Procesos en Ingeniería del Software
Práctica: Diseño de pruebas de software - Calculadora con pruebas unitarias

Descripción: 
    Este módulo contiene las funciones necesarias para realizar operaciones matemáticas básicas:
    suma, resta, multiplicación y división.

Funciones:
    - sumar(a, b): Calcula la suma de dos números.
    - restar(a, b): Calcula la diferencia entre dos números.
    - multiplicar(a, b): Calcula el producto de dos números.
    - dividir(a, b): Calcula el cociente de dos números, manejando errores como la división por cero.

Uso:
    Importa este módulo en otros scripts o proyectos para utilizar las funciones matemáticas básicas.

Ejemplo:
    >>> from operaciones import sumar, restar, multiplicar, dividir
    >>> sumar(2, 3)
    5
    >>> dividir(10, 2)
    5.0

Autores: 
    Cristina Cacho Martín
    Patricia Casas Vázquez
    Irene Dacosta Guisado
    José Ignacio Bravo Vicente

Histórico de Versiones:
    - 2024-01-13: Fork de versión inicial con funcionalidad básica.
    - 2024-01-14: Revisión de formato y separación en módulo operaciones.
    - 2024-01-16: Añadido verificación solo enteros.
    - 2024-01-17: Añadido verificación para float.
"""

# para verificar desbordamientos
from math import isinf


def verifica_overflow(n):
    """Función auxiliar para verificar si hay posible desbordamiento."""

    return isinstance(n, float) and isinf(n)


def sumar(a, b):
    """
    Calcula la suma de dos números.

    Esta función toma dos números como entrada y devuelve su suma. Es útil para
    realizar operaciones matemáticas básicas.

    Args:
        a (int | float): El primer número a sumar.
        b (int | float): El segundo número a sumar.

    Returns:
        int | float: La suma de los dos números proporcionados.

    Ejemplo:
        >>> sumar(2, 3)
        5
        >>> sumar(-1, 4.5)
        3.5
    """

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        # Lanzamos el error si uno de los dos argumentos no es un número
        raise TypeError("Los argumentos deben ser números.")
    
    if verifica_overflow(a) or verifica_overflow(b):
        # Lanzamos el error si uno de los dos argumentos es flotante y hay desbordamiento
        raise OverflowError("Valores demasiado grandes")

    return a + b


def restar(a, b):
    """
    Calcula la diferencia entre dos números.

    Esta función toma dos números como entrada y devuelve el resultado de restar
    el segundo número al primero.

    Args:
        a (int / float): El minuendo, es decir, el número al que se le resta.
        b (int / float): El sustraendo, es decir, el número que se resta.

    Returns:
        int | float: La diferencia resultante de la operación.

    Ejemplo:
        >>> restar(10, 3)
        7
        >>> restar(5.5, 2)
        3.5
        >>> restar(0, 4)
        -4
    """

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        # Lanzamos el error si uno de los dos argumentos no es un número
        raise TypeError("Los argumentos deben ser números.")

    if verifica_overflow(a) or verifica_overflow(b):
        # Lanzamos el error si uno de los dos argumentos es flotante y hay desbordamiento
        raise OverflowError("Valores demasiado grandes")
    
    return a - b


def multiplicar(a, b):
    """
    Calcula el producto de dos números.

    Esta función toma dos números como entrada y devuelve su producto. Es útil para
    realizar operaciones matemáticas básicas.

    Args:
        a (int | float): El primer número a multiplicar.
        b (int | float): El segundo número a multiplicar.

    Returns:
        int | float: El producto de los dos números proporcionados.

    Ejemplo:
        >>> multiplicar(2, 3)
        6
        >>> multiplicar(-1, 4)
        -4
        >>> multiplicar(0, 5)
        0
    """

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        # Lanzamos el error si uno de los dos argumentos no es un número
        raise TypeError("Los argumentos deben ser números.")

    if verifica_overflow(a) or verifica_overflow(b):
        # Lanzamos el error si uno de los dos argumentos es flotante y hay desbordamiento
        raise OverflowError("Valores demasiado grandes")
    
    return a * b


def dividir(a, b):
    """
    Calcula el cociente de dos números.

    Esta función toma dos números como entrada y devuelve el resultado de dividir
    el primer número entre el segundo. Si el divisor es cero, lanza una excepción
    para evitar errores de ejecución.

    Args:
        a (int | float): El dividendo, es decir, el número que se divide.
        b (int | float): El divisor, es decir, el número por el que se divide.

    Returns:
        float: El cociente resultante de la operación.

    Raises:
        ZeroDivisionError: Si el divisor (b) es igual a cero.

    Ejemplo:
        >>> dividir(10, 2)
        5.0
        >>> dividir(7, -3)
        -2.3333333333333335
        >>> dividir(5, 0)
        ZeroDivisionError: division by zero
    """

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        # Lanzamos el error si uno de los dos argumentos no es un número
        raise TypeError("Los argumentos deben ser números.")

    if verifica_overflow(a) or verifica_overflow(b):
        # Lanzamos el error si uno de los dos argumentos es flotante y hay desbordamiento
        raise OverflowError("Valores demasiado grandes")
    
    if b == 0:
        # Lanzamos el error al intentar dividir por 0
        raise ValueError("El divisor no puede ser cero.") 

    return a / b
