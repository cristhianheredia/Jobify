# Jobify — Instrucciones para Claude

Jobify es el sistema personal de Cristhian para gestionar su búsqueda de empleo como Product Designer. El objetivo es encontrar su próximo trabajo con el mayor nivel de preparación y seguimiento posible.

## Objetivo salarial

| Nivel | Salario mensual |
|---|---|
| Mínimo aceptable | $2,000 USD/mes |
| Intermedio | $3,000 USD/mes |
| **Meta real** | **$4,000 – $5,000 USD/mes** |

La meta es conseguir un rol en el rango de $4,000–$5,000/mes. Priorizar oportunidades en ese rango, no descartar automáticamente las intermedias si hay margen de negociación, rechazar cualquier oferta por debajo del mínimo salvo justificación explícita de Cristhian.

---

## Recursos del usuario

- **CV principal (inglés):** `resources/B Cristhian Heredia - Product Designer 2026 ENG-compress.pdf` — documento vigente
- **CV español:** `resources/Cristhian Heredia - Product Designer 2026 ESP-comprimido.pdf` — versión secundaria
- **Base de datos:** `jobs.db` (SQLite) — tablas: `raw_jobs`, `curated_jobs`

Siempre usar el CV en inglés como referencia principal para evaluaciones, cover letters y análisis de fit.

---

## Flujo del sistema

```
SCRAPER (automático)
└─> raw_jobs  (status: "unprocessed")
      ↓
job-scraper-filter.md  (Claude lee raw_jobs, aplica filtros, pre-score)
└─> curated_jobs  (status: "pending_review")
└─> raw_jobs.status → "filtered_pass" / "filtered_reject"
      ↓
Cristhian revisa curated_jobs y elige cuáles analizar
      ↓
job-opportunity-analyzer.md  (análisis profundo, fit score 1-10)
└─> curated_jobs.status → "analyzed"
└─> Si decide aplicar → pipeline de seguimiento
```

### Tablas en jobs.db

**raw_jobs** — todo lo que entra del scraper o se registra manualmente
- Campos: `id, company, role, url, description, location, salary, posted_date, source, status, rejection_reason, scraped_at`
- Status posibles: `unprocessed` → `filtered_pass` / `filtered_reject`

**curated_jobs** — jobs que pasaron el filtro, listos para revisión manual
- Campos: `id, raw_job_id, company, role, url, description, location, salary, pre_score, priority, keywords_matched, green_flags, yellow_flags, red_flags, status, filtered_at, notes`
- Status posibles: `pending_review` → `analyzed` → `applied` / `discarded`

---

## Skills disponibles

En la carpeta `skills/`. Leer el archivo correspondiente como instrucción al activar cada skill.

### Flujo de búsqueda
| Skill | Archivo | Cuándo usar |
|---|---|---|
| Job Scraper Filter | `job-scraper-filter.md` | Después de correr el scraper, para filtrar y pre-puntuar |
| Job Opportunity Analyzer | `job-opportunity-analyzer.md` | Análisis profundo de una oportunidad específica |
| Company Research Brief | `company-research-brief.md` | Investigar empresa antes de aplicar |

### Flujo de aplicación
| Skill | Archivo | Cuándo usar |
|---|---|---|
| Cover Letter Generator | `cover-letter-generator.md` | Redactar cover letter personalizada |
| Application Form Writer | `application-form-writer.md` | Responder formularios de aplicación |
| Design Challenge Strategist | `design-challenge-strategist.md` | Estrategia para retos de diseño |
| Salary Negotiation Advisor | `salary-negotiation-advisor.md` | Negociar oferta y compensación |

### Flujo de entrevistas
| Skill | Archivo | Cuándo usar |
|---|---|---|
| Interview Prep Coach | `interview-prep-coach.md` | Preparar entrevistas, historias STAR, portfolio walkthrough |
| Leadership Narrative Builder | `leadership-narrative-builder.md` | Narrativas de liderazgo para roles senior/lead |

### Marca personal y portfolio
| Skill | Archivo | Cuándo usar |
|---|---|---|
| LinkedIn Content Strategist | `linkedin-content-strategist.md` | Contenido de thought leadership para LinkedIn |
| Personal Brand Amplifier | `personal-brand-amplifier.md` | Visibilidad más allá de LinkedIn |
| Design Community Engagement | `design-community-engagement.md` | Participación en comunidades de diseño |
| Portfolio Case Study Evaluator | `portfolio-evaluator-senior-design.skill.md` | Evaluar case studies del portfolio |
| Case Study Expert | `case study expert.md` | Crear case studies listos para portfolio |
| Design Critique | `design critique expert.md` | Critiques de diseño con feedback estructurado |
| Job Pipeline Manager | `job-pipeline-manager.md` | Seguimiento del pipeline de aplicaciones |

---

## Operaciones frecuentes

### 1. Scrapear — agregar nuevos jobs a raw_jobs
```bash
python3 -m scraper.main              # todas las fuentes
python3 -m scraper.main --sources remoteok remotive  # fuentes específicas
```
`raw_jobs` es el registro histórico permanente. **Nunca se borra ni se resetea.** Cada job entra con `status = 'unprocessed'` y solo se actualiza a `filtered_pass` o `filtered_reject` al curar.

### 2. Curar — filtrar y pre-puntuar los nuevos jobs
```bash
python3 -m scraper.filter
```
Lee todos los `raw_jobs` con `status = 'unprocessed'`, aplica dealbreakers, calcula pre-score e inserta los que pasan en `curated_jobs`. Actualiza `raw_jobs.status` pero **nunca elimina registros**.

Correr bajo demanda cada vez que haya nuevos jobs en `raw_jobs`. El proceso es idempotente: solo toca registros `unprocessed`.

### 3. Registrar un job manual
Cuando Cristhian comparte una URL o descripción, insertarla en `raw_jobs` con `source = 'manual'` y `status = 'unprocessed'`, luego correr el proceso de **curar**.

### 4. Analizar una oportunidad de curated_jobs
Activar `job-opportunity-analyzer.md` con el job que Cristhian elija.

### Analizar una oportunidad
Activar `job-opportunity-analyzer.md` con el job de `curated_jobs` que Cristhian elija.

---

## Comportamiento esperado de Claude

- Al abrir sesión: preguntar "¿Filtramos los nuevos jobs, revisamos el pipeline, o trabajamos en una oportunidad específica?"
- Si hay aplicaciones en `curated_jobs` con `status = 'applied'` sin actualización reciente, recordar hacer seguimiento (meta: 3 veces por semana).
- Siempre leer el CV en inglés antes de generar cualquier material de aplicación.
- No inventar información del CV — si falta algo relevante, preguntar.
- Tono directo y estratégico, no genérico.
