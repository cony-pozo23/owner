# --- Datos proporcionados en la imagen ---
libros = [
    ['Papelucho programador', 'Marcela Paz', 1983],
    ['Don Python de la Mancha', 'Miguel de Cervantes', 1615],
    ['Raw_input y Julieta', 'William Shakespeare', 1597],
    ['La tuplamorfosis', 'Franz Kafka', 1915]
]

datos_autores = {
    # autor: [nacimiento, defuncion, idioma]
    'William Shakespeare': [[1564, 4, 26], [1616, 5, 3], 'inglés'],
    'Franz Kafka': [[1883, 7, 3], [1924, 6, 3], 'alemán'],
    'Marcela Paz': [[1902, 2, 28], [1985, 6, 12], 'español'],
    'Miguel de Cervantes': [[1547, 9, 29], [1616, 4, 22], 'español']
}

# --- Funciones a implementar ---

def obtener_autor(titulo):
    """Busca el título en la lista de libros y retorna el nombre del autor."""
    for libro in libros:
        if libro[0].lower() == titulo.lower(): # .lower() ayuda a evitar problemas de mayúsculas
            return libro[1]
    return None

def obtener_idioma(titulo):
    """Obtiene el autor del libro y luego busca su idioma en el diccionario."""
    autor = obtener_autor(titulo)
    if autor and autor in datos_autores:
        return datos_autores[autor][2] # El idioma está en el índice 2 de la lista del autor
    return "desconocido"

def calcular_annos_antes_de_morir(titulo):
    """Calcula cuántos años pasaron entre la publicación del libro y la muerte del autor."""
    autor = obtener_autor(titulo)
    
    # Buscamos el año de publicación del libro
    anno_publicacion = None
    for libro in libros:
        if libro[0].lower() == titulo.lower():
            anno_publicacion = libro[2]
            break
            
    if autor and anno_publicacion and autor in datos_autores:
        # La fecha de defunción es la segunda lista [1], y el año es el primer elemento [0]
        anno_defuncion = datos_autores[autor][1][0]
        return anno_defuncion - anno_publicacion
    return 0

# --- Flujo principal del programa (de la imagen) ---
titulo = input('Ingrese titulo del libro: ')

# Verificación simple por si el libro no existe en la base de datos
autor_encontrado = obtener_autor(titulo)
if autor_encontrado:
    print('El libro fue escrito en', obtener_idioma(titulo))
    print('por', autor_encontrado)
    print('El autor fallecio', calcular_annos_antes_de_morir(titulo), 'años')
    print('después de haber escrito el libro')
else:
    print('Libro no encontrado en el sistema.')
