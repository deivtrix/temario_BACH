# 📘 2DO BGU — GUÍA DOCENTE DE 45 MINUTOS (ARDUINO MÓDULO 3)

---

## 📅 CLASE 1: Entradas Analógicas (LDR / LM35) y Monitor Serial
* **Duración:** 45 Minutos | **Modalidad:** 💻 [100% PC en Tinkercad Circuits + Presentación]
* **Recurso / Presentación:** [PRESENTACION_2DO_BGU_ARDUINO_MOD3.pdf](file:///C:/Users/David/Desktop/clases%20bach/01_PRESENTACIONES_Y_MATERIAL/2DO_BGU/PRESENTACION_2DO_BGU_ARDUINO_MOD3.pdf)
* **Propósito Inicial:** Leer valores continuos del mundo físico mediante puertos analógicos (A0-A5) utilizando la función `analogRead()` y visualizándolos en el Monitor Serial.

---

### ⏱️ DESGLOSE PASO A PASO (45 MINUTOS)

#### 1. 🎯 Motivación y Frase de Entrada (00 - 05 min)
* **¿Qué decirles?** *"Chicos, el mundo no es solo encendido o apagado (0 o 1). Hay grados de luz, temperatura y distancia. Hoy aprenderemos a leer variables continuas del entorno usando la fotorresistencia LDR y el Monitor Serial."*

#### 2. 💡 Teoría Relámpago (05 - 10 min)
* **Los 3 Conceptos Clave:**
  1. **Conversión ADC:** El Arduino transforma señales de 0V a 5V en números enteros de 0 a 1023.
  2. **Monitor Serial (`Serial.begin(9600);`):** Permite ver en la computadora los datos en tiempo real.
  3. **Sensor LDR:** Disminuye su resistencia a mayor cantidad de luz recibida.

#### 3. 💻 Actividad Guiada Contigo (10 - 20 min)
* **Instrucción:** Todos abren Tinkercad Circuits:
  - Arrastrar 1 Arduino Uno + 1 Sensor LDR en divisor de tensión conectado al pin A0.
  - Escribir `Serial.println(analogRead(A0));` para observar la variación de números en el Monitor Serial.

#### 4. 🚀 Actividad Individual (Ellos Solos) (20 - 40 min)
* **El Reto:**
  > *"Crear una Alarma Alumbrada Automática: Si el valor de luz en A0 cae por debajo de 400 (oscuridad), encender automáticamente un LED de poste público."*

#### 5. 📝 Cierre y Evaluación (40 - 45 min)
* Revisar el funcionamiento del umbral de encendido del LED en el Monitor Serial.
