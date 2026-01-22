import re
from collections import defaultdict

def frecuencia_palabras(palabras, ruta_archivo):
    """Cuenta frecuencia de palabras en archivo."""
    freq = defaultdict(int)
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        texto = f.read().lower()
        texto_limpio = re.sub(r'[^\w\s]', '', texto)
        palabras_archivo = texto_limpio.split()
    
    for pal in palabras_archivo:
        if pal in palabras:
            freq[pal] += 1
    
    return dict(sorted(freq.items()))

# Prueba
palabras_buscar = ['hola', 'mundo', 'python']
print(frecuencia_palabras(palabras_buscar, 'test.txt'))
