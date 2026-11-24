---
name: gestion-temario
description: Checklist obligatorio para actualizar el diario de clases, notas, temarios, planificación semanal, memoria docente y GitHub en temario_BACH. Activar siempre que el usuario diga "actualiza todo", reporte clases dadas/perdidas, o modifique temas/fechas.
---

# 🎓 Gestión Integral de `temario_BACH`

Cuando el usuario reporte novedades de clases, pida un reporte o diga **"actualiza todo"**, ejecuta este checklist completo sin omitir capas:

1. **Registro Diario y Estado de 21 Paralelos:**
   - Actualizar `03_SISTEMA_Y_PLANTILLAS/diario_data.json` (estado `dada` / `perdida` / `alcance` + motivo/nota).
   - Regenerar/actualizar `DIARIO_CLASES.md` (Tablero de Decisiones Activas, Registro Semanal y Control de Notas `2 Ind + 1 Grupal + 1 Refuerzo`).
   - Actualizar `CONTROL_CALENDARIO_PARALELOS.md` (corte actual y bitácora de incidencias).

2. **Reglas Operativas Clave:**
   - **Cero choque de kits físicos Arduino:** `10MO EGB` y `1RO BGU` nunca hacen taller grupal físico en la misma semana (`10mo` en S6, `1ro BGU` en S7). Primero es simulación virtual, luego montaje físico.
   - **3ro BGU:** Avance progresivo independiente (6 clases/parcial).
   - **Banners y Slides en `02_CLASES_SEMANALES/`:** Organizar siempre por **Semana** (`PARCIAL_X/SEMANA_XX/`). Todo archivo semanal lleva arriba su banner (`👤 ACTIVIDAD INDIVIDUAL EVALUADA`, `👥 ACTIVIDAD GRUPAL EVALUADA`, `🛠️ REFUERZO Y NIVELACIÓN` o `📘 CLASE SIN ENTREGA`) y la línea **`📊 Slides: Sección X (Láminas Y–Z)`** (sin prompts largos de NotebookLM al pie). El Propósito y el Cierre diarios se ejecutan en vivo desde el guion, no en slides aparte.
   - **Classroom, Roles y Preguntas de Cierre:** Solo las clases evaluadas (`Individual` / `Grupal`) llevan `## 📢 TEXTO PARA GOOGLE CLASSROOM`. Toda `👥 Grupal` define **3 roles rotativos**, las prácticas incluyen el **Protocolo de Autodepuración en 3 pasos**, y en `10mo–3ro BGU` (código/lógica) se aplica **Predicción PRIMM (30 seg)** antes de simular. Las preguntas de cierre se aplican con **respuesta simultánea (dedos/pulgar) o Cold Call al azar**, e incluyen en el guion su **respuesta esperada** *(sin mostrar respuestas en los slides ni en la ficha de examen)*.
   - **Subtemas puntuales (máx. 2 nuevos/clase, sin repetir) y `04_PARA_NOTEBOOKLM/`:** Cada clase aporta máx. 2 subtemas nuevos y servibles (cero repeticiones). Los prompts de NotebookLM viven centralizados en `04_PARA_NOTEBOOKLM/<CURSO>/PARCIAL_X/PROMPTS_BLOQUES.md` (Tomo de Cómic dividido en `SECCIÓN 1` y `SECCIÓN 2` de `10–12` slides con Agente Pedagógico 80/20 + Prompt 3 Repaso/Examen + Prompt 4 Video sin personajes), junto a `FUENTE_<CURSO>_PARCIALX_COMPLETO.md` y `fuentes.md`.

3. **Si cambian temas, fechas o evaluaciones ("actualiza todo"):**
   - Actualizar `00_PANEL_CONTROL.md`.
   - Actualizar el temario maestro correspondiente en `01_TEMARIOS_POR_CURSO/` (y `MAPA_DE_RUTA_CURRICULAR.md` / `malla_curricular_robotica.html` si cambia un eje o herramienta).
   - Actualizar los guiones afectados en `02_CLASES_SEMANALES/`.
   - Actualizar las fuentes correspondientes en `04_PARA_NOTEBOOKLM/` (`FUENTE_<CURSO>_PARCIALX_COMPLETO.md` y `fuentes.md`).
   - Actualizar `03_SISTEMA_Y_PLANTILLAS/REGLAS_Y_MEMORIA_DOCENTE.md` y `INDEX_REPOSITORIO.md` si cambió la estructura o una regla.

4. **Auditoría de Documentación y Limpieza (Cero archivos muertos):**
   - Cada carpeta `04_PARA_NOTEBOOKLM/<CURSO>/PARCIAL_X/` debe tener **exactamente 3 archivos**: `FUENTE_<CURSO>_PARCIALX_COMPLETO.md` (solo teoría puntual y retos, cero guion docente), `fuentes.md` y `PROMPTS_BLOQUES.md` (Prompts 1–4).
   - Cada guion en `02_CLASES_SEMANALES/PARCIAL_X/SEMANA_XX/` debe tener su **banner superior**, **`📊 Slides: Sección X`**, **`Propósito` + `¿Cómo sé que lo logré?`** y cero prompts largos al pie.
   - Eliminar archivos sueltos duplicados, `__pycache__` o parciales obsoletos/inactivos según indicación del mediador.

5. **Respaldo en GitHub:**
   - Hacer `git add -A`, `git commit -m "..."` y `git push origin main`.
