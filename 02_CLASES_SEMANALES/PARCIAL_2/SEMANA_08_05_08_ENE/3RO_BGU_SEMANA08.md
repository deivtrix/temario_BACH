# 🟠 3RO BGU — PARCIAL 2 / SEMANA 8 (5 – 8 ene)
**Tema:** Refuerzo ESP32 en Wokwi y Cierre de Parcial 2 *(Colchón)*  
**Mediador:** David Castro  
**Modo de Clase:** Modo B — Repaso y Nivelación (45 min)  
**Entregable:** Verificación de entregas en Wokwi previas a evaluación quimestral.

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Revisar** nuestras simulaciones del ESP32 en Wokwi y nivelar entregas antes de la evaluación.
* **¿Para qué me sirve en la vida?** Para afianzar la lectura de sensores y periféricos en ESP32 antes de conectar proyectos a Internet e Inteligencia Artificial.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"Hoy cerramos el primer quimestre con ESP32. Revisamos quién tiene pendiente alguna simulación en Wokwi y hacemos un repaso rápido antes de las evaluaciones de la próxima semana."*
* **Propósito en pantalla:** *"Revisar nuestras simulaciones del ESP32 en Wokwi y nivelar entregas antes de la evaluación."*

### 2. Nivelación y Repaso en Wokwi (05 – 35 min)
* Estudiantes con prácticas pendientes (Semáforo, PWM/Buzzer, HC-SR04 o Teclado 4x4) completan y suben sus capturas en Classroom.
* Quienes están al día prueban combinar **HC-SR04 + LED + Buzzer** con mensajes en Monitor Serial.

### 4. Cierre y Autoevaluación Likert (1 al 5) (35 – 45 min)
* Repaso de criterios para el 11 de enero + autoevaluación del **1 al 5** (*1 = Todavía me cuesta | 5 = Lo domino*):
  1. Diferenciar pines GPIO y voltaje lógico de $3.3\text{V}$ del ESP32 en Wokwi.
  2. Programar salidas digitales y PWM/tonos (`analogWrite`, `tone`) en el ESP32.
  3. Medir distancias en cm con el sensor ultrasonido HC-SR04 y activar alertas.
  4. Integrar un teclado matricial 4x4 con `Keypad.h` para leer claves o notas.

## 📢 TEXTO PARA GOOGLE CLASSROOM
```text
TÍTULO: Cierre del Parcial 2: Repaso General ESP32 en Wokwi

PROPÓSITO: Revisar nuestras simulaciones del ESP32 en Wokwi y nivelar entregas antes de la evaluación.

ACTIVIDAD:
- Revisión y entrega final de simulaciones pendientes en Wokwi.
- Repaso previo a la semana de Evaluaciones de Áreas Especiales (11 de enero).
```

---

## 🎨 PROMPT PARA NOTEBOOKLM
```text
Crea una presentación estilo cómic educativo de las Tortugas Ninja en español para estudiantes de 3ro BGU (17-18 años) del Volumen 2: "Microcontroladores y Periféricos Digitales", como un capítulo autoconclusivo independiente ("Repaso ESP32 en Wokwi y Autoevaluación", etiqueta 🛠️ REFUERZO) basado en el CAPÍTULO #6 de FUENTE_3RO_BGU_PARCIAL2_COMPLETO.md.

ELENCO Y ALTERNANCIA VISUAL (CÓMIC + LÁMINA DE ESTUDIO):
Usa únicamente personajes de las Tortugas Ninja en TODAS las diapositivas: Leonardo, Donatello, Rafael, Miguel Ángel y el Maestro Splinter (prohibido dibujar niños genéricos, profesores o personajes externos).
- En Portada, Reto y Cierre: viñetas dinámicas de cómic con diálogos cerrando el módulo base de ESP32.
- En el Resumen: lámina visual limpia integrando GPIO 3.3V, PWM/Buzzer, HC-SR04 y Teclado 4x4 sin globos largos que tapen los esquemas.

Usa las diapositivas que necesites, siguiendo exactamente este orden de bloques:
1. Portada y gancho inicial con etiqueta 🛠️ REFUERZO.
2. Propósito LEV y explicación cercana a su edad (17-18 años) de para qué les sirve dominar periféricos digitales en ESP32 antes de pasar a IoT en red.
3. Lámina visual resumen del Parcial 2.
4. Preguntas de repaso (SIN respuestas visibles) y tabla de Autoevaluación Escala de Likert (1 al 5) con los 4 aspectos exactos de la fuente.
5. Cierre autoconclusivo.

Prohibido poner nombres de profesor/mediador, fechas, "Semana X", entregables amarrados, "Continuará..." o adelantos del próximo capítulo (este capítulo cierra al terminar).
```

### 🎬 VIDEO DE REPASO DEL PARCIAL
```text
Crea un video explicativo de repaso en español para estudiantes de 3ro BGU (17-18 años) sobre todo el Volumen 2: "Microcontroladores y Periféricos Digitales" usando el archivo FUENTE_3RO_BGU_PARCIAL2_COMPLETO.md.

Cubre de forma ordenada y solo teórica todos los temas y subtemas del parcial (arquitectura del ESP32, pines GPIO y lógica de 3.3V frente a 5V, salidas digitales en Wokwi, modulación PWM y control de frecuencias en buzzer, lectura del sensor ultrasonido HC-SR04 con pulseIn y escaneo por filas/columnas de un teclado matricial 4x4 con Keypad.h). Usa gráficos claros, diagramas de pines y ejemplos de ingeniería cercanos a su edad (sin personajes de cómics).

Prohibido mencionar nombres de profesor/mediador, fechas, "Semana X" o entregables.
```
