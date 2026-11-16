# 📘 10MO EGB — PLAN DE CLASE PRÁCTICO (SEMANA 5)
## 🤖 DEL CIRCUITO MANUAL AL CONTROL DIGITAL CON ARDUINO: PROGRAMACIÓN DE SALIDAS (BLINK)

**Propósito de la Clase (Taxonomía Lev / Diapositivas Oficiales):**  
> **Comprender** la transición de un circuito manual pasivo gobernado por interruptor simple a un sistema automatizado por microcontrolador según las diapositivas oficiales 55 a 63 (`CA.1.RB.5.PR.26-27`), **identificar** la estructura básica de programación en C++ (`void setup()` y `void loop()`), y **programar** el encendido, apagado y modulación de tiempos de parpadeo de un foco LED (`pinMode()`, `digitalWrite()`, `delay()`).

* **Curso:** 10mo EGB  
* **Duración:** 45 Minutos  
* **Modalidad de Trabajo:** 🛠️ **100% PRÁCTICA ACTIVA (Armado Físico con Arduino UNO en Mesa o Tinkercad Circuits en PC)**.  
* **Docente:** Ing. David Castro T.  
* **Diapositivas Oficiales Base:** `CA.1.RB.5.PR.26-27 (Ard mod1)` — Diapositivas 55 a 63 (Clase 4: Arduino Módulo 1, Salidas Digitales).  
* **Política de Entrega:** 🟢 **SIN INFORME ESCRITO.** Evaluación 100% formativa en vivo: el docente revisa en pantalla o mesa el foco titilando con el código personalizado del alumno.

---

### 🔗 CONEXIÓN PEDAGÓGICA (SEMANA 4 ➔ SEMANA 5)
* **Semana 4 (Antecedente Real):** Armamos en protoboard el circuito pasivo con LEDs, interruptor simple y pila. El foco solo encendía si el dedo del estudiante mantenía presionado el interruptor.
* **Semana 5 (Hoy - Diapositivas 55 a 63):** *"La semana pasada teníamos un circuito manual que no pensaba. Hoy jubilamos al interruptor manual y a la pila: conectamos la placa Arduino UNO y le enseñamos al microcontrolador a ser un interruptor digital automático gobernado por código C++."*

---

### 🛠️ DOS OPCIONES DE EJECUCIÓN PRÁCTICA

#### 🟢 OPCIÓN A: MONTAJE FÍSICO EN MESA DE TALLER
* **Componentes por puesto:** Placa Arduino UNO física + cable USB, protoboard (con el LED y resistencia que ya armaron), 2 cables jumper macho-macho, laptop con Arduino IDE.
* **Conexión en Mesa:**
  1. Cable negro desde el pin **GND** de Arduino hacia el bus azul/negro ($-$) de la protoboard.
  2. El **Cátodo** (pata corta) del LED va conectado a través de la resistencia de $220\ \Omega$ a ese bus GND.
  3. Cable desde el **Ánodo** (pata larga) del LED directamente al **Pin Digital 8** del Arduino (sustituyendo el interruptor simple).
  4. Conectar el Arduino por USB a la computadora.

#### 💻 OPCIÓN B: SIMULACIÓN EN COMPUTADORA (Tinkercad Circuits)
* Abrir [Tinkercad Circuits](https://www.tinkercad.com/) y armar el circuito con la placa Arduino UNO, protoboard, LED y resistencia conectados al Pin 8 y GND.

---

### 💻 EL CÓDIGO PRÁCTICO (C++ - Diapositivas 60 a 63)

```cpp
// =======================================================
// RETO ARDUINO: CONTROL DIGITAL DE SALIDAS (BLINK)
// Estudiante: [Nombre y Apellido] - 10mo EGB "____"
// Diapositivas Oficiales 60-63 (setup, loop, digitalWrite)
// =======================================================

const int foco = 8; // Pin digital que reemplaza al interruptor simple

void setup() {
  // setup(): Se ejecuta una sola vez al encender el Arduino (Slide 60)
  pinMode(foco, OUTPUT); // Configurar pin 8 como Salida Digital de corriente
}

void loop() {
  // loop(): Se ejecuta continuamente de forma infinita (Slide 61)
  
  digitalWrite(foco, HIGH); // Estado 1 / HIGH: Entrega +5V (Prende el foco)
  delay(1000);              // Pausa de 1000 ms (1 segundo)
  
  digitalWrite(foco, LOW);  // Estado 0 / LOW: Entrega 0V (Apaga el foco)
  delay(1000);              // Pausa de 1 segundo
}
```

---

### ⏱️ DESGLOSE DE LOS 45 MINUTOS (100% EXPERIMENTACIÓN)

1. **🎯 Demostración de Arranque — Diapositivas 57-62 (00 - 10 min):**
   * Mostrar en proyector las diapositivas 58 y 62: ¿Qué es una señal Digital? Solo tiene dos estados: $0\text{ (LOW)}$ y $1\text{ (HIGH)}$, exactamente igual que abrir o cerrar un interruptor.
   * Explicar que `void setup()` prepara el pin (`pinMode`) y `void loop()` repite la acción infinitamente.
2. **🛠️ Armado Físico / Virtual y Carga del Código (10 - 25 min):**
   * Los alumnos conectan su circuito y escriben las líneas de código.
   * Compilan y cargan al Arduino (o dan clic en "Iniciar Simulación").
   * Comprueban que el LED comienza a parpadear a ritmo de 1 segundo sin tocar ningún botón.
3. **🚀 El Reto Práctico: Modular los Delays (25 - 38 min):**
   * **Misión 1 (Alarma rápida):** Modificar a `delay(150);` para ver el destello rápido de emergencia tipo estroboscópico.
   * **Misión 2 (Latido cardíaco):** Crear un parpadeo asimétrico: `delay(2000);` encendido y `delay(200);` apagado.
4. **✅ Calificación Formativa en Vivo (38 - 45 min):**
   * El docente pasa por cada puesto, ve el LED parpadear al ritmo asignado y firma / registra el 10/10 en su planilla.

---

### 📢 TEXTO RÁPIDO PARA GOOGLE CLASSROOM (REGISTRO FORMATIVO)

```text
TÍTULO: Práctica N° 5: Del Interruptor Manual al Control Digital con Arduino (Blink)

INSTRUCCIONES:
Estimados estudiantes, en esta sesión avanzamos desde el circuito manual con interruptor simple de la semana anterior hacia el control digital por microcontrolador (Diapositivas 55 a 63):

📌 EVIDENCIA DE CLASE (Sin informe escrito):
- En clase física: Verificación y calificación formativa directa en tu mesa con el docente.
- En simulación Tinkercad: Sube 1 captura de pantalla de tu circuito simulando con el foco encendido y tu código C++ visible.

* Cero tareas para la casa. ¡Excelente trabajo en el laboratorio!
```
