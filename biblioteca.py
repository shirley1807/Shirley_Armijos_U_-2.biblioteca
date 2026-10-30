# ==================================================
# SISTEMA DE GESTIÓN DE BIBLIOTECA - UNIDAD 2
# Estructuras usadas: dict, set, sorted()
# ==================================================

# ------------------
# R1: Catálogo de libros (Diccionario / HashMap)
# Clave: código del libro | Valor: diccionario con título y autor
# ------------------
catalogo = {}

def registrar_libro(codigo: str, titulo: str, autor: str) -> None:
    """Registra un libro en el catálogo usando su código como clave única."""
    if codigo in catalogo:
        print(f"El libro con código {codigo} ya está registrado.")
        return
    catalogo[codigo] = {"titulo": titulo, "autor": autor}
    print(f"Libro registrado: {titulo} — {autor}")

def buscar_libro(codigo: str) -> dict | None:
    """Busca un libro por su código (acceso O(1) en diccionario)."""
    libro = catalogo.get(codigo)
    if libro:
        print(f"[{codigo}] {libro['titulo']} — {libro['autor']}")
        return libro
    print(f"No existe libro con código {codigo}")
    return None

# ------------------
# R2: Catálogo ordenado (simulación de TreeMap)
# ------------------
def mostrar_catalogo_ordenado() -> None:
    """Muestra el catálogo ordenado por código, equivalente al comportamiento de TreeMap."""
    if not catalogo:
        print("El catálogo está vacío.")
        return
    print("\n CATÁLOGO ORDENADO POR CÓDIGO:")
    for codigo in sorted(catalogo.keys()):
        libro = catalogo[codigo]
        print(f"  {codigo}: {libro['titulo']} — {libro['autor']}")

# ------------------
# R3: Socios registrados (Conjunto / Set)
# ------------------
socios_registrados = set()

def registrar_socio(id_socio: str) -> None:
    """Registra un socio evitando duplicados automáticamente (propiedad de conjunto)."""
    if id_socio in socios_registrados:
        print(f"El socio {id_socio} ya está registrado.")
        return
    socios_registrados.add(id_socio)
    print(f"Socio {id_socio} registrado correctamente.")

def verificar_socio(id_socio: str) -> bool:
    """Verifica si un socio está registrado (búsqueda O(1) en conjunto)."""
    existe = id_socio in socios_registrados
    estado = "ACTIVO" if existe else "NO REGISTRADO"
    print(f"Socio {id_socio}: {estado}")
    return existe

# ------------------
# Menú principal
# ------------------
def menu():
    while True:
        print("\n" + "="*50)
        print("        SISTEMA DE GESTIÓN DE BIBLIOTECA")
        print("="*50)
        print("1. Registrar libro")
        print("2. Buscar libro por código")
        print("3. Mostrar catálogo ordenado por código")
        print("4. Registrar socio")
        print("5. Verificar estado de socio")
        print("6. Salir")
        print("="*50)
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            codigo = input("Código del libro: ").strip()
            titulo = input("Título: ").strip()
            autor = input("Autor: ").strip()
            registrar_libro(codigo, titulo, autor)
        
        elif opcion == "2":
            codigo = input("Código del libro a buscar: ").strip()
            buscar_libro(codigo)
        
        elif opcion == "3":
            mostrar_catalogo_ordenado()
        
        elif opcion == "4":
            id_socio = input("Identificador del socio: ").strip()
            registrar_socio(id_socio)
        
        elif opcion == "5":
            id_socio = input("Identificador del socio: ").strip()
            verificar_socio(id_socio)
        
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

# ------------------
# Ejecución
# ------------------
if __name__ == "__main__":
    menu()