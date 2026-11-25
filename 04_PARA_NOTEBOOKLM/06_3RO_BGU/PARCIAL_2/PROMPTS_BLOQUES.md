# 🎨 PROMPTS POR BLOQUES — 3RO BGU / PARCIAL 2

> **Archivo fuente a subir:** `FUENTE_3RO_BGU_PARCIAL2_COMPLETO.md` | **Universo:** Tortugas Ninja | **Edad:** 17–18 años

---

## 📦 PROMPT 1 — SECCIÓN 1 (Capítulos 1 a 3 | 10–12 slides)

```text
Crea una presentación educativa de MÁXIMO 10 a 12 diapositivas en español para estudiantes de 17-18 años basada únicamente en los CAPÍTULOS 1, 2 y 3 de FUENTE_3RO_BGU_PARCIAL2_COMPLETO.md.

ESTILO VISUAL (CÓMIC + AGENTE PEDAGÓGICO):
- Diapositiva 1 (Portada/Gancho) y última diapositiva (Cierre): escena completa de cómic de las Tortugas Ninja.
- En todas las láminas de teoría técnica: página de cómic limpia donde el diagrama/tabla/código ocupa casi toda la lámina sobre fondo claro y un personaje guía de las Tortugas Ninja va pequeño en una esquina señalando el punto clave o dando 1 consejo corto (PROHIBIDO dibujar porcentajes en la imagen, globos gigantes o tramas tapando diagramas).

PORTADA (DIAPOSITIVA 1 — TODO JUNTO):
- Título exacto: "TOMO 2: Microcontroladores y Periféricos Digitales — SECCIÓN 1" (PROHIBIDO escribir "Tema:", fechas, nombre de profesor o el nombre del curso).
- "Propósito:" (verbo en infinitivo, sin decir "LEV") + "¿Dónde lo usas?" (1 frase cotidiana para 17-18 años).

ESTRUCTURA SIN REPETICIONES (3–4 SLIDES POR CLASE):
- Clase 1 y 2 — ¿Qué es ESP32? + Repaso en Wokwi:
  - 2 Láminas Ancla: (1) Arquitectura ESP32 vs. Arduino UNO (3.3V lógico, pines GPIO seguros vs. pines solo entrada/flash) y (2) Reglas de seguridad en Wokwi y depuración de errores de compilación (uso de IA como tutor de errores sin pedir código resuelto).
- Clase 3 — Semáforo ESP32 en Wokwi (👤 ACTIVIDAD INDIVIDUAL 1):
  - 2 Láminas Ancla: (1) Ejemplo Resuelto anotado + 1 pregunta de Predicción PRIMM (que pasa si cambias X) (5 líneas de salida digital GPIO en ESP32 con resistencia) y (2) Reto individual de Semáforo con Protocolo de Autodepuración en 3 pasos.
- Cierre de la Sección 1: 3 preguntas relámpago de verificación (SIN respuestas visibles).

CANDADOS OBLIGATORIOS:
0. TÉRMINOS TÉCNICOS REALES Y COMPLETOS: PROHIBIDO inventar nombres mágicos o infantiles (como "transformador mágico" o "energía mágica"); usa los términos técnicos reales de la fuente y cubre OBLIGATORIAMENTE todos los temas y eslabones listados arriba sin saltarse ninguno.
1. Usa ÚNICAMENTE simulador Wokwi y pines válidos del ESP32; PROHIBIDO adelantar WiFi/MQTT o HC-SR04.
2. En actividades evaluadas (👤): PROHIBIDO regalar el código completo del semáforo resuelto.
3. PROHIBIDO poner fechas, "Semana X", nombres de docente o "sube a Classroom".
```

---

## 📦 PROMPT 2 — SECCIÓN 2 (Capítulos 4 a 6 | 10–12 slides)

