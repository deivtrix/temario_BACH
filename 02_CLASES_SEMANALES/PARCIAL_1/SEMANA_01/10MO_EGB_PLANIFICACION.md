# 📘 10MO EGB — GUÍA DOCENTE DE 45 MINUTOS (ARDUINO MÓDULO 1)

---

## 📅 CLASE 1: Introducción a Arduino y Salidas Digitales (LEDs)
* **Duración:** 45 Minutos | **Modalidad:** 💻 [100% PC en Tinkercad Circuits + Presentación]
* **Recurso / Presentación:** [CA.1.RB.5.PR.26-27.pdf](file:///C:/Users/David/Desktop/clases%20bach/01_PRESENTACIONES_Y_MATERIAL/10MO_EGB/CA.1.RB.5.PR.26-27.pdf)
* **Propósito Inicial:** Conocer la estructura de un microcontrolador Arduino Uno y programar el primer encendido y parpadeo de LED usando `pinMode`, `digitalWrite` y `delay`.

---

### ⏱️ DESGLOSE PASO A PASO (45 MINUTOS)

#### 1. 🎯 Motivación y Frase de Entrada (00 - 05 min)
* **¿Qué decirles?** *"Chicos, bienvenidos a 10mo EGB. Hoy le daremos 'cerebro' a nuestros circuitos. Vamos a programar nuestra primera tarjeta Arduino para controlar el tiempo de encendido y apagado de un LED."*

#### 2. 💡 Teoría Relámpago (05 - 10 min)
* **La Estructura Básica C++:**
  1. `void setup()`: Se ejecuta una sola vez al encender. Configura los pines (`pinMode(13, OUTPUT);`).
  2. `void loop()`: Se repite infinitamente. Ejecuta las órdenes (`digitalWrite(13, HIGH);`, `delay(1000);`).

#### 3. 💻 Actividad Guiada Contigo (10 - 20 min)
* **Instrucción:** Todos ingresan a Tinkercad Circuits y conectan contigo en pantalla:
  - Arrastrar 1 Arduino Uno, 1 Protoboard, 1 LED y 1 Resistencia de 220$\Omega$.
  - Abrir el editor de **Código en Texto (C++)** y escribir la rutina Blink básica.

#### 4. 🚀 Actividad Individual (Ellos Solos) (20 - 40 min)
* **El Reto:**
  > *"Agreguen un segundo LED en el Pin 12 y hagan un circuito intermitente alternado (cuando el LED 13 se enciende, el 12 se apaga, y viceversa con un tiempo de 500ms)."*

#### 5. 📝 Cierre y Evaluación (40 - 45 min)
* Revisas la simulación en pantalla y calificas el funcionamiento del código alternado.
