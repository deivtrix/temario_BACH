# 📖 GUÍA MAESTRA DE PREPARACIÓN DOCENTE — SEMANA 1
**Docente:** Ing. David Rógel N.  
**Semana Lectiva:** Semana 1 (Clase 1 de 24)  
**Duración por Clase:** 45 Minutos  
**Equipamiento Base:** Kit Elegoo UNO R3 Ultimate / Computadoras del Laboratorio

---

## ⏱️ ESTRUCTURA ESTÁNDAR DE LA CLASE DE 45 MINUTOS (ERCA)

* **00 - 05 min | 🎯 MOTIVACIÓN (Experiencia):** Pregunta activadora, caso real o demostración rápida.
* **05 - 20 min | 💡 ENUNCIACIÓN (Conceptualización):** Explicación teórica usando el rango de diapositivas PDF indicadas.
* **20 - 40 min | 🛠️ / 💻 PRÁCTICA GUIADA (Aplicación):** Simulación en PC o ensamblaje en las mesas.
* **40 - 45 min | 📝 CIERRE (Evaluación):** Verificación del funcionamiento y revisión del cuaderno/informe.

---

## 📘 1. 8VO EGB — CLASE 1
* **Tema:** Carga Eléctrica y Formas de Energía
* **Modalidad:** 💻 [SIMULACIÓN INTERACTIVA PhET]
* **PDF Guía a Proyectar:** `CA.1.RB.4.OC.26-27(energía).pdf` *(Diapositivas 1 a 5)*
* **Recursos / Materiales:** Laptops o Computadoras, Canva o Cuaderno Digital.

### 🧠 Notas de Estudio para el Profesor (¿Qué debes explicar?):
1. **Definición de Energía:** Capacidad de realizar un trabajo o transformar la materia.
2. **Ley de Conservación:** La energía no se crea ni se destruye, solo se transforma (ejemplo: energía química de la comida $\rightarrow$ energía mecánica del cuerpo).
3. **Carga Eléctrica y Átomo:** Los protones tienen carga positiva (+), los electrones carga negativa (-). La corriente eléctrica es el flujo ordenado de electrones libres.

### ⏱️ Desglose de los 45 Minutos:
* **00-05 min:** Muestra una linterna apagada sin baterías y pregunta: *"¿Por qué no enciende si tiene el foco en buen estado?"* (Introducción al concepto de fuente de energía).
* **05-20 min:** Proyecta las **Diapositivas 1 a 5** del PDF `CA.1.RB.4.OC.26-27(energía).pdf`. Explica átomo, electrones y tipos de energía.
* **20-40 min:** Pide a los alumnos ingresar a Canva y elaborar un mapa conceptual con 4 tipos de energía usados en su vida diaria.
* **40-45 min:** Revisa en pantalla 3 mapas conceptuales y califica la actividad.

---

## 📗 2. 9NO EGB — CLASE 1
* **Tema:** Introducción a Tinkercad CAD 3D y Manipulación de Volúmenes
* **Modalidad:** 💻 [SIMULACIÓN / PC]
* **PDF Guía a Proyectar:** `CA.1.RB.4.NV.26-27.pdf` *(Diapositivas 1 a 5)*
* **Recursos / Materiales:** Computadoras del laboratorio con acceso a internet (`tinkercad.com`).

### 🧠 Notas de Estudio para el Profesor (¿Qué debes explicar?):
1. **Espacio Tridimensional:** Explicar el plano de trabajo y los 3 ejes cartesiano: $X$ (ancho, rojo), $Y$ (profundidad, verde) y $Z$ (altura, azul).
2. **Navegación 3D:** Clic derecho del mouse para rotar vista, rueda central (*scroll*) para zoom, clic central para desplazar (*pan*).
3. **Formas Sólidas vs Huecas:** Cómo combinar una forma sólida con una forma transparente (hueco) y usar la herramienta **Agrupar (`Ctrl + G`)** para hacer perforaciones.

