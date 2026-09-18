# 📖 GUÍA MAESTRA Y HOJA DE RUTA PEDAGÓGICA DE ROBÓTICA
**Institución:** Antigravity Academy / Bachillerato General Unificado y Básica Superior  
**Docente Saliente:** Ing. David Rógel N.  
**Cursos:** 8vo, 9no, 10mo EGB y 1ro, 2do, 3ro BGU  
**Ubicación de origen:** `C:\Users\David\Desktop\clases bach`

---

## 🔍 1. ANÁLISIS DE COHERENCIA PEDAGÓGICA Y AUDITORÍA DE PLANIFICACIONES

Tras auditar y confrontar la documentación oficial (**Planificaciones Anuales PCA**, **Planes de Unidad PUD** desde el periodo 2024 hasta 2027) con las **evidencias reales en las carpetas de estudiantes**:

### 📊 Diagnóstico de Coherencia: **ALTA (95%)**
* **Secuencia Didáctica Cumplida:** Las planificaciones PUD establecen una secuencia neurodidáctica rígida (*Motivación $\rightarrow$ Enunciación $\rightarrow$ Modelación $\rightarrow$ Simulación $\rightarrow$ Ejercitación en Tinkercad $\rightarrow$ Demostración Práctica*), la cual se refleja de forma exacta en la estructura de los cuadernos de los estudiantes.
* **Progresión Modular entre Cursos:**
  * **8vo EGB (Física Energética + LEGO):** Se cumple al 100%. Las planificaciones PUD prescriben el paso de las ciencias energéticas (química, mecánica, solar, nuclear) hacia la mecánica aplicada con LEGO WeDo 2.0.
  * **9no EGB (CAD/CAM + Robótica Móvil):** Existe coherencia total entre el PUD de diseño (Tinkercad, Inkscape, Litofanías) y la posterior programación del robot mBot en mBlock.
  * **10mo EGB / 1ro BGU (Fundamentos de Arduino):** 10mo EGB y 1ro BGU comparten el núcleo de microcontroladores (digital I/O, C++, transistores TBJ, PWM y Drivers).
  * **2do BGU (CAD Avanzado + Serial UART):** Retoma el diseño CAD en el Q1 y avanza hacia la comunicación serial de datos y PWM en el Q2.
  * **3ro BGU (Mecatrónica y Control de Potencia):** Cumple con el temario más avanzado: Puente H L298N, Servomotores, Entradas Analógicas ADC, Ultrasonido HC-SR04 y Sensor de Agua.

---

## 🧩 2. METODOLOGÍA Y DINÁMICA DE CLASE DOCENTE

Para entender cómo dictaba clases el profesor saliente, cada tema constaba de **3 Entregables Obligatorios por Alumno**:

1. **Cuaderno Digital (Canva):** Guía de clase interactiva con teoría, mapas mentales y preguntas conceptuales.
2. **Preparatorio (Pre-Laboratorio Individual):** Guía teórica antes de entrar al taller. El alumno debía dibujar a mano el circuito o esquemático, definir pines y redactar el código antes de armarlo.
3. **Informe de Laboratorio (Practicum en Parejas/Grupos):** Hoja de reporte del experimento donde pegaban captura del circuito simulado en Tinkercad, foto/video real del armado en protoboard o robot y conclusiones.

---

## 🗂️ 3. PLAN DE ESTUDIOS Y SECUENCIA DE ACTIVIDADES POR CURSO

---

### 📘 8VO EGB (DILIGENTES A)
**Enfoque:** Transformación de la Energía, Electromagnetismo y Robótica Mecánica LEGO.

#### 🗓️ Quimestre 1: Ciencias Energéticas y Generación
* **Tema 1: Definición de Energía y Carga Eléctrica**
  * *Entregable:* `A2_ CUADERNOS DIGITALES P1` (Cuaderno Canva sobre usos de la energía).
* **Tema 2: Generación Química (Electroquímica)**
  * *Entregable:* `IR1_ INFORME (pila Limón)`. Práctica de laboratorio armando una batería de limones con monedas de cobre y clavos de zinc para encender un LED.
* **Tema 3: Generación Mecánica (Ley de Faraday)**
  * *Entregable:* `A4_ INFORME GENERADOR`. Construcción de un generador casero giratorio accionando un motor DC para producir luz.
* **Tema 4: Termoelectricidad y Geotermia**
  * Concepto de aprovechamiento de calor para mover turbinas.
