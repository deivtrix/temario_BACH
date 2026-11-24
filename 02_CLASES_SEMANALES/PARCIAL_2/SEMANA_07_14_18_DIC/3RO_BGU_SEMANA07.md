# 🟠 3RO BGU — PARCIAL 2 / SEMANA 7 (14 – 18 dic)

> [!IMPORTANT]
> # 👥 ACTIVIDAD GRUPAL EVALUADA
**Tema:** Proyecto Grupal: Teclado Matricial 4x4 (Piano / Clave de Seguridad) en Wokwi *(Grupal)*  
**Mediador:** David Castro    
**📊 Slides:** Sección 2 (ver PROMPTS_BLOQUES.md)
**Modo de Clase:** Modo A/B — Mini-teoría (10 min) + Proyecto Grupal Wokwi (30 min) + Cierre (5 min)  
**Entregable:** Captura grupal en Wokwi mostrando el Teclado 4x4 funcionando en Monitor Serial + LED/Buzzer.

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Integrar** un teclado 4x4 al ESP32 en Wokwi para leer claves o tocar notas, como una cerradura digital.
* **¿Cómo sé que lo logré?** Al presionar teclas en la matriz 4x4 en Wokwi, el ESP32 lee la tecla exacta y activa la nota o clave.
* **¿Para qué me sirve en la vida?** Así funcionan los cajeros automáticos, cerraduras digitales de puertas, cajas fuertes y paneles de alarmas.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **Pregunta relámpago (60 seg):** Conectar oralmente con el concepto clave de la clase anterior.
* **¿Qué decirles?** *"Si quisiéramos conectar 16 botones sueltos al ESP32, nos quedaríamos sin pines. Un teclado 4x4 usa solo 8 pines (4 filas y 4 columnas) para leer 16 teclas."*
* **Propósito en pantalla:** *"Integrar un teclado 4x4 al ESP32 en Wokwi para leer claves o tocar notas, como una cerradura digital."*

### 2. Teoría Corta y Modelación (05 – 15 min)
* **Librería `Keypad.h`:** En Wokwi (`Library Manager` $\rightarrow$ agregar `Keypad`).
* **Conexión:** 4 pines de filas + 4 pines de columnas a GPIOs del ESP32 (ej. `13, 12, 14, 27` y `26, 25, 33, 32`).
* **Modelación:** Imprimir la tecla presionada en Monitor Serial (`char tecla = keypad.getKey();`).

### 3. Trabajo Grupal en Wokwi (15 – 40 min)
* **Protocolo de Autodepuración (3 pasos antes de llamar al mediador):** 1. Energía/GND -> 2. Pines/Polaridad -> 3. Monitor Serial/Multímetro.
* **Roles rotativos (3 por equipo):** 1. Armado/Diseño -> 2. Código/Parámetros -> 3. Verificador/Evidencia.
* **Instrucción:** En parejas/grupos eligen **1 de 2 opciones**:
  * **Opción A (Clave de Seguridad):** Si presionan `'1'`, `'2'`, `'3'`, `'4'` (o una tecla secreta como `'#'`), enciende LED Verde; si no, LED Rojo.
  * **Opción B (Mini Piano):** Cada tecla (`1` al `4`) toca una nota distinta en el Buzzer (`tone()`).
* **Tu rol:** Ayudas a agregar `Keypad` en `libraries.txt` de Wokwi y revisar el orden de filas/columnas.

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **2 preguntas rápidas:**
  1. *"¿Cuántos pines GPIO necesita un teclado de 16 botones gracias a la matriz 4x4?"*
  2. *"¿Para qué sirve la librería `Keypad.h`?"*
* **Cierre:** Subir captura grupal de Wokwi corriendo a Classroom.

## 📢 TEXTO PARA GOOGLE CLASSROOM
```text
TÍTULO: Actividad Grupal ESP32 (Wokwi): Teclado Matricial 4x4

PROPÓSITO: Integrar un teclado 4x4 al ESP32 en Wokwi para leer claves o tocar notas, como una cerradura digital.

INSTRUCCIONES (En grupos de 2):
1. En wokwi.com (ESP32), agreguen el componente "Membrane Keypad 4x4" y la librería "Keypad" en Library Manager.
2. Elijan una opción:
   - Opción A: Al presionar una tecla o clave secreta, enciende LED Verde (acceso) o Rojo (error).
   - Opción B: Las teclas 1, 2, 3 y 4 reproducen 4 notas distintas en un Buzzer.
3. Pongan los nombres del grupo en la línea 1 (// Nombre1 - Nombre2) y suban 1 captura funcionando con el Monitor Serial visible.

Calificación: 10 puntos (Actividad Grupal).
```
