from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import List
import json
import os
from datetime import datetime

app = FastAPI(
    title="Notes API",
    description="Una API simple para gestionar notas de texto",
    version="1.0.0"
)

# Modelo para el contenido de la nota
class NoteContent(BaseModel):
    content: str

# Directorio y archivo donde se guardarán las notas
DATA_DIR = os.getenv("DATA_DIR", "./data")
NOTES_FILE = os.path.join(DATA_DIR, "notes.json")

# Crear directorio de datos si no existe
os.makedirs(DATA_DIR, exist_ok=True)

def load_notes() -> List[dict]:
    """Cargar notas desde el archivo JSON"""
    if not os.path.exists(NOTES_FILE):
        return []
    
    try:
        with open(NOTES_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_notes(notes: List[dict]) -> None:
    """Guardar notas en el archivo JSON"""
    with open(NOTES_FILE, 'w', encoding='utf-8') as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)

@app.get("/")
async def root():
    """Endpoint raíz que indica que la API está activa"""
    instance_title = os.getenv("INSTANCE_TITLE", "API de Notas")
    instance_id = os.getenv("INSTANCE_ID", "default")
    pod_name = os.getenv("POD_NAME", "unknown")
    pod_ip = os.getenv("POD_IP", "unknown")
    
    return {
        "message": "La API de notas está activa y funcionando correctamente",
        "instance": instance_title,
        "instance_id": instance_id,
        "pod_name": pod_name,
        "pod_ip": pod_ip,
        "status": "active",
        "timestamp": datetime.now().isoformat()
    }

@app.post("/add/{title}")
async def add_note(
    title: str = Path(..., description="El título de la nota"),
    note_content: NoteContent = None
):
    """Agregar una nueva nota con título y contenido"""
    # Cargar notas existentes
    notes = load_notes()
    
    # Crear nueva nota con timestamp e ID único
    new_note = {
        "id": len(notes) + 1,
        "title": title,
        "content": note_content.content if note_content else "",
        "timestamp": datetime.now().isoformat()
    }
    
    # Agregar la nueva nota
    notes.append(new_note)
    
    # Guardar todas las notas
    save_notes(notes)
    
    return {
        "message": "Nota agregada exitosamente",
        "note": new_note
    }

@app.get("/list")
async def list_notes():
    """Listar todas las notas creadas"""
    notes = load_notes()
    
    return {
        "message": f"Se encontraron {len(notes)} nota(s)",
        "total_notes": len(notes),
        "notes": notes
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