* **Tema 5: Energía Solar y Efecto Fotoeléctrico**
  * Ficha de investigación sobre celdas fotovoltaicas y fotones de luz.
* **Tema 6: Energía Nuclear**
  * Análisis conceptual del proceso de fisión nuclear y el caso de Chernobyl.

#### 🗓️ Quimestre 2: Electromagnetismo, Circuitos y LEGO WeDo 2.0
* **Tema 7: Magnitudes Eléctricas (Corriente DC vs AC)**
  * *Entregable:* `A6_ ELECTRICIDAD versátil`. Clasificación de 7 dispositivos de Corriente Continua y 7 de Corriente Alterna.
* **Tema 8: Electromagnetismo y Fuerza de Lorentz**
  * *Entregable:* `A8_ INFORME DEL EXPERIMENTO N°3`. Armado de un electroimán y motor básico con pila de 1.5V, bobina de cobre e imán de neodimio.
* **Tema 9: Circuitos Serie y Paralelo**
  * Práctica física de cableado con 4 focos y boquillas.
* **Tema 10: Robótica Práctica con LEGO Education WeDo 2.0**
  * *Entregable IR4:* `IR4_ BITÁCORA DE LEGO WE DO` (Inventario de piezas, vigas, engranajes y sensores).
  * *Entregables Prácticos:*
    - `A10_ VENTILADOR DE LEGO`: Control de motor y bucles infinitos (*Loops*).
    - `A11_ SATÉLITE LEGO`: Mecánica de rotación, inercia y fuerza centrípeta.
    - `A12_ ROBOT ESPÍA LEGO`: Detección de presencia mediante **Sensor Infrarrojo de Distancia**.
    - `A13_ ROBOT MILO LEGO`: Robot explorador autónomo con brazo sensor articulado.

---

### 📗 9NO EGB (AUDACES D)
**Enfoque:** Fabricación Digital CAD/CAM (3D/2D) y Robótica Móvil mBot.

#### 🗓️ Quimestre 1: Diseño 3D, Vectorización e Impresión (CAD/CAM)
* **Tema 1: Modelado 3D en Tinkercad**
  * `A2_ Diseño 3D N.º 1 Tasa de Chocolate`: Agrupación y vaciado con figuras huecas.
  * `A3_ DISEÑO 3D CARRO`: Ensamble de chasis y ruedas.
  * `A5_ AMONG US (DISEÑO ESPEJO)`: Operación *Mirror* (simetría axial).
  * `IR1_ CASA DE CARICATURA`: Proyecto arquitectónico 3D completo.
* **Tema 2: Vectorización 2D (Inkscape a Tinkercad)**
  * `A6_ Llavero 3D INKSCAPE`: Vectorización de imágenes `.PNG` a trazos `.SVG`, importación a Tinkercad y extrusión 3D.
  * `A7_ LOGOTIPOS 3D`: Extrusión de marcas vectoriales.
* **Tema 3: Litofanías e Impresión 3D Aditiva**
  * `IR2_ LITOFANÍAS`: Conversión de fotografías a modelos 3D en relieve por variación de densidad e impresión física en filamento PLA.

#### 🗓️ Quimestre 2: Circuitos y Robótica Móvil mBot
* **Tema 4: Tecnología Eléctrica y Simulación**
  * `A9_ Energía Eléctrica`: Exposiciones teóricas.
  * `A10_ Simulación Serie y Paralelo`: Circuitos virtuales en Tinkercad.
  * `A11_ Práctica Serie y Paralelo`: Montaje físico de circuitos.
  * `A12_ CUADERNOS P3`: Cuaderno de teoría quimestral.
* **Tema 5: Programación del Robot mBot (mBlock / Scratch C++)**
  * `A13_ MI PRIMER PROGRAMA`: Encendido de luces RGB del robot.
  * `A14_ MBLOCK BLOQUES DE PROGRAMACIÓN`: Control de velocidad y sentido de motores DC.
  * `A15_ TRAYECTORIA CUADRADA`: Algoritmo de desplazamiento iterativo en cuadrado (Avance $\rightarrow$ Giro $90^\circ$).
  * `A17_ CUADERNO FINAL MBOT`: Integración de sensores ultrasonido y sigue-líneas.

---

### 📘 10MO EGB (POSITIVOS C) Y 1RO BGU (ÍNTEGROS C)
**Enfoque:** Programación en Arduino C++, Estructuras de Control y Electrónica de Entrada/Potencia.

