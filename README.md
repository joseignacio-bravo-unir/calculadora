# Calculadora con Pruebas Unitarias

Este repositorio contiene el desarrollo de una calculadora básica en Python que implementa las cuatro operaciones matemáticas fundamentales (suma, resta, multiplicación y división). También incluye pruebas unitarias diseñadas con la librería `unittest` para garantizar la correcta funcionalidad de cada operación.

El objetivo principal de esta práctica grupal es reforzar habilidades de programación y diseño de pruebas unitarias. Este proyecto fomenta la colaboración en equipo y permite desarrollar competencias clave para garantizar la calidad del software.

El proyecto incluye:

- El programa principal con la funcionalidad de calculadora básica. 
- Una clase o funciones que implementan las operaciones matemáticas básicas: suma, resta, multiplicación y división, asegurando el manejo de errores como la división por cero.
- Pruebas unitarias con casos que abarcan números positivos, negativos, cero y errores.

El código fuente con las operaciones se encuentra en `operaciones.py`, mientras que las pruebas unitarias están en `test_operaciones.py`. El código de la calculadora está en `calculadora_basica.py`.

Para ejecutar el proyecto:

1. Instala Python (si no lo tienes instalado) en tu máquina.
2. Ejecuta la calculadora con el siguiente comando: 
```
$ python calculadora_basica.py
============================================
            CALCULADORA BÁSICA
============================================

Universidad Internacional de La Rioja
Adaptación al Grado de Informática

Asignatura: Procesos en Ingeniería del software
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

Calculadora Básica

1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Salir

Elige una operación (1-5): 3

Introduce el primer número: 2
Introduce el segundo número: 3

La multiplicación de 2.0 y 3.0 es: 6.0

Calculadora Básica

1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Salir

Elige una operación (1-5): 5

¡Hasta luego!
```

3. Ejecuta las pruebas unitarias con el siguiente comando desde la raíz del repositorio:
```
$ python -m unittest test_operaciones.py
--- Probando operación: sumar ---
  -> Probando sumar con argumentos (10, 4), esperando 14...
  -> Probando sumar con argumentos (-5, 7), esperando 2...
  -> Probando sumar con argumentos (-9, -3), esperando -12...

--- Probando operación: restar ---
  -> Probando restar con argumentos (7, 4), esperando 3...
  -> Probando restar con argumentos (-12, 4), esperando -16...
  -> Probando restar con argumentos (-5, -5), esperando 0...

--- Probando operación: multiplicar ---
  -> Probando multiplicar con argumentos (7, 2), esperando 14...
  -> Probando multiplicar con argumentos (-3, 3), esperando -9...
  -> Probando multiplicar con argumentos (-5, -4), esperando 20...

--- Probando operación: dividir ---
  -> Probando dividir con argumentos (12, 3), esperando 4...
  -> Probando dividir con argumentos (15, 5), esperando 3...
  -> Probando dividir con argumentos (8, 0), esperando excepción ValueError...
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

