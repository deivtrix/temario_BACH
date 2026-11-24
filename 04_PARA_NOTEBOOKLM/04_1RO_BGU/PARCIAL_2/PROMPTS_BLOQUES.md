# 🎨 PROMPTS POR BLOQUES — 1RO BGU / PARCIAL 2

> **Archivo fuente a subir:** `FUENTE_1RO_BGU_PARCIAL2_COMPLETO.md` | **Universo:** Tortugas Ninja | **Edad:** 15–16 años

---

## 📦 PROMPT 1 — SECCIÓN 1 (Capítulos 1 a 3 | 10–12 slides)

```text
Crea una presentación educativa de MÁXIMO 10 a 12 diapositivas en español para estudiantes de 15-16 años basada únicamente en los CAPÍTULOS 1, 2 y 3 de FUENTE_1RO_BGU_PARCIAL2_COMPLETO.md.

ESTILO VISUAL (CÓMIC + AGENTE PEDAGÓGICO 80/20):
- Diapositiva 1 (Portada/Gancho) y última diapositiva (Cierre): escena completa de cómic de las Tortugas Ninja.
- En todas las láminas de teoría técnica: página de cómic limpia donde el 80% es el diagrama/tabla/código grande sobre fondo claro y el 20% es un personaje guía de las Tortugas Ninja pequeño en una esquina señalando el punto clave o dando 1 consejo corto (PROHIBIDO globos gigantes o tramas tapando diagramas).

PORTADA (DIAPOSITIVA 1 — TODO JUNTO):
- Título exacto: "TOMO 2: Señales Analógicas y Regulación PWM — SECCIÓN 1" (PROHIBIDO escribir "Tema:", fechas, nombre de profesor o el nombre del curso).
- "Propósito:" (verbo en infinitivo, sin decir "LEV") + "¿Dónde lo usas?" (1 frase cotidiana para 15-16 años).

ESTRUCTURA SIN REPETICIONES (3–4 SLIDES POR CLASE):
- Clase 1 y 2 — Potenciómetro (analogRead) + 4 LEDs con > y < (👤 ACTIVIDAD INDIVIDUAL 1 y 2):
  - 2 Láminas Ancla: (1) Señal digital (0/1) vs. analógica (0–1023 en pines A0–A5) y divisor de voltaje interno del potenciómetro y (2) Rangos con condicionales > y < + Ejemplo Resuelto anotado (5 líneas leyendo A0 y evaluando un umbral).
  - 1 Lámina de Reto: Informe y cuestionario de potenciómetro con 4 LEDs.
- Clase 3 — Atenuador de Brillo LED (map() + PWM analogWrite):
  - 2 Láminas Ancla (SIN repetir analogRead): (1) Qué es PWM por dentro (pulsos rápidos ON/OFF en pines ~, rango 0–255) y (2) Cómo funciona map(valor, 0, 1023, 0, 255) + Ejemplo Resuelto anotado (4 líneas).
  - 1 Lámina de Reto: Práctica en Tinkercad y kit físico con Protocolo de Autodepuración en 3 pasos.
- Cierre de la Sección 1: 3 preguntas relámpago de verificación (SIN respuestas visibles).

CANDADOS OBLIGATORIOS:
1. Usa ÚNICAMENTE las instrucciones vistas (analogRead, map, analogWrite, if/else); PROHIBIDO adelantar LDR o tone().
2. En actividades evaluadas (👤): PROHIBIDO regalar el código completo de los 4 LEDs resuelto.
3. PROHIBIDO poner fechas, "Semana X", nombres de docente o "sube a Classroom".
```

---

## 📦 PROMPT 2 — SECCIÓN 2 (Capítulos 4 a 7 | 10–12 slides)

