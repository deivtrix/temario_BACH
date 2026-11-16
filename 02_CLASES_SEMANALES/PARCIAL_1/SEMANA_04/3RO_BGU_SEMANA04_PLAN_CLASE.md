# 📘 3RO BGU — PLAN DE CLASE PRÁCTICO (SEMANA 4)
## ⚡ CIRCUITO DE POTENCIA: TRANSISTOR TBJ Y MOTOR DC (ACTIVIDAD GRUPAL)

**Propósito de la Clase (Taxonomía Lev):**  
> **Comprender** colaborativamente la función del transistor bipolar TBJ (NPN) como interruptor de potencia para desacoplar señales lógicas de cargas inductivas de alta corriente (motores DC), **construir en parejas** un circuito de conmutación de motor con diodo volante (*Flyback* 1N4007) de protección en Tinkercad Circuits / mesa física, y **demostrar** el giro del motor a plenas RPM registrando los nombres de los dos integrantes en el código.

* **Curso:** 3ro BGU  
* **Duración:** 45 Minutos  
* **Modalidad de Trabajo:** 👥 **ACTIVIDAD GRUPAL (Parejas de 2 Estudiantes / Tinkercad Circuits o Mesa Física)**.  
* **Docente:** Ing. David Castro T.  
* **Diapositivas Oficiales Base:** `CA.2.RB.5.SG.26-27 (Ard mod4)` — Módulo 4: Etapas de Potencia y Motores DC.  
* **Política de Entrega:** 🟢 **SIN INFORME ESCRITO.** Solo se entrega **1 sola captura de pantalla** por equipo. Cada uno de los dos integrantes sube **la misma captura** a su propio Classroom. La captura debe mostrar obligatoriamente los nombres de los dos integrantes en **dos líneas de comentario** dentro del código.

---

### 🔗 CONEXIÓN PEDAGÓGICA (SEMANA 3 ➔ SEMANA 4)
* **Semana 3 (TBJ con LED):** Se completó y entregó el informe técnico del transistor NPN controlando un foco LED de bajo consumo.
* **Semana 4 (Hoy):** *"Ya terminamos el informe de TBJ la semana pasada; hoy nos metemos en parejas a la **robótica de potencia real**. Conectaremos un **Motor DC**: una carga de alta corriente que exige la etapa de potencia con el transistor TBJ y el diodo de protección para no destruir el circuito."*

---

### 🛠️ ESQUEMA DEL CIRCUITO DE POTENCIA (TBJ + MOTOR DC)

* **Componentes por Pareja:** Placa Arduino UNO (o fuente de $5\text{V}/9\text{V}$), Protoboard, Transistor NPN (2N2222 o TIP120), Motor de aficionado DC, Diodo rectificador 1N4007, Resistencia de base ($1\ \text{k}\Omega$ o $330\ \Omega$), cables jumper.
* **Conexionado de Potencia:**
  1. **Alimentación:** Rieles de la protoboard alimentados con $+5\text{V}$ (o $+9\text{V}$) y GND.
  2. **Motor DC:**
     * Terminal positivo ($+$) del motor al riel positivo.
     * Terminal negativo ($-$) del motor al pin **Colector (C)** del transistor TBJ.
  3. **Transistor NPN:**
     * Pin **Emisor (E)** conectado directamente al riel negativo (GND).
     * Pin **Base (B)** conectado a través de la resistencia de $1\ \text{k}\Omega$ hacia el Pin Digital de Arduino (ej. Pin 9) o pulsador de prueba.
  4. **Diodo Flyback 1N4007 (Antiparalelo):**
     * Conectado en paralelo directo con los dos cables del motor:
       * Cátodo (la patita con la franja plateada/gris) hacia el $+$.
       * Ánodo hacia el Colector.
     *(Absorbe la patada inductiva de alto voltaje cuando el motor se detiene).*

---

### 💻 CÓDIGO C++ CON CANDADO DE DOS LÍNEAS DE COMENTARIO

Los estudiantes abren el editor de código en Tinkercad e insertan al inicio **sus dos nombres en dos líneas de comentario obligatorias**:

```cpp
// =======================================================
// RETO POTENCIA TBJ: ACCIONAMIENTO DE MOTOR DC
// Integrante 1: _________________________________________
// Integrante 2: _________________________________________
// CURSO Y PARALELO: 3ro BGU "____"
// =======================================================

const int pinControlMotor = 9; // Pin conectado a la Base del transistor

void setup() {
  pinMode(pinControlMotor, OUTPUT);
}

void loop() {
  // 1. Encender el motor a plenas RPM
  digitalWrite(pinControlMotor, HIGH);
  delay(3000); // Gira durante 3 segundos

  // 2. Apagar el motor (el diodo flyback absorbe la patada inductiva)
  digitalWrite(pinControlMotor, LOW);
  delay(1500); // Pausa de 1.5 segundos
}
```

---

### ⏱️ DESGLOSE DE LOS 45 MINUTOS (TRABAJO EN PAREJAS)

1. **🎯 Demostración de Potencia en Pizarra (00 - 10 min):**
   * Explicar por qué el motor no se conecta directo al pin de control (el motor jala hasta $500\text{ mA}$; el pin solo da $20\text{ mA}$).
   * El transistor actúa como interruptor electrónico de fuerza.
2. **🛠️ Armado del Circuito en Parejas (10 - 30 min):**
   * Conectar transistor, motor DC y diodo 1N4007 en protoboard/Tinkercad.
   * Escribir el código colocando **los dos nombres en las dos líneas de comentarios**.
3. **🚀 Prueba de Marcha y Tacómetro (30 - 38 min):**
   * Iniciar simulación: comprobar que el motor arranca y marca RPM activas en el tacómetro de Tinkercad.
   * Verificar que al apagarse no se queme el transistor gracias al diodo.
4. **📸 Captura Compartida y Cierre (38 - 45 min):**
   * El equipo toma **una sola captura de pantalla** donde se observe el motor girando a RPM activas y el código C++ abierto con los nombres de los dos integrantes en las dos líneas de comentario.
   * **Cada uno de los dos integrantes sube la misma captura a su respectiva tarea de Classroom.**

---

### 📢 TEXTO LISTO PARA PEGAR EN GOOGLE CLASSROOM (ENTREGA EN PAREJAS)

```text
TÍTULO: Reto Práctico Grupal: Circuito de Potencia con Transistor TBJ y Motor DC

INSTRUCCIONES:
Estimados estudiantes, en esta clase trabajamos en parejas implementando la etapa de potencia para un motor DC utilizando un transistor TBJ (NPN) y protección con diodo flyback:

📌 INSTRUCCIONES DE ENTREGA EN PAREJAS (Sin informe escrito):
1. En el editor de código C++, añadan como comentario en las primeras dos líneas los nombres de los dos integrantes:
   // Integrante 1: Nombre y Apellido
   // Integrante 2: Nombre y Apellido
2. Tomen UNA SOLA captura de pantalla clara de su circuito simulando donde se observe:
   - El motor DC conectado al transistor TBJ girando a RPM activas.
   - El diodo 1N4007 colocado en paralelo con el motor.
   - La ventana de código abierta mostrando claramente las dos líneas con los nombres de los dos integrantes.
3. CADA UNO de los dos integrantes sube la MISMA captura de pantalla a su respectiva cuenta de Google Classroom.

* Calificación: 10 Puntos grupales registrados en el laboratorio de robótica.
```
