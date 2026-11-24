# 🟠 3RO BGU — PARCIAL 2 / SEMANA 6 (7 – 11 dic)

> [!NOTE]
> # 📘 CLASE SIN ENTREGA
**Tema:** Sensor Ultrasonido HC-SR04 con ESP32 en Wokwi  
**Mediador:** David Castro  
**Modo de Clase:** Modo A — Tema Nuevo (45 min)  
**Entregable:** Captura en Wokwi con distancia en Monitor Serial y alerta LED/Buzzer en Classroom.

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
* **Cierre:** Subir captura de Wokwi mostrando la distancia `< 30 cm` y el LED encendido.

## 📢 TEXTO PARA GOOGLE CLASSROOM
```text
TÍTULO: Práctica ESP32 (Wokwi): Sensor Ultrasonido HC-SR04

PROPÓSITO: Medir distancias en centímetros con el sensor ultrasonido y el ESP32 para activar una alarma de choque.

INSTRUCCIONES:
1. En wokwi.com (ESP32), conecta el sensor HC-SR04 (TRIG a GPIO 5, ECHO a GPIO 18), 1 LED en GPIO 13 y 1 Buzzer en GPIO 14.
2. Calcula la distancia en centímetros e imprímela en el Monitor Serial (115200 baudios).
3. Programa la alerta: si distancia < 30 cm, enciende el LED y suena el buzzer.
4. Pon // Tu Nombre Apellido en la línea 1 y sube 1 captura probando una distancia menor a 30 cm.

Calificación: 10 puntos (Práctica de clase).
```

---

## 🎨 PROMPT PARA NOTEBOOKLM
```text
Crea una presentación estilo cómic educativo de las Tortugas Ninja en español para estudiantes de 3ro BGU (17-18 años) del Volumen 2: "Microcontroladores y Periféricos Digitales", como un capítulo autoconclusivo independiente ("Ultrasonido HC-SR04 con ESP32") basado en el CAPÍTULO #4 de FUENTE_3RO_BGU_PARCIAL2_COMPLETO.md.

ELENCO Y ALTERNANCIA VISUAL (CÓMIC + LÁMINA DE ESTUDIO):
Usa únicamente personajes de las Tortugas Ninja en TODAS las diapositivas: Leonardo, Donatello, Rafael y Miguel Ángel (prohibido dibujar niños genéricos, profesores o personajes externos).
- TRAMA EN 3 ACTOS: Inicio (el personaje tiene un problema concreto que solo se resuelve con este tema) -> Meollo (para ayudarlo, explican la teoría esencial con diagramas y consejos preventivos repetidos antes de construir/probar paso a paso) -> Final (logran resolver el problema inicial).
- En los bloques de HISTORIA (Portada, Misión de detección, Práctica y Cierre): usa viñetas dinámicas de cómic con diálogos midiendo distancias de intrusos con telemetría en tiempo real.
- En los bloques de TEORÍA: usa láminas explicativas profundas ("Trigger 10 µs -> Echo pulseIn() -> Fórmula distancia = duracion * 0.034 / 2" y "Precaución de 3.3V con Echo en hardware real"), presentadas por Donatello sin globos que tapen el cálculo.

Usa las diapositivas que necesites para no comprimir conceptos, siguiendo exactamente este orden de bloques:
1. Portada y gancho técnico.
2. Propósito LEV y explicación cercana a su edad (17-18 años) de para qué sirve calcular distancia por tiempo de vuelo en sensores industriales, drones y robótica.
3. Láminas explicativas profundas del HC-SR04 con ESP32 y fórmula de conversión a centímetros.
4. Práctica guiada paso a paso en Wokwi dentro de la historia, preguntas de verificación y cierre autoconclusivo.

ALCANCE ESTRICTO: Usa únicamente los conceptos y código verificado de la fuente (PROHIBIDO inventar código por tu cuenta o introducir bucles/librerías/temas avanzados no vistos en esta clase).
Prohibido poner nombres de profesor/mediador, fechas, "Semana X", entregables amarrados, "Continuará..." o adelantos del próximo capítulo (este capítulo cierra al terminar).
```