### ⏱️ Desglose de los 45 Minutos:
* **00-05 min:** Muestra un objeto real (ej. un cubo con un hueco en el centro) y pregunta *"¿Cómo creen que una máquina fabrica un agujero perfecto dentro de un cubo sólido?"*.
* **05-20 min:** Proyecta las **Diapositivas 1 a 5** del PDF `CA.1.RB.4.NV.26-27.pdf`. Realiza una demostración en vivo en Tinkercad creando un cubo y perforándolo con un cilindro hueco.
* **20-40 min:** Práctica guiada: Los estudiantes crean su cuenta en Tinkercad, diseñan un dado 3D e introducen perforaciones cilíndricas en las caras.
* **40-45 min:** Revisa que todos hayan logrado la agrupación sólida-hueca.

---

## 📘 3. 10MO EGB — CLASE 1
* **Tema:** Estructura de un Sketch de Arduino y Sintaxis C++
* **Modalidad:** 💻 [SIMULACIÓN / PC]
* **PDF Guía a Proyectar:** `ARDUINO MÓDULO 1 LEV.pdf` *(Diapositivas 1 a 6)*
* **Recursos / Materiales:** Computadoras con Tinkercad Circuits o IDE de Arduino.

### 🧠 Notas de Estudio para el Profesor (¿Qué debes explicar?):
1. **¿Qué es Arduino UNO?:** Placa con microcontrolador ATmega328P que ejecuta código en bucle.
2. **Las dos funciones obligatorias:**
   * `void setup()`: Se ejecuta **una sola vez** al encender o reiniciar la placa. Se usa para configurar pines.
   * `void loop()`: Se ejecuta de forma **infinita y repetitiva** mientras haya energía.
3. **Sintaxis estricta:** Todas las instrucciones en C++ terminan en punto y coma `;`. C++ distingue mayúsculas y minúsculas (`pinMode` $\neq$ `pinmode`).

### ⏱️ Desglose de los 45 Minutos:
* **00-05 min:** Muestra la tarjeta Arduino UNO física y pregunta: *"¿Qué diferencia hay entre un procesador de computadora y este pequeño chip ATmega328P?"*.
* **05-20 min:** Proyecta las **Diapositivas 1 a 6** del PDF `ARDUINO MÓDULO 1 LEV.pdf`. Escribe en la pantalla la estructura vacía del código explicando `setup()` y `loop()`.
* **20-40 min:** Los alumnos abren Tinkercad Circuits, agregan una placa Arduino UNO virtual y escriben su primer sketch con comentarios `// Mi primer programa`.
* **40-45 min:** Verificación de sintaxis (que no haya errores de compilación por falta de `;`).

---

## 📘 4. 1RO BGU — CLASE 1
* **Tema:** Protocolo Asíncrono Serial UART y Baud Rate
* **Modalidad:** 💻 [SIMULACIÓN / PC]
* **PDF Guía a Proyectar:** `CA.2.RB.5.PR.26-27(Ard mod2).pdf` *(Diapositivas 1 a 5)*
* **Recursos / Materiales:** Computadoras con Tinkercad Circuits / IDE Arduino (Monitor Serial).

### 🧠 Notas de Estudio para el Profesor (¿Qué debes explicar?):
1. **¿Qué es UART?:** Universal Asynchronous Receiver-Transmitter. Protocolo de comunicación bit a bit entre Arduino y la PC.
2. **Pines de Comunicación:** Pin 0 (RX - Recepción) y Pin 1 (TX - Transmisión).
3. **Baud Rate (Velocidad):** $9600\text{ bps}$ (bits por segundo) es el estándar. Ambos dispositivos deben estar sincronizados a la misma velocidad.
4. **Comandos C++:**
   * `Serial.begin(9600);` (en `setup()`) para iniciar el puerto.
   * `Serial.println("Mensaje");` (en `loop()`) para enviar datos con salto de línea.

### ⏱️ Desglose de los 45 Minutos:
* **00-05 min:** Pregunta: *"Cuando conectamos el celular a la computadora por USB, ¿cómo sabe la computadora qué archivos enviarle?"* (Introducción a la telemetría).
* **05-20 min:** Proyecta las **Diapositivas 1 a 5** del PDF `CA.2.RB.5.PR.26-27(Ard mod2).pdf`. Explica TX/RX y la apertura del Monitor Serial.
* **20-40 min:** Práctica en Tinkercad Circuits: Escribir un programa que imprima en el Monitor Serial *"Hola 1ro BGU - Sistema de Telemetría Iniciado"* cada 2 segundos.
* **40-45 min:** Verificación en pantalla del monitor de puerto serie.

