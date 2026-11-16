# 📘 1RO BGU — GUÍA DOCENTE DE 45 MINUTOS (ARDUINO MÓDULO 2)

---

## 📅 CLASE 1: Entradas Digitales (Pulsadores) y Tipos de Variables
* **Duración:** 45 Minutos | **Modalidad:** 💻 [100% PC en Tinkercad Circuits + Presentación]
* **Recurso / Presentación:** [PRESENTACION_1RO_BGU_ARDUINO_MOD2.pdf](file:///C:/Users/David/Desktop/clases%20bach/01_PRESENTACIONES_Y_MATERIAL/1RO_BGU/PRESENTACION_1RO_BGU_ARDUINO_MOD2.pdf)
* **Propósito Inicial:** Aprender a leer el estado de un botón o pulsador (`digitalRead`) utilizando variables optimizadas (`bool` / `unsigned int`) y estructuras de decisión `if-else`.

---

### ⏱️ DESGLOSE PASO A PASO (45 MINUTOS)

#### 1. 🎯 Motivación y Frase de Entrada (00 - 05 min)
* **¿Qué decirles?** *"Chicos, en 10mo aprendimos a hacer parpadear LEDs solos. Hoy en 1ro de Bachillerato daremos el paso a la interacción: el programa tomará decisiones según las acciones del usuario al presionar un botón."*

#### 2. 💡 Teoría Relámpago (05 - 10 min)
* **Los 3 Conceptos Clave:**
  1. **Entrada Digital (`INPUT`):** El Arduino lee un valor `HIGH` (1) o `LOW` (0).
  2. **Variables de Memoria:** Usar `bool` (1 bit para verdadero/falso) en lugar de recargar memoria.
  3. **Condicional `if(estado == HIGH)`:** Ejecuta una acción solo cuando se presiona el botón.

#### 3. 💻 Actividad Guiada Contigo (10 - 20 min)
* **Instrucción:** Todos abren Tinkercad Circuits y arman en pantalla:
  - 1 Arduino Uno + 1 Pulsador con Resistencia Pull-Down de 10k$\Omega$ al Pin 2 + 1 LED al Pin 13.
  - Escribir en código C++ la lectura del estado y la condición `if-else`.

#### 4. 🚀 Actividad Individual (Ellos Solos) (20 - 40 min)
* **El Reto:**
  > *"Diseñen un sistema donde al presionar el Pulsador 1 se encienda un LED Verde, y si no está presionado, se mantenga encendido un LED Rojo de advertencia."*

#### 5. 📝 Cierre y Evaluación (40 - 45 min)
* Verificación en pantalla del correcto uso de la resistencia Pull-Down y la condición `if-else`.
