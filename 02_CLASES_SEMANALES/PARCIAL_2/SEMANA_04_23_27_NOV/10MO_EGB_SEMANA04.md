# 📘 10MO EGB — PARCIAL 2 / SEMANA 4 (23 – 27 nov)

> [!NOTE]
> # 📘 CLASE SIN ENTREGA
**Tema:** Primer Programa en Arduino (*Blink*) en Tinkercad  
**Mediador:** David Castro  
**Modo de Clase:** Modo A — Tema Nuevo (45 min)  
**Entregable:** Práctica guiada en aula sin entrega obligatoria *(Ind. 1 y 2 ya completas en Classroom)*.

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Simular** un LED que parpadea solo con código Arduino (`Blink`) para dar vida a un circuito.
* **¿Para qué me sirve en la vida?** Es el primer paso para automatizar cualquier cosa: desde luces intermitentes de bicicleta hasta semáforos y alarmas.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"Hasta el parcial pasado, un foco solo prendía si tú aplastabas el interruptor con el dedo. Hoy jubilamos al dedo: vamos a darle cerebro con código C++ para que prenda y apague solo."*
* **Propósito en pantalla:** *"Simular un LED que parpadea solo con código Arduino (`Blink`) para dar vida a un circuito."*

### 2. Teoría Corta y Modelación (05 – 15 min)
* **2 bloques obligatorios de Arduino:**
  * `void setup()` $\rightarrow$ Corre **una sola vez** al prender (`pinMode(13, OUTPUT);`).
  * `void loop()` $\rightarrow$ Se **repite por siempre** (`digitalWrite(13, HIGH);`, `delay(1000);`, `LOW`).
* **Modelación en Tinkercad:** Arrastrar Arduino UNO + LED + Resistencia $220\,\Omega$ en Pin 13 y GND, cambiar código a **Texto**, simular y ver parpadear.

### 3. Práctica Guiada y Reto Individual (15 – 40 min)
* **15 – 25 min (Guiada):** Todos arman el circuito del LED en Pin 13 y prueban el código *Blink* básico contigo.
* **25 – 40 min (Reto Solos):** *"Agrega un segundo LED en el Pin 12 (con su resistencia) y haz que parpadeen alternados: cuando uno prende, el otro se apaga cada 500 ms. Pon tu nombre en un comentario `// Nombre`."*

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
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

---

## 🎨 PROMPT PARA NOTEBOOKLM
```text
Crea una presentación estilo cómic educativo de las Tortugas Ninja en español para estudiantes de 10mo EGB (14-15 años) del Volumen 2: "Conexiones Seguras y Primer Código", como un capítulo autoconclusivo independiente ("Primer Código: Blink en Tinkercad", etiqueta 👤 ACTIVIDAD INDIVIDUAL 2) basado en el CAPÍTULO #2 de FUENTE_10MO_EGB_PARCIAL2_COMPLETO.md.

ELENCO Y ALTERNANCIA VISUAL (CÓMIC + LÁMINA DE ESTUDIO):
Usa únicamente personajes de las Tortugas Ninja en TODAS las diapositivas: Leonardo, Donatello, Rafael, Miguel Ángel y Krang (prohibido dibujar niños genéricos, profesores o personajes externos).
- TRAMA EN 3 ACTOS: Inicio (el personaje tiene un problema concreto que solo se resuelve con este tema) -> Meollo (para ayudarlo, explican la teoría esencial con diagramas y consejos preventivos repetidos antes de construir/probar paso a paso) -> Final (logran resolver el problema inicial).
- En los bloques de HISTORIA (Portada, Conflicto, Reto y Cierre): usa viñetas dinámicas de cómic con diálogos programando su primera baliza luminosa de alerta contra Krang.
- En los bloques de TEORÍA: usa láminas explicativas profundas estilo pizarra ("Anatomía del código Arduino: void setup() corre 1 vez vs. void loop() repite por siempre" y "Qué hace pinMode, digitalWrite y delay"), con diagramas claros presentados por Donatello sin globos que tapen el código.

Usa las diapositivas que necesites para no comprimir conceptos, siguiendo exactamente este orden de bloques:
1. Portada y gancho de batalla con etiqueta 👤 ACTIVIDAD INDIVIDUAL.
2. Propósito LEV y explicación cercana a su edad (14-15 años) de para qué les sirve dominar la estructura básica de un programa embebido.
3. Láminas explicativas profundas sobre setup(), loop(), pinMode(), digitalWrite() y delay(ms).
4. Enunciado claro de la actividad individual en Tinkercad Circuits + 1 consejo (PROHIBIDO regalar el código completo del reto final).
5. Verificación y cierre autoconclusivo.

ALCANCE ESTRICTO: Usa únicamente los conceptos y código verificado de la fuente (PROHIBIDO inventar código por tu cuenta o introducir bucles/librerías/temas avanzados no vistos en esta clase).
Prohibido poner nombres de profesor/mediador, fechas, "Semana X", entregables amarrados, "Continuará..." o adelantos del próximo capítulo (este capítulo cierra al terminar).
```
