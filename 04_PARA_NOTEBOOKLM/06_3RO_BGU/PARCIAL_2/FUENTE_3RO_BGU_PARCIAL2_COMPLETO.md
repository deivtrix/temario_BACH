# 📘 3RO BGU — PARCIAL 2 (FUENTE ÚNICA PARA NOTEBOOKLM)
**Materia:** Robótica y Tecnología
**Unidad:** Microcontroladores y Periféricos Digitales
**Ya ejecutado al inicio del Parcial 2:** S2: ¿Qué es el ESP32? (3.3V, GPIO) + Sirena de Policía en Wokwi.


---

# CAPÍTULO #1
**Tema:** Formulario de Mejora de Calificaciones + Repaso Base ESP32 en Wokwi  
**Modo de Clase:** Modo B — Recuperación y Nivelación Autónoma (45 min)  

---

## 🎯 PROPÓSITO LEV Y SENTIDO PRÁCTICO
* **Propósito:** **Revisar** cómo funciona el ESP32 y recuperar notas con el formulario antes de pasar a sensores.
* **¿Para qué me sirve en la vida?** Para no quemar placas de 3.3V y tener claras las bases antes de programar proyectos IoT.

---

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)

### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"Chicos, hoy tenemos una oportunidad puntual para nivelar y mejorar calificaciones antes de avanzar a sensores en el ESP32. Primero hacemos el formulario individual y luego nivelamos en Wokwi."*
* **Presentar el Propósito (Página 2):** *"Revisar cómo funciona el ESP32 y recuperar notas con el formulario antes de pasar a sensores."**verificar y corregir** los fundamentos del ESP32 (pines GPIO y 3.3V) para consolidar la base técnica sin dañar hardware."*

### 2. Repaso Express + Formulario Individual (05 – 25 min)
* **05 – 08 min (Repaso rápido con Página 3):** Recordar: ESP32 trabaja a **3.3V** (no 5V), tiene WiFi/Bluetooth integrado y usa `115200` baudios.
* **08 – 25 min (Formulario):** Trabajo estrictamente individual en el cuestionario de repaso y nivelación.

### 3. Nivelación Práctica en Wokwi (25 – 40 min)
* **Instrucción:**
  * *"Quienes debían la Sirena de Policía en Wokwi, termínenla ahora con su nombre en la línea 1 (`// Nombre`) y súbanla."*
  * *"Quienes ya la entregaron, agreguen un tercer LED o un patrón de ráfaga doble para practicar."*
* **Tu rol:** Revisas los enlaces/capturas de quienes están recuperando y corriges errores de pines GPIO o resistencias en Wokwi.

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **Retroalimentación rápida del formulario:**
  1. *"¿Por qué un sensor o alimentación de 5V directo al pin GPIO puede dañar el ESP32?"*
  2. *"¿A cuántos baudios configuramos el Monitor Serial del ESP32?"*

---



---

# CAPÍTULO #2
**Tema:** Semáforo Inteligente con ESP32 en Wokwi *(Individual 1)*  
**Modo de Clase:** Modo A — Tema Nuevo / Ambientación (45 min)  

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Construir** un semáforo de 3 luces en el ESP32 usando Wokwi para controlar varios pines a tiempo.
* **¿Para qué me sirve en la vida?** Para controlar secuencias temporizadas en tráfico, procesos industriales y cualquier sistema con múltiples indicadores.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"La semana pasada hicimos la nivelación y la sirena de 2 LEDs. Hoy nos ambientamos con el clásico semáforo de 3 luces, pero ya en arquitectura ESP32."*
* **Propósito en pantalla:** *"Construir un semáforo de 3 luces en el ESP32 usando Wokwi para controlar varios pines a tiempo."*

### 2. Teoría Corta y Modelación (05 – 15 min)
* **Pines seguros en ESP32 (Wokwi):** Usar por ejemplo `GPIO 12` (Rojo), `GPIO 14` (Amarillo), `GPIO 27` (Verde), cada uno con su resistencia de 220 Ω a `GND`.
* **Buenas prácticas:** Declarar variables `const int` al inicio y usar `Serial.begin(115200);` para imprimir en consola qué luz está activa (`"VERDE - AVANCE"`).

