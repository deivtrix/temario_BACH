# 📘 3RO BGU — GUÍA DOCENTE DE 45 MINUTOS (ARDUINO MÓDULO 4)

---

## 📅 CLASE 1: Control de Potencia con Transistores NPN y Motores DC
* **Duración:** 45 Minutos | **Modalidad:** 💻 [100% PC en Tinkercad Circuits + Presentación]
* **Recurso / Presentación:** [PRESENTACION_3RO_BGU_MECATRONICA_MOD4.pdf](file:///C:/Users/David/Desktop/clases%20bach/01_PRESENTACIONES_Y_MATERIAL/3RO_BGU/PRESENTACION_3RO_BGU_MECATRONICA_MOD4.pdf)
* **Propósito Inicial:** Comprender por qué un pin de Arduino no puede alimentar motores directamente y diseñar un circuito de interfaz de potencia mediante transistores BJT NPN.

---

### ⏱️ DESGLOSE PASO A PASO (45 MINUTOS)

#### 1. 🎯 Motivación y Frase de Entrada (00 - 05 min)
* **¿Qué decirles?** *"Chicos, si conectamos un motor industrial directo al pin del Arduino, el microcontrolador se quema debido al alto consumo de corriente. Hoy aprenderemos a usar un Transistor como un interruptor electrónico de alta potencia."*

#### 2. 💡 Teoría Relámpago (05 - 10 min)
* **Los 3 Conceptos Clave:**
  1. **Límite de Corriente:** Un pin de Arduino solo entrega hasta 40mA. Un motor requiere +200mA.
  2. **Transistor BJT (NPN):** Usa una pequeña corriente en la Base para activar una corriente grande entre Colector y Emisor.
  3. **Diodo Flyback:** Protege al circuito de los picos de voltaje inducidos por el motor.

#### 3. 💻 Actividad Guiada Contigo (10 - 20 min)
* **Instrucción:** Todos ingresan a Tinkercad Circuits:
  - Arrastrar 1 Arduino Uno + 1 Transistor NPN (TIP120/2N2222) + 1 Motor DC + 1 Diodo + Batería Externa de 9V.
  - Escribir la rutina de activación digital del pin de Base.

#### 4. 🚀 Actividad Individual (Ellos Solos) (20 - 40 min)
* **El Reto:**
  > *"Aplicar modulación PWM (`analogWrite`) a la Base del transistor para controlar 3 velocidades distintas en el motor DC (Baja: 80, Media: 170, Alta: 255) mediante botones."*

#### 5. 📝 Cierre y Evaluación (40 - 45 min)
* Evaluación del cambio de revoluciones del motor en el simulador.
