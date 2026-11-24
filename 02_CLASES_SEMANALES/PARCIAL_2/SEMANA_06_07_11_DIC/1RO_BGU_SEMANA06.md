# 🔴 1RO BGU — PARCIAL 2 / SEMANA 6 (7 – 11 dic)

> [!IMPORTANT]
> # 👥 ACTIVIDAD GRUPAL EVALUADA
**Tema:** Theremin Musical Controlado por Luz (LDR + Buzzer `tone()`) *(Simulación Virtual en Tinkercad)*  
**Mediador:** David Castro    
**📊 Slides:** Sección 2 (ver PROMPTS_BLOQUES.md)
**Modo de Clase:** Modo A — Mini-teoría (10 min) + Simulación Virtual en Tinkercad (30 min) + Cierre (5 min)  
**Entregable:** Circuito y código probados en Tinkercad *(base para armar el Grupal Físico en Semana 7 — sin chocar kits con 10mo EGB)*.

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Construir** un instrumento musical (Theremin) que cambia de sonido al tapar la luz con la mano.
* **¿Cómo sé que lo logré?** Tu Theremin virtual en Tinkercad cambia el tono del buzzer al variar la luz sobre la LDR.
* **¿Para qué me sirve en la vida?** Muestra cómo un sensor analógico puede controlar actuadores distintos a las luces, como alarmas sonoras, sintetizadores o sensores de proximidad.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **Pregunta relámpago (60 seg):** Conectar oralmente con el concepto clave de la clase anterior.
* **¿Qué decirles?** *"Hoy vamos a construir un instrumento musical que se toca sin tocarlo: solo moviendo la mano encima de un sensor de luz. Se llama Theremin."*
* **Propósito en pantalla:** *"Construir un instrumento musical (Theremin) que cambia de sonido al tapar la luz con la mano."*

### 2. Teoría Corta y Modelación (05 – 15 min)
* **Mismo circuito LDR de la semana pasada** (`A0` + $10\text{k}\Omega$ a GND) + **1 Buzzer** conectado al Pin `8` y `GND`.
* **Lógica clave:**
  `int nota = map(luz, 100, 900, 150, 2000);`  
  `tone(8, nota);`
* Proyectar la simulación funcionando en Tinkercad para que vean cómo suena al mover la luz.

### 3. Trabajo Grupal Físico con Intervención del Mediador (15 – 40 min)
* **Protocolo de Autodepuración (3 pasos antes de llamar al mediador):** 1. Energía/GND -> 2. Pines/Polaridad -> 3. Monitor Serial/Multímetro.
* **Roles rotativos (3 por equipo):** 1. Armado/Diseño -> 2. Código/Parámetros -> 3. Verificador/Evidencia.
* **Instrucción:** En grupos con su kit físico Arduino, arman la LDR + Buzzer, calibran los valores reales de luz del aula en el Monitor Serial y ajustan `map()` para que suene grave al tapar y agudo con luz.
* **Tu rol:** Ayudas a diferenciar si el buzzer es activo o pasivo y a calibrar el rango de `map()` según la luz del laboratorio.

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **2 preguntas rápidas:**
  1. *"¿Qué hace la función `tone(8, nota)`?"*
  2. *"¿Por qué tuvimos que cambiar los números de entrada en `map()` según la luz del aula?"*
* **Cierre:** Demostración en vivo en mesa + entrega de foto grupal y parámetros en Classroom.

## 📢 TEXTO PARA GOOGLE CLASSROOM
```text
TÍTULO: Actividad Grupal Física: Theremin Musical con Luz (LDR + Buzzer)

PROPÓSITO: Construir un instrumento musical (Theremin) que cambia de sonido al tapar la luz con la mano.

CÓDIGO BASE:
void setup() {
  Serial.begin(9600);
}
void loop() {
  int luz = analogRead(A0);
  int nota = map(luz, 100, 900, 200, 2000); // Ajustar según tu lectura real
  tone(8, nota);
  delay(20);
}

INSTRUCCIONES (En grupos):
1. Armen el circuito físico (LDR en A0 con 10k a GND + Buzzer en Pin 8 y GND).
2. Calibren el map() según la luz real del laboratorio.
3. Suban 1 foto del circuito con un papel con sus nombres e indiquen en el comentario:
   - ¿Qué valores mínimo y máximo marcó su LDR?
   - ¿Qué pasaba con el sonido al acercar y alejar la mano?

Calificación: 10 puntos (Actividad Grupal Física).
```
