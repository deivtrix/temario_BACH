# 🐢 PROMPTS PARA NOTEBOOKLM — 1RO BGU PARCIAL 2 (100% ESPAÑOL + AUTO-EXPLICATIVO)

## 📌 CÓMO USARLO
1. En **NotebookLM**, sube **1 solo archivo**: `FUENTE_1RO_BGU_PARCIAL2_COMPLETO.md`.
2. *(Opcional)* En **Descubrir fuentes**, pega estos temas en español:
   * `Entrada analógica analogRead en Arduino con potenciómetro 0 a 1023`
   * `Función map y PWM analogWrite en Arduino para controlar brillo de LED`
   * `Sensor fotoresistencia LDR con Arduino divisor de voltaje 10k ohmios`
   * `Función tone en Arduino con buzzer pasivo`
3. Haz **2 generaciones** (4 slides por clase + Autoevaluación Likert al final):

---

## 🟢 GENERACIÓN 1 (12 Diapositivas): SEMANAS 3, 4 y 5
```text
IDIOMA OBLIGATORIO: Todo el texto, títulos, mapas, etiquetas y diagramas deben estar 100% en ESPAÑOL. Prohibido usar inglés.

Crea una presentación de exactamente 12 diapositivas para 1ro BGU (15-16 años) basada en las SEMANAS 3, 4 y 5 de la fuente subida (4 slides por semana).

REGLAS OBLIGATORIAS:
- Enfoque "MINI-LIBRO AUTO-EXPLICATIVO".
- ETIQUETA VISIBLE OBLIGATORIA: `👤 ACTIVIDAD INDIVIDUAL` o `📘 TEMA NUEVO`.
- En `👤 ACTIVIDAD INDIVIDUAL`: SOLO enunciado + diseño de referencia + candados/parámetros + 1 tip (CERO código nuevo si ya se dio; en Semana 4 por ser tema nuevo de PWM sí incluye código referencial).
- Temática: Tortugas Ninja (TMNT).
ESTRUCTURA:
- Slides 1–4 -> SEMANA 3 (Informe Potenciómetro 4 LEDs + Cuestionario | 👤 ACTIVIDAD INDIVIDUAL):
  1. Portada (`👤 ACTIVIDAD INDIVIDUAL`) + Propósito LEV exacto + ¿Para qué sirve?
  2. Mapa técnico: `analogRead(A0)` (0 a 1023) + condicionales `if (valor > X)` sobre 4 LEDs.
  3. Imagen de referencia y los 3 Candados Anti-IA (Nota virtual con nombre, 4 umbrales exactos, respuestas de máx. 3 líneas).
  4. `👤 ACTIVIDAD INDIVIDUAL`: Enunciado de entrega (Informe corto + Cuestionario de 4 preguntas en Classroom) + 1 tip (`else { LOW }`).

- Slides 5–8 -> SEMANA 4 (Atenuador PWM con map() | 👤 ACTIVIDAD INDIVIDUAL / 📘 TEMA NUEVO):
  5. Portada (`👤 ACTIVIDAD INDIVIDUAL`) + Propósito LEV exacto + ¿Para qué sirve?
  6. Mapa conceptual: Pines PWM (`~` 3, 5, 6, 9, 10, 11) + `map(valor, 0, 1023, 0, 255)` + `analogWrite()`.
  7. Diagrama de conexión (Potenciómetro en A0 + LED en Pin ~9) + Código referencial base completo.
  8. `👤 ACTIVIDAD INDIVIDUAL`: Enunciado del reto (2do LED invertido en Pin ~10 con `255 - brillo`) + 2 preguntas de cierre.

- Slides 9–12 -> SEMANA 5 (Poste de Alumbrado con LDR | 📘 TEMA NUEVO):
  9. Portada (`📘 TEMA NUEVO`) + Propósito LEV exacto + ¿Para qué sirve?
  10. Mapa de conexión: Divisor de voltaje con LDR a 5V y A0 + resistencia 10k ohmios a GND.
  11. Código referencial completo con `Serial.begin(9600)` + Paso a paso numerado (1, 2, 3) para probar luz vs. oscuridad.
  12. Reto práctico + 2 preguntas de verificación y entrega en Classroom.
```

---

## 🟡 GENERACIÓN 2 (13 Diapositivas): SEMANAS 6, 7, 8 + AUTOEVALUACIÓN FINAL
```text
IDIOMA OBLIGATORIO: Todo el texto, títulos, mapas y etiquetas deben estar 100% en ESPAÑOL. Prohibido usar inglés.

Crea una presentación de exactamente 13 diapositivas para 1ro BGU basada en las SEMANAS 6, 7 y 8 de la fuente subida (4 slides por semana + Slide 13 de Autoevaluación).
Temática: Tortugas Ninja (TMNT).
ESTRUCTURA:
- Slides 1–4 -> SEMANA 6 (Theremin Musical con Luz: LDR + Buzzer | 👥 ACTIVIDAD GRUPAL):
  1. Portada (`👥 ACTIVIDAD GRUPAL`) + Propósito LEV exacto + ¿Para qué sirve?
  2. Mapa funcional: Luz en LDR -> `analogRead(A0)` -> `map()` -> Frecuencia Hz en Buzzer (`tone(8, nota)`).
  3. Diagrama de conexión física en kit Arduino (LDR en A0 con 10k a GND + Buzzer en Pin 8 y GND) + materiales.
  4. `👥 ACTIVIDAD GRUPAL`: Enunciado de calibración en grupo + foto con papelito de nombres + 1 tip (SIN regalar el código completo).

- Slides 5–8 -> SEMANA 7 (Calibración con Monitor Serial | 🛠️ REFUERZO):
  5. Portada (`🛠️ REFUERZO`) + Propósito LEV exacto + ¿Para qué sirve?
  6. Mapa de diagnóstico: Cómo calcular el umbral perfecto `(min + max) / 2` usando `Serial.println()`.
  7. Esquema de prueba rápida en Tinkercad/kit.
  8. `🛠️ REFUERZO`: Solo nombrar ("Calibración real en Monitor Serial y nivelación de prácticas").

- Slides 9–12 -> SEMANA 8 (Repaso Analógico y Cierre | 🛠️ REFUERZO):
  9. Portada (`🛠️ REFUERZO`) + Propósito LEV exacto + ¿Para qué sirve?
  10. Mapa resumen del Parcial 2: `analogRead` -> `map` -> `analogWrite` / `tone` -> LDR.
  11. `🛠️ REFUERZO`: Solo nombrar ("Repaso combinado y revisión final de entregas").
  12. Indicaciones para la Evaluación de Áreas Especiales (semana del 11 de enero).

- Slide 13 -> AUTOEVALUACIÓN FINAL DEL PARCIAL 2 (Escala de Likert 1 al 5):
  13. Tabla visual del 1 al 5 (1 = Todavía me cuesta | 5 = Lo domino y lo puedo explicar) con los 4 aspectos exactos de la Semana 8 de la fuente.
```
