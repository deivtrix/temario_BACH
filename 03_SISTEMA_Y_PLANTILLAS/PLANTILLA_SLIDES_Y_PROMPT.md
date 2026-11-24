# 🎨 PLANTILLA MAESTRA DE DIAPOSITIVAS Y PROMPT (NOTEBOOKLM / CANVA / GEMINI)

Usa esta plantilla alineada con [REGLAS_Y_MEMORIA_DOCENTE.md](REGLAS_Y_MEMORIA_DOCENTE.md) para generar presentaciones en formato híbrido (*Cómic de Historia/Versus + Láminas Explicativas Profundas*).

---

## 1. PORTADA ESTRICTA (DIAPOSITIVA 1 — TODO JUNTO, NUNCA EN SLIDES SEPARADAS)

La **Diapositiva 1** debe incluir obligatoriamente estos 4 elementos juntos (prohibido poner la palabra `"TEMA:"` o mandar el Propósito a la diapositiva 2):
1. **Etiqueta** *(solo si es evaluada/refuerzo)*: `👤 ACTIVIDAD INDIVIDUAL`, `👥 ACTIVIDAD GRUPAL` o `🛠️ REFUERZO`.
2. **Tomo y Título exacto:** `TOMO [X]: [NOMBRE_OFICIAL_PARCIAL] — [TÍTULO_DEL_EPISODIO]` (sin nombre del mediador ni fechas).
3. **Propósito LEV:** `[Verbo infinitivo LEV]` + qué haremos hoy.
4. **¿Para qué me sirve en la vida real?:** 1 frase directa conectada con la vida cotidiana o industria.

---

## 2. PROMPT BASE PARA NOTEBOOKLM (9NO EGB A 3RO BGU)

```text
Crea una presentación estilo cómic educativo de [UNIVERSO_DEL_CURSO] en español para estudiantes de [CURSO] ([EDAD] años) basada en el EPISODIO #[N] de FUENTE_[CURSO]_PARCIAL[X]_COMPLETO.md.

REGLA ESTRICTA DE PORTADA (DIAPOSITIVA 1):
- En la PRIMERA diapositiva pon TODO junto: [ETIQUETA_SI_APLICA], el título exacto "TOMO [X]: [TÍTULO_DEL_EPISODIO]" (PROHIBIDO escribir la palabra "Tema:"), el Propósito (con verbo en infinitivo LEV) y "¿Para qué me sirve en la vida real?" en 1 frase. PROHIBIDO mandar el Propósito a una diapositiva aparte.

PROFUNDIDAD Y CONTENIDO (4 SUBTEMAS EN ORDEN):
- Desarrolla estos 4 subtemas con PROFUNDIDAD TÉCNICA REAL (prohibido definiciones superficiales de 1 línea):
  - Paso 1: [SUBTEMA 1 — explicar mecanismo interno / cómo funciona por dentro]
  - Paso 2: [SUBTEMA 2 — explicar mecanismo interno / parámetros reales]
  - Paso 3: [SUBTEMA 3 — comparación visual X vs. Y o qué pasa si se hace mal]
  - Paso 4: [SUBTEMA 4 — aplicación o regla clave de verificación]
- Incluye siempre comparaciones visuales (tablas comparativas, "antes vs. después" o "correcto vs. error") y explica el PORQUÉ interno de cada concepto.

CANDADOS OBLIGATORIOS:
1. Usa ÚNICAMENTE los bloques, instrucciones y componentes de este episodio; PROHIBIDO introducir temas avanzados no vistos aún o inventar código.
2. Si es actividad evaluativa (👤 Individual / 👥 Grupal): ve directo al reto tras el recordatorio técnico y PROHIBIDO regalar el código completo o la solución resuelta.
3. PROHIBIDO poner nombres de profesor/mediador, fechas, "Semana X", entregables amarrados ("sube a Classroom"), "Continuará..." o adelantos del próximo episodio.
```
