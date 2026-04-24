# Jobify

Sistema de búsqueda de empleo. Agrega ofertas de múltiples fuentes en una base de datos local.

## Scraper

Módulo en `scraper/` que rastrea ofertas de trabajo remotas desde fuentes públicas.

### Fuentes

| Fuente | Método | Notas |
|---|---|---|
| RemoteOK | API JSON | `https://remoteok.com/api` |
| Remotive | API JSON | `https://remotive.com/api/remote-jobs` |
| We Work Remotely | RSS | 5 categorías (dev, devops, diseño, producto, datos) |
| Arbeitnow | API JSON | Hasta 3 páginas por ejecución |
| HackerNews | API Algolia + Firebase | Hilo mensual "Who is hiring?" |

### Requisitos

```bash
pip3 install httpx
```

### Uso

```bash
# Todas las fuentes
python3 -m scraper.main

# Fuentes específicas
python3 -m scraper.main --sources remoteok remotive

# Ver fuentes disponibles
python3 -m scraper.main --list
```

### Almacenamiento

Los jobs se guardan en `jobs.db` (SQLite). Tabla `jobs`:

| Campo | Tipo | Descripción |
|---|---|---|
| url | TEXT UNIQUE | Enlace a la oferta (clave de deduplicación) |
| title | TEXT | Título del puesto |
| company | TEXT | Empresa |
| source | TEXT | Fuente (remoteok, remotive, etc.) |
| location | TEXT | Ubicación o "Remote" |
| salary | TEXT | Rango salarial si está disponible |
| description | TEXT | Primeros 500 chars de la descripción |
| tags | TEXT | JSON array de etiquetas |
| posted_at | TEXT | Fecha de publicación |
| scraped_at | TEXT | Fecha de scraping |

### Estructura

```
scraper/
├── main.py          # CLI y punto de entrada
├── base.py          # Clase base BaseScraper
├── models.py        # Dataclass Job
├── storage.py       # SQLite (get_db, save_job)
└── sources/
    ├── remoteok.py
    ├── remotive.py
    ├── weworkremotely.py
    ├── arbeitnow.py
    └── hackernews.py
```
