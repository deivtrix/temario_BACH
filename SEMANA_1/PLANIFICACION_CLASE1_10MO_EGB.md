# 📋 PLANIFICACIÓN DE CLASE 1: 10MO EGB — ESTRUCTURA DE UN SKETCH DE ARDUINO Y SINTAXIS C++

* **Curso:** 10mo EGB
* **Tema:** Arquitectura del Microcontrolador Arduino UNO, Sintaxis C++, `void setup()`, `void loop()` y Telemetría Serial
* **Modalidad:** 💻 100% Práctico en Simulador PC (`tinkercad.com` - Módulo Circuits)
* **Duración:** 45 Minutos
* **PDF Guía Base:** `ARDUINO MÓDULO 1 LEV.pdf` (Diapositivas 1 a 6)

---

## 🧭 SECCIÓN 1: CONEXIÓN PUD Y MATRIZ DE LOGRO

* **Competencia Medida:** `CE.CN.4.8` (Programar sistemas embebidos mediante lenguaje de código estructurado para el control de actuadores y sensores).
* **Eje Afectivo (A2 - Compromiso):** Valora el rigor de la sintaxis en la programación y demuestra perseverancia en la corrección de errores de código. *Cualidad LEV: Riguroso / Persistente*.
* **Eje Cognitivo (C3 - Análisis):** Comprende la diferencia estructural y de ciclo de vida entre la función de configuración inicial `void setup()` y el bucle infinito `void loop()`.
* **Eje Praxitivo (P3 - Aplicación):** Escribe un Sketch en C++ para Arduino UNO en Tinkercad Circuits controlando el LED integrado del pin 13 e imprimiendo estados en el Monitor Serial.

---

## 🎯 SECCIÓN 2: CONEXIÓN INICIAL Y PROPÓSITO LEV

### 1. ¿Para qué me servirá aprender esto?
Para darle "cerebro" y vida a tus proyectos de electrónica: aprenderás a programar en el lenguaje real (C++) para controlar luces, motores y pantallas desde la computadora.

### 2. PROPÓSITO DE LA CLASE:
💡 **"Escribir tu primer programa C++ en Arduino para hacer parpadear una luz LED y mandar mensajes en vivo a la pantalla."**

### 3. CONEXIÓN REAL E INTERDISCIPLINAR:
* 🔗 **Vida Real:** Así funcionan los semáforos de la ciudad: ejecutan un código que enciende y apaga luces en un ciclo infinito.
* 📚 **Interdisciplinar:** Lógica de Programación + Robótica.

### 4. PREGUNTAS DE VERIFICACIÓN DEL PROPÓSITO (Espejo Literal):
* *Pregunta 1:* ¿Qué vamos a programar hoy en Arduino?  
  *👉 Respuesta esperada:* El parpadeo del LED 13 y mensajes en el monitor serial.
* *Pregunta 2:* ¿En qué lenguaje de código vamos a programar?  
  *👉 Respuesta esperada:* En C++.
* *Pregunta 3 (De oro):* ¿Qué signo obligatorio debemos poner siempre al final de cada orden en C++?  
  *👉 Respuesta esperada:* El punto y coma `;`.

---

## 📋 SECCIÓN 3: ESTRUCTURA DE LA PLANIFICACIÓN (45 MINUTOS)

> **REGLA LEV:** Máximo 10 Minutos de Teoría / Mínimo 25 Minutos de Práctica Activa.

### 1. Motivación (00-05 min) — El Microprocesador vs el Microcontrolador
* Muestra la placa física Arduino UNO (o su imagen en pantalla) y la compara con la placa madre de una laptop: *"¿Por qué este pequeño chip ATmega328P de $5 USD puede controlar un brazo robótico sin necesitar Windows ni mouse?"*

### 2. Encuadre (05-07 min) — Entorno de Desarrollo Tinkercad Circuits
* **Norma 1:** Atención estricta a mayúsculas y minúsculas en C++ (`pinMode` NO es lo mismo que `pinmode`).
* **Plataforma:** Entrar a `tinkercad.com` $\rightarrow$ Diseños $\rightarrow$ Circuitos $\rightarrow$ Crear nuevo circuito $\rightarrow$ Arrastrar **Arduino UNO**.

