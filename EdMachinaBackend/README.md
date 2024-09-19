# EdMachina Backend

## Configuiracion del entorno

### 1. Entorno virtual

1. Crear un entorno virtual (en el ejemplo se muestra como hacerlo con Conda)

```bash
conda create --name edmachina python=3.10.14
```

2. Activar el entorno virtual

```bash
conda activate edmachina
```

3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

## Migracion de base de datos

### 2. Base de datos

1. Necesita tener configurada una bas de datos postgres llamada ed-machina

2. Modificar cadena de conexión en la variable DATABASE_URL en `db.py`

3. Iniciar alembic

```bash
alembic.ini
```

4. Ejecutar migracion para la base de datos

```bash
alembic revision -m "Mensaje de migración"
```

5. Aplicar la migracion

```bash
alembic upgrade head
```

## Ejecutar aplicacion

### 3. Ejecucion

```bash
uvicorn  main:app --reload
```

### 4. Tests unitarios

```bash
pytest
```
