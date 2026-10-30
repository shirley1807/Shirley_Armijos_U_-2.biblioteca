# ==================================================
# SISTEMA DE GESTIÓN DE BIBLIOTECA — UNIDAD 2
# ==================================================

# R1: Catálogo de libros (Diccionario / HashMap)
catalogo = {}

def registrar_libro(codigo: str, titulo: str, autor: str) -> None:
    if codigo in catalogo:
        print(f"El libro con código {codigo} ya está registrado.")
        return
    catalogo[codigo] = {"titulo": titulo, "autor": autor}
    print(f"Libro registrado: {titulo} — {autor}")

def buscar_libro(codigo: str) -> dict | None:
    libro = catalogo.get(codigo)
    if libro:
        print(f"[{codigo}] {libro['titulo']} — {libro['autor']}")
        return libro
    print(f"No existe libro con código {codigo}")
    return None

# Menú
def menu():
    while True:
        print("\n" + "="*50)
        print("        SISTEMA DE GESTIÓN DE BIBLIOTECA")
        print("="*50)
        print("1. Registrar libro")
print("2. Buscar libro por código")
print("3. Mostrar catálogo ordenado por código")
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
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
    # R2: Catálogo ordenado — simula TreeMap
def mostrar_catalogo_ordenado() -> None:
    if not catalogo:
        print("El catálogo está vacío.")
        return
    print("\n CATÁLOGO ORDENADO POR CÓDIGO:")
    for codigo in sorted(catalogo.keys()):
        libro = catalogo[codigo]
        print(f"  {codigo}: {libro['titulo']} — {libro['autor']}")
