# 🟠 3RO BGU — PARCIAL 2 / SEMANA 6 (7 – 11 dic)

> [!NOTE]
> # 📘 CLASE SIN ENTREGA
**Tema:** Sensor Ultrasonido HC-SR04 con ESP32 en Wokwi  
**Cargo:** Mediador    
**📊 Slides:** Sección 2 (ver PROMPTS_BLOQUES.md)
**Modo de Clase:** Modo A — Tema Nuevo (45 min)  
**Entregable:** Captura en Wokwi con distancia en Monitor Serial y alerta LED/Buzzer en Classroom.

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Comprobar** distancias en centímetros con el sensor ultrasonido y el ESP32 para activar una alarma de choque.
* **¿Cómo sé que lo logré?** El Monitor Serial muestra la distancia real en cm y activa el LED/buzzer cuando un objeto se acerca al umbral.
* **¿Para qué me sirve en la vida?** Es el principio de los sensores de parqueo de autos, robots que esquivan obstáculos y medidores de nivel en tanques.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **Pregunta relámpago (60 seg):** Conectar oralmente con el concepto clave de la clase anterior.
* **¿Qué decirles?** *"¿Cómo sabe un carro moderno o un robot que está a 20 cm de chocar sin tocar la pared? Usa ondas de sonido que rebotan, igual que los murciélagos."*
* **Propósito en pantalla:** *"Comprobar distancias en centímetros con el sensor ultrasonido y el ESP32 para activar una alarma de choque."*

### 2. Teoría Corta y Modelación (05 – 15 min)
* **Predicción PRIMM (30 seg antes de simular):** Preguntar qué hará el ejemplo o qué cambia si modifican un parámetro antes de correrlo.
* **Pines del HC-SR04:** `VCC` (5V/3.3V en Wokwi), `GND`, `TRIG` (envía pulso `10 µs`), `ECHO` (recibe rebote con `pulseIn()`).
* **Fórmula:** `distancia = duracion * 0.034 / 2;` (velocidad del sonido ida y vuelta).
* **Modelación en Wokwi:** Conectar `TRIG -> GPIO 5`, `ECHO -> GPIO 18`, abrir Monitor Serial y mover el slider de distancia del sensor en Wokwi.

### 3. Práctica Guiada y Reto Individual (15 – 40 min)
* **Protocolo de Autodepuración (3 pasos antes de llamar al mediador):** 1. Energía/GND -> 2. Pines/Polaridad -> 3. Monitor Serial/Multímetro.
* **15 – 25 min (Guiada):** Conectan el HC-SR04 en Wokwi y ven la distancia en cm cambiando en el Monitor Serial al mover el slider.
* **25 – 40 min (Reto Solos):** *"Agrega 1 LED Rojo (GPIO 13) y 1 Buzzer (GPIO 14): si la distancia es menor a `30 cm`, prende el LED y suena una alerta; si es mayor, apaga todo."*

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **Dinámica de cierre (30 seg):** Respuesta simultánea (dedos/pulgar) o *Cold Call* al azar (evitar que respondan solo los mismos 2).
* **2 preguntas rápidas:**
  1. *"¿Para qué sirve el pin `TRIG` y para qué el pin `ECHO`?"*
  2. *"¿Por qué dividimos entre 2 en la fórmula de distancia?"*
* **Cierre:** Subir captura de Wokwi mostrando la distancia `< 30 cm` y el LED encendido.
