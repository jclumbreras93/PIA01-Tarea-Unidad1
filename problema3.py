def operaciones_conjuntos(lista1, lista2):
    """Intersección, unión y diferencia simétrica con sets."""
    set1 = set(lista1)
    set2 = set(lista2)
    
    resultado = {
        'interseccion': sorted(set1 & set2),
        'union': sorted(set1 | set2),
        'diferencia_simetrica': sorted(set1 ^ set2)
    }
    return resultado

# Prueba
print(operaciones_conjuntos([1, 2, 3, 4], [3, 4, 5, 6]))
# {'interseccion': [3, 4], 'union': [1, 2, 3, 4, 5, 6], 'diferencia_simetrica': [1, 2, 5, 6]}
