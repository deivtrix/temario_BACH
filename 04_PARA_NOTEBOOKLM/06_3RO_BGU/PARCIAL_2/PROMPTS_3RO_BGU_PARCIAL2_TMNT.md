# 🐢 PROMPTS PARA NOTEBOOKLM — 3RO BGU PARCIAL 2 (100% ESPAÑOL + AUTO-EXPLICATIVO)

## 📌 CÓMO USARLO
1. En **NotebookLM**, sube **1 solo archivo**: `FUENTE_3RO_BGU_PARCIAL2_COMPLETO.md`.
2. *(Opcional)* En **Descubrir fuentes**, pega estos temas en español:
   * `ESP32 en simulador Wokwi pines GPIO 3.3V y semáforo LED`
   * `ESP32 PWM analogWrite y buzzer con función tone en Arduino IDE`
   * `Sensor ultrasonido HC-SR04 con ESP32 código distancia en cm`
   * `Teclado matricial 4x4 con ESP32 librería Keypad`
3. Haz **2 generaciones** (4 slides por clase + Autoevaluación Likert al final):

---

## 🟢 GENERACIÓN 1 (12 Diapositivas): SEMANAS 3, 4 y 5
```text
IDIOMA OBLIGATORIO: Todo el texto, títulos, mapas, etiquetas y diagramas deben estar 100% en ESPAÑOL. Prohibido usar inglés.

Crea una presentación de exactamente 12 diapositivas para 3ro BGU (17-18 años) basada en las SEMANAS 3, 4 y 5 de la fuente subida (4 slides por semana).

REGLAS OBLIGATORIAS:
- Enfoque "MINI-LIBRO AUTO-EXPLICATIVO". Todo es 100% simulado en Wokwi (sin ESP32 físico).
- ETIQUETA VISIBLE OBLIGATORIA: `🛠️ REFUERZO`, `👤 ACTIVIDAD INDIVIDUAL` o `📘 TEMA NUEVO`.
- En `🛠️ REFUERZO` solo se nombra; en `👤 ACTIVIDAD INDIVIDUAL` sobre temas nuevos (Semáforo / PWM en ESP32) incluye diagrama de pines GPIO y código referencial base.
- Temática: Tortugas Ninja (TMNT). Mediador: David Castro.

ESTRUCTURA:
- Slides 1–4 -> SEMANA 3 (Formulario de Mejora y Repaso ESP32 | 🛠️ REFUERZO):
  1. Portada (`🛠️ REFUERZO` | Mediador: David Castro) + Propósito LEV exacto + ¿Para qué sirve?
  2. Mapa comparativo: Arduino UNO (5V) vs. ESP32 (3.3V, WiFi/BT, 115200 baudios).
  3. Imagen de referencia: Sirena de Policía en Wokwi (GPIO 2 y GPIO 4 con 220 ohmios).
  4. `🛠️ REFUERZO`: Solo nombrar ("Formulario de mejora de calificaciones y nivelación en Wokwi").

- Slides 5–8 -> SEMANA 4 (Semáforo en ESP32 con Wokwi | 👤 ACTIVIDAD INDIVIDUAL):
  5. Portada (`👤 ACTIVIDAD INDIVIDUAL` | Mediador: David Castro) + Propósito LEV exacto + ¿Para qué sirve?
  6. Mapa técnico: Variables `const int` + pines GPIO seguros (`12, 14, 27`) + `Serial.begin(115200)`.
  7. Diagrama de conexión en Wokwi (3 LEDs con 220 ohmios a GND) + Paso a paso numerado.
  8. `👤 ACTIVIDAD INDIVIDUAL`: Enunciado del reto (parpadeo 3 veces en Verde + estado en Monitor Serial) + 1 tip.

- Slides 9–12 -> SEMANA 5 (ESP32 PWM y Buzzer en Wokwi | 👤 ACTIVIDAD INDIVIDUAL / 📘 TEMA NUEVO):
  9. Portada (`👤 ACTIVIDAD INDIVIDUAL` | Mediador: David Castro) + Propósito LEV exacto + ¿Para qué sirve?
  10. Mapa funcional: `analogWrite(pin, 0-255)` para brillo Fade + `tone(pin, freq, dur)` para notas en Buzzer.
  11. Diagrama en Wokwi (LED en GPIO 13 + Buzzer en GPIO 14) + Código referencial base.
  12. `👤 ACTIVIDAD INDIVIDUAL`: Enunciado (alarma o melodía de 4 notas sincronizada con brillo LED) + 2 preguntas de cierre.
```

---

## 🟡 GENERACIÓN 2 (13 Diapositivas): SEMANAS 6, 7, 8 + AUTOEVALUACIÓN FINAL
```text
IDIOMA OBLIGATORIO: Todo el texto, títulos, mapas y etiquetas deben estar 100% en ESPAÑOL. Prohibido usar inglés.

Crea una presentación de exactamente 13 diapositivas para 3ro BGU basada en las SEMANAS 6, 7 y 8 de la fuente subida (4 slides por semana + Slide 13 de Autoevaluación).
Todo 100% simulado en Wokwi. Temática: Tortugas Ninja (TMNT). Mediador: David Castro.

ESTRUCTURA:
- Slides 1–4 -> SEMANA 6 (Sensor Ultrasonido HC-SR04 con ESP32 | 📘 TEMA NUEVO):
  1. Portada (`📘 TEMA NUEVO`) + Propósito LEV exacto + ¿Para qué sirve?
  2. Mapa de funcionamiento: `TRIG` (GPIO 5) envía onda -> `ECHO` (GPIO 18) mide tiempo -> `distancia = duracion * 0.034 / 2`.
  3. Diagrama en Wokwi (HC-SR04 + LED GPIO 13 + Buzzer GPIO 14) + Código referencial base y paso a paso.
  4. Reto práctico (alerta si `distancia < 30 cm`) + 2 preguntas de cierre.

- Slides 5–8 -> SEMANA 7 (Teclado Matricial 4x4 en Wokwi | 👥 ACTIVIDAD GRUPAL):
  5. Portada (`👥 ACTIVIDAD GRUPAL`) + Propósito LEV exacto + ¿Para qué sirve?
  6. Mapa técnico: Matriz 4 filas + 4 columnas = 16 teclas usando solo 8 pines GPIO + librería `Keypad` en Wokwi.
  7. Diagrama de conexión en Wokwi (4 filas a `13,12,14,27` y 4 columnas a `26,25,33,32`).
  8. `👥 ACTIVIDAD GRUPAL`: Enunciado (elegir Opción A: Clave con LED Verde/Rojo u Opción B: Mini Piano 4 notas) + 1 tip (SIN regalar el código completo).

- Slides 9–12 -> SEMANA 8 (Cierre Parcial 2 ESP32 | 🛠️ REFUERZO):
  9. Portada (`🛠️ REFUERZO`) + Propósito LEV exacto + ¿Para qué sirve?
  10. Mapa resumen del Parcial 2 en Wokwi: GPIO/3.3V -> PWM/Buzzer -> HC-SR04 -> Keypad 4x4.
  11. `🛠️ REFUERZO`: Solo nombrar ("Nivelación de simulaciones pendientes y repaso general en Wokwi").
  12. Indicaciones para la Evaluación de Áreas Especiales (semana del 11 de enero).

- Slide 13 -> AUTOEVALUACIÓN FINAL DEL PARCIAL 2 (Escala de Likert 1 al 5):
  13. Tabla visual del 1 al 5 (1 = Todavía me cuesta | 5 = Lo domino y lo puedo explicar) con los 4 aspectos exactos de la Semana 8 de la fuente.
```
