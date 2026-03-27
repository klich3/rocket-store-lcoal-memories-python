---
name: rocket-store
description: "Skill to use Rocket-Store for local file-based data persistence. Use when asked to store persistent data, memories, or records locally without a full database server. Perfect for agents needing a simple local storage mechanism."
---

# Rocket-Store Skill

This skill allows you to use the `Rocket-Store` package to store and retrieve data locally as Markdown files (by default). It functions as a lightweight, searchable database using the filesystem.

## Prerequisites

- Python installed in the environment.
- `Rocket-Store` package installed: `pip install Rocket-Store`

## Usage Guide

### Basic Initialization

```python
from Rocketstore import Rocketstore
rs = Rocketstore()
```

### Configuring Data Storage Area

By default, Rocket-Store uses a temporary system directory. You can specify a custom directory:

```python
rs.options(data_storage_area="./my_local_db", data_format=Rocketstore._FORMAT_MARKDOWN)
```

### Storing Data (Post)

```python
# rs.post(collection, key, record, flags)
rs.post("users", "user_1", {"name": "Alice", "age": 30}, Rocketstore._FORMAT_MARKDOWN)
```

### Retrieving Data (Get)

```python
# Get a specific record
result = rs.get("users", "user_1")

# Get all records in a collection
all_users = rs.get("users")

# Wildcard search
search_results = rs.get("users", "user_*")
```

### Deleting Data

```python
# Delete a specific record
rs.delete("users", "user_1")

# Delete an entire collection
rs.delete("users")
```

## Step-by-Step Workflow

1. **Setup**: Ensure the `Rocket-Store` package is installed.
2. **Options**: Set the `data_storage_area` if you want the data to persist in a specific project folder.
3. **Operations**: Use `post`, `get`, and `delete` to manage your local data.
4. **Verification**: Check the specified storage directory to see the JSON files created.

## Manual Verification

Confirm that data is being saved in the directory specified in `data_storage_area`. Each collection will be a subdirectory, and each key will be a Markdown file.
