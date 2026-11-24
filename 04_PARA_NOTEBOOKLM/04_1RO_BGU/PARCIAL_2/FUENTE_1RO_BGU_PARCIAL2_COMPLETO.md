# 📘 1RO BGU — PARCIAL 2 (FUENTE ÚNICA PARA NOTEBOOKLM)
**Materia:** Robótica y Tecnología
**Unidad:** Señales Analógicas y Regulación PWM
**Ya ejecutado al inicio del Parcial 2:** S1-S2: Potenciómetro (analogRead) + 4 LEDs con > y < en Tinkercad y Arduino.

---

# CAPÍTULO #1
**Tema:** Informe de Potenciómetro con 4 LEDs (`analogRead`, `>`, `<`) + Cuestionario *(Individual 1)*  

---

## 🎯 PROPÓSITO LEV Y SENTIDO PRÁCTICO
* **Propósito:** **Explicar** cómo la perilla del potenciómetro enciende 4 LEDs por turnos, igual que un medidor de batería.
* **¿Para qué me sirve en la vida?** Es la misma idea que usan los indicadores de batería, gasolina o volumen por luces.

---

## 📚 CONTENIDO EXPLICATIVO Y PRÁCTICA

### Teoría Puntual
* **Proyectar Página 5:** *"Ojo: no quiero definiciones de ChatGPT. Su informe debe tener: 1) Captura con su Nota de Nombre y LEDs prendidos, 2) Sus 4 números exactos de umbral `>`, y 3) Respuestas de máximo 3 líneas sobre lo que vieron en pantalla."*

### Práctica / Reto
* **Instrucción:** Abren su Tinkercad de la semana pasada, verifican sus valores `>` / `<`, toman la captura, pegan su código en Google Docs y responden las 3 preguntas vivenciales.

---

---

# CAPÍTULO #2
**Tema:** Atenuador de Brillo LED (`map()` + PWM `analogWrite`) *(Individual 2)*  

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Modificar** el brillo de un LED suavemente con el potenciómetro, como el brillo de un celular.
* **¿Para qué me sirve en la vida?** Así funcionan los reguladores de luz (*dimmers*), el brillo de la pantalla del celular y el control de velocidad de motores.

## 📚 CONTENIDO EXPLICATIVO Y PRÁCTICA

### Teoría Puntual
* **Pines PWM (`~`):** En Arduino UNO son los pines **3, 5, 6, 9, 10, 11**. Aceptan valores de **0 a 255** con `analogWrite(pin, brillo);`.
* **Función `map()`:** Convierte el rango del potenciómetro (`0–1023`) al rango PWM (`0–255`):
  `int brillo = map(valor, 0, 1023, 0, 255);`
* **Modelación:** Conectar Potenciómetro en `A0` y 1 LED en Pin `~9`, cargar código y girar la perilla.

### Práctica / Reto
* **15 – 25 min (Guiada):** Todos arman y prueban el código base del atenuador en Tinkercad (o kit físico).
* **25 – 40 min (Reto Solos):** *"Agrega un segundo LED en el Pin `~10` que haga exactamente lo contrario: cuando uno sube al máximo de brillo, el otro baja a cero (`255 - brillo`)."*

---

# CAPÍTULO #3
**Tema:** Poste de Alumbrado Público Automático (Sensor LDR)  

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Construir** un circuito con sensor de luz (LDR) que prenda un LED solo cuando oscurece, como un poste de calle.
* **¿Para qué me sirve en la vida?** Para automatizar luces de jardines, pasillos, faros de vehículos y pantallas que ajustan su brillo según la luz del ambiente.

## 📚 CONTENIDO EXPLICATIVO Y PRÁCTICA

### Teoría Puntual
* **¿Qué es una LDR?** Una resistencia que cambia su valor según la luz que recibe.
* **Conexión (Divisor de Voltaje):** 1 pata de la LDR a `5V`, la otra pata al pin **`A0`**, y desde ese mismo punto **`A0`** una resistencia de **10 kΩ a `GND`**.
* **Modelación:** Leer `analogRead(A0)` en Monitor Serial, tapar la LDR con el dedo para ver cómo cambia el número y poner el `if (luz < umbral)`.

### Práctica / Reto
* **15 – 25 min (Guiada):** Conectan la LDR + resistencia 10 kΩ + 1 LED en Pin 9 y ven los valores de luz vs. oscuridad en el Monitor Serial.
* **25 – 40 min (Reto Solos):** *"Ajusta tu umbral para que el LED prenda cuando tapas la LDR, y agrega un **segundo LED** o haz que el brillo suba gradualmente con `map()` mientras más oscuro esté."*

---

# CAPÍTULO #4
**Tema:** Theremin Musical Controlado por Luz (LDR + Buzzer `tone()`) *(Grupal Físico)*  

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Construir** un instrumento musical (Theremin) que cambia de sonido al tapar la luz con la mano.
* **¿Para qué me sirve en la vida?** Muestra cómo un sensor analógico puede controlar actuadores distintos a las luces, como alarmas sonoras, sintetizadores o sensores de proximidad.

## 📚 CONTENIDO EXPLICATIVO Y PRÁCTICA

### Teoría Puntual
* **Mismo circuito LDR de la semana pasada** (`A0` + 10 kΩ a GND) + **1 Buzzer** conectado al Pin `8` y `GND`.
* **Lógica clave:**
  `int nota = map(luz, 100, 900, 150, 2000);`  
  `tone(8, nota);`
* Proyectar la simulación funcionando en Tinkercad para que vean cómo suena al mover la luz.

### Práctica / Reto
* **Instrucción:** En grupos con su kit físico Arduino, arman la LDR + Buzzer, calibran los valores reales de luz del aula en el Monitor Serial y ajustan `map()` para que suene grave al tapar y agudo con luz.

---

# CAPÍTULO #5
**Tema:** Refuerzo: Calibración con Monitor Serial y Nivelación *(Refuerzo)*  

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Verificar** los valores reales de luz en el Monitor Serial para ajustar bien nuestros sensores.
* **¿Para qué me sirve en la vida?** Todo sensor físico cambia según el lugar (más o menos luz); saber leer el Monitor Serial permite ajustar cualquier proyecto en segundos.

## 📚 CONTENIDO EXPLICATIVO Y PRÁCTICA

### Teoría Puntual
* Proyectar cómo imprimir `Serial.print("Valor: "); Serial.println(analogRead(A0));` y calcular el **punto medio** `(min + max) / 2` como umbral perfecto.

### Práctica / Reto
* Quienes deban alguna práctica del Parcial 2 (Potenciómetro, Atenuador PWM, LDR o Theremin) la completan hoy.
* Quienes estén al día calibran un circuito en Tinkercad/kit usando la fórmula de punto medio e imprimen en Serial `"DIA"` o `"NOCHE"`.

---

# CAPÍTULO #6
**Tema:** Repaso General de Sensores Analógicos y Cierre de Parcial 2 *(Colchón)*  

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Integrar** lo visto de potenciómetro, brillo PWM y sensor de luz antes de pasar a nuevos sensores.
* **¿Para qué me sirve en la vida?** Para consolidar cómo leer cualquier sensor analógico del mundo real antes de trabajar con sensores más complejos.

## 📚 CONTENIDO EXPLICATIVO Y PRÁCTICA

### Teoría Puntual
* Quienes están al día combinan en Tinkercad **Potenciómetro + LED PWM** o **LDR + Buzzer** en un solo repaso guiado.

### Práctica / Reto
* Revisión de informes/capturas pendientes del Parcial 2.