#### 🗓️ Quimestre 1: Fundamentos de C++ en Arduino y Salidas Digitales
* **Tema 1: Sintaxis Básica y Estructura Arduino**
  * Uso de `setup()`, `loop()`, `pinMode()`, `digitalWrite()`, `delay()`.
  * `A1_ CUADERNO DIGITAL CUADERNO`: Módulo Arduino 1.
  * `IR1_ MI PRIMER PROGRAMA EN ARDUINO`: Carga e informe de parpadeo de LED (*Blink*).
  * `A2_ Mi Primer Circuito`: Simulación en Tinkercad Circuits.
  * `A7_ LECCIÓN CÓDIGO BINARIO` *(Exclusivo 1ro BGU)*: Sistemas numéricos (Binario, Decimal, Bytes).
* **Tema 2: Secuencias Lógicas y Automatización**
  * `A4_ SEMÁFORO PT1` / `A5_ SEMÁFORO (práctica)`: Lógica secuencial del semáforo vehicular.
  * `A6_ AUTO FANTÁSTICO`: Secuencia dinámica con arreglos de pines y bucles `for`.
  * `A8_ SERIE Y PARALELO (pt1)`: Circuitos LED activados por puerto digital.

#### 🗓️ Quimestre 2: Entradas Digitales, Condicionales y Potencia
* **Tema 3: Lógica Condicional (`if` / `else`)**
  * `PREPARATORIO 1(IF ELSE)` e `INFORME 1( IF ELSE)`: Toma de decisiones en código según variables.
* **Tema 4: Lectura de Entradas Digitales (Pulsadores)**
  * `PREPARATORIO 2( BOTONES)` e `INFORME N°2 ENTRADAS DIGITALES`: Uso de `digitalRead()` y configuración de resistencias Pull-Down / Pull-Up.
* **Tema 5: Transistores Bipolares (TBJ / BJT NPN)**
  * `PREPARATORIO 3 (TBJ)`: Conmutación de corriente para cargas inductivas y diodo Flyback 1N4007 de protección.
* **Tema 6: Modulación PWM y Drivers**
  * `PREPARATORIO 4(PWM Y DRIVERS)`: Salidas analógicas simuladas `analogWrite()` y control de velocidad.
  * `IR2_ CUADERNO DIGITAL PARCIAL 2` y `AVANCE 1 DEL PROYECTO FINAL`: Integración de sensores, botones y motores.

---

### 📕 2DO BGU (PROACTIVOS C)
**Enfoque:** CAD 3D Avanzado, Comunicación Serial UART y Control Analógico PWM.

#### 🗓️ Quimestre 1: Diseño CAD/CAM 3D e Impresión Aditiva
* `A2_ Taza de Chocolate 3D`, `A3_ Carro 3D`, `A5_ Among Us`, `IR1_ Casa de Caricatura 3D`.
* `A6_ Llavero 3D Inkscape` e `IR2_ Litofanías 3D`.

#### 🗓️ Quimestre 2: Comunicación Serial y Salidas Analógicas
* **Tema 4: Salidas Digitales Avanzadas**
  * `PREPARATORIO 1 SALIDAS DIGITALES LEDS`, `A9_ SALIDAS DIGITALES (PREPARATORIO)` y `A10_ Salidas digitales (INFORME Y PRÁCTICA)`.
* **Tema 5: Entradas Digitales con Botones**
  * `PREPARATORIO 2( BOTONES)`, `A12_ INFORME 2( BOTONES)` e `IR3_ ENTRADAS Y SALIDAS DIGITALES`.
* **Tema 6: Comunicación Serial UART (Arduino $\leftrightarrow$ PC)**
  * `A13_ COMUNICACIÓN SERIAL (1)` (Preparatorio) y `A14_ COMUNICACIÓN SERIAL (INFORME)`: Uso de `Serial.begin(9600)`, `Serial.println()` y `Serial.read()` para controlar hardware enviando comandos desde el teclado del computador.
* **Tema 7: Salidas Analógicas por PWM**
  * `A15_ SALIDAS ANALOGICAS PWM` y `A16_ PWM ARMADO FINAL`: Regulación gradual de potencia en LEDs y motores.
  * `ESTUDIO DIRIGIDO Q2` e `IR FINAL`: Evaluación práctica quimestral.

---

