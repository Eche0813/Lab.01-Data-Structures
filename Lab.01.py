"""
Módulo de Generación de Matriz de Gran Tamaño en Texto Plano.

Este script crea una matriz de 100,000 x 100,000 elementos almacenada en disco
utilizando comas (',') como delimitador de columna y el carácter '1' (',1') 
como delimitador de fin de fila en lugar del salto de línea estándar ('\n').
"""

import os

# ==============================================================================
# CONFIGURACIÓN GLOBAL
# ==============================================================================
# Ruta absoluta del archivo contenedor en disco duro
NOMBRE_ARCHIVO = r"C:\Users\samue\Documents\Personal\University\2026-2\Estructuras\matriz_separador_uno.txt"

# Dimensiones de la matriz bidimensional
FILAS = 100000
COLUMNAS = 100000


def generar_matriz_separador_uno(
    ruta_salida: str, total_filas: int, total_columnas: int
) -> None:
    """Genera y escribe la matriz de 100k x 100k en el disco duro.

    Aplica escritura en buffer por filas para mantener el uso de memoria RAM

    constante en ~200 KB durante todo el proceso de escritura.

    Parameters:
        ruta_salida (str): Ruta completa donde se creará el archivo de texto.
        total_filas (int): Número total de filas a escribir.
        total_columnas (int): Número de columnas por cada fila.
    """
    # 1. Construcción del buffer de una sola fila en RAM:
    # 100,000 '0's unidos por comas + el delimitador de cierre de fila ',1'
    # Tamaño por fila: 199,999 caracteres de datos/comas + 2 del delimitador = 200,001 caracteres
    fila_texto = ",".join(["0"] * total_columnas) + ",1"

    print(f"Iniciando generación de matriz ({total_filas}x{total_columnas})...")
    print(f"Ruta de destino: {ruta_salida}\n")

    # 2. Apertura del archivo en modo escritura de texto con codificación UTF-8
    with open(ruta_salida, "w", encoding="utf-8") as archivo:
        for i in range(total_filas):
            # Escritura directa en disco (o buffer del SO) de la fila actual
            archivo.write(fila_texto)

            # Control de progreso cada 10,000 filas procesadas
            if (i + 1) % 10000 == 0:
                print(
                    f"Progreso de escritura: {i + 1:,} / {total_filas:,} filas completadas"
                )

    print("\n✔ Matriz guardada exitosamente con '1' como separador de fila.")


# ==============================================================================
# PUNTO DE ENTRADA
# ==============================================================================
if __name__ == "__main__":
    generar_matriz_separador_uno(NOMBRE_ARCHIVO, FILAS, COLUMNAS)