### 3. Enunciación (07-15 min — TEORÍA 8 MINUTOS MAX)
* **Demostración en Pantalla con Diapositivas 1-6 (`ARDUINO MÓDULO 1 LEV.pdf`):**
  * **Anatomía del Sketch C++:**
    * `void setup() { ... }`: Configuración de pines (`pinMode`) y comunicación serial. Se ejecuta **1 sola vez**.
    * `void loop() { ... }`: Bucle de ejecución **infinito**.
  * **Comandos Fundamentales:**
    * `pinMode(13, OUTPUT);` $\rightarrow$ Configura el pin 13 como salida digital.
    * `digitalWrite(13, HIGH / LOW);` $\rightarrow$ Envía 5V (HIGH) o 0V (LOW).
    * `delay(1000);` $\rightarrow$ Pausa la ejecución por 1000 milisegundos (1 segundo).
    * `Serial.begin(9600);` y `Serial.println("Texto");` $\rightarrow$ Telemetría a la PC.

### 4. Simulación / Práctica Intensiva (15-40 min — 25 MINUTOS) — RETO BLINK + TELEMETRÍA SERIAL

* **PASO 1 (Configuración del Entorno):**
  1. Cambiar la vista de código en Tinkercad de "Bloques" a **"Texto"**.
  2. Borrar el código por defecto y escribir la estructura limpia desde cero.

* **PASO 2 (Escritura del Código C++):**
  ```cpp
  // PLANIFICACIÓN CLASE 1 - 10MO EGB
  // Estudiante: [Nombre del Estudiante]

  void setup() {
    pinMode(13, OUTPUT);      // Configura el LED integrado L como Salida
    Serial.begin(9600);       // Inicia la comunicación serial a 9600 baudios
  }

  void loop() {
    digitalWrite(13, HIGH);   // Enciende el LED (5V)
    Serial.println("LED ENCENDIDO [ON]");
    delay(1000);              // Espera 1 segundo

    digitalWrite(13, LOW);    // Apaga el LED (0V)
    Serial.println("LED APAGADO [OFF]");
    delay(1000);              // Espera 1 segundo
  }
  ```

* **PASO 3 (Ejecución y Depuración):**
  1. Hacer clic en **"Iniciar Simulación"**.
  2. Abrir el **Monitor Serie** (botón en la parte inferior derecha).
  3. Verificar que el LED etiquetado con la letra `L` parpadee al ritmo del mensaje transmitido por consola.

### 5. Cierre y Entregable (40-45 min)
* Revisión de código sin errores sintácticos (sin fallas de `;` o llaves descompensadas).

---

## 🛠️ SECCIÓN 4: RECURSOS Y CHECKLIST DOCENTE

### Recursos Digitales y Físicos:
* Laptops/PCs de laboratorio.
* Tinkercad Circuits.
* PDF Guía: `ARDUINO MÓDULO 1 LEV.pdf`.

### Checklist de Prueba Docente (Hacer antes de la clase):
* [x] Simular el código en Tinkercad Circuits comprobando que el Monitor Serial imprima a 9600 bps.
* [x] Verificar que los estudiantes sepan cambiar de la interfaz de Bloques a Texto en Tinkercad.
* [x] Tener lista la explicación de errores comunes (ej: olvidar el `;` o escribir `serial` con minúscula).

---

## 📝 SECCIÓN 5: LISTA DE COTEJO DEL ENTREGABLE

| Criterio de Evaluación | Cumple (1.0) | En Proceso (0.5) | No Cumple (0.0) | Observaciones |
| :--- | :---: | :---: | :---: | :--- |
| **1. Estructura C++:** Inclusión correcta de `void setup()` y `void loop()` con llaves cerradas. | | | | |
| **2. Control Digital:** Uso correcto de `digitalWrite(13, HIGH/LOW)` con delays de 1s. | | | | |
| **3. Telemetría Serial:** Configuración de `Serial.begin(9600)` e impresión de estado en consola. | | | | |
| **4. Sintaxis Limpia:** Código libre de errores de compilación y comentado con el nombre del alumno. | | | | |

**Producto Final:** Archivo de código C++ / Captura de pantalla de la simulación en Tinkercad con el Monitor Serial imprimiendo los estados `[ON]` y `[OFF]`.
