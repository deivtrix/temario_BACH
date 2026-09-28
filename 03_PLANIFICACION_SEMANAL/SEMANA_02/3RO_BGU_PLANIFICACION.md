# 📘 3RO BGU — PLANIFICACIÓN DE CLASE (SEMANA 2)

**Propósito de la Clase:**  
> **Construir** un circuito de interfaz de potencia con Transistor BJT NPN (2N2222) en Tinkercad Circuits para conmutar un Motor DC de cinta transportadora industrial mediante comandos digitales de Arduino.

---
![[{3F2042CE-155C-4FCA-87AF-0FAB3BF170E1}.png]]


### ⏱️ DESGLOSE DE CLASE (45 MINUTOS)

1. **🎯 Motivación y Teoría de Potencia (00 - 10 min):**
   * ¿Por qué un pin digital de Arduino ($40\text{ mA}$) no debe alimentar directamente cargas de potencia y requiere un Transistor BJT NPN como interfaz de conmutación?
   * Identificación de terminales del Transistor BJT NPN: Base (B), Colector (C) y Emisor (E).

2. **💻 Paso 1: Demostración con Código Base Novato (10 - 18 min):**
   * El docente muestra el control directo sin temporización ni funciones (Pin 2 de control de Base según la imagen):
   ```cpp
   int pinControl = 2; // Pin de control conectado a la Base del transistor
   void setup() {
     pinMode(pinControl, OUTPUT);
   }
   void loop() {
     digitalWrite(pinControl, HIGH); // Activación continua de la carga vía transistor
   }
   ```

3. **🧠 Paso 2: Explicación y Refactorización del Docente (18 - 25 min):**
   * El docente refactoriza el código introduciendo variables `bool` y tiempos de ciclo industrial (`int`):
   ```cpp
   int transistorPin = 2; // Pin 2 conectado a la resistencia de Base
   bool estadoMarcha = true;
   bool estadoParada = false;
   int tiempoActivo = 3000;  // 3 segundos de activación
   int tiempoReposo = 1500;  // 1.5 segundos de reposo

   void setup() {
     pinMode(transistorPin, OUTPUT);
   }
   ```

4. **🚀 Paso 3: Reto Autónomo de Estudiantes (25 - 40 min):**
   * **Práctica Guiada (Conmutación con Transistor NPN):** Armar el circuito de la diapositiva en Tinkercad (Pin 2 a la Base del Transistor NPN, Colector a la carga/LED verde y Emisor a GND) y programar en el `void loop()` la secuencia temporizada:
     * *Fase 1 (Activación):* Activar la Base del transistor (`estadoMarcha`) durante `tiempoActivo`.
     * *Fase 2 (Reposo):* Desactivar el transistor (`estadoParada`) durante `tiempoReposo`.

5. **📝 Calificación Directa en Classroom (40 - 45 min):** Captura del circuito armado con el Transistor NPN + Resistencia de Base en Tinkercad.


---

### 🔗 CONEXIÓN PEDAGÓGICA (SEMANA 1 $\rightarrow$ SEMANA 2)
* **Semana 1:** Introducción a cargas de potencia y límites de corriente del Arduino ($40\text{ mA}$).
* **Semana 2:** *"Hoy armaremos el circuito de conmutación de potencia con transistor NPN para mover la cinta transportadora."*

---

### 🔮 ¿QUÉ VEREMOS LA PRÓXIMA CLASE? (SEMANA 3)
* **Tema a Futuro:** **Operar** el control bidireccional (avance y reversa) de motores DC mediante el driver con puente H L298N.

---

### 📦 MATERIALES Y PERMISOS PARA LA PRÓXIMA CLASE (SEMANA 3)
> 📢 **AVISO A ESTUDIANTES:**  
> 💻 **Sin material físico extra.** Continuación en Tinkercad Circuits.

