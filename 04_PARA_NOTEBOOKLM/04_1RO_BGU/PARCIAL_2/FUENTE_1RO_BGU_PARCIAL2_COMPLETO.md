# 📘 1RO BGU — PARCIAL 2 (FUENTE ÚNICA PARA NOTEBOOKLM)
**Materia:** Robótica y Tecnología
**Unidad:** Señales Analógicas y Regulación PWM
**Ya ejecutado al inicio del Parcial 2:** S1-S2: Potenciómetro (analogRead) + 4 LEDs con > y < en Tinkercad y Arduino.


---

# CAPÍTULO #1
**Tema:** Informe de Potenciómetro con 4 LEDs (`analogRead`, `>`, `<`) + Cuestionario *(Individual 1)*  
**Modo de Clase:** Modo B — Actividad Autónoma Evaluada (45 min)  

---

## 🎯 PROPÓSITO LEV Y SENTIDO PRÁCTICO
* **Propósito:** **Explicar** cómo la perilla del potenciómetro enciende 4 LEDs por turnos, igual que un medidor de batería.
* **¿Para qué me sirve en la vida?** Es la misma idea que usan los indicadores de batería, gasolina o volumen por luces.

---

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)

### 1. Inicio, Motivación y Propósito (00 – 05 min)
* **¿Qué decirles?** *"Chicos, ya lograron que 4 LEDs se enciendan por rangos con el potenciómetro. Hoy vamos a documentar técnicamente su circuito y comprobar que entienden qué pasa por dentro."*
* **Presentar el Propósito (Página 2):** *"Explicar cómo la perilla del potenciómetro enciende 4 LEDs por turnos, igual que un medidor de batería."**documentar y verificar** el funcionamiento del potenciómetro con condicionales (`>` / `<`) para entender cómo los sensores controlan indicadores por rangos en la vida real."*

### 2. Encuadre de los 3 Candados Anti-IA (05 – 10 min)
* **Proyectar Página 5:** *"Ojo: no quiero definiciones de ChatGPT. Su informe debe tener: 1) Captura con su Nota de Nombre y LEDs prendidos, 2) Sus 4 números exactos de umbral `>`, y 3) Respuestas de máximo 3 líneas sobre lo que vieron en pantalla."*

### 3. Trabajo Autónomo: Informe Corto (10 – 35 min)
* **Instrucción:** Abren su Tinkercad de la semana pasada, verifican sus valores `>` / `<`, toman la captura, pegan su código en Google Docs y responden las 3 preguntas vivenciales.
* **Tu rol:** Ayudas a quienes tenían el error de que los LEDs no se apagaban al bajar el potenciómetro (faltaba el `else { digitalWrite(..., LOW); }`).

### 4. Cuestionario y Cierre (35 – 45 min)
* **35 – 42 min:** Responden el cuestionario corto de 4 preguntas.
* **42 – 45 min (Preguntas orales de cierre):**
  1. *"¿Cuál es el valor mínimo y máximo de `analogRead()` en Arduino UNO?"*
  2. *"¿Por qué usamos `>` o `<` en lugar de `==` con un potenciómetro?"*

---



---

# CAPÍTULO #2
**Tema:** Atenuador de Brillo LED (`map()` + PWM `analogWrite`) *(Individual 2)*  
**Modo de Clase:** Modo A — Tema Nuevo (45 min)  

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Modificar** el brillo de un LED suavemente con el potenciómetro, como el brillo de un celular.
* **¿Para qué me sirve en la vida?** Así funcionan los reguladores de luz (*dimmers*), el brillo de la pantalla del celular y el control de velocidad de motores.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"La semana pasada sus LEDs solo tenían dos estados: apagado o prendido al 100%. ¿Cómo hacemos para que un LED suba su brillo suavecito como la pantalla del teléfono?"*
* **Propósito en pantalla:** *"Modificar el brillo de un LED suavemente con el potenciómetro, como el brillo de un celular."*

### 2. Teoría Corta y Modelación (05 – 15 min)
* **Pines PWM (`~`):** En Arduino UNO son los pines **3, 5, 6, 9, 10, 11**. Aceptan valores de **0 a 255** con `analogWrite(pin, brillo);`.
* **Función `map()`:** Convierte el rango del potenciómetro (`0–1023`) al rango PWM (`0–255`):
  `int brillo = map(valor, 0, 1023, 0, 255);`
