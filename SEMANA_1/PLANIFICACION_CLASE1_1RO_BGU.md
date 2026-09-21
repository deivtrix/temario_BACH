# 📋 PLANIFICACIÓN DE CLASE 1: 1RO BGU — PROTOCOLO ASÍNCRONO SERIAL UART Y CÁLCULO DE AUTONOMÍA EN ENERGÍA

* **Curso:** 1ro BGU
* **Tema:** Comunicaciones Seriales UART (TX/RX), Baud Rate y Cálculo Práctico de Autonomía de Baterías de EV (Vehículos Eléctricos) en Ah
* **Modalidad:** 💻 100% Práctico en Simulador PC (`tinkercad.com` - Circuits / Arduino C++)
* **Duración:** 45 Minutos
* **PDF Guía Base:** `CA.2.RB.5.PR.26-27(Ard mod2).pdf` (Diapositivas 1 a 5)

---

## 🧭 SECCIÓN 1: CONEXIÓN PUD Y MATRIZ DE LOGRO

* **Competencia Medida:** `CE.CN.B.5.9` (Analizar e interpretar la telemetría de datos en tiempo real mediante protocolos de comunicación industrial y optimización energética).
* **Eje Afectivo (A2 - Compromiso):** Muestra pensamiento crítico frente a la eficiencia energética en la vida cotidiana y la tecnología automotriz de vanguardia. *Cualidad LEV: Analítico / Consciente*.
* **Eje Cognitivo (C3 - Análisis):** Comprende el principio de comunicación asíncrona UART, los roles de transmisión (TX - Pin 1) y recepción (RX - Pin 0), la tasa de baudios (*baud rate*) y la ecuación de autonomía eléctrica ($t = \text{Ah} / \text{A}$).
* **Eje Praxitivo (P3 - Aplicación):** Modela un algoritmo en Arduino C++ que simule el ordenador de a bordo de un auto eléctrico, transmitiendo por el Monitor Serial la telemetría de consumo de corriente y tiempo de autonomía restante.

---

## 🎯 SECCIÓN 2: CONEXIÓN INICIAL Y PROPÓSITO LEV

### 1. ¿Para qué me servirá aprender esto?
Para entender cómo se comunican las computadoras con las máquinas y aprender a calcular cuántas horas de viaje rinde la batería de un carro eléctrico antes de quedarse sin energía.

### 2. PROPÓSITO DE LA CLASE:
🚗 **"Programar la pantalla del computador a bordo de un carro eléctrico para calcular en vivo cuántas horas dura su batería."**

### 3. CONEXIÓN REAL E INTERDISCIPLINAR:
* 🔗 **Vida Real:** Si el auto de tus padres tiene una batería de 60 Ah y gasta 20 Amperios en carretera: $60 / 20 = 3\text{ horas}$ de viaje garantizadas.
* 📚 **Interdisciplinar:** Física (Energía y Corriente) + Computación Automotriz.

### 4. PREGUNTAS DE VERIFICACIÓN DEL PROPÓSITO (Espejo Literal):
* *Pregunta 1:* ¿Qué tablero vamos a programar hoy en la compu?  
  *👉 Respuesta esperada:* El computador a bordo de un auto eléctrico.
* *Pregunta 2:* ¿Qué cálculo importante nos va a mostrar en pantalla?  
  *👉 Respuesta esperada:* Las horas de autonomía que le quedan a la batería.
* *Pregunta 3 (De oro):* Si la batería es de 50 Ah y el motor consume 10 A, ¿cuántas horas podemos manejar?  
  *👉 Respuesta esperada:* 5 horas de viaje ($50 / 10 = 5$).

---

## 📋 SECCIÓN 3: ESTRUCTURA DE LA PLANIFICACIÓN (45 MINUTOS)

> **REGLA LEV:** Máximo 10 Minutos de Teoría / Mínimo 25 Minutos de Práctica Activa.

### 1. Motivación (00-05 min) — El Caso del Auto Eléctrico Varado
* Lanza la pregunta de la vida real: *"Imaginen que van de viaje a la playa en un vehículo eléctrico. El tablero dice que la batería tiene 60 Amperios-hora (Ah) y el motor consume 20 Amperios continuos. ¿Llegamos o nos quedamos varados a mitad del camino?"*

### 2. Encuadre (05-07 min) — Entorno de Telemetría Serial
* **Norma 1:** Sincronizar siempre el Baud Rate entre el código (`Serial.begin`) y la velocidad del Monitor Serial.
* **Plataforma:** Abrir Tinkercad Circuits con la placa Arduino UNO en modo C++ Texto.

