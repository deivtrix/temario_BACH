# 📘 10MO EGB — PARCIAL 2 / SEMANA 5 (30 nov – 4 dic)

> [!IMPORTANT]
> # 👤 ACTIVIDAD INDIVIDUAL EVALUADA
**Tema:** Cuestionario Inicial: Parpadeo del LED (*Blink*) (`Individual 1`) + Instalación de Arduino IDE y *Blink* Físico  
**Subtemas puntuales (2 nuevos):**
1. Instalación y configuración del entorno **Arduino IDE** (selección de placa `Arduino UNO` y puerto `COM`).
2. Carga física del programa *Blink* por cable USB y montaje real de 1 LED con resistencia de $220\,\Omega$ en protoboard.
**Cargo:** Mediador    
**📊 Slides:** Sección 2 (ver PROMPTS_BLOQUES.md)
**Modo de Clase:** Modo A — Evaluación Diagnóstica Inicial (`10 min`) + Práctica Física Guiada (`35 min`)  
**Entregable:** **Cuestionario Individual 1 (Parpadeo del LED / *Blink*)** al inicio de la clase + verificación en mesa del Arduino UNO parpadeando en físico.

---

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Evaluar** los fundamentos del parpadeo del LED (*Blink*) y **cargar** nuestro primer programa real desde Arduino IDE hacia la placa física Arduino UNO.
* **¿Cómo sé que lo logré?** Completaste el Cuestionario Individual 1 de *Blink* al inicio de la clase y tu Arduino UNO físico hace parpadear el LED conectado al pin 13.
* **¿Para qué me sirve en la vida?** Para pasar de la simulación a la electrónica real: instalar drivers, conectar placas por USB y validar que una computadora puede controlar hardware físico.

---

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Cuestionario Inicial (`Individual 1`) y Propósito (00 – 12 min)
* **00 – 10 min (Cuestionario Individual 1 — Antes de la clase):** Aplicar el **Cuestionario sobre el Parpadeo del LED (*Blink*)** en Google Forms / Classroom (6 preguntas sobre lo visto en Semana 4).
  * *Nota para **10MO Perspicaces** (que perdió clase el mar 24 nov):* Hacer un repaso exprés de 5 minutos proyectando el código *Blink* (`setup`, `loop`, `pinMode`, `digitalWrite`, `delay` y resistencia $220\,\Omega$) antes de abrir el cuestionario.
* **10 – 12 min (Conexión y Propósito):** *"La semana pasada hicimos parpadear un LED en la pantalla de Tinkercad. Hoy damos el salto al mundo real: vamos a instalar el Arduino IDE y subir el parpadeo directamente a una placa Arduino UNO física."*
* **Propósito en pantalla:** *"Cargar nuestro primer programa real desde Arduino IDE hacia la placa física Arduino UNO."*

### 2. Instalación de Arduino IDE y Conexión Segura (12 – 22 min)
* **Instalación / Apertura:** Verificar que el **Arduino IDE** esté instalado/abierto en las computadoras del laboratorio.
* **Reglas físicas antes de conectar USB:**
  1. Verificar pata larga del LED ($+$ al pin 13) y pata corta ($-$ a `GND`) pasando por resistencia de $220\,\Omega$.
  2. Conectar el cable USB azul al Arduino UNO y a la computadora.
  3. En Arduino IDE: ir a **Herramientas $\rightarrow$ Placa $\rightarrow$ `Arduino UNO`** y **Puerto $\rightarrow$ `COMx (Arduino UNO)`**.

### 3. Práctica Guiada: Subir *Blink* al Arduino Físico (22 – 40 min)
* **Protocolo de Autodepuración (3 pasos antes de llamar al mediador):** 1. Cable USB / Puerto `COM` -> 2. Pines / Polaridad del LED y resistencia -> 3. Sintaxis (`;` y llaves `{}`).
* **22 – 32 min (Guiada):** Copian su código *Blink* desde Tinkercad (o escriben el código base de Pin 13) en Arduino IDE, hacen clic en **Verificar (✓)** y luego en **Subir (→)**.
* **32 – 40 min (Reto Exprés en físico):** *"Cambia el tiempo en `delay()` para que el LED físico parpadee más rápido (ej. `200` ms) y vuelve a subirlo para comprobar que tienes control real de la placa."*

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **Dinámica de cierre (30 seg):** Respuesta simultánea (dedos/pulgar) o *Cold Call* al azar.
* **2 preguntas rápidas:**
  1. *"¿Qué dos opciones debes revisar en el menú Herramientas antes de subir un código al Arduino físico?"*
  2. *"¿Para qué sirve el botón Verificar (✓) antes de presionar Subir (→)?"*
