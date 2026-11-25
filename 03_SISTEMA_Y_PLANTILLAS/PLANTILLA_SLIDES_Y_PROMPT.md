# 🎨 PLANTILLA MAESTRA DE CÓMIC POR TOMOS Y SECCIONES (NOTEBOOKLM / GEMINI)

Usa esta plantilla alineada con [REGLAS_Y_MEMORIA_DOCENTE.md](REGLAS_Y_MEMORIA_DOCENTE.md) para generar **2 Secciones por Tomo/Parcial** (`10–12` slides por sección = `20–24` slides totales por parcial) + **Prompt 3 (Repaso)** + **Prompt 4 (Video)**.

---

## 1. PORTADA ESTRICTA (SLIDE 1 DE CADA SECCIÓN — TODO JUNTO)

La **Diapositiva 1** de cada sección debe incluir obligatoriamente estos 4 elementos juntos (prohibido poner la palabra `"TEMA:"` o nombrar el curso):
1. **Tomo y Sección:** `TOMO [X]: [NOMBRE_OFICIAL_PARCIAL] — SECCIÓN [1 ó 2]` (sin nombre del mediador ni fechas).
2. **Propósito de la Sección:** `[Verbo infinitivo]` + qué lograremos en esta sección *(sin escribir "LEV"; el propósito diario va en vivo, no en slides aparte)*.
3. **Conexión real:** `¿Dónde lo usas?` + 1 frase directa según la edad del curso.
4. **Escena de Cómic:** El universo del tomo presentando el problema central de la sección.

---

## 2. PROMPT BASE PARA SECCIÓN 1 O SECCIÓN 2 (`PROMPTS_BLOQUES.md`)

```text
Crea una presentación estilo cómic educativo de MÁXIMO 10 a 12 diapositivas en español para estudiantes de [CURSO] ([EDAD] años) basada únicamente en las CLASES [X a Y] de FUENTE_[CURSO]_PARCIAL[N]_COMPLETO.md.

ESTILO VISUAL (CÓMIC + AGENTE PEDAGÓGICO):
- Diapositiva 1 (Portada/Gancho) y última diapositiva (Cierre): escena completa de cómic del universo de [UNIVERSO_DEL_CURSO].
- En todas las láminas de teoría técnica: estilo página de cómic limpia donde el diagrama/tabla/código ocupa casi toda la lámina sobre fondo claro y un personaje guía de [UNIVERSO_DEL_CURSO] va pequeño en una esquina señalando el punto clave o dando 1 consejo corto (PROHIBIDO dibujar porcentajes en la imagen, globos gigantes o tramas tapando diagramas).

PORTADA (DIAPOSITIVA 1 — TODO JUNTO):
- Título exacto: "TOMO [N]: [NOMBRE_OFICIAL_PARCIAL] — SECCIÓN [1/2]" (PROHIBIDO escribir "Tema:", fechas, nombre de profesor o el nombre del curso).
- "Propósito:" (verbo en infinitivo, sin decir "LEV") + "¿Dónde lo usas?" (1 frase cotidiana para [EDAD] años).

ESTRUCTURA SIN REPETICIONES (2 A 4 SLIDES POR CLASE — SIN SLIDES DE PROPÓSITO/CIERRE DIARIO):
- Clase [A] — [Título]:
  - 2 Láminas Ancla de teoría puntual (1 idea por lámina: cómo funciona por dentro con diagrama/flechas + regla práctica + "Correcto vs. Error").
  - [Si es 10mo–3ro BGU con código nuevo: incluir 1 Ejemplo Resuelto anotado de 4–8 líneas antes del reto].
  - 1 Lámina de Reto/Práctica [Agregar etiqueta 👤 ACTIVIDAD INDIVIDUAL / 👥 ACTIVIDAD GRUPAL si aplica; si es grupal incluir 3 roles rotativos].
- Clase [B] — [Título]:
  - (Misma regla: solo 1–2 subtemas NUEVOS sin repetir lo ya explicado en la Clase [A]) + 1 Lámina de Reto.
- [En Sección 2, incluir al final 1 diapositiva exclusiva de Autoevaluación con Escala de Likert (1 al 5) en 4 aspectos concretos del parcial].

CANDADOS OBLIGATORIOS:
1. RIGOR TÉCNICO Y ESPAÑOL 100%: Usa términos técnicos reales de la fuente (PROHIBIDO metáforas mágicas/infantiles o teoría universitaria compleja). Todo texto visible —incluidos rótulos de cajas como "Objetivo" o "Alerta"— debe ir en ESPAÑOL.
2. COBERTURA COMPLETA: Enumera y cubre OBLIGATORIAMENTE todos los temas y eslabones técnicos listados arriba sin saltarse ninguno.
3. SEGURIDAD Y ALCANCE: Usa ÚNICAMENTE los componentes, bloques e instrucciones vistos en estas clases respetando las reglas de seguridad técnica del nivel; PROHIBIDO inventar código o adelantar temas futuros.
4. Si hay actividad evaluada (👤/👥): PROHIBIDO regalar el código completo, la tabla llena o la solución resuelta.
5. PROHIBIDO poner fechas, "Semana X", nombres de docente o "sube a Classroom".
```

---

## 3. PROMPT 3 — REPASO Y EXAMEN (Ficha Resumen + 10 Preguntas)

```text
Basado en FUENTE_[CURSO]_PARCIAL[N]_COMPLETO.md, genera un documento de repaso para examen con:
1. FICHA RESUMEN DE 1 PÁGINA: Tabla/mapa visual con los ~12 conceptos clave y reglas prácticas de todo el parcial (sin relleno, texto plano limpio).
2. BANCO DE 10 PREGUNTAS TIPO EXAMEN: Casos prácticos cortos ("Si pasa X, ¿por qué falló Y?") que conecten los temas del parcial, SIN mostrar respuestas.
```

---

## 4. PROMPT 4 — VIDEO DE REPASO (Studio -> Video)

```text
Crea un Video de Repaso teórico ordenado de todo el parcial basado en FUENTE_[CURSO]_PARCIAL[N]_COMPLETO.md para estudiantes de [EDAD] años.
Usa gráficos, esquemas y diagramas claros con ejemplos cercanos a su edad (PROHIBIDO usar personajes de cómics o mencionar fechas, semanas o nombre de docente).
```
