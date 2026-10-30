# Gestión de Biblioteca — Unidad 2
**Asignatura:** Estructuras de Datos
**Estudiante:** Shirley Armijos

## Descripción
Programa de consola en Python que administra el catálogo de libros y el registro de socios de una biblioteca, usando diccionarios y conjuntos.

## Estructuras utilizadas

| Requerimiento | Estructura | Uso |
|---|---|---|
| R1 — Catálogo de libros | `dict` (HashMap) | Clave = código del libro; búsqueda inmediata O(1) |
| R2 — Listado ordenado | `sorted()` → simula TreeMap | Muestra libros ordenados por código automáticamente |
| R3 — Registro de socios | `set` (Conjunto) | Evita duplicados; verificación rápida O(1) |

## Cómo ejecutar
```bash
python biblioteca.py
