# 📘 10MO EGB — PLAN DE CLASE PRÁCTICO (SEMANA 4)
## 🤖 DEL INTERRUPTOR MANUAL AL CONTROL CON ARDUINO: PROGRAMACIÓN DE SALIDAS DIGITALES (FÍSICO O SIMULADOR)

**Propósito de la Clase (Taxonomía Lev / Diapositivas Oficiales):**  
> **Comprender** la estructura básica de un sketch de Arduino (`setup()`, `loop()`) y la diferencia entre control analógico y digital (0/LOW vs 1/HIGH) según las diapositivas oficiales 55 a 63 (`CA.1.RB.5.PR.26-27`), **reemplazar** el interruptor manual de la semana anterior por un pin digital de salida, y **programar** el encendido, apagado y modulación de tiempos de un foco LED (`pinMode()`, `digitalWrite()`, `delay()`).

* **Curso:** 10mo EGB  
* **Duración:** 45 Minutos  
* **Modalidad de Trabajo:** 🛠️ **100% PRÁCTICA ACTIVA (Armado Físico con Arduino UNO en Mesa o Tinkercad Circuits en PC)**.  
* **Docente:** Ing. David Castro T.  
* **Diapositivas Oficiales Base:** `CA.1.RB.5.PR.26-27 (Ard mod1)` — Diapositivas 55 a 63 (Clase 4: Arduino Módulo 1, Salidas Digitales).  
* **Política de Entrega:** 🟢 **SIN INFORME ESCRITO.** Evaluación 100% formativa en vivo: el docente revisa en pantalla o mesa el foco titilando con el código personalizado del alumno.

---

### 🔗 CONEXIÓN PEDAGÓGICA (SEMANA 3 ➔ SEMANA 4)
* **Semana 3 (Antecedente Real):** Trabajo formativo no calificado donde conectaron focos LEDs en serie y paralelo con un interruptor manual en el protoboard (Diapositivas 41 a 44). El circuito dependía 100% del dedo del estudiante pulsando el interruptor.
* **Semana 4 (Hoy - Diapositivas 55 a 63):** *"La semana pasada teníamos un circuito pasivo: si tu dedo no aplastaba el interruptor, el foco no hacía nada. Hoy jubilamos al interruptor manual y conectamos la placa Arduino: le enseñaremos al microcontrolador a ser un 'interruptor automático digital' que prende y apaga el foco por código C++."*

---

### 🛠️ DOS OPCIONES DE EJECUCIÓN PRÁCTICA

#### 🟢 OPCIÓN A: MONTAJE FÍSICO EN MESA DE TALLER
* **Componentes por puesto:** Placa Arduino UNO física + cable USB, protoboard (la armada la semana pasada), 1 Foco LED, resistencia de $220\ \Omega$ o $330\ \Omega$, 2 cables jumper macho-macho, laptop con Arduino IDE.
* **Conexión en Mesa:**
  1. Conectar cable negro desde el pin **GND** de Arduino hacia el bus azul/negro ($-$) de la protoboard.
  2. El **Cátodo** (pata corta) del LED va conectado a través de la resistencia a ese bus GND.
  3. Conectar cable desde el **Ánodo** (pata larga) del LED directamente al **Pin Digital 8** del Arduino (sustituyendo el cable del interruptor).
  4. Conectar el Arduino por USB a la computadora.

#### 💻 OPCIÓN B: SIMULACIÓN EN COMPUTADORA (Tinkercad Circuits)
* Abrir [Tinkercad Circuits](https://www.tinkercad.com/) y arrastrar los componentes virtuales: Arduino UNO, protoboard, LED y resistencia, reemplazando el pulsador por el Pin Digital 8.

---

### 💻 EL CÓDIGO PRÁCTICO (C++ - Diapositivas 60 a 63)

```cpp
// =======================================================
// RETO ARDUINO: CONTROL DIGITAL DE SALIDAS (BLINK)
// Estudiante: [Nombre y Apellido] - 10mo EGB "____"
// Diapositivas Oficiales 60-63 (setup, loop, digitalWrite)
// =======================================================

const int foco = 8; // Pin digital que reemplaza al interruptor

void setup() {
  // setup(): Se ejecuta una sola vez al encender el Arduino (Slide 60)
  pinMode(foco, OUTPUT); // Configurar pin 8 como Salida Digital
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
   * Los alumnos conectan su circuito y escriben las 6 líneas de código.
   * Compilan y cargan al Arduino (o dan clic en "Iniciar Simulación").
   * Comprueban que el LED comienza a parpadear a ritmo de 1 segundo sin tocar ningún botón.
3. **🚀 El Reto Práctico: Modular los Delays (25 - 38 min):**
   * **Misión 1 (Alarma rápida):** Modificar a `delay(150);` para ver el destello rápido de emergencia.
   * **Misión 2 (Latido cardíaco):** Crear un parpadeo asimétrico: `delay(2000);` encendido y `delay(200);` apagado.
4. **✅ Calificación Formativa en Vivo (38 - 45 min):**
   * El docente pasa por cada puesto, ve el LED parpadear al ritmo asignado y firma / registra el 10/10 en su planilla.

---

### 📢 TEXTO RÁPIDO PARA GOOGLE CLASSROOM (REGISTRO FORMATIVO)

```text
TÍTULO: Práctica N° 4: Del Interruptor Manual al Control Digital con Arduino (Blink)

INSTRUCCIONES:
Estimados estudiantes, en esta sesión avanzamos desde el circuito en protoboard de la semana anterior hacia el control digital por microcontrolador (Diapositivas 55 a 63):

📌 EVIDENCIA DE CLASE (Sin informe escrito):
- En clase física: Verificación y calificación formativa directa en tu mesa con el docente.
- En simulación Tinkercad: Sube 1 captura de pantalla de tu circuito simulando con el foco encendido y tu código C++ visible.

* Cero tareas para la casa. ¡Excelente trabajo en el laboratorio!
```