### 3. Enunciación (07-15 min — TEORÍA 8 MINUTOS MAX)
* **Demostración en Pantalla con Diapositivas 1-5 (`CA.2.RB.5.PR.26-27(Ard mod2).pdf`):**
  * **Protocolo UART (Universal Asynchronous Receiver-Transmitter):**
    * **Pin 1 (TX - Transmitter):** Envía bits de la placa a la PC.
    * **Pin 0 (RX - Receiver):** Recibe bits de la PC a la placa.
    * **Baud Rate:** Velocidad de transmisión en bits/segundo (Estándar: 9600 bps).
  * **Fórmula Energética de Autonomía de Baterías:**
    $$\text{Autonomía (horas)} = \frac{\text{Capacidad de Batería (Ah)}}{\text{Consumo de Corriente del Motor (A)}}$$

### 4. Simulación / Práctica Intensiva (15-40 min — 25 MINUTOS) — TELEMETRÍA Y CALCULADORA EV EN ARDUINO

* **PASO 1 (Programa Base de Telemetría UART):**
  1. En Tinkercad Circuits, configurar el puerto serie a 9600 bps.
  2. Imprimir el encabezado del sistema de telemetría automotriz.

* **PASO 2 (Código C++ del Ordenador de A Bordo EV):**
  ```cpp
  // PLANIFICACIÓN CLASE 1 - 1RO BGU
  // Telemetría UART y Autonomía de Batería EV
  // Estudiante: [Nombre del Estudiante]

  float capacidadBateriaAh = 60.0; // Batería de 60 Amperios-hora (Ah)
  float consumoMotorA = 20.0;       // Consumo de 20 Amperios (A)
  float autonomiaHoras;

  void setup() {
    Serial.begin(9600); // Inicia UART a 9600 baudios
    
    // Cálculo de Autonomía
    autonomiaHoras = capacidadBateriaAh / consumoMotorA;

    Serial.println("==========================================");
    Serial.println("   SISTEMA DE TELEMETRIA EV - LEV MOTORS  ");
    Serial.println("==========================================");
    Serial.print("Capacidad Bateria: ");
    Serial.print(capacidadBateriaAh);
    Serial.println(" Ah");
    Serial.print("Consumo Motor: ");
    Serial.print(consumoMotorA);
    Serial.println(" A");
    Serial.print("Autonomia Estimada: ");
    Serial.print(autonomiaHoras);
    Serial.println(" Horas de Viaje");
    Serial.println("------------------------------------------");
  }

  void loop() {
    // Transmisión continua de telemetría de monitoreo cada 2 segundos
    Serial.print("TELEMETRIA EN VIVO -> Estado Bateria: OPTIMO | Autonomia: ");
    Serial.print(autonomiaHoras);
    Serial.println(" h");
    delay(2000);
  }
  ```

* **PASO 3 (Desafío de Modificación de Código):**
  1. Los alumnos deben modificar la variable `consumoMotorA` a $30\text{ A}$ (simulando subir una montaña) y verificar en el Monitor Serial cómo se recalcula la autonomía automáticamente a $2\text{ horas}$.

### 5. Cierre y Entregable (40-45 min)
* Revisión de los datos impresos en el Monitor Serial a 9600 bps y validación matemática de la fórmula de autonomía.

---

## 🛠️ SECCIÓN 4: RECURSOS Y CHECKLIST DOCENTE

### Recursos Digitales y Físicos:
* Laptops/PCs de laboratorio.
* Tinkercad Circuits.
* PDF Guía: `CA.2.RB.5.PR.26-27(Ard mod2).pdf`.

### Checklist de Prueba Docente (Hacer antes de la clase):
* [x] Probar el código en Tinkercad asegurando que el cálculo con `float` no trunque los decimales.
* [x] Verificar que el Monitor Serial esté configurado explícitamente a 9600 baudios para evitar caracteres basura.
* [x] Tener lista la diapositiva con el cálculo de Ah para proyectar en la parte teórica.

---

## 📝 SECCIÓN 5: LISTA DE COTEJO DEL ENTREGABLE

| Criterio de Evaluación | Cumple (1.0) | En Proceso (0.5) | No Cumple (0.0) | Observaciones |
| :--- | :---: | :---: | :---: | :--- |
| **1. Configuración UART:** Inclusión correcta de `Serial.begin(9600)` en `void setup()`. | | | | |
| **2. Algoritmo de Autonomía:** Declaración adecuada de variables y fórmula $t = \text{Ah} / \text{A}$. | | | | |
| **3. Impresión Formateada:** Uso de `Serial.print` y `Serial.println` para generar un reporte legible. | | | | |
| **4. Modificación de Parámetros:** Prueba exitosa al cambiar el consumo de corriente y recalcular el tiempo. | | | | |

**Producto Final:** Captura de pantalla del Monitor Serial imprimiendo la telemetría del vehículo eléctrico y el cálculo de autonomía en horas.
