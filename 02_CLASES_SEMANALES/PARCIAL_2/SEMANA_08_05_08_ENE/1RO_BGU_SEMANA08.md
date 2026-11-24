# 🔴 1RO BGU — PARCIAL 2 / SEMANA 8 (5 – 8 ene)

> [!TIP]
> # 🛠️ REFUERZO Y NIVELACIÓN
**Tema:** Refuerzo: Calibración con Monitor Serial, Cierre de Parcial 2 y Autoevaluación *(Refuerzo)*  
**Mediador:** David Castro    
**📊 Slides:** Sección 2 (ver PROMPTS_BLOQUES.md)
**Modo de Clase:** Modo B — Refuerzo Práctico, Nivelación y Autoevaluación Likert 1–5 (45 min)  
**Entregable:** Revisión de notas, calibración final y Autoevaluación Likert (1–5).

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Integrar** lo visto de potenciómetro, brillo PWM y sensor de luz antes de pasar a nuevos sensores.
* **¿Cómo sé que lo logré?** Mides el valor mínimo y máximo de luz en el Monitor Serial para fijar el umbral exacto y completas tu Likert.
* **¿Para qué me sirve en la vida?** Para consolidar cómo leer cualquier sensor analógico del mundo real antes de trabajar con sensores más complejos.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **Pregunta relámpago (60 seg):** Conectar oralmente con el concepto clave de la clase anterior.
* **¿Qué decirles?** *"Última clase antes de evaluaciones de Áreas Especiales. Hoy repasamos `analogRead`, `map` y PWM, y revisamos que nadie quede debiendo notas."*
* **Propósito en pantalla:** *"Integrar lo visto de potenciómetro, brillo PWM y sensor de luz antes de pasar a nuevos sensores."*

### 2. Repaso / Mini-Reto en Tinkercad (05 – 25 min)
* Quienes están al día combinan en Tinkercad **Potenciómetro + LED PWM** o **LDR + Buzzer** en un solo repaso guiado.

### 3. Nivelación Final (25 – 40 min)
* **Protocolo de Autodepuración (3 pasos antes de llamar al mediador):** 1. Energía/GND -> 2. Pines/Polaridad -> 3. Monitor Serial/Multímetro.
* Revisión de informes/capturas pendientes del Parcial 2.

### 4. Cierre y Autoevaluación Likert (1 al 5) (40 – 45 min)
* Indicaciones para el 11 de enero + autoevaluación del **1 al 5** (*1 = Todavía me cuesta | 5 = Lo domino*):
  1. Leer sensores analógicos con `analogRead()` y usar condicionales `>` / `<`.
  2. Transformar rangos con `map()` y controlar brillo con PWM (`analogWrite()`).
  3. Armar y calibrar una fotoresistencia (LDR) con el Monitor Serial.
  4. Convertir lecturas de luz en sonido usando `tone()` en el Buzzer.
