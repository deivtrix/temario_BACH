# 📘 1RO BGU — PLANIFICACIÓN DE CLASE (SEMANA 3: CONSOLIDACIÓN DE CÓDIGO - SIRENA DE POLICÍA)

**Propósito de la Clase (Taxonomía Lev):**  
> **Reconstruir** la lógica de programación en Arduino C++ mediante el análisis estructurado de variables y retardos, **validar** el circuito virtual de la Sirena de Policía de 2 LEDs en Tinkercad Circuits y **documentar** la experiencia en un informe técnico en Google Docs con respuestas reflexivas.

* **Duración:** 45 Minutos  
* **Modalidad:** 💻 100% Virtual en Computadoras (Tinkercad Circuits + Google Docs).  
* **Circuito Virtual:** Arduino UNO + 2 LEDs (Rojo y Azul) en Pines Digitales 2 y 3 + 2 Resistencias de $220\ \Omega$ o $330\ \Omega$ a GND.  
* **Entregable:** Informe en Google Docs (con Captura + Código C++ comentado + 2 Preguntas reflexivas) subido a Google Classroom.

---

### ⏱️ DESGLOSE PASO A PASO (45 MINUTOS)

1. **🎯 Diagnóstico y Motivación (00 - 05 min):**  
   * *"Chicos, la clase anterior armamos el circuito físico/virtual pero varios tuvieron dudas al momento de programar. Programar en C++ no es memorizar, es entender cómo darle órdenes al microcontrolador. Hoy dejamos el código 100% dominado y documentado en nuestro informe."*

2. **💡 Explicación del Código Maestro en la Pizarra (05 - 18 min):**  
   El docente proyecta y analiza línea por línea el código limpio con variables:

   ```cpp
   // ========================================================
   // PRÁCTICA 2: SIRENA DE POLICÍA BICOLOR
   // CURSO: 1RO BGU - ROBÓTICA Y TECNOLOGÍA
   // ========================================================

   // 1. DECLARACIÓN DE VARIABLES (Asignamos nombres claros a los pines)
   const int pinRojo = 2;   // LED Rojo en el Pin Digital 2
   const int pinAzul = 3;   // LED Azul en el Pin Digital 3
   const int tiempo = 200;  // Tiempo de alternancia en milisegundos (0.2 seg)

   void setup() {
     // Configuramos ambos pines como SALIDAS de corriente
     pinMode(pinRojo, OUTPUT);
     pinMode(pinAzul, OUTPUT);
   }

   void loop() {
     // PASO 1: Encendemos Rojo y apagamos Azul
     digitalWrite(pinRojo, HIGH);
     digitalWrite(pinAzul, LOW);
     delay(tiempo); // Espera según la variable tiempo

     // PASO 2: Apagamos Rojo y encendemos Azul
     digitalWrite(pinRojo, LOW);
     digitalWrite(pinAzul, HIGH);
     delay(tiempo); // Espera según la variable tiempo
   }
   ```

   * *Puntos clave a reforzar:*
     * Por qué usamos variables (`const int`) en vez de números sueltos.
     * La diferencia entre `setup()` (se ejecuta 1 sola vez) y `loop()` (bucle infinito).
     * `HIGH` = 5V (Luz ON) y `LOW` = 0V (Luz OFF).

3. **💻 Validación en Tinkercad y Redacción del Informe (18 - 38 min):**  
   * Los alumnos abren Tinkercad Circuits, verifican las conexiones de sus 2 LEDs y pegan/escriben el código.
   * Inician simulación y comprueban el destello alternado tipo patrulla.
   * Toman captura de pantalla de su circuito simulando con el código visible.
   * Abren la [Plantilla de Informe Anti-IA](file:///C:/Users/Master_Lab2_DavidC/Documents/LEV/temario_BACH/03_PLANIFICACION_SEMANAL/SEMANA_03/1RO_BGU_PLANTILLA_INFORME_SIRENA_POLICIA.md), pegan su captura con la Nota Virtual, colocan sus parámetros propios y redactan las respuestas vivenciales.

4. **📝 Cierre y Entrega en Classroom (38 - 45 min):**  
   * Subida del enlace de Google Docs o descarga en PDF directamente en la tarea de Classroom.

---

### 📌 2 PREGUNTAS REFLEXIVAS VIVENCIALES (ANTI-IA)

1. **Pregunta 1 (Prueba de error en vivo en tu simulador):** Haz esta prueba en tu código de Tinkercad: En el `setup()`, cambia `pinMode(pinRojo, OUTPUT);` por `pinMode(pinRojo, INPUT);` y dale a Iniciar Simulación. ¿Qué le ocurrió visualmente al brillo del LED rojo en tu pantalla y por qué el pin no entregó energía suficiente?
2. **Pregunta 2 (Modificación extrema de variables):** Cambia en tu código el valor de tu variable 'tiempo' a 10 ms (`tiempo = 10;`). Al iniciar la simulación, ¿qué parece que le ocurre a los dos LEDs frente al ojo humano? ¿Por qué es vital usar retardos visibles en sistemas de emergencia?

---

### 📢 TEXTO LISTO PARA PEGAR EN GOOGLE CLASSROOM

```text
TÍTULO: Informe Técnico: Simulación y Programación de Sirena de Policía (Arduino C++)

INSTRUCCIONES:
Estimados estudiantes, consolidamos la práctica de la Sirena Bicolor en Tinkercad Circuits. Cada estudiante debe entregar de forma individual su Informe en Documentos de Google utilizando la plantilla oficial del curso.

🔒 REGLA ANTI-IA: Prohibido usar respuestas teóricas generadas por ChatGPT. Las preguntas evalúan las pruebas y errores ejecutados en tu propio circuito virtual.

El informe debe contener:
1. Captura de pantalla clara del circuito en Tinkercad en plena simulación con la NOTA VIRTUAL de tu nombre pegada sobre el protoboard.
2. Tus parámetros reales (colores de LED, pines, resistencias, valor de variable 'tiempo').
3. El código fuente C++ que compilaste en tu cuenta.
4. Respuestas en máximo 3 líneas a las dos preguntas reflexivas vivenciales.

RÚBRICA DE CALIFICACIÓN (Total: 10 Puntos):
- Captura con circuito simulando y Nota Virtual con nombre: 2.5 pts
- Parámetros reales y código C++ compilado en su cuenta: 2.5 pts
- Pregunta 1 respondida probando el error en vivo de INPUT/OUTPUT: 2.5 pts
- Pregunta 2 explicada desde la observación del retardo en pantalla: 2.5 pts
```