### 3. Práctica Guiada y Reto Individual (15 – 40 min)
* **15 – 25 min (Guiada):** Montan en `wokwi.com/projects/new/esp32` los 3 LEDs y prueban el ciclo básico Verde -> Amarillo -> Rojo.
* **25 – 40 min (Reto Solos):** *"Haz que la luz Verde parpadee 3 veces antes de pasar a Amarillo (aviso peatonal) e imprime el estado actual en el Monitor Serial a 115200 baudios."*

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **2 preguntas rápidas:**
  1. *"¿Por qué declaramos los pines como `const int` en lugar de escribir el número directo en cada `digitalWrite`?"*
  2. *"¿Qué velocidad de baudios usamos en `Serial.begin()` con el ESP32?"*
* **Cierre:** Comprobar el funcionamiento en vivo y responder las preguntas de verificación.



---

# CAPÍTULO #3
**Tema:** ESP32 PWM y Buzzer (Zumbador) en Wokwi *(Individual 2)*  
**Modo de Clase:** Modo A — Tema Nuevo (45 min)  

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Modificar** el brillo de un LED y hacer sonar notas en un buzzer con el ESP32 para crear alertas.
* **¿Para qué me sirve en la vida?** Así funcionan los reguladores de luces LED, las alarmas de microondas, timbres y alertas auditivas en equipos médicos o industriales.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"En el ESP32 casi todos los pines GPIO sirven para PWM. Hoy vamos a hacer que un LED suba y baje de brillo suavemente y que un buzzer suene con distintas notas."*
* **Propósito en pantalla:** *"Modificar el brillo de un LED y hacer sonar notas en un buzzer con el ESP32 para crear alertas."*

### 2. Teoría Corta y Modelación (05 – 15 min)
* **PWM en ESP32 (Arduino Core 3.x / Wokwi):** Se puede usar `analogWrite(pin, 0–255);` directamente en pines GPIO (ej. `GPIO 13`) con un bucle `for` de `0` a `255`.
* **Buzzer Pasivo:** Conectar un Buzzer en Wokwi (`GPIO 14` y `GND`) y usar `tone(14, frecuencia, duracion);` + `noTone(14);`.

### 3. Práctica Guiada y Reto Individual (15 – 40 min)
* **15 – 25 min (Guiada):** Montan 1 LED en `GPIO 13` + 1 Buzzer en `GPIO 14` en Wokwi y prueban el efecto *Fade* (sube/baja brillo) + un pitido corto.
* **25 – 40 min (Reto Solos):** *"Programa una **alarma de emergencia o mini melodía de 4 notas** donde el LED suba su brillo al ritmo de los tonos del buzzer."*

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **2 preguntas rápidas:**
  1. *"¿Qué cambia en el buzzer cuando aumentas el número de frecuencia en `tone(pin, freq)`?"*
  2. *"¿Qué rango de valores acepta `analogWrite()` para variar el brillo del LED?"*
* **Cierre:** Comprobar el funcionamiento en vivo y responder las preguntas de verificación.



---

# CAPÍTULO #4
**Tema:** Sensor Ultrasonido HC-SR04 con ESP32 en Wokwi  
**Modo de Clase:** Modo A — Tema Nuevo (45 min)  

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Medir** distancias en centímetros con el sensor ultrasonido y el ESP32 para activar una alarma de choque.
* **¿Para qué me sirve en la vida?** Es el principio de los sensores de parqueo de autos, robots que esquivan obstáculos y medidores de nivel en tanques.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"¿Cómo sabe un carro moderno o un robot que está a 20 cm de chocar sin tocar la pared? Usa ondas de sonido que rebotan, igual que los murciélagos."*
* **Propósito en pantalla:** *"Medir distancias en centímetros con el sensor ultrasonido y el ESP32 para activar una alarma de choque."*

### 2. Teoría Corta y Modelación (05 – 15 min)
* **Pines del HC-SR04:** `VCC` (5V/3.3V en Wokwi), `GND`, `TRIG` (envía pulso `10 µs`), `ECHO` (recibe rebote con `pulseIn()`).
* **Fórmula:** `distancia = duracion * 0.034 / 2;` (velocidad del sonido ida y vuelta).
* **Modelación en Wokwi:** Conectar `TRIG -> GPIO 5`, `ECHO -> GPIO 18`, abrir Monitor Serial y mover el slider de distancia del sensor en Wokwi.

### 3. Práctica Guiada y Reto Individual (15 – 40 min)
* **15 – 25 min (Guiada):** Conectan el HC-SR04 en Wokwi y ven la distancia en cm cambiando en el Monitor Serial al mover el slider.
* **25 – 40 min (Reto Solos):** *"Agrega 1 LED Rojo (GPIO 13) y 1 Buzzer (GPIO 14): si la distancia es menor a `30 cm`, prende el LED y suena una alerta; si es mayor, apaga todo."*

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **2 preguntas rápidas:**
  1. *"¿Para qué sirve el pin `TRIG` y para qué el pin `ECHO`?"*
  2. *"¿Por qué dividimos entre 2 en la fórmula de distancia?"*
