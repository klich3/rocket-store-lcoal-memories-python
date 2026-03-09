# Rocket-Store Skill for Python

[English](#english) | [Español](#español)

---

<a name="english"></a>

## English Description

This project provides an integration of the `Rocket-Store` package as an AI **Skill**, allowing AI agents to use the filesystem as a local, persistent, and searchable database using JSON files.

### What is it for?

It's designed for lightweight data storage where a full database server is overkill. It allows storing and retrieving records organized in collections using unique keys.

### Why is it good?

- **High Performance**: Optimized for fast record retrieval.
- **Low Footprint**: No external dependencies or server required—just the filesystem.
- **Searchable**: Supports wildcard searches (`*`, `?`) in both keys and collections.
- **Simple**: Uses standard JSON format for easy inspection and manual editing.

### Use Cases

- **Local JSON Storage**: Store structured data locally like a mini-SQL database.
- **Agent Memory**: Save persistent memories or context for AI agents between sessions.
- **Listings & Catalogs**: Manage simple product catalogs, user lists, or configuration settings.
- **Activity Logs**: Record events or logs that need to be queried later.

### Usage Example (English)

```python
from Rocketstore import Rocketstore
rs = Rocketstore()

# Configure local storage
rs.options(data_storage_area="./my_db", data_format=Rocketstore._FORMAT_JSON)

# Store a memory
rs.post("memory", "last_interaction", {"action": "greet", "timestamp": "2024-03-09"}, Rocketstore._FORMAT_JSON)

# Retrieve all memories
memories = rs.get("memory")
print(memories['result'])
```

---

<a name="español"></a>

## Descripción en Español

Este proyecto proporciona una integración del paquete `Rocket-Store` como un **Skill**, permitiendo a los agentes de IA utilizar el sistema de archivos como una base de datos local, persistente y buscable mediante archivos JSON.

### ¿Para qué sirve?

Está diseñado para el almacenamiento ligero de datos donde un servidor de base de datos completo es excesivo. Permite guardar y recuperar registros organizados en colecciones mediante claves únicas.

### ¿En qué es bueno?

- **Alto Rendimiento**: Optimizado para la recuperación rápida de registros.
- **Bajo Impacto**: Sin dependencias externas ni servidores, solo usa el sistema de archivos.
- **Buscable**: Soporta búsquedas con comodines (`*`, `?`) tanto en claves como en colecciones.
- **Simple**: Utiliza el formato JSON estándar para facilitar la inspección y edición manual.

### Casos de Uso

- **Almacenamiento Local JSON**: Guarda datos estructurados localmente tipo mini-SQL.
- **Memoria de Agentes**: Guarda memorias persistentes o contexto para agentes de IA entre sesiones.
- **Listados y Catálogos**: Gestiona catálogos de productos, listas de usuarios o configuraciones.
- **Logs de Actividad**: Registra eventos que necesiten ser consultados posteriormente.

### Ejemplo de Uso (Español)

```python
from Rocketstore import Rocketstore
rs = Rocketstore()

# Configuración de área de almacenamiento
rs.options(data_storage_area="./mi_base_de_datos", data_format=Rocketstore._FORMAT_JSON)

# Guardar un registro
rs.post("usuarios", "u1", {"nombre": "Ana", "puntos": 100}, Rocketstore._FORMAT_JSON)

# Recuperar con comodín
resultado = rs.get("usuarios", "u*")
print(resultado['result'])
```

---

## Instalación / Installation

```bash
pip install Rocket-Store
```