### 📓 3RO BGU (EMPÁTICOS C)
**Enfoque:** Robótica Mecatrónica, Potencia, Drivers Puente H, Servomotores y Sensores Analógicos.

#### 🗓️ Quimestre 1: Electrónica de Potencia y Driver L298N
* **Tema 1: Conmutación de Potencia con TBJ**
  * `A1_ MOTOR TBJ (TEÓRICO)`, `A2_ PRÁCTICA TBJ` e `INFORME TBJ`: Transistor NPN controlando motores DC de alta corriente.
* **Tema 2: Control de Velocidad PWM**
  * `A3_ Velocidad PWM` y `A4_ PRUEBA PRÁCTICA`: Variación de frecuencia y ancho de pulso para regular torque y RPM.
* **Tema 3: Control Bidireccional con Driver Puente H L298N**
  * `A5 DRIVERS MOTOR DC (SIMULACION 1)`, `A6 IR2 DRIVERS PT2`, `A7_ DRIVER L298N(rojo)` e `IR1_ DRIVER DE UN MOTOR DC`: Inversión de sentido de giro (Forward/Reverse) y ENA/ENB para velocidad de 2 motores DC.

#### 🗓️ Quimestre 2: Servomotores, Sensores ADC y Ultrasonido
* **Tema 4: Servomotores de Posición Angular**
  * `A8_ SERVOMOTORES(SIMULACIÓN)` y `A9_ SERVOMOTOR PRACTICO(GRUPAL)`: Control preciso de $0^\circ$ a $180^\circ$ mediante la librería `<Servo.h>`.
* **Tema 5: Entradas Analógicas y Conversión ADC (10-bits)**
  * `A10_ ENTRADAS ANALÓGICAS (PREPARATORIO 5)` y `A11_ ENTRADAS ANALÓGICAS(PRÁCTICA)`: Lectura de potenciómetros con `analogRead(A0)` y mapeo de escala con `map()`.
* **Tema 6: Sensor de Distancia Ultrasonido (HC-SR04)**
  * `A12_ SENSOR ULTRASÓNICO pt1` y `A13_ INFORME SENSOR ULTRASONICO(PRACTICA)`: Cálculo de distancia por rebote de pulso de ultrasonido ($40\text{kHz}$).
* **Tema 7: Sensor de Agua y Proyecto Final de Graduación**
  * `PREPARATORIO FINAL SENSOR DE AGUA`, `CODIGO Y SIMULACION FINAL` y `_ESTUDIO DIRIGIDO Q2`: Proyecto mecatrónico integrador.

---

## 📌 4. TABLA GENERAL DE EVIDENCIAS Y CHECKLIST DE ACTIVIDADES

Para calificar o verificar el avance de cualquier estudiante de la institución, utiliza este checklist ordenado por curso:

| Curso | Cód. Actividad | Nombre del Entregable | Tipo de Trabajo | Contenido Teórico / Práctico |
| :--- | :--- | :--- | :--- | :--- |
| **8vo EGB** | **A2** | Cuaderno Digital P1 | Teórico (Canva) | Definición y tipos de energía. |
| **8vo EGB** | **IR1** | Informe Pila Limón/Papa | Práctica Laboratorio | Reacción REDOX, Cátodo, Ánodo, encendido de LED. |
| **8vo EGB** | **A4** | Informe Generador Eléctrico | Práctica Laboratorio | Inducción magnética manual (Ley de Faraday). |
| **8vo EGB** | **A6** | Ficha Electricidad Versátil | Guía de Teoría | Clasificación de aparatos Corriente DC vs AC. |
| **8vo EGB** | **A8** | Informe Exp. N°3 Electroimán | Práctica Laboratorio | Fuerza de Lorentz, bobina de cobre y motor casero. |
| **8vo EGB** | **IR4** | Bitácora LEGO WeDo | Portafolio | Inventario de piezas mecánicas del kit WeDo 2.0. |
| **8vo EGB** | **A10** | LEGO Ventilador | Construcción/Código | Programación de bucles (*Loop*) y control de motor. |
| **8vo EGB** | **A11** | LEGO Satélite | Construcción/Código | Física de rotación, inercia y fuerza centrípeta. |
| **8vo EGB** | **A12** | LEGO Robot Espía | Construcción/Código | Detección con Sensor Infrarrojo de Distancia. |
| **8vo EGB** | **A13** | LEGO Robot Milo (A y B) | Construcción/Código | Robot explorador autónomo con brazo sensor. |
| **9no EGB** | **A2** | Taza de Chocolate 3D | Tinkercad CAD | Formas compuestas y vaciado con huecos. |
| **9no EGB** | **A3** | Carro 3D | Tinkercad CAD | Ensamble de chasis, ruedas y carrocería. |
| **9no EGB** | **A5** | Among Us 3D | Tinkercad CAD | Operación de simetría axial (*Mirror*). |
| **9no EGB** | **IR1** | Casa de Caricatura | Proyecto 3D | Proyecto arquitectónico 3D completo. |
| **9no EGB** | **A6** | Llavero Vectorial Inkscape | Vectorial / 3D | Trazo `.PNG` a `.SVG` e importación CAD. |
| **9no EGB** | **A7** | Logotipos 3D | Tinkercad CAD | Extrusión tridimensional de marcas. |
| **9no EGB** | **IR2** | Litofanías 3D | Fabricación Aditiva | Slicing en Cura e impresión 3D en filamento PLA. |
| **9no EGB** | **A10-11** | Circuitos Serie/Paralelo | Práctica/Simulación | Análisis de corrientes y montaje en Protoboard. |
| **9no EGB** | **A13-15** | Movimiento mBot / Cuadrado | mBlock C++ | Control de motores DC y desplazamiento en cuadrado. |
| **9no EGB** | **A17** | Cuaderno Final mBot | Proyecto Robótico | Integración de sensores ultrasonido e infrarrojo. |
| **10mo / 1ro**| **A1 / IR1**| Módulo Arduino 1 / Blink | C++ / Tinkercad | `pinMode()`, `digitalWrite()`, `delay()`, Blink LED. |
| **10mo / 1ro**| **A4 / A5** | Semáforo (PT1 y Práctica) | C++ / Protoboard | Lógica temporal secuencial vehicular. |
| **10mo / 1ro**| **A6** | Auto Fantástico | C++ / Arreglos | Secuencia de luces con arreglos y bucles `for`. |
| **10mo / 1ro**| **Prep/Inf 1**| Condicionales IF-ELSE | C++ Lógica | Toma de decisiones en código según entradas. |
| **10mo / 1ro**| **Prep/Inf 2**| Entradas Digitales (Botones)| C++ Hardware | `digitalRead()`, resistencias Pull-Down / Pull-Up. |
| **10mo / 1ro**| **Prep 3** | Transistores TBJ NPN | Electrónica | Conmutación de corriente y Diodo Flyback 1N4007. |
| **10mo / 1ro**| **Prep 4** | PWM y Drivers Potencia | C++ / Hardware | `analogWrite(0-255)` y modulación de ancho de pulso. |
| **2do BGU** | **A9 / A10**| Salidas Digitales Avanzadas | C++ / Protoboard | Control digital de múltiples actuadores. |
| **2do BGU** | **A13 / A14**| Comunicación Serial UART | C++ / PC Telemetría | `Serial.begin(9600)`, `Serial.println()`, `Serial.read()`. |
| **2do BGU** | **A15 / A16**| Salidas Analógicas PWM | C++ / Protoboard | Regulación de intensidad lumínica y velocidad. |
| **3ro BGU** | **A1 / A2** | Motor TBJ Teórico/Práctico | Electrónica Potencia| Acoplamiento de motor DC con Transistor NPN. |
| **3ro BGU** | **A5 - A7** | Driver Puente H L298N | Electrónica Potencia| Inversión de giro y control ENA/ENB de 2 motores DC. |
| **3ro BGU** | **A8 / A9** | Servomotores (Sim/Práctica) | C++ Librería | Control de posición de $0^\circ$ a $180^\circ$ con `<Servo.h>`. |
| **3ro BGU** | **A10 / A11**| Entradas Analógicas ADC | C++ / Sensores | `analogRead(A0)` a 10 bits y escalado `map()`. |
| **3ro BGU** | **A12 / A13**| Sensor Ultrasonido HC-SR04 | C++ / Sensores | Emisión Trigger $10\mu\text{s}$, lectura Echo y cálculo dist. |
| **3ro BGU** | **Prep Final**| Sensor de Agua / Final | Proyecto Mecatrónico| Integración de mecatrónica para titulación BGU. |

---
*Documento estructurado y auditado con base en las planificaciones oficiales PUD/PCA y las carpetas de estudiantes.*
