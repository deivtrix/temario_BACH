# 📘 3RO BGU — PLANIFICACIÓN DE CLASE (SEMANA 2)

**Propósito de la Clase:**  
> **Construir** un circuito de interfaz de potencia con Transistor BJT NPN (2N2222) en Tinkercad Circuits para conmutar un Motor DC de cinta transportadora industrial mediante comandos digitales de Arduino.

---

### ⏱️ DESGLOSE DE CLASE (45 MINUTOS)

1. **🎯 Motivación y Teoría de Potencia (00 - 10 min):**
   * ¿Por qué un pin digital de Arduino ($40\text{ mA}$) destruye la placa si se conecta a un motor directamente?
   * Explicación del Transistor NPN actuando como "Interruptor Electrónico" (Base, Colector, Emisor).

2. **💻 Paso 1: Demostración con Código Base Novato (10 - 18 min):**
   * El docente muestra un código básico directo sin funciones ni temporización clara (Motor encendido permanentemente):
   ```cpp
   int pinMotor = 9;
   void setup() {
     pinMode(pinMotor, OUTPUT);
   }
   void loop() {
     digitalWrite(pinMotor, HIGH); // Motor encendido directo
   }
   ```

3. **🧠 Paso 2: Explicación y Refactorización del Docente (18 - 25 min):**
   * El docente refactoriza el código introduciendo tiempos de ciclo de trabajo industrial mediante variables tipo `int` y estados booleanos `bool`:
   ```cpp
   int transistorPin = 9;
   bool cintaMarcha = true;
   bool cintaParada = false;
   int tiempoAvance = 3000; // 3 segundos de movimiento
   int tiempoDescanso = 1500; // 1.5 segundos de parada

   void setup() {
     pinMode(transistorPin, OUTPUT);
   }
   ```

4. **🚀 Paso 3: Reto Autónomo de Estudiantes (25 - 40 min):**
   * **Práctica 1 (Cinta Transportadora Industrial):** Los estudiantes deben programar en el `void loop()` la secuencia de carga automatizada:
     * *Fase 1 (Avance):* Encender la cinta (`cintaMarcha`) durante `tiempoAvance`.
     * *Fase 2 (Detención):* Apagar la cinta (`cintaParada`) durante `tiempoDescanso` para simular el empaque de productos.

5. **📝 Calificación Directa en Classroom (40 - 45 min):** Captura del circuito armado con el Transistor NPN + Batería 9V en Tinkercad.

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

