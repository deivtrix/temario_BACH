# 📘 1RO BGU — GUÍA DOCENTE DE 45 MINUTOS (CLASE 1)

---

## 📅 CLASE 1: Entradas Digitales y Control de Estados por Botones en C++
* **Duración:** 45 Minutos | **Modalidad:** 💻 [100% PC en Tinkercad Circuits]
* **Propósito Inicial:** Leer entradas digitales externas mediante pulsadores con configuración `INPUT_PULLUP` y tomar decisiones lógicas en C++ para controlar actuadores/LEDs.
* **Conexión con la Vida Real:** Es el sistema de control de tableros de producción industrial o botones de encendido/apagado de sistemas electrónicos (como los botones de ventanas de un auto o controles de máquinas).

---

### ⏱️ DESGLOSE PASO A PASO (45 MINUTOS)

#### 1. 🎯 Motivación y Vida Real (00 - 05 min)
* **¿Qué decirles?** *"Chicos, bienvenidos a 1ro BGU. El año pasado aprendimos a hacer parpadear LEDs solos. Hoy aprenderemos a tomar decisiones: cómo leer botones reales para que el microcontrolador responda a las órdenes de un usuario en tiempo real."*

#### 2. 💡 Teoría Relámpago (05 - 10 min)
* **Las 2 Reglas Clave:**
  1. `pinMode(pin, INPUT_PULLUP);` $\rightarrow$ Activa la resistencia interna de Arduino. Sin aplastar el botón vale 1 (`HIGH`), al aplastarlo vale 0 (`LOW`).
  2. `digitalRead(pin)` $\rightarrow$ Consulta en tiempo real el estado del botón.

#### 3. 💻 Actividad Guiada Contigo (10 - 20 min)
* **Instrucción:** Todos abren Tinkercad Circuits, conectan 2 Botones (Pines 11 y 12), 2 LEDs (Pin 5 Verde, Pin 4 Rojo) y copian contigo en pantalla el código C++ completo:
  ```cpp
  // CÓDIGO GUIADO COMPLETO CLASE 1 (1RO BGU)
  int rojo = 4;
  int verde = 5;
  int b1 = 11; // Botón de Marcha / Encendido
  int b2 = 12; // Botón de Parada / Apagado

  void setup() {
    pinMode(rojo, OUTPUT);
    pinMode(verde, OUTPUT);
    pinMode(b1, INPUT_PULLUP); // Botón 1 activo en LOW
    pinMode(b2, INPUT_PULLUP); // Botón 2 activo en LOW
  }

  void loop() {
    bool estado1 = digitalRead(b1);
    bool estado2 = digitalRead(b2);

    if (estado1 == LOW) {          // Al presionar b1 (Marcha)
      digitalWrite(verde, HIGH);   // Enciende LED verde
      digitalWrite(rojo, LOW);     // Apaga LED rojo
    } 
    else if (estado2 == LOW) {     // Al presionar b2 (Parada)
      digitalWrite(verde, LOW);    // Apaga LED verde
      digitalWrite(rojo, HIGH);    // Enciende LED rojo
    }
  }
  ```

#### 4. 🚀 Actividad Individual (Ellos Solos) (20 - 40 min)
* **El Reto:** Apagas o congelas tu proyector y les lanzas el desafío:
  > *"Añadan un 3er LED (Azul en el Pin 6) para indicar modo Temporizado. Modifiquen el código para que al presionar el Botón 1 (`b1`), el LED Verde se encienda por 3 segundos, se apague automáticamente y luego quede encendido el LED Azul."*
* **Solución que ellos deben descubrir:**
  ```cpp
  // SOLUCIÓN DEL RETO INDIVIDUAL
  if (estado1 == LOW) {
    digitalWrite(verde, HIGH);
    digitalWrite(rojo, LOW);
    digitalWrite(azul, LOW);
    delay(3000); // 3 segundos encendido
    digitalWrite(verde, LOW);
    digitalWrite(azul, HIGH); // Pasa a modo Azul
  }
  ```

#### 5. 📝 Cierre y Evaluación (40 - 45 min)
* Revisas en pantalla las simulaciones de los que lograron la conmutación de los botones y la secuencia del LED Azul.

#### 📦 Materiales para la Clase 2:
> 🚫 **Ningún material de casa.** Todo se trabaja en las computadoras del colegio.

---

---

## 📅 CLASE 2: Lectura de Entradas Digitales (Pulsadores) y Telemetría
* **Duración:** 45 Minutos | **Modalidad:** 💻 [100% PC en Tinkercad Circuits]
* **Propósito Inicial:** Leer señales externas de botones y mostrarlas en el Monitor Serial.
* **Conexión con la Vida Real:** Es el sistema de los botones de subida/bajada de vidrios de un automóvil o los botones de un ascensor.

---

### ⏱️ DESGLOSE PASO A PASO (45 MINUTOS)

#### 1. 🎯 Motivación y Vida Real (00 - 05 min)
* **¿Qué decirles?** *"¿Cómo sabe un coche que presionaste el botón de subir la ventana? Hoy conectaremos botones reales a pines de entrada para leer estados de Presionado (0) y Suelto (1)."*

#### 2. 💡 Teoría Relámpago (05 - 10 min)
* **Las 2 Reglas Clave:**
  1. `pinMode(2, INPUT_PULLUP);` $\rightarrow$ Usa la resistencia interna de Arduino (evita conectar resistencias extra).
  2. `digitalRead(2)` $\rightarrow$ Lee si el botón está aplastado (`LOW` / `0`) o suelto (`HIGH` / `1`).

#### 3. 💻 Actividad Guiada Contigo (10 - 20 min)
* **Instrucción:** Conectan en Tinkercad 1 Pulsador entre el Pin 2 y GND. Escriben contigo en pantalla:
  ```cpp
  // CÓDIGO GUIADO CLASE 2 (1RO BGU)
  int boton = 2;

  void setup() {
    pinMode(boton, INPUT_PULLUP);
    Serial.begin(9600);
  }

  void loop() {
    int estado = digitalRead(boton);
    if (estado == LOW) {
      Serial.println("BOTÓN PRESIONADO [ON]");
    } else {
      Serial.println("BOTÓN SUELTO [OFF]");
    }
    delay(200);
  }
  ```

#### 4. 🚀 Actividad Individual (Ellos Solos) (20 - 40 min)
* **El Reto:**
  > *"Conecten un 2do botón en el Pin 3. Si presionan el Botón 1, el Monitor Serie debe decir: 'ENCENDIENDO AIRE ACONDICIONADO'. Si presionan el Botón 2, debe decir: 'APAGANDO AIRE ACONDICIONADO'."*

#### 5. 📝 Cierre y Evaluación (40 - 45 min)
* Revisión rápida en pantalla del funcionamiento del selector de aire acondicionado.

#### 📦 Materiales para la Clase 3:
> 🚫 **Ningún material de casa.**
