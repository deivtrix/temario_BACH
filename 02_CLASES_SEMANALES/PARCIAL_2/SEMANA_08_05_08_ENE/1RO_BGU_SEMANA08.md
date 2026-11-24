# 🔴 1RO BGU — PARCIAL 2 / SEMANA 8 (5 – 8 ene)
**Tema:** Refuerzo: Calibración con Monitor Serial, Cierre de Parcial 2 y Autoevaluación *(Refuerzo)*  
**Mediador:** David Castro  
**Modo de Clase:** Modo B — Refuerzo Práctico, Nivelación y Autoevaluación Likert 1–5 (45 min)  
**Entregable:** Revisión de notas, calibración final y Autoevaluación Likert (1–5).

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Integrar** lo visto de potenciómetro, brillo PWM y sensor de luz antes de pasar a nuevos sensores.
* **¿Para qué me sirve en la vida?** Para consolidar cómo leer cualquier sensor analógico del mundo real antes de trabajar con sensores más complejos.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"Última clase antes de evaluaciones de Áreas Especiales. Hoy repasamos `analogRead`, `map` y PWM, y revisamos que nadie quede debiendo notas."*
* **Propósito en pantalla:** *"Integrar lo visto de potenciómetro, brillo PWM y sensor de luz antes de pasar a nuevos sensores."*

### 2. Repaso / Mini-Reto en Tinkercad (05 – 25 min)
* Quienes están al día combinan en Tinkercad **Potenciómetro + LED PWM** o **LDR + Buzzer** en un solo repaso guiado.

### 3. Nivelación Final (25 – 40 min)
* Revisión de informes/capturas pendientes del Parcial 2.

### 4. Cierre y Autoevaluación Likert (1 al 5) (40 – 45 min)
* Indicaciones para el 11 de enero + autoevaluación del **1 al 5** (*1 = Todavía me cuesta | 5 = Lo domino*):
  1. Leer sensores analógicos con `analogRead()` y usar condicionales `>` / `<`.
  2. Transformar rangos con `map()` y controlar brillo con PWM (`analogWrite()`).
  3. Armar y calibrar una fotoresistencia (LDR) con el Monitor Serial.
  4. Convertir lecturas de luz en sonido usando `tone()` en el Buzzer.

## 📢 TEXTO PARA GOOGLE CLASSROOM
```text
TÍTULO: Cierre del Parcial 2: Repaso de Entradas Analógicas y PWM

PROPÓSITO: Integrar lo visto de potenciómetro, brillo PWM y sensor de luz antes de pasar a nuevos sensores.

ACTIVIDAD:
- Repaso general de analogRead(), map(), analogWrite() y tone().
- Revisión final de entregas antes de Evaluaciones de Áreas Especiales (11 de enero).
```

---

## 🎨 PROMPT PARA NOTEBOOKLM
```text
Crea una presentación estilo cómic educativo de las Tortugas Ninja en español para estudiantes de 1ro BGU (15-16 años) del Volumen 2: "Señales Analógicas y Regulación PWM", como un capítulo autoconclusivo independiente ("Repaso Integrador y Autoevaluación", etiqueta 🛠️ REFUERZO) basado en el CAPÍTULO #6 de FUENTE_1RO_BGU_PARCIAL2_COMPLETO.md.

ELENCO Y ALTERNANCIA VISUAL (CÓMIC + LÁMINA DE ESTUDIO):
Usa únicamente personajes de las Tortugas Ninja en TODAS las diapositivas: Leonardo, Donatello, Rafael, Miguel Ángel y el Maestro Splinter (prohibido dibujar niños genéricos, profesores o personajes externos).
- TRAMA EN 3 ACTOS: Inicio (el personaje tiene un problema concreto que solo se resuelve con este tema) -> Meollo (para ayudarlo, explican la teoría esencial con diagramas y consejos preventivos repetidos antes de construir/probar paso a paso) -> Final (logran resolver el problema inicial).
- En Portada, Reto y Cierre: viñetas dinámicas de cómic con diálogos en la evaluación de dominio del dojo.
- En el Resumen: lámina visual limpia integrando analogRead, map(), PWM, LDR y calibración Serial sin globos largos que tapen los esquemas.

Usa las diapositivas que necesites, siguiendo exactamente este orden de bloques:
1. Portada y gancho inicial con etiqueta 🛠️ REFUERZO.
2. Propósito LEV y explicación cercana a su edad (15-16 años) de para qué les sirve dominar entradas analógicas y salidas PWM.
3. Lámina visual resumen del Parcial 2.
4. Preguntas de repaso (SIN respuestas visibles) y tabla de Autoevaluación Escala de Likert (1 al 5) con los 4 aspectos clave del parcial.
5. Cierre autoconclusivo.

ALCANCE ESTRICTO: Usa únicamente los conceptos y código verificado de la fuente (PROHIBIDO inventar código por tu cuenta o introducir bucles/librerías/temas avanzados no vistos en esta clase).
Prohibido poner nombres de profesor/mediador, fechas, "Semana X", entregables amarrados, "Continuará..." o adelantos del próximo capítulo (este capítulo cierra al terminar).
```

### 🎬 VIDEO DE REPASO DEL PARCIAL
```text
Crea un video explicativo de repaso en español para estudiantes de 1ro BGU (15-16 años) sobre todo el Volumen 2: "Señales Analógicas y Regulación PWM" usando el archivo FUENTE_1RO_BGU_PARCIAL2_COMPLETO.md.

Cubre de forma ordenada y solo teórica todos los temas y subtemas del parcial (lectura analógica analogRead de 0 a 1023, función map() para reescalar rangos, modulación PWM con analogWrite de 0 a 255, divisor de voltaje con fotorresistencia LDR y resistencia de 10 kΩ, generación de frecuencias con tone() y calibración de umbrales con punto medio en Monitor Serial). Usa gráficos claros, esquemas de señal y ejemplos cercanos a su edad (sin personajes de cómics).

Prohibido mencionar nombres de profesor/mediador, fechas, "Semana X" o entregables.
```
