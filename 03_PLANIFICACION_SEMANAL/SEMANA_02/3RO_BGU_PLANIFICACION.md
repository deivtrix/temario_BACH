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

3. **🧠 Paso 2: Tu Explicación (Usar temporizador y bool):**
   ```cpp
   int motor = 2;
   bool prende = true;
   bool apaga = false;

   void setup() {
     pinMode(motor, OUTPUT);
   }
   ```

4. **🚀 Paso 3: Código Final Fácil (Intermitencia del Transistor):**
   ```cpp
   void loop() {
     digitalWrite(2, true);  // Prende 3 segundos
     delay(3000);

     digitalWrite(2, false); // Apaga 1 segundo
     delay(1000);
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

