# 🟠 3RO BGU — TEMARIO MAESTRO ANUAL (2026 - 2027)

**Materia:** Robótica y Tecnología  
**Título General del Año:** Sistemas Inteligentes Conectados  
**Propósito General:** **Desarrollar** sistemas inteligentes conectados en red para automatizar procesos reales mediante IoT e Inteligencia Artificial con criterio ético.  
**Mediador:** David Castro  
**Regla de Clase (45 min):** 10 min de teoría + 35 min de práctica conjunta (**100% Simulador Wokwi + Herramientas Web de IA** — sin ESP32 físico).  
**Referencia Base ESP32:** Curso de ESP32 de *Programador Novato* (`programadornovato.com/category/curso-de-esp32/`).  
**Estructura por Parcial:** 4 Parciales (**6 clases reales por parcial** para compensar eventos/pérdidas de clase y graduación en junio).

---

## 🟢 PARCIAL 1 (27 ago – 30 oct) — TEMA 1: Electrónica de Potencia con Arduino
*(Estado: Cerrado / Ejecutado según `03_PLANIFICACION_SEMANAL`)*

1. `[x]` **Transistor BJT NPN (2N2222) como Interruptor** — Operación en Corte y Saturación (Base, Colector, Emisor).
2. `[x]` **Control de Motor DC + Diodo Flyback 1N4007 (Cinta Transportadora)** — Protección de potencia y manejo de cargas.

---

## 🟡 PARCIAL 2 (4 nov – 30 ene) — TEMA 2: ESP32 desde Cero en Wokwi (Salidas, Sensores y Teclado)
*(Estado: En curso — Hoy: Semana 3, 16–19 nov | Cierre Áreas Especiales: semana del 11 ene)*

1. `[x]` **S2 (9–13 nov) — ¿Qué es el ESP32? + Sirena de Policía en Wokwi** *(ejecutado)* — Pines GPIO, lógica de $3.3\text{V}$ y primer código en Wokwi.
2. `[→]` **S3 (16–19 nov — Esta semana) — Formulario de Mejora de Calificaciones + Repaso ESP32** *(ejecutado/en curso)* — Recuperación y nivelación de conceptos base.
3. `[ ]` **S4 (23–27 nov) — Semáforo en Wokwi** *(Individual 1)* — Ambientación con salidas digitales y tiempos en ESP32.
4. `[ ]` **S5 (30 nov – 4 dic) — ESP32 PWM y Buzzer (Zumbador)** *(Individual 2)* — Control de intensidad de LED (PWM) y emisión de frecuencias/tonos con buzzer.
5. `[ ]` **S6 (7–11 dic) — Sensor Ultrasonido HC-SR04 con ESP32** *(Práctica PC)* — Medición de distancia y alerta con LEDs/Buzzer en Wokwi.
6. `[ ]` **S7 (14–18 dic) — Proyecto: Teclado Matricial 4x4 (Piano / Clave de Seguridad)** *(Grupal en Wokwi)* — Lectura de teclado 4x4 reproduciendo notas en buzzer o validando clave.
7. `[ ]` **S8 (5–8 ene) — Cierre Parcial 2: Repaso ESP32 en Wokwi y Autoevaluación** *(Refuerzo y Cierre)* — Nivelación de simulaciones (Semáforo, PWM/Buzzer, HC-SR04, Teclado 4x4) y **Autoevaluación Likert (1–5)** en 4 aspectos previa a Evaluaciones de Áreas Especiales (semana del 11 de enero).

---

## 🔵 PARCIAL 3 (2 feb – 10 abr) — TEMA 3: Servomotores, LCD 16x2 e IoT Bidireccional (Wokwi + Gemini)
*(Estado: Pendiente — 6 clases | 100% nativo en `wokwi.com` gratis)*

1. `[ ]` **Control de Servomotor (180°) con ESP32** *(Individual 1 — calificada)* — Posicionamiento angular y barrido en Wokwi.
2. `[ ]` **Pantalla LCD 16x2 con ESP32 (Textos y *Scroll*)** *(Individual 2 — calificada)* — Despliegue de mensajes dinámicos en pantalla.
3. `[ ]` **Proyecto: Barrera de Peaje / Parqueo (HC-SR04 + Servo + LCD 16x2)** *(Grupal en Wokwi — calificada)* — Abre al detectar distancia y muestra estado en la LCD.
4. `[ ]` **WiFi en Wokwi (`Wokwi-GUEST`) y Protocolo IoT MQTT (`PubSubClient`)** *(Tema Nuevo — clase normal)* — Conectar el ESP32 a un broker público (`broker.hivemq.com`) enviando lecturas (texto/JSON) y recibiendo comandos.
5. `[ ]` **Panel Web IoT con Gemini (HTML + `mqtt.js`) para Controlar Wokwi en Vivo** *(Práctica PC — sin nota extra / o evaluable)* — Crear en Gemini una página `.html` externa que muestre la distancia del HC-SR04 en vivo y mueva el servo de la puerta en Wokwi.
6. `[ ]` **Refuerzo, Seguridad IoT (Credenciales/Tópicos) y Autoevaluación** *(Refuerzo y Cierre)* — Buenas prácticas de seguridad IoT, depuración con IA y **Autoevaluación Likert (1–5)** en 4 aspectos.

---

## 🟣 PARCIAL 4 (13 abr – 19 jun) — TEMA 4: Inteligencia Artificial + ESP32 (Enfoque Universitario)
*(Estado: Pendiente — 6 clases | Cierre anticipado por graduación de 3ro BGU)*

1. `[ ]` **Entrenamiento de IA Visual con *Google Teachable Machine*** *(Individual 1 — calificada)* — Entrenar modelo de cámara en el navegador (gestos/objetos) y analizar **sesgo de datos** (luz, ángulos y fondos).
2. `[ ]` **Puente IA -> ESP32 (Simulación por Monitor Serial en Wokwi)** *(Individual 2 — calificada)* — Traducir la clase detectada por la IA en comandos (`'A'` / `'C'`) probados en el Monitor Serial de Wokwi.
3. `[ ]` **Proyecto Final: Acceso Inteligente con Visión IA — Parte 1** *(Grupal — avance)* — Montaje en Wokwi con **LCD 16x2 + Servomotor + LEDs + Buzzer**.
4. `[ ]` **Proyecto Final: Acceso Inteligente con Visión IA — Parte 2** *(Grupal — calificada)* — Pruebas en vivo (la IA reconoce gesto/objeto -> abre puerta en Wokwi y saluda en la LCD).
5. `[ ]` **Mini-Sustentación estilo Universitario** *(Refuerzo)* — Defensa técnica de arquitectura (IA -> ESP32 -> Actuador), límites y ética/sesgo del modelo.
6. `[ ]` **Cierre Final de 3ro BGU y Autoevaluación** *(Refuerzo y Cierre)* — Evaluación quimestral previa a graduación y **Autoevaluación Likert (1–5)** en 4 aspectos.
