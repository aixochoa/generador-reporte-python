import csv

def generar_reporte(archivo_csv, columna_numerica, archivo_reporte):
    valores = []

    # Leer valores numéricos
    with open(archivo_csv, "r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            try:
                valor = float(fila[columna_numerica])
                valores.append(valor)
            except ValueError:
                continue

    if not valores:
        print("No se encontraron valores numéricos válidos.")
        return

    # Cálculos
    total_registros = len(valores)
    valor_max = max(valores)
    valor_min = min(valores)
    promedio = sum(valores) / total_registros

    # Crear reporte
    with open(archivo_reporte, "w", encoding="utf-8") as f:
        f.write("REPORTE AUTOMÁTICO\n")
        f.write("-------------------\n")
        f.write(f"Total de registros: {total_registros}\n")
        f.write(f"Valor máximo: {valor_max}\n")
        f.write(f"Valor mínimo: {valor_min}\n")
        f.write(f"Promedio: {promedio:.2f}\n")

    print(f"Reporte generado: {archivo_reporte}")
