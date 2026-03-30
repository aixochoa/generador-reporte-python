# Generador Automático de Reportes

Este proyecto es un script en Python que genera un reporte automático a partir de un archivo CSV.  
Calcula totales, valores máximos y mínimos, y el promedio de una columna numérica seleccionada.

## Funcionalidades
- Lectura automática de archivos CSV  
- Extracción de valores numéricos  
- Cálculo de estadísticas básicas  
- Generación de un archivo de reporte en formato `.txt`  

## Uso
```python
generar_reporte("datos.csv", "precio", "reporte.txt")
