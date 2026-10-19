# 📘 10MO EGB — PLAN DE CLASE PRÁCTICO (SEMANA 4)
## 🤖 DEL CIRCUITO MANUAL AL CONTROL CON ARDUINO: PROGRAMACIÓN DE PARPADEO (FÍSICO O SIMULADOR)

**Propósito de la Clase (Taxonomía Lev):**  
> **Comprender** la diferencia entre un circuito manual pasivo y un circuito programado por microcontrolador, **cablear** el circuito del foco LED a un pin de salida digital (Pin 8) y GND de Arduino, y **programar** el ritmo de parpadeo modificando la instrucción `delay()` en C++.

* **Curso:** 10mo EGB  
* **Duración:** 45 Minutos  
* **Modalidad de Trabajo:** 🛠️ **100% PRÁCTICA ACTIVA (Armado Físico con Arduino UNO en Mesa o Tinkercad Circuits en PC)**.  
* **Docente:** Ing. David Castro T.  
* **Política de Entrega:** 🟢 **SIN INFORME ESCRITO.** Evaluación 100% formativa en vivo: el docente revisa en pantalla o mesa el foco titilando con el código personalizado del alumno.

---

### 🔗 CONEXIÓN PEDAGÓGICA (SEMANA 3 ➔ SEMANA 4)
* **Semana 3 (Protoboard Básico):** Armamos cables, LED y batería. El foco quedaba siempre prendido sin control.
* **Semana 4 (Hoy):** *"La semana pasada teníamos un circuito que no pensaba. Hoy le conectamos el 'cerebro': la placa Arduino. Con solo 4 líneas de código le diremos cuándo prenderse, cuándo apagarse y a qué velocidad parpadear."*

---

### 🛠️ DOS OPCIONES DE EJECUCIÓN PRÁCTICA

#### 🟢 OPCIÓN A: MONTAJE FÍSICO EN MESA DE TALLER
* **Componentes por puesto:** Placa Arduino UNO física + cable USB, protoboard (la armada la semana pasada), 1 Foco LED, resistencia de $220\ \Omega$ o $330\ \Omega$, 2 cables jumper macho-macho, laptop con Arduino IDE.
* **Conexión en Mesa:**
  1. Conectar cable negro desde el pin **GND** de Arduino hacia el bus azul/negro ($-$) de la protoboard.
  2. El **Cátodo** (pata corta) del LED va conectado a través de la resistencia a ese bus GND.
  3. Conectar cable desde el **Ánodo** (pata larga) del LED directamente al **Pin Digital 8** del Arduino.
  4. Conectar el Arduino por USB a la computadora.

#### 💻 OPCIÓN B: SIMULACIÓN EN COMPUTADORA (Tinkercad Circuits)
* Si no se dispone de kits suficientes para todos los alumnos, abren [Tinkercad Circuits](https://www.tinkercad.com/) y arrastran los mismos componentes virtuales: Arduino UNO, protoboard, LED y resistencia.

---

### 💻 EL CÓDIGO PRÁCTICO (C++)

```cpp
// Práctica Blink - 10mo EGB
const int foco = 8; // Pin conectado al foco

void setup() {
  pinMode(foco, OUTPUT); // Definir pin como salida de corriente
}

void loop() {
  digitalWrite(foco, HIGH); // Prende foco (5V)
  delay(1000);              // Espera 1 segundo
  
  digitalWrite(foco, LOW);  // Apaga foco (0V)
  delay(1000);              // Espera 1 segundo
}
```

---

### ⏱️ DESGLOSE DE LOS 45 MINUTOS (100% EXPERIMENTACIÓN)

1. **🎯 Demostración de Arranque en Pizarra / Proyector (00 - 10 min):**
   * Mostrar cómo el pin digital entrega $+5\text{V}$ (`HIGH`) o $0\text{V}$ (`LOW`).
   * Explicar que `delay(1000)` son milisegundos ($1\text{ s}$).
2. **🛠️ Armado Físico / Virtual y Carga del Código (10 - 25 min):**
   * Los alumnos conectan su circuito y escriben el código.
   * Compilan y cargan al Arduino (o dan clic en "Iniciar Simulación").
   * Comprueban que el LED comienza a parpadear a ritmo de 1 segundo.
3. **🚀 El Reto Práctico: Cambiar el Ritmo (25 - 38 min):**
   * **Misión 1:** Cambiar los tiempos a `delay(150);` para crear un efecto de alarma o estroboscopio rápido.
   * **Misión 2:** Crear un parpadeo asimétrico: `delay(2000);` encendido y `delay(200);` apagado (latido).
4. **✅ Calificación Formativa en Vivo (38 - 45 min):**
   * El docente pasa por cada puesto, ve el LED parpadear al ritmo asignado y firma / registra el 10/10 en su planilla.

---

### 📢 TEXTO RÁPIDO PARA GOOGLE CLASSROOM (REGISTRO FORMATIVO)

```text
TÍTULO: Práctica N° 4: Control de Salidas Digitales con Arduino (Blink y Delays)

INSTRUCCIONES:
Estimados estudiantes, en esta sesión dimos vida al circuito de protoboard de la semana anterior programando nuestra placa Arduino UNO:

📌 EVIDENCIA DE CLASE (Sin informe escrito):
- En clase física: Verificación y calificación formativa directa en tu mesa con el docente.
- En simulación Tinkercad: Sube 1 captura de pantalla de tu circuito simulando con el foco encendido y tu código C++ visible.

* Cero tareas para la casa. ¡Excelente trabajo en el laboratorio!
```