* **Cierre:** Comprobar el funcionamiento en vivo y responder las preguntas de verificación.



---

# CAPÍTULO #5
**Tema:** Proyecto Grupal: Teclado Matricial 4x4 (Piano / Clave de Seguridad) en Wokwi *(Grupal)*  
**Modo de Clase:** Modo A/B — Mini-teoría (10 min) + Proyecto Grupal Wokwi (30 min) + Cierre (5 min)  

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Integrar** un teclado 4x4 al ESP32 en Wokwi para leer claves o tocar notas, como una cerradura digital.
* **¿Para qué me sirve en la vida?** Así funcionan los cajeros automáticos, cerraduras digitales de puertas, cajas fuertes y paneles de alarmas.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"Si quisiéramos conectar 16 botones sueltos al ESP32, nos quedaríamos sin pines. Un teclado 4x4 usa solo 8 pines (4 filas y 4 columnas) para leer 16 teclas."*
* **Propósito en pantalla:** *"Integrar un teclado 4x4 al ESP32 en Wokwi para leer claves o tocar notas, como una cerradura digital."*

### 2. Teoría Corta y Modelación (05 – 15 min)
* **Librería `Keypad.h`:** En Wokwi (`Library Manager` -> agregar `Keypad`).
* **Conexión:** 4 pines de filas + 4 pines de columnas a GPIOs del ESP32 (ej. `13, 12, 14, 27` y `26, 25, 33, 32`).
* **Modelación:** Imprimir la tecla presionada en Monitor Serial (`char tecla = keypad.getKey();`).

### 3. Trabajo Grupal en Wokwi (15 – 40 min)
* **Instrucción:** En parejas/grupos eligen **1 de 2 opciones**:
  * **Opción A (Clave de Seguridad):** Si presionan `'1'`, `'2'`, `'3'`, `'4'` (o una tecla secreta como `'#'`), enciende LED Verde; si no, LED Rojo.
  * **Opción B (Mini Piano):** Cada tecla (`1` al `4`) toca una nota distinta en el Buzzer (`tone()`).
* **Tu rol:** Ayudas a agregar `Keypad` en `libraries.txt` de Wokwi y revisar el orden de filas/columnas.

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **2 preguntas rápidas:**
  1. *"¿Cuántos pines GPIO necesita un teclado de 16 botones gracias a la matriz 4x4?"*
  2. *"¿Para qué sirve la librería `Keypad.h`?"*
* **Cierre:** Subir captura grupal de Wokwi corriendo.



---

# CAPÍTULO #6
**Tema:** Refuerzo ESP32 en Wokwi y Cierre de Parcial 2 *(Colchón)*  
**Modo de Clase:** Modo B — Repaso y Nivelación (45 min)  

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Revisar** nuestras simulaciones del ESP32 en Wokwi y nivelar entregas antes de la evaluación.
* **¿Para qué me sirve en la vida?** Para afianzar la lectura de sensores y periféricos en ESP32 antes de conectar proyectos a Internet e Inteligencia Artificial.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"Hoy cerramos el primer quimestre con ESP32. Revisamos quién tiene pendiente alguna simulación en Wokwi y hacemos un repaso rápido antes de las evaluaciones de la próxima semana."*
* **Propósito en pantalla:** *"Revisar nuestras simulaciones del ESP32 en Wokwi y nivelar entregas antes de la evaluación."*

### 2. Nivelación y Repaso en Wokwi (05 – 35 min)
* Estudiantes con prácticas pendientes (Semáforo, PWM/Buzzer, HC-SR04 o Teclado 4x4) completan y suben sus capturas.
* Quienes están al día prueban combinar **HC-SR04 + LED + Buzzer** con mensajes en Monitor Serial.

### 4. Cierre y Autoevaluación Likert (1 al 5) (35 – 45 min)
* Repaso de criterios para el 11 de enero + autoevaluación del **1 al 5** (*1 = Todavía me cuesta | 5 = Lo domino*):
  1. Diferenciar pines GPIO y voltaje lógico de 3.3V del ESP32 en Wokwi.
  2. Programar salidas digitales y PWM/tonos (`analogWrite`, `tone`) en el ESP32.
  3. Medir distancias en cm con el sensor ultrasonido HC-SR04 y activar alertas.
  4. Integrar un teclado matricial 4x4 con `Keypad.h` para leer claves o notas.

