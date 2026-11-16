# 📘 3RO BGU — PLANIFICACIÓN DE CLASE (SEMANA 2)

**Propósito de la Clase:**  
> **Construir** un circuito de interfaz de potencia con Transistor BJT NPN (2N2222) en Tinkercad Circuits para conmutar un Motor DC de cinta transportadora industrial mediante comandos digitales de Arduino.

---
![[{3F2042CE-155C-4FCA-87AF-0FAB3BF170E1}.png]]


### ⏱️ DESGLOSE DE CLASE (45 MINUTOS)

1. **🎯 Motivación y Teoría de Potencia (00 - 10 min):**
   * ¿Por qué un pin digital de Arduino ($40\text{ mA}$) no debe alimentar directamente cargas de potencia y requiere un Transistor BJT NPN como interfaz de conmutación?
   * Identificación de terminales del Transistor BJT NPN: Base (B), Colector (C) y Emisor (E).

2. **💻 Paso 1: Código Base Directo (Prendido continuo):**
   ```cpp
   void setup() {
     pinMode(2, OUTPUT);
   }

   void loop() {
     digitalWrite(2, HIGH); // Prende el transistor
   }
   ```

3. **🧠 Paso 2: Explicación del Docente (Variables de control y temporización):**
   * El docente muestra el código estructurado con variables `int` para el pin del motor y booleanos `true`/`false` para los estados de conmutación del transistor:
   ```cpp
   // ==========================================
   // PASO 2: EXPLICACIÓN Y REFACTORIZACIÓN
   // Control del Transistor NPN con variables y tiempos
   // ==========================================

   int pinMotor = 2;       // Pin digital conectado a la Base del transistor NPN
   bool activado = true;   // Activa la conducción Colector-Emisor
   bool detenido = false;  // Corta la corriente del motor

   void setup() {
     pinMode(pinMotor, OUTPUT);
   }

   void loop() {
     digitalWrite(pinMotor, activado);  // Enciende el motor
     delay(2000);

     digitalWrite(pinMotor, detenido);  // Apaga el motor
     delay(2000);
   }
   ```

4. **🚀 Paso 3: Reto Autónomo de Estudiantes (Control de Banda Transportadora Industrial):**
   * Explicación a los alumnos: *"El Transistor NPN actúa como el interruptor electromecánico de una **Banda / Cinta Transportadora Industrial**: cuando el Arduino manda `true`, la banda se mueve para avanzar cajas (3 segundos); cuando manda `false`, la banda se detiene (1 segundo) para que un operario o sensor empaque el producto."*
   ```cpp
   // ==========================================
   // PASO 3: RETO FINAL COMPLETO (BANDA INDUSTRIAL)
   // Código 100% funcional y listo para Tinkercad Circuits
   // ==========================================

   int pinMotor = 2;       // Pin conectado a la Base del Transistor 2N2222
   bool avanza = true;     // Conducción en saturación: banda en marcha
   bool frena = false;     // Corte del transistor: banda detenida

   void setup() {
     pinMode(pinMotor, OUTPUT);
   }

   void loop() {
     // La Banda Transportadora avanza para transportar las cajas
     digitalWrite(pinMotor, avanza);
     delay(3000); // 3 segundos de avance

     // La Banda Transportadora se detiene para la estación de empaque
     digitalWrite(pinMotor, frena);
     delay(1000); // 1 segundo de parada
   }
   ```



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

