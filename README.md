# Laboratorio 01 - Estructuras de Datos: Matriz Masiva en Disco - Samuel Echeverri Ortiz

Este proyecto implementa la generación y lectura por bloques (streaming) de una matriz de **100,000 × 100,000** en almacenamiento secundario. 

Para este ejercicio se diseñó un formato delimitado que optimiza el espacio y permite la lectura por flujos acotados sin saturar la memoria RAM.

---

## 🛠️ Estructura y Formato de la Matriz

- **Dimensiones:** 100,000 filas × 100,000 columnas ($10^{10}$ elementos).
- **Separador de columnas:** Coma `,`
- **Separador de filas:** Carácter `1` (delimitador de cierre `,1`).
- **Gestión de Memoria:** Tanto la escritura como las lecturas se realizan por buffers acotados (~200 KB a 400 KB) para evitar cargar los ~20 GB del archivo en la RAM.

---

## 📁 Archivos del Repositorio

- `Lab.01.py`: Script principal que genera y escribe la matriz en disco.
- `Pruebas_separador_1 Lab.01.py`: Script de prueba que lee la Fila 0 mediante streaming y extrae las 100,000 columnas.
- `evidencia_separador_uno.txt`: Muestra en texto etiquetado de la Fila 0 procesada.
- `.gitignore`: Configurado para ignorar el archivo masivo de datos (`.txt`/`.csv`) y evitar subirlo al repositorio.

---

## 🚀 Instrucciones de Ejecución (Python)

1. **Generar la matriz localmente:**
   ```bash
   python Lab.01.py
