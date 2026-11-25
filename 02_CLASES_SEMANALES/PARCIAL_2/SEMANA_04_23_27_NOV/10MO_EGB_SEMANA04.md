# 📘 10MO EGB — PARCIAL 2 / SEMANA 4 (23 – 27 nov)

> [!NOTE]
> # 📘 CLASE SIN ENTREGA
**Tema:** Primer Programa en Arduino (*Blink*) en Tinkercad  
**Subtemas puntuales (2 nuevos):**
1. Estructura base de Arduino: `void setup()` vs. `void loop()` / Configuración de salida digital con `pinMode(pin, OUTPUT)`.
2. Encendido, apagado y pausas (`digitalWrite` + `delay`) / Simulación segura de LED con resistencia en Tinkercad.
**Cargo:** Mediador    
**📊 Slides:** Sección 2 (ver PROMPTS_BLOQUES.md)
**Modo de Clase:** Modo A — Tema Nuevo (45 min)  
**Entregable:** Práctica guiada en aula sin entrega obligatoria *(Base para el Cuestionario Individual 1 al inicio de Semana 5)*.

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Simular** un LED que parpadea solo con código Arduino (`Blink`) para dar vida a un circuito.
* **¿Cómo sé que lo logré?** Tu LED en Tinkercad enciende 1 segundo y se apaga 1 segundo sin errores de compilación.
* **¿Para qué me sirve en la vida?** Es el primer paso para automatizar cualquier cosa: desde luces intermitentes de bicicleta hasta semáforos y alarmas.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **Pregunta relámpago (60 seg):** Conectar oralmente con el concepto clave de la clase anterior.
* **¿Qué decirles?** *"Hasta el parcial pasado, un foco solo prendía si tú aplastabas el interruptor con el dedo. Hoy jubilamos al dedo: vamos a darle cerebro con código C++ para que prenda y apague solo."*
* **Propósito en pantalla:** *"Simular un LED que parpadea solo con código Arduino (`Blink`) para dar vida a un circuito."*

### 2. Teoría Corta y Modelación (05 – 15 min)
* **Predicción PRIMM (30 seg antes de simular):** Preguntar qué hará el ejemplo o qué cambia si modifican un parámetro antes de correrlo.
* **2 bloques obligatorios de Arduino:**
  * `void setup()` $\rightarrow$ Corre **una sola vez** al prender (`pinMode(13, OUTPUT);`).
  * `void loop()` $\rightarrow$ Se **repite por siempre** (`digitalWrite(13, HIGH);`, `delay(1000);`, `LOW`).
* **Modelación en Tinkercad:** Arrastrar Arduino UNO + LED + Resistencia $220\,\Omega$ en Pin 13 y GND, cambiar código a **Texto**, simular y ver parpadear.

### 3. Práctica Guiada y Reto Individual (15 – 40 min)
* **Protocolo de Autodepuración (3 pasos antes de llamar al mediador):** 1. Energía/GND -> 2. Pines/Polaridad -> 3. Monitor Serial/Multímetro.
* **15 – 25 min (Guiada):** Todos arman el circuito del LED en Pin 13 y prueban el código *Blink* básico contigo.
* **25 – 40 min (Reto Solos):** *"Agrega un segundo LED en el Pin 12 (con su resistencia) y haz que parpadeen alternados: cuando uno prende, el otro se apaga cada 500 ms. Pon tu nombre en un comentario `// Nombre`."*

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **Dinámica de cierre (30 seg):** Respuesta simultánea (dedos/pulgar) o *Cold Call* al azar (evitar que respondan solo los mismos 2).
* **2 preguntas rápidas:**
  1. *"¿Qué diferencia hay entre `void setup()` y `void loop()`?"*
  2. *"Si pongo `delay(500);`, ¿cuántos segundos espera el Arduino?"*
* **Cierre:** Subir captura en Tinkercad con el LED encendido y el código visible a Classroom.
---

## ❓ PREGUNTAS DE CIERRE (CON RESPUESTA ESPERADA)
1. **¿Qué diferencia hay entre `void setup()` y `void loop()` en Arduino?**
   * *Respuesta esperada:* `setup()` se ejecuta una sola vez al encender (para configurar pines), mientras `loop()` se repite infinitamente.
2. **¿Para qué sirve `pinMode(13, OUTPUT);`?**
   * *Respuesta esperada:* Le indica al Arduino que el pin 13 enviará corriente/señal hacia afuera (por ejemplo, para encender un LED).
3. **¿Qué pasa si olvidamos poner `delay(1000);` entre `HIGH` y `LOW`?**
   * *Respuesta esperada:* El LED parpadea tan rápido (millones de veces por segundo) que el ojo humano lo ve encendido fijo o muy tenue.
