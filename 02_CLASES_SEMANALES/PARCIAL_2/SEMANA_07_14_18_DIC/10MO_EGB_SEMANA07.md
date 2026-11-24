# 📘 10MO EGB — PARCIAL 2 / SEMANA 7 (14 – 18 dic)

> [!TIP]
> # 🛠️ REFUERZO Y NIVELACIÓN
**Tema:** Reto de Secuencias e Intro a Bucles `for` *(Refuerzo)*  
**Mediador:** David Castro    
**📊 Slides:** Sección 2 (ver PROMPTS_BLOQUES.md)
**Modo de Clase:** Modo A — Tema Nuevo / Refuerzo (45 min)  
**Entregable:** Captura en Tinkercad del barrido de LEDs usando `for` en Classroom.

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Optimizar** el encendido de 6 LEDs en fila usando un bucle `for` en lugar de repetir tantas líneas.
* **¿Cómo sé que lo logré?** Tu bucle for recorre y enciende los 6 LEDs en secuencia sin repetir líneas de código.
* **¿Para qué me sirve en la vida?** En programación real nadie escribe 100 veces la misma línea: los bucles `for` automatizan tareas repetitivas en segundos.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **Pregunta relámpago (60 seg):** Conectar oralmente con el concepto clave de la clase anterior.
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
* **Protocolo de Autodepuración (3 pasos antes de llamar al mediador):** 1. Energía/GND -> 2. Pines/Polaridad -> 3. Monitor Serial/Multímetro.
* **15 – 25 min (Guiada):** Conectan 4–6 LEDs en pines consecutivos (`2` al `7`) en Tinkercad y prueban el bucle `for` de ida.
* **25 – 40 min (Reto Solos):** *"Agrega un segundo bucle `for` debajo que regrese la luz de derecha a izquierda (`for (int pin = 7; pin >= 2; pin--)`)."*

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **2 preguntas rápidas:**
  1. *"¿Qué significa `pin++` y qué significa `pin--`?"*
  2. *"¿Qué pasa si conectas los LEDs en pines saltados (ej. 2, 5, 9) cuando usas un `for` consecutivo?"*
* **Cierre:** Subir captura de Tinkercad corriendo a Classroom.