```text
Crea una presentación educativa de MÁXIMO 10 a 12 diapositivas en español para estudiantes de 15-16 años basada únicamente en los CAPÍTULOS 4, 5, 6 y 7 de FUENTE_1RO_BGU_PARCIAL2_COMPLETO.md.

ESTILO VISUAL (CÓMIC + AGENTE PEDAGÓGICO 80/20):
- Diapositiva 1 (Portada/Gancho) y última diapositiva (Cierre): escena completa de cómic de las Tortugas Ninja.
- En todas las láminas de teoría técnica: página de cómic limpia donde el 80% es el diagrama/tabla/código grande sobre fondo claro y el 20% es un personaje guía de las Tortugas Ninja pequeño en una esquina señalando el punto clave o dando 1 consejo corto (PROHIBIDO globos gigantes o tramas tapando diagramas).

PORTADA (DIAPOSITIVA 1 — TODO JUNTO):
- Título exacto: "TOMO 2: Señales Analógicas y Regulación PWM — SECCIÓN 2" (PROHIBIDO escribir "Tema:", fechas, nombre de profesor o el nombre del curso).
- "Propósito:" (verbo en infinitivo, sin decir "LEV") + "¿Dónde lo usas?" (1 frase cotidiana para 15-16 años).

ESTRUCTURA SIN REPETICIONES (2–3 SLIDES POR CLASE):
- Clase 4 — Poste de Alumbrado Automático con LDR:
  - 2 Láminas Ancla: (1) Cómo funciona una fotoresistencia (LDR) por dentro + divisor de voltaje con resistencia fija de 10k y (2) Ejemplo Resuelto anotado de encendido por umbral de oscuridad + Reto virtual en Tinkercad.
- Clase 5 y 6 — Theremin Musical con Luz (LDR + Buzzer tone()): Virtual y Grupal Físico (👥 ACTIVIDAD GRUPAL):
  - 2 Láminas Ancla: (1) Frecuencia sonora en Hz con tone(pin, freq) y mapeo de luz a notas musicales y (2) Reto Grupal Físico con 3 roles rotativos (1. Montaje LDR/Buzzer, 2. Código/Mapeo, 3. Calibración/Verificación) + Protocolo de 3 pasos.
- Clase 7 — Refuerzo: Calibración con Monitor Serial y Cierre (🛠️ REFUERZO):
  - 1 Lámina: Cómo leer valores min/máx reales en Serial.println() para calibrar umbrales sin adivinar.
  - 1 Diapositiva exclusiva de Autoevaluación con Escala de Likert (1 al 5) en 4 aspectos concretos aprendidos.

CANDADOS OBLIGATORIOS:
1. Usa ÚNICAMENTE código verificado de la fuente; PROHIBIDO inventar funciones o librerías externas.
2. En actividades evaluadas (👥): PROHIBIDO regalar el código completo del Theremin resuelto.
3. PROHIBIDO poner fechas, "Semana X", nombres de docente o "sube a Classroom".
```

---

## 📝 PROMPT 3 — REPASO Y EXAMEN (Ficha Resumen + 10 Preguntas)

```text
Basado en FUENTE_1RO_BGU_PARCIAL2_COMPLETO.md, genera un documento de repaso para examen con:
1. FICHA RESUMEN DE 1 PÁGINA: Tabla/mapa visual con los conceptos clave de todo el parcial (Digital vs. Analógico 0–1023, PWM 0–255 en pines ~, map(), LDR + divisor de voltaje 10k, tone() en Hz, Calibración con Monitor Serial), texto plano limpio.
2. BANCO DE 10 PREGUNTAS TIPO EXAMEN: Casos prácticos cortos ("Si la luz del aula cambia y el poste no enciende, ¿cómo calibras?") SIN mostrar respuestas.
`

---

## 🎬 PROMPT 4 — VIDEO DE REPASO (Studio -> Video)

`	ext
Crea un Video de Repaso teórico ordenado de todo el parcial basado en FUENTE_1RO_BGU_PARCIAL2_COMPLETO.md para estudiantes de 15-16 años.
Usa gráficos, esquemas y diagramas claros con ejemplos cercanos a su edad (PROHIBIDO usar personajes de cómics o mencionar fechas, semanas o nombre de docente).
```
