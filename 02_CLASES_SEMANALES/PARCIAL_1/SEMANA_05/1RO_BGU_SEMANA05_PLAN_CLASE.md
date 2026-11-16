# 📘 1RO BGU — PLAN DE CLASE PRÁCTICO (SEMANA 5)
## 🔘 ENTRADAS DIGITALES: LECTURA DE PULSADORES CON DIGITALREAD() Y RESISTENCIAS PULL-UP

**Propósito de la Clase (Taxonomía Lev / Diapositivas Oficiales):**  
> **Comprender** el funcionamiento de los puertos de entrada digital de Arduino y la configuración de resistencias `INPUT_PULLUP` según las diapositivas oficiales 21 a 28 (`CA.2.RB.5.PR.26-27`), **evitar** estados indeterminados (ruido eléctrico por pines flotantes al aire), y **programar** la lectura en tiempo real de un pulsador con la función `digitalRead()` para gobernar el encendido y apagado de focos LEDs indicadores.

* **Curso:** 1ro BGU  
* **Duración:** 45 Minutos  
* **Modalidad de Trabajo:** 💻 **100% PRÁCTICA ACTIVA (Tinkercad Circuits en PC o Arduino UNO Físico en Mesa)**.  
* **Docente:** Ing. David Castro T.  
* **Diapositivas Oficiales Base:** `CA.2.RB.5.PR.26-27 (Ard mod2)` — Diapositivas 21 a 28 (Entradas Digitales, ¿Cómo se conecta un pulsador? y `INPUT_PULLUP`).  
* **Política de Entrega:** 🟢 **SIN INFORME ESCRITO.** Solo se entrega **1 sola captura de pantalla** o fotografía del circuito simulando con el botón presionado y el código C++ visible en Google Classroom.

---

### 🔗 CONEXIÓN PEDAGÓGICA (SEMANA 4 ➔ SEMANA 5)
* **Semana 4:** Concluimos el cálculo del promedio con condicionales `if - else` (salidas digitales fijas por código).
* **Semana 5 (Hoy - Diapositivas 21 a 28):** *"Hasta ahora el Arduino solo enviaba órdenes hacia afuera (salidas). Hoy le daremos 'ojos y tacto' al microcontrolador: aprenderemos a **leer entradas externas** mediante un pulsador usando `digitalRead()` y la función interna `INPUT_PULLUP`."*

---

### 🛠️ ESQUEMA DEL CIRCUITO (PULSADOR + LED INDICADOR)

* **Componentes:** Placa Arduino UNO, protoboard, 1 Pulsador de 4 pines, 1 Foco LED Verde (o Rojo), 1 Resistencia de $220\ \Omega$, cables jumper.
* **Cableado Simplificado (Modo INPUT_PULLUP - Diapositiva 27):**
  1. Pin **GND** de Arduino al bus negativo ($-$) de la protoboard.
  2. **El Pulsador:**
     * Una pata del pulsador conectada directamente al **Pin Digital 2** de Arduino.
     * La pata opuesta conectada al bus **GND**.  
     *(¡No requiere resistencias externas adicionales gracias a la resistencia Pull-Up interna del chip!)*
  3. **El Foco LED:**
     * Ánodo al **Pin Digital 8**.
     * Cátodo a través de resistencia de $220\ \Omega$ hacia **GND**.

---

### 💻 CÓDIGO C++ PRÁCTICO (Diapositivas 27 y 28)

```cpp
// =======================================================
// RETO ARDUINO: LECTURA DE ENTRADA DIGITAL (PULL-UP)
// Estudiante: [Nombre y Apellido] - 1ro BGU "____"
// Diapositivas Oficiales 27-28 (digitalRead y INPUT_PULLUP)
// =======================================================

const int pinBoton = 2; // Pin de Entrada Digital
const int pinLed = 8;   // Pin de Salida Digital

void setup() {
  // Configurar el pin 2 con resistencia Pull-Up interna (Slide 27)
  pinMode(pinBoton, INPUT_PULLUP);
  
  // Configurar el pin 8 como salida de corriente
  pinMode(pinLed, OUTPUT);
  
  Serial.begin(9600); // Para monitorear el estado en la computadora
}

void loop() {
  // Leer el estado del pulsador (Slide 27):
  // Con INPUT_PULLUP: Sin aplastar = HIGH (1), Aplastado = LOW (0)
  bool estadoBoton = digitalRead(pinBoton);
  
  Serial.print("Estado del Boton: ");
  Serial.println(estadoBoton);

  // Si el botón está aplastado (LOW):
  if (estadoBoton == LOW) {
    digitalWrite(pinLed, HIGH); // Prende el foco mientras se aplasta
  } else {
    digitalWrite(pinLed, LOW);  // Apaga el foco al soltar el botón
  }

  delay(50); // Pequeña pausa anti-rebote
}
```

---

### ⏱️ DESGLOSE DE LOS 45 MINUTOS (100% DINÁMICO)

1. **🎯 El Secreto del "Pin al Aire" — Diapositivas 23-26 (00 - 10 min):**
   * Mostrar en proyector la diapositiva 24: ¿Por qué no conectar un cable flotando al aire? El aire tiene estática y hace que el pin lea valores locos (indeterminados).
   * La solución elegante de Arduino: `pinMode(pin, INPUT_PULLUP);` que conecta una resistencia interna de $20\text{ k}\Omega$ a $+5\text{V}$.
2. **🛠️ Armado del Circuito en Tinkercad / Físico (10 - 25 min):**
   * Conectar el pulsador entre el Pin 2 y GND.
   * Conectar el foco LED con su resistencia en el Pin 8.
3. **🚀 Reto en Pantalla y Prueba Interactiva (25 - 38 min):**
   * Iniciar simulación: comprobar que al dar clic sostenido en el pulsador de Tinkercad el foco se ilumina instantáneamente, y al soltarlo se apaga.
   * *Reto adicional (Lógica Inversa):* Cambiar la condición a `if (estadoBoton == HIGH)` para que el foco pase siempre encendido y solo se apague al pulsar.
4. **📸 Calificación en Vivo y Cierre (38 - 45 min):**
   * El docente pasa registrando el 10/10 en el aula al ver la interacción en pantalla.
   * El estudiante sube **1 captura** del circuito simulando con el botón presionado a Classroom.

---

### 📢 TEXTO LISTO PARA PEGAR EN GOOGLE CLASSROOM (ENTREGA EXPRÉS)

```text
TÍTULO: Práctica N° 5: Entradas Digitales con Pulsador y Resistencia Pull-Up (Diapositivas 21 a 28)

INSTRUCCIONES:
Estimados estudiantes, en esta clase avanzamos con el programa oficial aprendiendo a leer entradas digitales con Arduino C++:

📌 EVIDENCIA DE CLASE (Sin informe escrito):
1. Toma una captura de pantalla clara de tu circuito en Tinkercad Circuits simulando donde se observe:
   - El pulsador conectado al Pin 2 y GND.
   - El foco LED encendido al presionar el pulsador.
   - La ventana de código C++ abierta con la instrucción pinMode(pinBoton, INPUT_PULLUP) y digitalRead().
2. Sube la captura de pantalla a esta tarea y presiona "Entregar".

* Calificación: 10 Puntos evaluados en vivo en el laboratorio de computación.
```
