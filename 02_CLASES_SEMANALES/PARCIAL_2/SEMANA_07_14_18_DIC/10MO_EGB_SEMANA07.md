# 📘 10MO EGB — PARCIAL 2 / SEMANA 7 (14 – 18 dic)
**Tema:** Reto de Secuencias e Intro a Bucles `for` *(Refuerzo)*  
**Mediador:** David Castro  
**Modo de Clase:** Modo A — Tema Nuevo / Refuerzo (45 min)  
**Entregable:** Captura en Tinkercad del barrido de LEDs usando `for` en Classroom.

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Optimizar** el encendido de 6 LEDs en fila usando un bucle `for` en lugar de repetir tantas líneas.
* **¿Para qué me sirve en la vida?** En programación real nadie escribe 100 veces la misma línea: los bucles `for` automatizan tareas repetitivas en segundos.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"Si les pido encender 6 LEDs en fila uno por uno, tendrían que escribir 24 líneas de `digitalWrite`. Hoy les enseño el truco para hacerlo en solo 4 líneas."*
* **Propósito en pantalla:** *"Optimizar el encendido de 6 LEDs en fila usando un bucle `for` en lugar de repetir tantas líneas."*

### 2. Teoría Corta y Modelación (05 – 15 min)
* **Estructura del `for`:**
  ```cpp
  for (int pin = 2; pin <= 7; pin++) {
    digitalWrite(pin, HIGH);
    delay(150);
    digitalWrite(pin, LOW);
  }
  ```
* Explicar las 3 partes: inicio (`pin = 2`), límite (`pin <= 7`) y paso (`pin++`).

### 3. Práctica Guiada y Reto Individual (15 – 40 min)
* **15 – 25 min (Guiada):** Conectan 4–6 LEDs en pines consecutivos (`2` al `7`) en Tinkercad y prueban el bucle `for` de ida.
* **25 – 40 min (Reto Solos):** *"Agrega un segundo bucle `for` debajo que regrese la luz de derecha a izquierda (`for (int pin = 7; pin >= 2; pin--)`)."*

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **2 preguntas rápidas:**
  1. *"¿Qué significa `pin++` y qué significa `pin--`?"*
  2. *"¿Qué pasa si conectas los LEDs en pines saltados (ej. 2, 5, 9) cuando usas un `for` consecutivo?"*
* **Cierre:** Subir captura de Tinkercad corriendo a Classroom.

## 📢 TEXTO PARA GOOGLE CLASSROOM
```text
TÍTULO: Refuerzo Arduino: Secuencia de Luces con Bucle for

PROPÓSITO: Optimizar el encendido de 6 LEDs en fila usando un bucle `for` en lugar de repetir tantas líneas.

INSTRUCCIONES:
1. En Tinkercad, conecta 6 LEDs desde el Pin 2 hasta el Pin 7 (con resistencias de 220 ohmios a GND).
2. Usa un bucle for para encenderlos en orden de ida (2 -> 7) y otro bucle for para regresarlos (7 -> 2).
3. Pon // Tu Nombre en la línea 1 y sube 1 captura de la simulación corriendo.

Calificación: Refuerzo formativo (10 puntos).
```

---

## 🎨 PROMPT PARA NOTEBOOKLM
```text
Crea una presentación estilo cómic educativo de las Tortugas Ninja en español para estudiantes de 10mo EGB (14-15 años) del Volumen 2: "Conexiones Seguras y Primer Código", como un capítulo autoconclusivo independiente ("Depuración de Código: Encuentra el Error", etiqueta 🛠️ REFUERZO) basado en el CAPÍTULO #5 de FUENTE_10MO_EGB_PARCIAL2_COMPLETO.md.

ELENCO Y ALTERNANCIA VISUAL (CÓMIC + LÁMINA DE ESTUDIO):
Usa únicamente personajes de las Tortugas Ninja en TODAS las diapositivas: Leonardo, Donatello, Rafael, Miguel Ángel y Destructor saboteando el código (prohibido dibujar niños genéricos, profesores o personajes externos).
- TRAMA EN 3 ACTOS: Inicio (el personaje tiene un problema concreto que solo se resuelve con este tema) -> Meollo (para ayudarlo, explican la teoría esencial con diagramas y consejos preventivos repetidos antes de construir/probar paso a paso) -> Final (logran resolver el problema inicial).
- En Portada, Sabotaje y Cierre: viñetas dinámicas de cómic con diálogos detectando fallas introducidas en el código de la guarida.
- En Teoría: lámina explicativa visual ("Los 4 errores clásicos en Arduino C++: falta de punto y coma ;, llaves { } abiertas, pin equivocado y mayúsculas/minúsculas"), sin mostrar las respuestas de los retos.

Usa las diapositivas que necesites, siguiendo exactamente este orden de bloques:
1. Portada y gancho de sabotaje con etiqueta 🛠️ REFUERZO.
2. Propósito LEV y explicación cercana a su edad (14-15 años) de para qué les sirve saber leer mensajes de error y depurar código como programadores reales.
3. Lámina visual de errores comunes de sintaxis y lógica.
4. Casos de código con errores para corregir en clase (SIN mostrar las soluciones) y tabla de Autoevaluación Escala de Likert (1 al 5) si aplica al cierre.
5. Cierre autoconclusivo.

ALCANCE ESTRICTO: Usa únicamente los conceptos y código verificado de la fuente (PROHIBIDO inventar código por tu cuenta o introducir bucles/librerías/temas avanzados no vistos en esta clase).
Prohibido poner nombres de profesor/mediador, fechas, "Semana X", entregables amarrados, "Continuará..." o adelantos del próximo capítulo (este capítulo cierra al terminar).
```