---

## 📕 5. 2DO BGU — CLASE 1
* **Tema:** Principio del Puente H y Control Bidireccional de Motores DC
* **Modalidad:** 💻 [SIMULACIÓN / PC]
* **PDF Guía a Proyectar:** `CA.1.RB.4.NV.26-27.pdf` / `FABRICACION.gslides.pdf` *(Diapositivas 1 a 5)*
* **Recursos / Materiales:** Computadoras con Tinkercad Circuits.

### 🧠 Notas de Estudio para el Profesor (¿Qué debes explicar?):
1. **El Problema del Motor DC:** Si conectamos un motor DC directo, solo gira en un sentido. Si invertimos la polaridad (+ y -), gira en sentido contrario.
2. **El Puente H:** Circuito formado por 4 transistores en forma de "H". Activando en diagonal los transistores (Q1 y Q4), el motor gira a la derecha; activando (Q2 y Q3), gira a la izquierda.
3. **Regla de Seguridad:** NUNCA activar los transistores del mismo lado a la vez (Q1 y Q2), de lo contrario ocurre un cortocircuito directo a tierra.

### ⏱️ Desglose de los 45 Minutos:
* **00-05 min:** Muestra un carrito a control remoto y pregunta: *"¿Cómo hace el motor de las ruedas para ir hacia adelante y luego poner marcha atrás sin cambiar cables a mano?"*.
* **05-20 min:** Proyecta las **Diapositivas 1 a 5** de la unidad de potencia. Dibuja el esquema del Puente H en la pizarra explicando la combinación de interruptores.
* **20-40 min:** Simulación en Tinkercad Circuits: Armar un motor DC con 4 interruptores o transistores para lograr el giro horario y antihorario.
* **40-45 min:** Cierre y comprobación de la inversión de sentido de giro.

---

## 📓 6. 3RO BGU — CLASE 1
* **Tema:** Sensor de Nivel de Agua Analógico y Conductividad
* **Modalidad:** 💻 [SIMULACIÓN / PC]
* **PDF Guía a Proyectar:** `CA.2.RB.5.SG.26-27(Ard mod4).pdf` *(Diapositivas 1 a 5)*
* **Recursos / Materiales:** Tinkercad Circuits / Sensor de nivel de agua (Kit Elegoo - Placa roja con trazas).

### 🧠 Notas de Estudio para el Profesor (¿Qué debes explicar?):
1. **Funcionamiento del Sensor de Agua:** Consiste en una serie de trazas de cobre paralelas expuestas. El agua actúa como un conductor de resistencia variable.
2. **Resistencia Inversa al Nivel:** A mayor profundidad de inmersión en el líquido, más trazas de cobre se conectan por el agua, aumentando la conductividad y el voltaje de salida.
3. **Lectura ADC en Arduino:** Conectado al pin A0, entrega valores de $0$ (seco) a aproximadamente $500\text{-}650$ (totalmente sumergido).

### ⏱️ Desglose de los 45 Minutos:
* **00-05 min:** Muestra el sensor de nivel de agua del Kit Elegoo y pregunta: *"¿Cómo sabe un tanque de agua industrial o una lavadora inteligente cuándo el agua llegó al tope sin derramarse?"*.
* **05-20 min:** Proyecta las **Diapositivas 1 a 5** del PDF `CA.2.RB.5.SG.26-27(Ard mod4).pdf`. Explica el principio de conductividad y lectura analógica `analogRead(A0)`.
* **20-40 min:** Simulación en Tinkercad Circuits: Conectar el sensor de agua al pin A0 e imprimir el porcentaje de nivel de agua en el Monitor Serial ($Nivel = map(val, 0, 650, 0, 100)$).
* **40-45 min:** Verificación de fórmulas de conversión e informes.

---

## 📝 RESUMEN DE MATERIALES A TENER LISTOS (SEMANA 1)

* **Proyector:** Listo para mostrar los rangos de diapositivas PDF indicados.
* **Computadoras de Estudiantes:** Con navegador web abierto en `tinkercad.com` y `canva.com`.
* **Para el Docente:** Tener esta guía a la mano para repasar los 5 minutos previos a cada clase.