* **Modelación:** Conectar Potenciómetro en `A0` y 1 LED en Pin `~9`, cargar código y girar la perilla.

### 3. Práctica Guiada y Reto Individual (15 – 40 min)
* **15 – 25 min (Guiada):** Todos arman y prueban el código base del atenuador en Tinkercad (o kit físico).
* **25 – 40 min (Reto Solos):** *"Agrega un segundo LED en el Pin `~10` que haga exactamente lo contrario: cuando uno sube al máximo de brillo, el otro baja a cero (`255 - brillo`)."*

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **2 preguntas rápidas:**
  1. *"¿Qué símbolo tienen en la placa los pines que soportan `analogWrite()`?"*
  2. *"¿Por qué usamos `map(valor, 0, 1023, 0, 255)`?"*
* **Cierre:** Comprobar el funcionamiento en vivo y responder las preguntas de verificación.



---

# CAPÍTULO #3
**Tema:** Poste de Alumbrado Público Automático (Sensor LDR)  
**Modo de Clase:** Modo A — Tema Nuevo (45 min)  

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Construir** un circuito con sensor de luz (LDR) que prenda un LED solo cuando oscurece, como un poste de calle.
* **¿Para qué me sirve en la vida?** Para automatizar luces de jardines, pasillos, faros de vehículos y pantallas que ajustan su brillo según la luz del ambiente.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"¿Quién apaga y prende los postes de luz de la calle cada noche? No hay una persona con un interruptor: usan un sensor que 've' la oscuridad. Hoy lo armamos."*
* **Propósito en pantalla:** *"Construir un circuito con sensor de luz (LDR) que prenda un LED solo cuando oscurece, como un poste de calle."*

### 2. Teoría Corta y Modelación (05 – 15 min)
* **¿Qué es una LDR?** Una resistencia que cambia su valor según la luz que recibe.
* **Conexión (Divisor de Voltaje):** 1 pata de la LDR a `5V`, la otra pata al pin **`A0`**, y desde ese mismo punto **`A0`** una resistencia de **10 kΩ a `GND`**.
* **Modelación:** Leer `analogRead(A0)` en Monitor Serial, tapar la LDR con el dedo para ver cómo cambia el número y poner el `if (luz < umbral)`.

### 3. Práctica Guiada y Reto Individual (15 – 40 min)
* **15 – 25 min (Guiada):** Conectan la LDR + resistencia 10 kΩ + 1 LED en Pin 9 y ven los valores de luz vs. oscuridad en el Monitor Serial.
* **25 – 40 min (Reto Solos):** *"Ajusta tu umbral para que el LED prenda cuando tapas la LDR, y agrega un **segundo LED** o haz que el brillo suba gradualmente con `map()` mientras más oscuro esté."*

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **2 preguntas rápidas:**
  1. *"¿Por qué la LDR necesita una resistencia de 10 kΩ hacia `GND` para poder leerse en `A0`?"*
  2. *"¿Qué número marcó tu Monitor Serial con luz vs. tapado con el dedo?"*
* **Cierre:** Visto bueno en kit / subida de captura con valores reales.



---

# CAPÍTULO #4
**Tema:** Theremin Musical Controlado por Luz (LDR + Buzzer `tone()`) *(Grupal Físico)*  
**Modo de Clase:** Modo A/B — Mini-teoría (10 min) + Montaje Grupal Físico (30 min) + Cierre (5 min)  

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Construir** un instrumento musical (Theremin) que cambia de sonido al tapar la luz con la mano.
* **¿Para qué me sirve en la vida?** Muestra cómo un sensor analógico puede controlar actuadores distintos a las luces, como alarmas sonoras, sintetizadores o sensores de proximidad.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"Hoy vamos a construir un instrumento musical que se toca sin tocarlo: solo moviendo la mano encima de un sensor de luz. Se llama Theremin."*
* **Propósito en pantalla:** *"Construir un instrumento musical (Theremin) que cambia de sonido al tapar la luz con la mano."*

### 2. Teoría Corta y Modelación (05 – 15 min)
* **Mismo circuito LDR de la semana pasada** (`A0` + 10 kΩ a GND) + **1 Buzzer** conectado al Pin `8` y `GND`.
* **Lógica clave:**
  `int nota = map(luz, 100, 900, 150, 2000);`  
  `tone(8, nota);`
