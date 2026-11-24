# 🔴 1RO BGU — TEMARIO MAESTRO ANUAL (2026 - 2027)

**Materia:** Robótica y Tecnología  
**Título General del Año:** Sensores y Control Automático  
**Propósito General del Año:** **Construir** sistemas de control automático integrando entradas digitales, señales analógicas (PWM), sensores ambientales y servomotores para responder a estímulos del entorno.  
**Cargo:** Mediador  
**Regla de Clase (45 min):** 10 min de teoría + 35 min de práctica conjunta (Tinkercad Circuits + Kit físico Arduino con sensores).  
**Estructura por Parcial:** 4 Parciales (1 Tema por Parcial × 7 clases), medido para sesiones de 35 min reales, garantizando mínimo **2 actividades individuales + 1 grupal + 1 refuerzo**.

---

## 🟢 PARCIAL 1 (27 ago – 30 oct) — TEMA 1: Lógica Condicional y Entradas Digitales
*(Estado: Cerrado / Ejecutado según `03_PLANIFICACION_SEMANAL` | Nota: Nivelación de transición 2026–2027; para próximas cohortes se omite al cubrirse en 10mo EGB)*
**Propósito del Parcial:** **Implementar** lógica condicional mediante entradas digitales y pulsadores para tomar decisiones automatizadas en microcontroladores.  

1. `[x]` **Tipos de Datos (`bool`, `int`, `float`) y Sirena de Policía** — Refactorización de código e intermitencia en Tinkercad.
2. `[x]` **Sentencias `if - else` / `else if`** — Comparación de valores, promedio de 3 notas y Semáforo de calificaciones.
3. `[x]` **Entradas Digitales (`digitalRead()` e `INPUT_PULLUP`)** — Lectura booleana de pulsadores sin resistencia externa.

---

## 🟡 PARCIAL 2 (4 nov – 30 ene) — TEMA 2: Señales Analógicas y Regulación PWM
*(Estado: En curso — Hoy: Semana 3, 16–19 nov | Cierre Áreas Especiales: semana del 11 ene)*
**Propósito del Parcial:** **Modificar** y regular señales analógicas y salidas PWM mediante potenciómetros, fotoresistencias (LDR) y calibración serial.  

1. `[x]` **S1–S2 (4–13 nov) — Potenciómetro (`analogRead`) + 4 LEDs con `>` y `<`** *(ejecutado)* — Lectura analógica en Arduino y Tinkercad encendiendo LEDs por rangos.
2. `[x]` **S3 (16–19 nov) — Informe de Potenciómetro con 4 LEDs + Cuestionario** *(Individual 1 y 2 completas)* — Entrega de informe (`AI5`) y cuestionario (`AI6`).
3. `[→]` **S4 (23–27 nov) — Proyecto: Atenuador de Brillo LED (`map()` + PWM `analogWrite`)** *(Práctica sin entrega)* — Regulación suave de 1 LED con potenciómetro en Tinkercad y kit.
4. `[ ]` **S5 (30 nov – 4 dic) — Proyecto: Poste de Alumbrado Automático (LDR)** *(Simulación Virtual en Tinkercad)* — Encendido automático de 1 LED al oscurecer con umbral `>` / `<`.
5. `[ ]` **S6 (7–11 dic) — Theremin Musical con Luz (LDR + Buzzer `tone()`)** *(Simulación Virtual en Tinkercad)* — Diseño y prueba del circuito en virtual *(sin chocar kits con 10mo EGB)*.
6. `[ ]` **S7 (14–18 dic) — Theremin Musical con Luz (LDR + Buzzer `tone()`)** *(Grupal Físico — Kits Arduino)* — Montaje físico grupal usando el código validado en S6.
7. `[ ]` **S8 (5–8 ene) — Refuerzo: Calibración con Monitor Serial y Cierre** *(Refuerzo y Cierre)* — Lectura min/máx de LDR, nivelación y **Autoevaluación Likert (1–5)** previa a Evaluaciones de Áreas Especiales.

---

## 🔵 PARCIAL 3 (2 feb – 10 abr) — TEMA 3: Detección Ambiental y Alertas
*(Estado: Pendiente — 7 clases | Refuerzo de `analogRead` + `if/else` por umbrales sin abrumar)*
**Propósito del Parcial:** **Construir** sistemas de detección ambiental y alertas tempranas integrando sensores analógicos y digitales.  

1. `[ ]` **Termómetro Digital por Monitor Serial (TMP36 / LM35)** *(Individual 1 — calificada)* — Conexión del sensor de temperatura y lectura en °C.
2. `[ ]` **Alarma Térmica con 2 LEDs y Buzzer** *(Tema Nuevo — clase normal)* — Refuerzo de `if/else` por umbral de temperatura (normal vs. alerta).
3. `[ ]` **Medidor de Distancia con Ultrasonido HC-SR04** *(Tema Nuevo — clase normal)* — Conexión Trigger/Echo y lectura en cm por Monitor Serial.
4. `[ ]` **Sensor de Parqueo — Parte 1 (Simulación en Tinkercad)** *(Individual 2 — calificada)* — `if / else if` por zonas de distancia (verde/amarillo/rojo + alerta Buzzer).
5. `[ ]` **Sensor de Parqueo — Parte 2 (Montaje Físico y Demo)** *(Grupal Físico — calificada)* — Armado real con HC-SR04 + Buzzer + LEDs y calibración en vivo.
6. `[ ]` **Refuerzo: Detector de Nivel de Agua / Humedad** *(Refuerzo — sin nota extra)* — Mismo `if` analógico aplicado a un sensor nuevo con alerta LED.
7. `[ ]` **Cierre de Parcial 3 y Autoevaluación** *(Refuerzo y Cierre)* — Repaso integrador y **Autoevaluación Likert (1–5)** en 4 aspectos.

---

## 🟣 PARCIAL 4 (13 abr – 1 jul) — TEMA 4: Control Angular y Sistemas Autónomos
*(Estado: Pendiente — 7 clases)*
**Propósito del Parcial:** **Diseñar** sistemas autónomos con control angular de servomotores y verificación de respuestas en tiempo real.  

1. `[ ]` **Control Angular del Servomotor SG90 (`<Servo.h>`)** *(Individual 1 — calificada)* — Posicionamiento básico (0°, 90°, 180°).
2. `[ ]` **Aguja Indicadora con Potenciómetro (`map()` + Servo)** *(Individual 2 — calificada)* — Movimiento del servomotor en tiempo real desde el potenciómetro.
3. `[ ]` **Control desde PC (`Serial.read()`)** *(Tema Nuevo — clase normal)* — Abrir/cerrar el servo escribiendo `'A'` o `'C'` en el Monitor Serial.
4. `[ ]` **Barrera / Garaje Automático — Parte 1 (Simulación + funciones `void`)** *(Práctica en Equipos — avance)* — Diseño y prueba lógica en Tinkercad (Ultrasonido + Servo + LED + funciones modulares `void`).
5. `[ ]` **Barrera / Garaje Automático — Parte 2 (Montaje Físico)** *(Práctica en Equipos — avance)* — Cableado físico en protoboard con el kit Arduino.
6. `[ ]` **Barrera / Garaje Automático — Parte 3 (Programación y Entrega)** *(Grupal — calificada)* — Carga de código, calibración y demostración en vivo.
7. `[ ]` **Refuerzo, Inventario y Autoevaluación** *(Refuerzo y Cierre)* — Ajustes finales, orden del kit y **Autoevaluación Likert (1–5)** en 4 aspectos.
