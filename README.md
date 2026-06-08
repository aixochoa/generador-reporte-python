#  Generador Automático de Reportes

Script en Python que procesa archivos CSV y genera reportes automáticos 
con estadísticas básicas de cualquier columna numérica.

---

##  Funcionalidades

- Lectura automática de archivos CSV
- Extracción de valores numéricos
- Cálculo de estadísticas básicas (total, promedio, máximo y mínimo)
- Genera reporte automático en formato .txt

---

##  Tecnologías utilizadas

- Python 3
- Pandas
- CSV

---

##  Cómo usarlo

1. Clonar el repositorio
git clone https://github.com/aixochoa/generador-reporte-python

2. Instalar dependencias
pip install pandas

3. Ejecutar el script
python generador_reporte.py

4. Ejemplo de uso
generar_reporte("datos.csv", "precio", "reporte.txt")

---

##  Ejemplo de salida

=== REPORTE ESTADÍSTICO ===
Columna analizada: precio
Total: 15,430.00
Promedio: 257.17
Valor máximo: 980.00
Valor mínimo: 12.50

---

## Autor
Aixo Ochoa
Estudiante de Medicina (UBA) & Análisis de Datos | Talento Tech
[github.com/aixochoa](https://github.com/aixochoa)
