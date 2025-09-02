# API de Notas

Una API simple en Python usando FastAPI para gestionar notas de texto.

## Características

- **Endpoint raíz**: Verifica que la API está activa
- **Agregar notas**: Permite guardar notas con título y contenido
- **Listar notas**: Muestra todas las notas guardadas
- **Persistencia**: Las notas se guardan en un archivo JSON
- **Timestamps**: Cada nota incluye fecha y hora de creación
- **Estructura completa**: Cada nota tiene ID, título, contenido y timestamp

## Instalación

1. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

### Ejecutar la API

```bash
python main.py
```

La API estará disponible en: `http://localhost:8000`

### Endpoints

#### 1. Verificar estado de la API
```
GET /
```

**Respuesta:**
```json
{
  "message": "La API de notas está activa y funcionando correctamente",
  "status": "active",
  "timestamp": "2024-01-15T10:30:00.123456"
}
```

#### 2. Agregar una nota
```
POST /add/{title}
```

**Parámetros:**
- `title` (string): El título de la nota (en la URL)
- `content` (string): El contenido de la nota (en el body JSON)

**Ejemplo:**
```bash
curl -X POST "http://localhost:8000/add/Mi%20Primera%20Nota" \
  -H "Content-Type: application/json" \
  -d '{"content": "Este es el contenido completo de mi primera nota"}'
```

**Ejemplo con HTTPie:**
```bash
http POST localhost:8000/add/"Mi Primera Nota" content="Contenido de la nota"
```

**Body JSON:**
```json
{
  "content": "Este es el contenido completo de la nota"
}
```

**Respuesta:**
```json
{
  "message": "Nota agregada exitosamente",
  "note": {
    "id": 1,
    "title": "Mi Primera Nota",
    "content": "Este es el contenido completo de mi primera nota",
    "timestamp": "2024-01-15T10:30:00.123456"
  }
}
```

#### 3. Listar todas las notas
```
GET /list
```

**Ejemplo:**
```bash
curl -X GET "http://localhost:8000/list"
```

**Respuesta:**
```json
{
  "message": "Se encontraron 2 nota(s)",
  "total_notes": 2,
  "notes": [
    {
      "id": 1,
      "title": "Mi Primera Nota",
      "content": "Este es el contenido completo de mi primera nota",
      "timestamp": "2024-01-15T10:30:00.123456"
    },
    {
      "id": 2,
      "title": "Lista de Tareas",
      "content": "1. Revisar código\n2. Hacer deploy\n3. Documentar API",
      "timestamp": "2024-01-15T10:31:00.123456"
    }
  ]
}
```

## Documentación Automática

FastAPI genera documentación automática:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Estructura del Proyecto

```
.
├── main.py           # Archivo principal de la API
├── requirements.txt  # Dependencias del proyecto
├── README.md        # Este archivo
└── notes.json       # Archivo donde se guardan las notas (se crea automáticamente)
```

## Ejecución con Docker

### Usando Docker Compose (recomendado)
```bash
docker-compose up -d
```

### Usando Docker directamente
```bash
# Construir la imagen
docker build -t api-notas .

# Ejecutar el contenedor
docker run -d -p 8000:8000 --name api-notas-container api-notas
```

## Notas Técnicas

- Las notas se guardan en un archivo `notes.json` que se crea automáticamente
- Cada nota tiene un ID único, título, contenido y timestamp
- La API usa FastAPI con uvicorn como servidor ASGI
- Codificación UTF-8 para soporte de caracteres especiales
- El título se pasa como parámetro en la URL
- El contenido se envía en el body como JSON
# api-notas