```text
Crea una presentación educativa de MÁXIMO 10 a 12 diapositivas en español para estudiantes de 17-18 años basada únicamente en los CAPÍTULOS 4, 5 y 6 de FUENTE_3RO_BGU_PARCIAL2_COMPLETO.md.

ESTILO VISUAL (CÓMIC + AGENTE PEDAGÓGICO):
- Diapositiva 1 (Portada/Gancho) y última diapositiva (Cierre): escena completa de cómic de las Tortugas Ninja.
- En todas las láminas de teoría técnica: página de cómic limpia donde el diagrama/tabla/código ocupa casi toda la lámina sobre fondo claro y un personaje guía de las Tortugas Ninja va pequeño en una esquina señalando el punto clave o dando 1 consejo corto (PROHIBIDO dibujar porcentajes en la imagen, globos gigantes o tramas tapando diagramas).

PORTADA (DIAPOSITIVA 1 — TODO JUNTO):
- Título exacto: "TOMO 2: Microcontroladores y Periféricos Digitales — SECCIÓN 2" (PROHIBIDO escribir "Tema:", fechas, nombre de profesor o el nombre del curso).
- "Propósito:" (verbo en infinitivo, sin decir "LEV") + "¿Dónde lo usas?" (1 frase cotidiana para 17-18 años).

ESTRUCTURA SIN REPETICIONES (2–3 SLIDES POR CLASE):
- Clase 4 — ESP32 PWM y Buzzer (👤 ACTIVIDAD INDIVIDUAL 2):
  - 2 Láminas Ancla: (1) PWM en ESP32 (analogWrite / ledc en Wokwi) y frecuencias con tone() y (2) Ejemplo Resuelto anotado + 1 pregunta de Predicción PRIMM (que pasa si cambias X) (4 líneas) + Reto.
- Clase 5 — Sensor Ultrasonido HC-SR04 con ESP32:
  - 2 Láminas Ancla (SIN repetir PWM): (1) Principio físico Trig/Echo y cálculo de distancia en cm (velocidad del sonido / 2) y (2) Ejemplo Resuelto anotado + 1 pregunta de Predicción PRIMM (que pasa si cambias X) (pulseIn) + Reto alerta de distancia.
- Clase 6 — Proyecto Grupal: Teclado Matricial 4x4 (👥 ACTIVIDAD GRUPAL):
  - 2 Láminas Ancla: (1) Matriz de filas y columnas (escaneo sin usar 16 pines) + librería Keypad y (2) Reto Grupal (Piano/Clave) con 3 roles rotativos (1. Cableado Matriz/Buzzer, 2. Lógica Keypad/Clave, 3. Pruebas/Monitor Serial).
- Clase 7 — Cierre Parcial 2 y Autoevaluación (🛠️ REFUERZO):
  - 1 Lámina integradora (errores típicos en ESP32) + Diapositiva exclusiva de Autoevaluación Likert (1 al 5) en 4 aspectos concretos.

CANDADOS OBLIGATORIOS:
0. TÉRMINOS TÉCNICOS REALES Y COMPLETOS: PROHIBIDO inventar nombres mágicos o infantiles (como "transformador mágico" o "energía mágica"); usa los términos técnicos reales de la fuente y cubre OBLIGATORIAMENTE todos los temas y eslabones listados arriba sin saltarse ninguno.
1. Usa ÚNICAMENTE librerías estándar en Wokwi (Keypad.h, etc.); PROHIBIDO adelantar WiFi o MQTT.
2. En actividades evaluadas (👤/👥): PROHIBIDO regalar el código completo resuelto.
3. PROHIBIDO poner fechas, "Semana X", nombres de docente o "sube a Classroom".
```

---

## 📝 PROMPT 3 — REPASO Y EXAMEN (Ficha Resumen + 10 Preguntas)

```text
Basado en FUENTE_3RO_BGU_PARCIAL2_COMPLETO.md, genera un documento de repaso para examen con:
1. FICHA RESUMEN DE 1 PÁGINA: Tabla/mapa visual con los conceptos clave de todo el parcial (ESP32 3.3V y GPIO seguros, PWM/tone, HC-SR04 Trig/Echo y pulseIn, Matriz 4x4 filas/columnas), texto plano limpio.
2. BANCO DE 10 PREGUNTAS TIPO EXAMEN: Casos prácticos cortos ("Si el HC-SR04 siempre marca 0 cm en Wokwi, ¿qué pin o línea revisas?") SIN mostrar respuestas.
`

---

## 🎬 PROMPT 4 — VIDEO DE REPASO (Studio -> Video)

`	ext
Crea un Video de Repaso teórico ordenado de todo el parcial basado en FUENTE_3RO_BGU_PARCIAL2_COMPLETO.md para estudiantes de 17-18 años.
Usa gráficos, esquemas y diagramas claros con ejemplos cercanos a su edad (PROHIBIDO usar personajes de cómics o mencionar fechas, semanas o nombre de docente).
```
