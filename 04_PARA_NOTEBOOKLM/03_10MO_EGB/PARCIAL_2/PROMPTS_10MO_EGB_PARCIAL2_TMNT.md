# 🐢 PROMPTS PARA NOTEBOOKLM — 10MO EGB PARCIAL 2 (100% ESPAÑOL + AUTO-EXPLICATIVO)

## 📌 CÓMO USARLO
1. En **NotebookLM**, sube **1 solo archivo**: `FUENTE_10MO_EGB_PARCIAL2_COMPLETO.md`.
2. *(Opcional)* En **Descubrir fuentes**, pega estos temas en español:
   * `Tipos de conectores eléctricos Dupont borneras y aislantes termocontraíble`
   * `Primer programa en Arduino Blink setup loop digitalWrite delay explicación sencilla`
   * `Semáforo con 3 LEDs en Arduino Tinkercad código y conexión protoboard`
   * `Bucle for en Arduino para encender varios LEDs en secuencia`
3. Haz **2 generaciones** (4 slides por clase + Autoevaluación Likert al final):

---

## 🟢 GENERACIÓN 1 (12 Diapositivas): SEMANAS 3, 4 y 5
```text
IDIOMA OBLIGATORIO: Todo el texto, títulos, mapas, etiquetas y diagramas deben estar 100% en ESPAÑOL. Prohibido usar inglés.

Crea una presentación de exactamente 12 diapositivas para 10mo EGB (14-15 años) basada en las SEMANAS 3, 4 y 5 de la fuente subida (4 slides por semana).

REGLAS OBLIGATORIAS:
- Enfoque "MINI-LIBRO AUTO-EXPLICATIVO".
- ETIQUETA VISIBLE OBLIGATORIA: `👤 ACTIVIDAD INDIVIDUAL` o `📘 TEMA NUEVO`.
- En `👤 ACTIVIDAD INDIVIDUAL`: SOLO enunciado + diseño/requisitos + 1 tip (CERO código y CERO paso a paso donde ya se explicó). En TEMA NUEVO sí incluye código referencial completo y paso a paso.
- Temática: Tortugas Ninja (TMNT). Mediador: David Castro.

ESTRUCTURA:
- Slides 1–4 -> SEMANA 3 (Infografía de Conectores y Aislantes | 👤 ACTIVIDAD INDIVIDUAL):
  1. Portada (`👤 ACTIVIDAD INDIVIDUAL` | Mediador: David Castro) + Propósito LEV exacto + ¿Para qué sirve?
  2. Mapa conceptual visual: 3 conectores (Jumper Dupont, Borneras/Clemas, Capuchones/Caimanes) y 3 aislantes (PVC, Termocontraíble, Silicona/Cerámica).
  3. Diseño de referencia: Cómo organizar la infografía en 1 página de Canva (2 columnas + pie con nombre).
  4. `👤 ACTIVIDAD INDIVIDUAL`: Enunciado exacto (4 conectores incluyendo Dupont y Bornera + 4 aislantes incluyendo PVC y Termocontraíble) + 1 tip.

- Slides 5–8 -> SEMANA 4 (Primer Programa Arduino: Blink | 👤 ACTIVIDAD INDIVIDUAL / 📘 TEMA NUEVO):
  5. Portada (`👤 ACTIVIDAD INDIVIDUAL` | Mediador: David Castro) + Propósito LEV exacto + ¿Para qué sirve?
  6. Mapa de estructura C++: `void setup()` (corre 1 vez) vs. `void loop()` (se repite siempre) + `pinMode`, `digitalWrite`, `delay`.
  7. Diagrama de conexión en Tinkercad (Pin 13 -> LED -> 220 ohmios -> GND) + Código referencial base de Blink.
  8. `👤 ACTIVIDAD INDIVIDUAL`: Enunciado del reto (agregar 2do LED en Pin 12 alternado cada 500 ms + `// Nombre`) + 2 preguntas de cierre.

- Slides 9–12 -> SEMANA 5 (Semáforo en Tinkercad | 📘 TEMA NUEVO):
  9. Portada (`📘 TEMA NUEVO` | Mediador: David Castro) + Propósito LEV exacto + ¿Para qué sirve?
  10. Mapa visual: Por qué usar variables `int rojo = 13;` en lugar de números directos.
  11. Diagrama de conexión en Tinkercad (Pines 13, 12, 11 -> 3 LEDs -> 220 ohmios -> GND) + Paso a paso numerado (1, 2, 3).
  12. Reto práctico (Verde parpadea 3 veces antes de Amarillo) + 2 preguntas de cierre y Classroom.
```

---

## 🟡 GENERACIÓN 2 (13 Diapositivas): SEMANAS 6, 7, 8 + AUTOEVALUACIÓN FINAL
```text
IDIOMA OBLIGATORIO: Todo el texto, títulos, mapas y etiquetas deben estar 100% en ESPAÑOL. Prohibido usar inglés.

Crea una presentación de exactamente 13 diapositivas para 10mo EGB basada en las SEMANAS 6, 7 y 8 de la fuente subida (4 slides por semana + Slide 13 de Autoevaluación).
Temática: Tortugas Ninja (TMNT). Mediador: David Castro.

ESTRUCTURA:
- Slides 1–4 -> SEMANA 6 (Semáforo Físico en Protoboard con Arduino UNO | 👥 ACTIVIDAD GRUPAL):
  1. Portada (`👥 ACTIVIDAD GRUPAL`) + Propósito LEV exacto + ¿Para qué sirve?
  2. Mapa de seguridad física: Pata larga (+ al pin) vs. Pata corta (- a GND), resistencia 220 ohmios obligatoria, puerto COM.
  3. Imagen de referencia: Protoboard física con 3 LEDs, resistencias a bus GND común y cables a Pines 13, 12, 11.
  4. `👥 ACTIVIDAD GRUPAL`: Enunciado directo en equipo (armar, cargar código, foto con papelito de nombres) + 1 tip (SIN código).

- Slides 5–8 -> SEMANA 7 (Bucles for con 6 LEDs | 🛠️ REFUERZO):
  5. Portada (`🛠️ REFUERZO`) + Propósito LEV exacto + ¿Para qué sirve?
  6. Mapa visual del bucle `for (int pin = 2; pin <= 7; pin++)` (inicio, límite, paso) + código referencial de ida.
  7. Diagrama en Tinkercad: 6 LEDs conectados en Pines 2 al 7 con resistencias 220 ohmios.
  8. `🛠️ REFUERZO`: Solo nombrar la actividad ("Secuencia de 6 LEDs ida y vuelta con for").

- Slides 9–12 -> SEMANA 8 (Depuración C++ y Cierre | 🛠️ REFUERZO):
  9. Portada (`🛠️ REFUERZO`) + Propósito LEV exacto + ¿Para qué sirve?
  10. Mapa de los 3 errores clásicos en Arduino (falta `;`, falta `pinMode`, LED sin resistencia/al revés).
  11. `🛠️ REFUERZO`: Solo nombrar ("Reto Encuentra el error y nivelación de prácticas").
  12. Indicaciones para la Evaluación de Áreas Especiales (semana del 11 de enero).

- Slide 13 -> AUTOEVALUACIÓN FINAL DEL PARCIAL 2 (Escala de Likert 1 al 5):
  13. Tabla visual del 1 al 5 (1 = Todavía me cuesta | 5 = Lo domino y lo puedo explicar) con los 4 aspectos exactos de la Semana 8 de la fuente.
```
