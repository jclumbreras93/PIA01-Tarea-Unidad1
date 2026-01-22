def procesar_lista_enteros(lista):
    """Elimina negativos, duplicados y ordena."""
    positivos_unicos = sorted(set(x for x in lista if x > 0))
    return positivos_unicos

# Prueba
print(procesar_lista_enteros([4, -1, 2, 4, 3, -5, 2]))  # [2, 3, 4]