* Proyectar la simulación funcionando en Tinkercad para que vean cómo suena al mover la luz.

### 3. Trabajo Grupal Físico con Intervención del Mediador (15 – 40 min)
* **Instrucción:** En grupos con su kit físico Arduino, arman la LDR + Buzzer, calibran los valores reales de luz del aula en el Monitor Serial y ajustan `map()` para que suene grave al tapar y agudo con luz.
* **Tu rol:** Ayudas a diferenciar si el buzzer es activo o pasivo y a calibrar el rango de `map()` según la luz del laboratorio.

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **2 preguntas rápidas:**
  1. *"¿Qué hace la función `tone(8, nota)`?"*
  2. *"¿Por qué tuvimos que cambiar los números de entrada en `map()` según la luz del aula?"*
* **Cierre:** Demostración en vivo en mesa + entrega de foto grupal y parámetros.



---

# CAPÍTULO #5
**Tema:** Refuerzo: Calibración con Monitor Serial y Nivelación *(Refuerzo)*  
**Modo de Clase:** Modo B — Refuerzo Práctico (45 min)  

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Verificar** los valores reales de luz en el Monitor Serial para ajustar bien nuestros sensores.
* **¿Para qué me sirve en la vida?** Todo sensor físico cambia según el lugar (más o menos luz); saber leer el Monitor Serial permite ajustar cualquier proyecto en segundos.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"Muchos copiaron un número como `400` para su LDR sin mirar qué número marcaba su propio sensor en esta aula. Hoy aprendemos a diagnosticar y calibrar como ingenieros."*
* **Propósito en pantalla:** *"Verificar los valores reales de luz en el Monitor Serial para ajustar bien nuestros sensores."*

### 2. Demostración Rápida de Diagnóstico (05 – 12 min)
* Proyectar cómo imprimir `Serial.print("Valor: "); Serial.println(analogRead(A0));` y calcular el **punto medio** `(min + max) / 2` como umbral perfecto.

### 3. Nivelación y Reto de Calibración (12 – 40 min)
* Quienes deban alguna práctica del Parcial 2 (Potenciómetro, Atenuador PWM, LDR o Theremin) la completan hoy.
* Quienes estén al día calibran un circuito en Tinkercad/kit usando la fórmula de punto medio e imprimen en Serial `"DIA"` o `"NOCHE"`.

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **2 preguntas rápidas:**
  1. *"¿Cómo encuentras el umbral ideal para un sensor LDR en cualquier habitación?"*
  2. *"¿Qué comando inicia la comunicación entre Arduino y la pantalla de la PC?"*



---

# CAPÍTULO #6
**Tema:** Repaso General de Sensores Analógicos y Cierre de Parcial 2 *(Colchón)*  
**Modo de Clase:** Modo B — Repaso y Nivelación (45 min)  

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Integrar** lo visto de potenciómetro, brillo PWM y sensor de luz antes de pasar a nuevos sensores.
* **¿Para qué me sirve en la vida?** Para consolidar cómo leer cualquier sensor analógico del mundo real antes de trabajar con sensores más complejos.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"Última clase antes de evaluaciones de Áreas Especiales. Hoy repasamos `analogRead`, `map` y PWM, y revisamos que nadie quede debiendo notas."*
* **Propósito en pantalla:** *"Integrar lo visto de potenciómetro, brillo PWM y sensor de luz antes de pasar a nuevos sensores."*

### 2. Repaso / Mini-Reto en Tinkercad (05 – 25 min)
* Quienes están al día combinan en Tinkercad **Potenciómetro + LED PWM** o **LDR + Buzzer** en un solo repaso guiado.

### 3. Nivelación Final (25 – 40 min)
* Revisión de informes/capturas pendientes del Parcial 2.

### 4. Cierre y Autoevaluación Likert (1 al 5) (40 – 45 min)
* Indicaciones para el 11 de enero + autoevaluación del **1 al 5** (*1 = Todavía me cuesta | 5 = Lo domino*):
  1. Leer sensores analógicos con `analogRead()` y usar condicionales `>` / `<`.
  2. Transformar rangos con `map()` y controlar brillo con PWM (`analogWrite()`).
  3. Armar y calibrar una fotoresistencia (LDR) con el Monitor Serial.
  4. Convertir lecturas de luz en sonido usando `tone()` en el Buzzer.

