# 📘 3RO BGU — PARCIAL 2 (FUENTE ÚNICA PARA NOTEBOOKLM)
**Materia:** Robótica y Tecnología
**Unidad:** Microcontroladores y Periféricos Digitales
**Ya ejecutado al inicio del Parcial 2:** S2: ¿Qué es el ESP32? (3.3V, GPIO) + Sirena de Policía en Wokwi.

---

# CAPÍTULO #1
**Tema:** Formulario de Mejora de Calificaciones + Repaso Base ESP32 en Wokwi  

---

## 🎯 PROPÓSITO LEV Y SENTIDO PRÁCTICO
* **Propósito:** **Revisar** cómo funciona el ESP32 y recuperar notas con el formulario antes de pasar a sensores.
* **¿Para qué me sirve en la vida?** Para no quemar placas de 3.3V y tener claras las bases antes de programar proyectos IoT.

---

## 📚 CONTENIDO EXPLICATIVO Y PRÁCTICA

### Teoría Puntual
* **05 – 08 min (Repaso rápido con Página 3):** Recordar: ESP32 trabaja a **3.3V** (no 5V), tiene WiFi/Bluetooth integrado y usa `115200` baudios.
* **08 – 25 min (Formulario):** Trabajo estrictamente individual en el cuestionario de repaso y nivelación.

### Práctica / Reto
* **Instrucción:**
  * *"Quienes debían la Sirena de Policía en Wokwi, termínenla ahora con su nombre en la línea 1 (`// Nombre`) y súbanla."*
  * *"Quienes ya la entregaron, agreguen un tercer LED o un patrón de ráfaga doble para practicar."*

---

---

# CAPÍTULO #2
**Tema:** Semáforo Inteligente con ESP32 en Wokwi *(Individual 1)*  

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Construir** un semáforo de 3 luces en el ESP32 usando Wokwi para controlar varios pines a tiempo.
* **¿Para qué me sirve en la vida?** Para controlar secuencias temporizadas en tráfico, procesos industriales y cualquier sistema con múltiples indicadores.

## 📚 CONTENIDO EXPLICATIVO Y PRÁCTICA

### Teoría Puntual
* **Pines seguros en ESP32 (Wokwi):** Usar por ejemplo `GPIO 12` (Rojo), `GPIO 14` (Amarillo), `GPIO 27` (Verde), cada uno con su resistencia de 220 Ω a `GND`.
* **Buenas prácticas:** Declarar variables `const int` al inicio y usar `Serial.begin(115200);` para imprimir en consola qué luz está activa (`"VERDE - AVANCE"`).

### Práctica / Reto
* **15 – 25 min (Guiada):** Montan en `wokwi.com/projects/new/esp32` los 3 LEDs y prueban el ciclo básico Verde -> Amarillo -> Rojo.
* **25 – 40 min (Reto Solos):** *"Haz que la luz Verde parpadee 3 veces antes de pasar a Amarillo (aviso peatonal) e imprime el estado actual en el Monitor Serial a 115200 baudios."*

---

# CAPÍTULO #3
**Tema:** ESP32 PWM y Buzzer (Zumbador) en Wokwi *(Individual 2)*  

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Modificar** el brillo de un LED y hacer sonar notas en un buzzer con el ESP32 para crear alertas.
* **¿Para qué me sirve en la vida?** Así funcionan los reguladores de luces LED, las alarmas de microondas, timbres y alertas auditivas en equipos médicos o industriales.

## 📚 CONTENIDO EXPLICATIVO Y PRÁCTICA

### Teoría Puntual
* **PWM en ESP32 (Arduino Core 3.x / Wokwi):** Se puede usar `analogWrite(pin, 0–255);` directamente en pines GPIO (ej. `GPIO 13`) con un bucle `for` de `0` a `255`.
* **Buzzer Pasivo:** Conectar un Buzzer en Wokwi (`GPIO 14` y `GND`) y usar `tone(14, frecuencia, duracion);` + `noTone(14);`.

