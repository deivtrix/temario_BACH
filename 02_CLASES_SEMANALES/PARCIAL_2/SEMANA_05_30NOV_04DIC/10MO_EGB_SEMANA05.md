# 📘 10MO EGB — PARCIAL 2 / SEMANA 5 (30 nov – 4 dic)

> [!IMPORTANT]
> # 👤 ACTIVIDAD INDIVIDUAL EVALUADA
**Tema:** Cuestionario Inicial: Parpadeo del LED (*Blink*) (`Individual 2`) + Múltiples Salidas Digitales: Semáforo en Tinkercad  
**Subtemas puntuales (2 nuevos):**
1. Control de 3 pines digitales independientes (Rojo, Amarillo, Verde) / Secuencia lógica de un semáforo real con `digitalWrite()` y `delay()`.
2. Conexión ordenada de 3 LEDs + 3 resistencias en protoboard virtual / Validación del código en Tinkercad (base para el Grupal Físico de Semana 6).
**Cargo:** Mediador    
**📊 Slides:** Sección 2 (ver PROMPTS_BLOQUES.md)
**Modo de Clase:** Modo A — Evaluación Diagnóstica Inicial (`10 min`) + Tema Nuevo (`35 min`)  
**Entregable:** **Cuestionario Individual 2 (Parpadeo del LED / *Blink*)** al inicio de la clase + captura exprés en Classroom del semáforo funcionando con variables `int`.

---

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Evaluar** los fundamentos del parpadeo del LED (*Blink*) y **simular** un semáforo de 3 luces en Tinkercad usando nombres (`int`) para ordenar los pines.
* **¿Cómo sé que lo logré?** Completaste el Cuestionario Individual 2 de *Blink* al inicio de la clase y tu semáforo en Tinkercad usa variables `int` ejecutando la secuencia completa de los 3 LEDs en orden.
* **¿Para qué me sirve en la vida?** Para organizar cualquier programa grande usando nombres claros (`ledRojo`, `ledVerde`) en lugar de memorizar números de pines.

---

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Cuestionario Inicial (`Individual 2`) y Propósito (00 – 12 min)
* **00 – 10 min (Cuestionario Individual 2 — Antes de la clase):** Aplicar el **Cuestionario sobre el Parpadeo del LED (*Blink*)** en Google Forms / Classroom (6 preguntas sobre lo visto en Semana 4).
  * *Nota para **10MO Perspicaces** (que perdió clase el mar 24 nov):* Hacer un repaso exprés de 5 minutos proyectando el código *Blink* (`setup`, `loop`, `pinMode`, `digitalWrite`, `delay` y resistencia $220\,\Omega$) antes de abrir el cuestionario.
* **10 – 12 min (Conexión y Propósito):** *"La semana pasada controlamos 1 o 2 LEDs usando `13` y `12`. Pero si tuviéramos 20 luces, ¿se acordarían qué hace cada número? Hoy vamos a ponerles nombre con variables."*
* **Propósito en pantalla:** *"Simular un semáforo de 3 luces en Tinkercad usando nombres (`int`) para ordenar los pines."*

### 2. Teoría Corta y Modelación (12 – 20 min)
* **Predicción PRIMM (30 seg antes de simular):** Preguntar qué hará el ejemplo o qué cambia si modifican un parámetro antes de correrlo.
* **Variables `int`:** `int rojo = 13;`, `int amarillo = 12;`, `int verde = 11;`. Si mañana cambias un cable de pin, solo cambias el número arriba una vez.
* **Modelación en Tinkercad:** Conectar 3 LEDs (Rojo, Amarillo, Verde) con resistencias de $220\,\Omega$ a GND y cargar el ciclo básico.

### 3. Práctica Guiada y Reto Individual (20 – 40 min)
* **Protocolo de Autodepuración (3 pasos antes de llamar al mediador):** 1. Energía/GND -> 2. Pines/Polaridad -> 3. Monitor Serial/Multímetro.
* **20 – 28 min (Guiada):** Todos arman el semáforo de 3 LEDs en protoboard dentro de Tinkercad y prueban el encendido secuencial.
* **28 – 40 min (Reto Solos):** *"Haz que la luz **Verde** parpadee 3 veces antes de pasar a Amarillo (como semáforo real de ciudad), y coloca tiempos reales: Verde 3s, Amarillo 1s, Rojo 3s."*

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **Dinámica de cierre (30 seg):** Respuesta simultánea (dedos/pulgar) o *Cold Call* al azar (evitar que respondan solo los mismos 2).
* **2 preguntas rápidas:**
  1. *"¿Para qué sirve declarar `int rojo = 13;` al inicio del código?"*
  2. *"¿Qué pasa si olvidas apagar el LED anterior con `LOW` antes de encender el siguiente?"*
* **Cierre:** Subir captura de Tinkercad con el código y el semáforo encendido a Classroom.

---

## 📢 TEXTO PARA GOOGLE CLASSROOM
> **👤 ACTIVIDAD INDIVIDUAL 2 — Cuestionario: Parpadeo del LED (*Blink*) en Arduino**  
> **Instrucciones:**  
> 1. Responde el cuestionario corto al **inicio de la clase** sobre lo aprendido la semana pasada acerca del parpadeo del LED (*Blink*) en Tinkercad (`void setup()`, `void loop()`, `pinMode()`, `digitalWrite()`, `delay()` y uso de resistencia).  
> 2. Es una actividad **individual** y **sin ayuda de apuntes** durante los primeros 10 minutos.  
> 3. Al finalizar el cuestionario, continúa en Tinkercad con la práctica de **Semáforo con variables `int`** y sube tu captura como evidencia de clase.

---

## 📝 CUESTIONARIO INDIVIDUAL 2: PARPADEO DEL LED (*BLINK*) — LISTO PARA GOOGLE FORMS
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
1. **¿Cuántas resistencias necesita un semáforo de 3 LEDs y por qué?**
   * *Respuesta esperada:* 3 resistencias (una por cada LED) para proteger cada pin y evitar que se quemen.
2. **¿Qué pasa si olvidamos apagar el LED verde (`LOW`) cuando encendemos el amarillo (`HIGH`)?**
   * *Respuesta esperada:* Quedan encendidos dos colores al mismo tiempo, rompiendo la lógica del semáforo.
3. **¿Por qué probamos primero el semáforo en Tinkercad antes de armarlo en físico?**
   * *Respuesta esperada:* Para verificar que el código y las conexiones funcionan sin riesgo de dañar componentes reales.
