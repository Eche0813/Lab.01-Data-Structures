"""
Módulo de Verificación y Lectura Aislada de Matriz.

Este script valida la integridad de la estructura de la matriz en disco,
leyendo únicamente los caracteres necesarios para analizar la Fila 0,
extrayendo las 100,000 columnas e identificando el delimitador '1'.
"""

import os

# ==============================================================================
# CONFIGURACIÓN GLOBAL
# ==============================================================================
# Ruta absoluta del archivo contenedor en disco duro
NOMBRE_ARCHIVO = r"C:\Users\samue\Documents\Personal\University\2026-2\Estructuras\matriz_separador_uno.txt"
COLUMNAS = 100000

# Tamaño exacto de caracteres de la primera fila:
# 100,000 ceros + 99,999 comas + 2 caracteres del delimitador final ',1' = 200,001 caracteres
CARACTERES_PRIMERA_FILA = (COLUMNAS * 2) + 1


def verificar_separador_uno(ruta_archivo: str) -> None:
    """Lee y valida la estructura de la Fila 0 en la matriz masiva.

    Realiza una lectura acotada desde almacenamiento secundario para evitar
    cargados masivos de memoria y exporta un archivo de evidencia con las
    celdas etiquetadas.

    Parameters:
        ruta_archivo (str): Ruta del archivo de texto a verificar.
    """
    # 1. Validación de existencia del archivo
    if not os.path.exists(ruta_archivo):
        print(f"❌ No se encontró el archivo en:\n{ruta_archivo}")
        return

    print("Leyendo la primera fila usando '1' como delimitador de cierre...")

    # 2. Lectura acotada (Streaming): Se leen exactamente 200,001 caracteres del archivo
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        bloque_primera_fila = archivo.read(CARACTERES_PRIMERA_FILA)

    # 3. Parsing del bloque: Se separa el bloque de texto usando la marca ',1'
    filas_segmentadas = bloque_primera_fila.split(",1")
    contenido_fila_0 = filas_segmentadas[0]

    # 4. Parsing de columnas: Se dividen las celdas usando la coma como separador
    columnas = contenido_fila_0.split(",")

    # 5. Impresión de resultados del análisis
    print("\n=== PRUEBA DE ESTRUCTURA ===")
    print(f"Total de caracteres leídos      : {len(bloque_primera_fila):,}")
    print(
        f"Último carácter (Separador fila): '{bloque_primera_fila[-1]}'"
    )
    print(f"Total de columnas extraídas     : {len(columnas):,}")

    # Validación formal
    if len(columnas) == COLUMNAS and bloque_primera_fila[-1] == "1":
        print(
            "✔ ÉXITO: La fila contiene 100,000 celdas y cierra correctamente con el '1'.\n"
        )

    # 6. Generación del reporte de evidencia en texto plano
    carpeta_destino = os.path.dirname(ruta_archivo)
    evidencia_txt = os.path.join(carpeta_destino, "evidencia_separador_uno.txt")

    with open(evidencia_txt, "w", encoding="utf-8") as salida:
        salida.write(
            "=== EVIDENCIA DE FILA CON '1' COMO SEPARADOR DE FILA ===\n\n"
        )

        # Formateo de salida: 10 celdas enumeradas por línea
        for idx, val in enumerate(columnas):
            salida.write(f"[{idx:5d}]: {val:<2s}\t")
            if (idx + 1) % 10 == 0:
                salida.write("\n")

        salida.write(
            f"\n\nMARCA FINAL DE FILA DETECTADA EN EL ARCHIVO: '{bloque_primera_fila[-1]}'\n"
        )

    print(f"✔ Archivo de evidencia exportado a:\n{evidencia_txt}")


# ==============================================================================
# PUNTO DE ENTRADA
# ==============================================================================
if __name__ == "__main__":
    verificar_separador_uno(NOMBRE_ARCHIVO)