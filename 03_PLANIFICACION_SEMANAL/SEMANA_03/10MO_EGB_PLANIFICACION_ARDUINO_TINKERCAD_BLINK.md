# 📘 10MO EGB — PLANIFICACIÓN DE CLASE (SEMANA 3: INTRODUCCIÓN A ARDUINO EN TINKERCAD)

**Propósito de la Clase (Taxonomía Lev):**  
> **Explorar** el entorno de simulación virtual de Tinkercad Circuits, **identificar** los 4 elementos funcionales primarios de la placa Arduino UNO y **experimentar** la modificación de retardos temporales (`delay`) en la simulación del LED integrado de prueba ("L") sin sobrecarga de sintaxis de código.

* **Duración:** 45 Minutos  
* **Modalidad:** 💻 100% Virtual en Computadoras del Laboratorio.  
* **Plataforma:** [Autodesk Tinkercad Circuits](https://www.tinkercad.com/).  
* **Entregable:** Captura de pantalla en Tinkercad con el código modificado + 2 Preguntas reflexivas en Google Classroom.

---

### ⏱️ DESGLOSE PASO A PASO (45 MINUTOS)

1. **🎯 Acceso y Vinculación al Aula (00 - 12 min):**  
   * Los estudiantes abren el navegador, ingresan el enlace de la **Clase de Tinkercad** y colocan su apodo oficial (*nickname*).
   * El docente proyecta la pantalla principal y verifica que todos hayan ingresado a la sección de **Circuitos** y hagan clic en `Crear nuevo circuito`.

2. **💡 Anatomía Esencial del Arduino UNO (12 - 22 min):**  
   * Se arrastra una placa Arduino UNO R3 al espacio de trabajo.
   * El docente explica **únicamente 4 partes clave** para no saturar al estudiante:
     1. **🔌 Puerto USB:** Alimenta la placa y carga los programas desde la computadora.
     2. **⚡ Pines de Alimentación (5V y GND):** El polo positivo ($+5\text{V}$) y la tierra/negativo ($\text{GND}$) para alimentar componentes.
     3. **🔢 Pines Digitales (0 al 13):** Las compuertas que envían señales binarias: encendido (`HIGH`) o apagado (`LOW`).
     4. **💡 LED Integrado "L":** Un pequeño bombillo soldado directamente en la placa que está interconectado al **Pin Digital 13**.

3. **💻 Práctica Interactiva "El Latido del Arduino" (22 - 38 min):**  
   * Los alumnos hacen clic en el botón superior **Código** (pueden usar Bloques o Texto C++).
   * Notarán que Tinkercad ya tiene cargado el código base de fábrica (*Blink*):
     ```cpp
     void setup() {
       pinMode(13, OUTPUT);
     }
     void loop() {
       digitalWrite(13, HIGH);
       delay(1000); // Espera 1 segundo
       digitalWrite(13, LOW);
       delay(1000); // Espera 1 segundo
     }
     ```
   * Clic en **Iniciar Simulación**: Observan el LED "L" parpadeando a ritmo constante.
   * **🚀 Reto Autónomo:** Modificar los números del `delay(1000)` a `delay(150)` (o en bloques cambiar `1 segundo` por `0.2 segundos`). Al reiniciar la simulación, verán cómo el LED late a toda velocidad como si estuviera acelerado.

4. **📝 Cierre y Entrega en Classroom (38 - 45 min):**  
   * Tomar captura de pantalla nítida donde se aprecie la placa simulando (con el LED encendido) y la ventana de código con los nuevos valores.
   * Subir la imagen a la tarea de Google Classroom y responder las 2 preguntas.

---

### 📌 2 PREGUNTAS REFLEXIVAS VIVENCIALES (ANTI-IA)

1. **Pregunta 1 (Prueba de error en vivo en tu simulador):** Haz esta prueba en tu Tinkercad: Borra o ponle doble barra '//' a la línea `digitalWrite(13, LOW);` y dale a Iniciar Simulación. ¿Qué le ocurre visualmente al LED 'L' ahora en tu pantalla y por qué?
2. **Pregunta 2 (Observación directa de hardware):** En la placa virtual de tu pantalla, ubica el LED 'L'. ¿Qué letra tiene al lado el pin digital donde está conectado internamente? ¿Por qué esta placa nos permitió hacer la práctica sin necesidad de conectar ningún cable externo?

---

### 📢 TEXTO LISTO PARA PEGAR EN GOOGLE CLASSROOM

```text
TÍTULO: Práctica 1: Exploración de Arduino UNO y Simulación de Parpadeo en Tinkercad

INSTRUCCIONES:
Estimados estudiantes, hoy ingresamos oficialmente a Tinkercad Circuits y pusimos en marcha nuestro primer microcontrolador Arduino UNO virtual.

🔒 REGLA ANTI-IA: Prohibido usar respuestas generadas por ChatGPT. Las preguntas evalúan lo que modificaste y comprobaste en tu propia pantalla.

Adjunta en esta tarea:
1. Una captura de pantalla completa de tu circuito en Tinkercad CON LA NOTA VIRTUAL de tu nombre, la simulación activa (LED "L" parpadeando rápido) y la ventana de código abierta.
2. Escribe en el cuadro de entrega o en tu plantilla de Google Docs las respuestas vivenciales (máx. 3 líneas):
   - Pregunta 1: ¿Qué ocurrió visualmente cuando borraste la línea digitalWrite(13, LOW);?
   - Pregunta 2: ¿A qué pin digital está interconectado el LED 'L' y por qué no necesitamos cables externos hoy?

RÚBRICA DE CALIFICACIÓN (Total: 10 Puntos):
- Captura en Tinkercad con Nota Virtual y usuario visible: 2.5 pts
- Registro auténtico de tiempos probados en el simulador: 2.5 pts
- Pregunta 1 respondida comprobando el error en el simulador: 2.5 pts
- Pregunta 2 explicada con observación directa de la placa: 2.5 pts
```