### Práctica / Reto
* **15 – 25 min (Guiada):** Montan 1 LED en `GPIO 13` + 1 Buzzer en `GPIO 14` en Wokwi y prueban el efecto *Fade* (sube/baja brillo) + un pitido corto.
* **25 – 40 min (Reto Solos):** *"Programa una **alarma de emergencia o mini melodía de 4 notas** donde el LED suba su brillo al ritmo de los tonos del buzzer."*

---

# CAPÍTULO #4
**Tema:** Sensor Ultrasonido HC-SR04 con ESP32 en Wokwi  

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Medir** distancias en centímetros con el sensor ultrasonido y el ESP32 para activar una alarma de choque.
* **¿Para qué me sirve en la vida?** Es el principio de los sensores de parqueo de autos, robots que esquivan obstáculos y medidores de nivel en tanques.

## 📚 CONTENIDO EXPLICATIVO Y PRÁCTICA

### Teoría Puntual
* **Pines del HC-SR04:** `VCC` (5V/3.3V en Wokwi), `GND`, `TRIG` (envía pulso `10 µs`), `ECHO` (recibe rebote con `pulseIn()`).
* **Fórmula:** `distancia = duracion * 0.034 / 2;` (velocidad del sonido ida y vuelta).
* **Modelación en Wokwi:** Conectar `TRIG -> GPIO 5`, `ECHO -> GPIO 18`, abrir Monitor Serial y mover el slider de distancia del sensor en Wokwi.

### Práctica / Reto
* **15 – 25 min (Guiada):** Conectan el HC-SR04 en Wokwi y ven la distancia en cm cambiando en el Monitor Serial al mover el slider.
* **25 – 40 min (Reto Solos):** *"Agrega 1 LED Rojo (GPIO 13) y 1 Buzzer (GPIO 14): si la distancia es menor a `30 cm`, prende el LED y suena una alerta; si es mayor, apaga todo."*

---

# CAPÍTULO #5
**Tema:** Proyecto Grupal: Teclado Matricial 4x4 (Piano / Clave de Seguridad) en Wokwi *(Grupal)*  

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Integrar** un teclado 4x4 al ESP32 en Wokwi para leer claves o tocar notas, como una cerradura digital.
* **¿Para qué me sirve en la vida?** Así funcionan los cajeros automáticos, cerraduras digitales de puertas, cajas fuertes y paneles de alarmas.

## 📚 CONTENIDO EXPLICATIVO Y PRÁCTICA

### Teoría Puntual
* **Librería `Keypad.h`:** En Wokwi (`Library Manager` -> agregar `Keypad`).
* **Conexión:** 4 pines de filas + 4 pines de columnas a GPIOs del ESP32 (ej. `13, 12, 14, 27` y `26, 25, 33, 32`).
* **Modelación:** Imprimir la tecla presionada en Monitor Serial (`char tecla = keypad.getKey();`).

### Práctica / Reto
* **Instrucción:** En parejas/grupos eligen **1 de 2 opciones**:
  * **Opción A (Clave de Seguridad):** Si presionan `'1'`, `'2'`, `'3'`, `'4'` (o una tecla secreta como `'#'`), enciende LED Verde; si no, LED Rojo.
  * **Opción B (Mini Piano):** Cada tecla (`1` al `4`) toca una nota distinta en el Buzzer (`tone()`).

---

# CAPÍTULO #6
**Tema:** Refuerzo ESP32 en Wokwi y Cierre de Parcial 2 *(Colchón)*  

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Revisar** nuestras simulaciones del ESP32 en Wokwi y nivelar entregas antes de la evaluación.
* **¿Para qué me sirve en la vida?** Para afianzar la lectura de sensores y periféricos en ESP32 antes de conectar proyectos a Internet e Inteligencia Artificial.

## 📚 CONTENIDO EXPLICATIVO Y PRÁCTICA

### Teoría Puntual
* Estudiantes con prácticas pendientes (Semáforo, PWM/Buzzer, HC-SR04 o Teclado 4x4) completan y suben sus capturas.
* Quienes están al día prueban combinar **HC-SR04 + LED + Buzzer** con mensajes en Monitor Serial.