* **Cierre:** Visto bueno en mesa de que el Arduino IDE quedó operativo y el LED parpadea en físico (base lista para el **Grupal 1: Semáforo Físico** de Semana 6).

---

## 📢 TEXTO PARA GOOGLE CLASSROOM
> **👤 ACTIVIDAD INDIVIDUAL 1 — Cuestionario: Parpadeo del LED (*Blink*) en Arduino**  
> **Instrucciones:**  
> 1. Responde el cuestionario corto al **inicio de la clase** sobre lo aprendido la semana pasada acerca del parpadeo del LED (*Blink*) en Tinkercad (`void setup()`, `void loop()`, `pinMode()`, `digitalWrite()`, `delay()` y uso de resistencia).  
> 2. Es una actividad **individual** y **sin ayuda de apuntes** durante los primeros 10 minutos.  
> 3. Al finalizar el cuestionario, instalaremos/abriremos **Arduino IDE** en clase para subir tu código *Blink* al Arduino UNO físico.

---

## 📝 CUESTIONARIO INDIVIDUAL 1: PARPADEO DEL LED (*BLINK*) — LISTO PARA GOOGLE FORMS
*(6 preguntas objetivas para aplicar en 8–10 minutos al inicio de la clase. **No proyectar las respuestas**).*

1. **¿Cuál es la diferencia principal entre `void setup()` y `void loop()` en un programa de Arduino?**
   * a) `setup()` apaga el Arduino y `loop()` lo enciende.
   * b) `setup()` se ejecuta una sola vez al iniciar y `loop()` se repite infinitamente. ✅
   * c) `loop()` se ejecuta una sola vez y `setup()` se repite para siempre.
   * d) Ambos bloques se ejecutan exactamente una sola vez.

2. **¿Para qué sirve la instrucción `pinMode(13, OUTPUT);` dentro de `void setup()`?**
   * a) Para encender el LED inmediatamente.
   * b) Para pausar el programa 13 milisegundos.
   * c) Para configurar el pin 13 como salida de señal/corriente hacia el LED. ✅
   * d) Para leer si un botón está presionado en el pin 13.

3. **Si quieres que el LED conectado al pin 13 permanezca encendido durante medio segundo y luego se apague, ¿qué bloque de código es correcto?**
   * a) `digitalWrite(13, HIGH); delay(500); digitalWrite(13, LOW);` ✅
   * b) `digitalWrite(13, LOW); delay(5000); digitalWrite(13, HIGH);`
   * c) `pinMode(13, HIGH); delay(50); pinMode(13, LOW);`
   * d) `digitalWrite(13, HIGH); delay(0.5); digitalWrite(13, LOW);`

4. **¿Qué ocurre si olvidas colocar `delay(1000);` entre `digitalWrite(13, HIGH);` y `digitalWrite(13, LOW);`?**
   * a) El LED explota en Tinkercad por exceso de tiempo.
   * b) El código no compila y marca error de sintaxis.
   * c) El LED parpadea tan rápido que el ojo humano lo percibe encendido fijo o muy tenue. ✅
   * d) El Arduino se apaga automáticamente.

5. **¿Por qué es obligatorio conectar una resistencia (ej. $220\,\Omega$) en serie con el LED al conectarlo al pin digital del Arduino?**
   * a) Para que el LED cambie de color automáticamente.
   * b) Para limitar la corriente y evitar que el LED o el pin del Arduino se quemen. ✅
   * c) Para acelerar la velocidad del `void loop()`.
   * d) Para reemplazar la conexión a tierra (`GND`).

6. **Observa esta línea de código: `digitalWrite(13, HIGH)` (sin punto y coma al final). ¿Qué sucederá al iniciar la simulación?**
   * a) El LED parpadea normalmente.
   * b) El LED solo enciende a la mitad de su brillo.
   * c) Aparece un error de compilación porque en C++ cada instrucción debe terminar en `;`. ✅
   * d) El Arduino ignora esa línea y ejecuta la siguiente.

---

## ❓ PREGUNTAS DE CIERRE (CON RESPUESTA ESPERADA)
1. **¿Qué dos opciones debes configurar en Arduino IDE antes de subir un programa por USB?**
   * *Respuesta esperada:* La placa (`Arduino UNO`) y el puerto (`COM` correspondiente).
2. **¿Cómo sabes físicamente cuál pata del LED va conectada al pin digital y cuál a `GND`?**
   * *Respuesta esperada:* La pata larga (ánodo, $+$) va al pin digital (mediante la resistencia) y la pata corta (cátodo, $-$) va a `GND`.
3. **¿Qué ventaja tiene haber probado primero el código en Tinkercad antes de subirlo al Arduino real?**
   * *Respuesta esperada:* Permite verificar que no haya errores de sintaxis ni cortocircuitos antes de conectar componentes físicos.
