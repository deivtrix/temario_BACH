# 📓 3RO BGU — GUÍA DOCENTE DE 45 MINUTOS (CLASE POR CLASE)

---

## 📅 CLASE 1: Manejo de Potencia con Transistor BJT (NPN) y Motor DC
* **Duración:** 45 Minutos | **Modalidad:** 💻 [100% PC en Tinkercad Circuits]
* **Propósito Inicial:** Comprender cómo un microchip de baja corriente (Arduino) usa un Transistor BJT como interruptor de potencia para mover un Motor DC sin quemarse.
* **Conexión con la Vida Real:** Es el principio de activación de las Cintas Transportadoras en fábricas de embotellado o líneas de equipaje en los aeropuertos.

---

### ⏱️ DESGLOSE PASO A PASO (45 MINUTOS)

#### 1. 🎯 Motivación y Vida Real (00 - 05 min)
* **¿Qué decirles?** *"Chicos, bienvenidos a 3ro BGU. ¿Por qué no podemos conectar el motor de una licuadora o de un auto eléctrico directo a la salida de un celular o microchip? Porque el chip se quema por exceso de corriente. Hoy aprenderemos a usar un Transistor BJT como interruptor de potencia para mover motores pesados."*

#### 2. 💡 Teoría Relámpago (05 - 10 min)
* **La Analogía del Grifo de Agua 💧 (3 Patitas del Transistor NPN):**
  1. **Colector (C):** Entrada principal donde llega la corriente grande de la batería.
  2. **Base (B):** La "llave del grifo" que abre el paso al recibir una pequeña señal del Pin 10 de Arduino.
  3. **Emisor (E):** Salida a tierra (GND).

#### 3. 💻 Actividad Guiada Contigo (10 - 20 min)
* **Instrucción:** Arman en Tinkercad el circuito (Arduino Pin 10 $\rightarrow$ Resistencia $1\text{k}\Omega$ $\rightarrow$ Base Transistor NPN; Colector $\rightarrow$ Motor DC; Emisor $\rightarrow$ GND; Pin 11 $\rightarrow$ Botón). Escriben contigo en pantalla el código base:
  ```cpp
  // CÓDIGO GUIADO CLASE 1 (3RO BGU)
  int motor = 10;
  int boton = 11;

  void setup() {
    pinMode(motor, OUTPUT);
    pinMode(boton, INPUT_PULLUP);
  }

  void loop() {
    if (digitalRead(boton) == LOW) {
      digitalWrite(motor, HIGH); // El transistor abre el paso y enciende el motor
    } else {
      digitalWrite(motor, LOW);  // El transistor se cierra y apaga el motor
    }
  }
  ```

#### 4. 🚀 Actividad Individual (Ellos Solos) (20 - 40 min)
* **El Reto:** Apagas o congelas tu proyector y les lanzas el desafío:
  > *"Añadan al circuito 1 LED Verde y 1 LED Rojo. Cuando la cinta transportadora (motor) esté girando, debe encenderse el LED Verde. Cuando la cinta esté detenida, debe encenderse el LED Rojo de parada."*
* **Solución que ellos deben descubrir:**
  ```cpp
  // SOLUCIÓN DEL RETO INDIVIDUAL
  if (digitalRead(boton) == LOW) {
    digitalWrite(motor, HIGH);
    digitalWrite(verde, HIGH);
    digitalWrite(rojo, LOW);
  } else {
    digitalWrite(motor, LOW);
    digitalWrite(verde, LOW);
    digitalWrite(rojo, HIGH);
  }
  ```

#### 5. 📝 Cierre y Evaluación (40 - 45 min)
* Revisas en pantalla la activación del motor y la alternancia de LEDs Rojo/Verde.

#### 📦 Materiales para la Clase 2:
> 🚫 **Ningún material de casa.** Se continuará en las computadoras regulando la velocidad del motor por PWM.
