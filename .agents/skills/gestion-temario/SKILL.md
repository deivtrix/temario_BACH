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
   - **Banners en `02_CLASES_SEMANALES/`:** Todo archivo semanal debe llevar arriba su banner (`👤 ACTIVIDAD INDIVIDUAL EVALUADA`, `👥 ACTIVIDAD GRUPAL EVALUADA`, `🛠️ REFUERZO Y NIVELACIÓN` o `📘 CLASE SIN ENTREGA`).
   - **Classroom y Preguntas de Cierre:** Solo las clases evaluadas (`Individual` / `Grupal`) llevan `## 📢 TEXTO PARA GOOGLE CLASSROOM`. Las preguntas de cierre en el guion del mediador deben incluir siempre su **respuesta esperada** *(sin mostrar respuestas en los prompts/slides de NotebookLM)*.
   - **Subtemas puntuales (3–4 máx.):** Cada guion semanal en `02_CLASES_SEMANALES/` debe listar sus 3–4 subtemas puntuales y reflejarlos en orden dentro de su `## 🎨 PROMPT PARA NOTEBOOKLM`.

3. **Si cambian temas, fechas o evaluaciones ("actualiza todo"):**
   - Actualizar `00_PANEL_CONTROL.md`.
   - Actualizar el temario maestro correspondiente en `01_TEMARIOS_POR_CURSO/` (y `MAPA_DE_RUTA_CURRICULAR.md` / `malla_curricular_robotica.html` si cambia un eje o herramienta).
   - Actualizar los guiones afectados en `02_CLASES_SEMANALES/`.
   - Actualizar las fuentes correspondientes en `04_PARA_NOTEBOOKLM/` (`FUENTE_<CURSO>_PARCIALX_COMPLETO.md` y `fuentes.md`).
   - Actualizar `03_SISTEMA_Y_PLANTILLAS/REGLAS_Y_MEMORIA_DOCENTE.md` y `INDEX_REPOSITORIO.md` si cambió la estructura o una regla.

4. **Respaldo en GitHub:**
   - Hacer `git add -A`, `git commit -m "..."` y `git push origin main`.
